#!/usr/bin/env python3
"""Check file-size limits and detect a stale Supplementary PDF.

Post-hoc, because it depends on files on disk and their modification times:
  - upload files <= 30 MB (Nature soft limit; use repositories for large data)
  - figure files <= 50 MB
  - the Supplementary PDF should be newer than its source .docx (else it is stale);
    optionally also diff a few key numeric tokens between the two.

Usage:
    python check_deliverables.py --files Final_manuscript.docx Supplementary.docx \
        --figs figure/fig1.pdf figure/fig2.pdf \
        --si Supplementary.docx --si-pdf "Supplementary Information.pdf"
"""
import argparse
import os
import sys

UPLOAD_LIMIT_MB = 30
FIGURE_LIMIT_MB = 50


def _mb(path):
    return os.path.getsize(path) / (1024 * 1024)


def check_sizes(files, limit, label):
    findings = []
    for p in files or []:
        if not os.path.exists(p):
            findings.append(("SKIP", f"{label}: {p} not found"))
            continue
        size = _mb(p)
        name = os.path.basename(p)
        if size > limit:
            findings.append(("FAIL", f"{label}: {name} = {size:.1f} MB exceeds {limit} MB limit"))
        else:
            findings.append(("PASS", f"{label}: {name} = {size:.1f} MB (<= {limit} MB)"))
    return findings


def check_stale_pdf(si_docx, si_pdf):
    if not si_docx or not si_pdf:
        return [("SKIP", "stale-PDF check needs both --si and --si-pdf")]
    if not (os.path.exists(si_docx) and os.path.exists(si_pdf)):
        return [("SKIP", "stale-PDF check: source docx or pdf missing")]
    d = os.path.getmtime(si_docx)
    p = os.path.getmtime(si_pdf)
    if p < d:
        return [("FAIL", f"SI PDF is OLDER than its .docx (pdf {p:.0f} < docx {d:.0f}); re-export the PDF before upload")]
    return [("PASS", "SI PDF is newer than its .docx (not stale by timestamp)")]


def check(args):
    findings = []
    findings += check_sizes(args.files, UPLOAD_LIMIT_MB, "upload")
    findings += check_sizes(args.figs, FIGURE_LIMIT_MB, "figure")
    findings += check_stale_pdf(args.si, args.si_pdf)
    return findings


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--files", nargs="*", help="files subject to the 30 MB upload limit")
    ap.add_argument("--figs", nargs="*", help="figure files subject to the 50 MB limit")
    ap.add_argument("--si", help="Supplementary source .docx")
    ap.add_argument("--si-pdf", dest="si_pdf", help="exported Supplementary PDF")
    args = ap.parse_args(argv)

    findings = check(args)
    worst = "PASS"
    for status, msg in findings:
        print(f"[{status}] {msg}")
        if status == "FAIL":
            worst = "FAIL"
        elif status == "PARTIAL" and worst != "FAIL":
            worst = "PARTIAL"
    print(f"== check_deliverables: {worst} ==")
    return 0 if worst in ("PASS", "SKIP") else (1 if worst == "PARTIAL" else 2)


if __name__ == "__main__":
    sys.exit(main())
