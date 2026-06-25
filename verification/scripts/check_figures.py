#!/usr/bin/env python3
"""Scan finished figure images for red-green colour-blind hazards.

For each image it (1) counts strongly-red and strongly-green pixels, flagging figures
where both are abundant, and (2) converts to greyscale and checks whether the red and
green regions collapse to a similar grey (the real colour-blind failure mode).

This is post-hoc because it inspects the rendered pixels, not the plotting code. To fix a
flagged figure, recolour with a colour-blind-safe palette (see writing/07).

Usage:
    python check_figures.py --figdir path/to/figures
    python check_figures.py --images fig1.png fig2.png
"""
import argparse
import glob
import os
import sys

try:
    from PIL import Image
    import numpy as np
    HAVE_DEPS = True
except ImportError:
    HAVE_DEPS = False


def scan(path):
    img = Image.open(path).convert("RGB")
    px = np.asarray(img, dtype=np.int16)
    r, g, b = px[..., 0], px[..., 1], px[..., 2]
    total = px.shape[0] * px.shape[1]

    strong_red = (r > 150) & (g < 100) & (b < 100)
    strong_green = (g > 150) & (r < 100) & (b < 100)
    red_frac = strong_red.sum() / total
    green_frac = strong_green.sum() / total

    # greyscale collapse: mean luminance of the two regions
    lum = 0.299 * r + 0.587 * g + 0.114 * b
    note = ""
    if strong_red.any() and strong_green.any():
        dr = lum[strong_red].mean()
        dg = lum[strong_green].mean()
        if abs(dr - dg) < 30:
            note = f"red/green collapse to similar grey (Δlum={abs(dr-dg):.0f}); indistinguishable in greyscale"
    return red_frac, green_frac, note


def check(paths):
    findings = []
    if not HAVE_DEPS:
        return [("SKIP", "Pillow/numpy not installed; cannot scan figure pixels")]
    if not paths:
        return [("SKIP", "no images found to scan")]
    for p in paths:
        try:
            red_frac, green_frac, note = scan(p)
        except Exception as exc:  # noqa: BLE001 - report, don't crash the sweep
            findings.append(("SKIP", f"{os.path.basename(p)}: cannot read ({exc})"))
            continue
        name = os.path.basename(p)
        if red_frac > 0.005 and green_frac > 0.005:
            detail = f"red={red_frac*100:.1f}% green={green_frac*100:.1f}%"
            if note:
                detail += f"; {note}"
            findings.append(("PARTIAL", f"{name}: strong red AND green present ({detail}); verify colour-blind safety"))
        else:
            findings.append(("PASS", f"{name}: no problematic red-green mix"))
    return findings


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--figdir", help="directory of figure images (png/jpg/tif)")
    ap.add_argument("--images", nargs="*", help="explicit image paths")
    args = ap.parse_args(argv)

    paths = list(args.images or [])
    if args.figdir:
        for ext in ("png", "jpg", "jpeg", "tif", "tiff"):
            paths += glob.glob(os.path.join(args.figdir, f"*.{ext}"))
    paths = sorted(set(paths))

    findings = check(paths)
    worst = "PASS"
    for status, msg in findings:
        print(f"[{status}] {msg}")
        if status == "FAIL":
            worst = "FAIL"
        elif status == "PARTIAL" and worst != "FAIL":
            worst = "PARTIAL"
    print(f"== check_figures: {worst} ==")
    return 0 if worst in ("PASS", "SKIP") else (1 if worst == "PARTIAL" else 2)


if __name__ == "__main__":
    sys.exit(main())
