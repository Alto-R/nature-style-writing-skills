#!/usr/bin/env python3
"""Run the full pre-upload mechanical sweep and print a combined summary.

This is the optional final safety net described in verification-workflow.md. It never
substitutes for writing each section correctly with the writing/ guides.

Usage:
    python check_all.py --docx Final_manuscript.docx \
                        --si Supplementary.docx --si-pdf "Supplementary Information.pdf" \
                        --figdir figure
Any argument may be omitted; the corresponding checks report SKIP.
"""
import argparse
import sys

import check_deliverables
import check_figures
import check_ooxml
import extract_text


def _roll(worst, status):
    order = {"PASS": 0, "SKIP": 0, "PARTIAL": 1, "FAIL": 2}
    return status if order.get(status, 0) > order.get(worst, 0) else worst


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--docx", help="main manuscript .docx")
    ap.add_argument("--si", help="Supplementary source .docx")
    ap.add_argument("--si-pdf", dest="si_pdf", help="exported Supplementary PDF")
    ap.add_argument("--figdir", help="directory of finished figure images")
    args = ap.parse_args(argv)

    overall = "PASS"

    def run(title, findings):
        nonlocal overall
        print(f"\n--- {title} ---")
        sub = "PASS"
        for status, msg in findings:
            print(f"[{status}] {msg}")
            sub = _roll(sub, status)
        overall = _roll(overall, sub)

    if args.docx:
        run("OOXML", check_ooxml.check(args.docx))
        run("Text scan", extract_text.scan(extract_text.to_markdown(args.docx)[0] or ""))
    if args.si:
        run("OOXML (SI)", check_ooxml.check(args.si))
    if args.figdir:
        import glob, os
        imgs = []
        for ext in ("png", "jpg", "jpeg", "tif", "tiff"):
            imgs += glob.glob(os.path.join(args.figdir, f"*.{ext}"))
        run("Figures", check_figures.check(sorted(set(imgs))))

    files = [p for p in (args.docx, args.si) if p]
    run("Deliverables", check_deliverables.check(
        argparse.Namespace(files=files, figs=None, si=args.si, si_pdf=args.si_pdf)))

    print(f"\n===== OVERALL: {overall} =====")
    return {"PASS": 0, "PARTIAL": 1, "FAIL": 2}.get(overall, 0)


if __name__ == "__main__":
    sys.exit(main())
