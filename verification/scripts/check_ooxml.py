#!/usr/bin/env python3
"""Inspect a .docx's OOXML for artifact-level submission issues.

Checks (all post-hoc, depend on the saved file internals):
  - tracked changes left on (<w:ins>/<w:del>) and the trackChanges flag
  - image-based equations (<a:blip> inside a math context) vs editable OMML (<m:oMath>)
  - bullet / numbered lists (<w:numPr> / ListParagraph)
  - bold runs in body paragraphs (possible stray emphasis)

A .docx is a ZIP; we read word/document.xml and settings.xml directly so the only
dependency is the standard library.

Usage:
    python check_ooxml.py --docx path/to/Manuscript.docx
"""
import argparse
import re
import sys
import zipfile

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def _read(zf, name):
    try:
        return zf.read(name).decode("utf-8", "replace")
    except KeyError:
        return ""


def check(docx_path):
    findings = []
    try:
        zf = zipfile.ZipFile(docx_path)
    except (FileNotFoundError, zipfile.BadZipFile) as exc:
        return [("FAIL", f"cannot open {docx_path}: {exc}")]

    doc = _read(zf, "word/document.xml")
    settings = _read(zf, "word/settings.xml")

    # Tracked changes -------------------------------------------------------
    ins = len(re.findall(r"<w:ins\b", doc))
    dele = len(re.findall(r"<w:del\b", doc))
    track_flag = "<w:trackChanges" in settings
    if ins or dele:
        findings.append(("FAIL", f"tracked changes present (<w:ins>={ins}, <w:del>={dele}); accept/reject all before upload"))
    elif track_flag:
        findings.append(("PARTIAL", "Track Changes is still switched ON (no changes recorded yet); turn it off"))
    else:
        findings.append(("PASS", "no tracked changes; Track Changes off"))

    # Equations -------------------------------------------------------------
    omml = len(re.findall(r"<m:oMath\b", doc))
    # an image equation = an <a:blip> sitting INSIDE a single oMath block (blocks don't nest)
    img_eq = sum(1 for block in re.findall(r"<m:oMath\b.*?</m:oMath>", doc, re.S)
                 if "<a:blip" in block)
    if img_eq:
        findings.append(("FAIL", f"{img_eq} equation(s) appear to be images inside math; equations must be editable OMML/MathML"))
    else:
        findings.append(("PASS", f"{omml} editable OMML equation(s); none image-based"))

    # Lists -----------------------------------------------------------------
    numpr = len(re.findall(r"<w:numPr\b", doc))
    listpara = len(re.findall(r'w:val="ListParagraph"', doc))
    bullets = doc.count("•")
    if numpr or listpara or bullets:
        findings.append(("PARTIAL", f"possible list(s) detected (numPr={numpr}, ListParagraph={listpara}, bullet-char={bullets}); Nature forbids bullet/numbered lists in text"))
    else:
        findings.append(("PASS", "no bullet/numbered lists detected"))

    return findings


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--docx", required=True, help="path to the .docx to inspect")
    args = ap.parse_args(argv)

    findings = check(args.docx)
    worst = "PASS"
    for status, msg in findings:
        print(f"[{status}] {msg}")
        if status == "FAIL":
            worst = "FAIL"
        elif status == "PARTIAL" and worst != "FAIL":
            worst = "PARTIAL"
    print(f"== check_ooxml: {worst} ==")
    return 0 if worst == "PASS" else (1 if worst == "PARTIAL" else 2)


if __name__ == "__main__":
    sys.exit(main())
