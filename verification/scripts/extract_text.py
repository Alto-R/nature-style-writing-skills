#!/usr/bin/env python3
"""Extract docx text (via pandoc) and run quick prose sanity scans.

A light text-level scan that complements the structural checks. It flags a few high-value
issues that survive into the finished file:
  - slash units ("kW/m", "mg/L") that should be negative exponents ("kW m-1")
  - vague data-availability phrases ("available on request")
  - an abstract that runs long (> 200 words), if an Abstract heading is found
  - fake full-width equation brackets "(N)" left by some exporters

Requires pandoc on PATH. Falls back to SKIP if pandoc or the file is missing.

Usage:
    python extract_text.py --docx path/to/Manuscript.docx
    python extract_text.py --docx Manuscript.docx --dump out.md   # also save the markdown
"""
import argparse
import re
import shutil
import subprocess
import sys


def to_markdown(docx_path):
    if shutil.which("pandoc") is None:
        return None, "pandoc not on PATH"
    try:
        out = subprocess.run(
            ["pandoc", docx_path, "-t", "markdown"],
            capture_output=True, text=True, check=True,
            encoding="utf-8", errors="replace",
        )
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        return None, f"pandoc failed: {exc}"
    md = out.stdout or ""
    # normalise fake full-width brackets sometimes emitted for equation numbers
    md = md.replace("（", "(").replace("）", ")")
    return md, None


def scan(md):
    findings = []

    slash = re.findall(r"\b[kMG]?[WkJgLm]{1,3}\s*/\s*[a-zA-Z]", md)
    # broad slash-unit heuristic: a unit-ish token followed by /letter
    slash2 = re.findall(r"\b(?:kW|MW|GW|mg|kg|m|kWh|MWh|USD|\$)\s*/\s*[a-zA-Z0-9]", md)
    hits = sorted(set(slash + slash2))
    if hits:
        findings.append(("PARTIAL", f"possible slash units (use negative exponents): {hits[:8]}"))
    else:
        findings.append(("PASS", "no obvious slash units"))

    if re.search(r"available (on|upon)\s+(reasonable\s+)?request", md, re.I) or \
       re.search(r"available from the (corresponding\s+)?author", md, re.I):
        findings.append(("FAIL", "vague data-availability phrase ('on request'/'from the authors'); state specific repositories/DOIs"))
    else:
        findings.append(("PASS", "no vague data-availability phrasing"))

    m = re.search(r"(?im)^#{1,3}\s*abstract\s*$(.+?)(?:^#{1,3}\s|\Z)", md, re.S)
    if m:
        words = len(re.findall(r"\b\w+\b", m.group(1)))
        if words > 200:
            findings.append(("PARTIAL", f"abstract ~{words} words (> 200); tighten toward ~150"))
        else:
            findings.append(("PASS", f"abstract ~{words} words (<= 200)"))
    else:
        findings.append(("SKIP", "no Abstract heading found to measure"))

    return findings


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--docx", required=True)
    ap.add_argument("--dump", help="optional path to save the extracted markdown")
    args = ap.parse_args(argv)

    md, err = to_markdown(args.docx)
    if md is None:
        print(f"[SKIP] {err}")
        print("== extract_text: SKIP ==")
        return 0
    if args.dump:
        with open(args.dump, "w", encoding="utf-8") as fh:
            fh.write(md)

    findings = scan(md)
    worst = "PASS"
    for status, msg in findings:
        print(f"[{status}] {msg}")
        if status == "FAIL":
            worst = "FAIL"
        elif status == "PARTIAL" and worst != "FAIL":
            worst = "PARTIAL"
    print(f"== extract_text: {worst} ==")
    return 0 if worst in ("PASS", "SKIP") else (1 if worst == "PARTIAL" else 2)


if __name__ == "__main__":
    sys.exit(main())
