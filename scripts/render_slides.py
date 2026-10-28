"""Render slide decks to auto-cropped JPEGs for embedding: Assets/crops/ls/<deck>_<nnn>.jpg
usage: render_slides.py <pdf> <prefix> [width=1300] [first] [last]"""
import os, sys
import fitz
from PIL import Image, ImageChops

def autocrop(im, pad=14, bg_tol=12):
    bg = Image.new(im.mode, im.size, (255, 255, 255))
    diff = ImageChops.difference(im, bg).convert("L").point(lambda p: 255 if p > bg_tol else 0)
    bbox = diff.getbbox()
    if not bbox:
        return im
    x0, y0, x1, y1 = bbox
    return im.crop((max(0, x0 - pad), max(0, y0 - pad), min(im.width, x1 + pad), min(im.height, y1 + pad)))

def main(pdf, prefix, width=1300, first=1, last=None):
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Assets", "crops", "ls")
    os.makedirs(out, exist_ok=True)
    doc = fitz.open(pdf)
    last = last or len(doc)
    for i in range(first, last + 1):
        page = doc[i - 1]
        z = width / page.rect.width
        pix = page.get_pixmap(matrix=fitz.Matrix(z, z), alpha=False)
        im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        im = autocrop(im)
        im.save(os.path.join(out, f"{prefix}_{i:03d}.jpg"), quality=72, optimize=True)
    print("done", prefix, first, last)

if __name__ == "__main__":
    a = sys.argv
    main(a[1], a[2], int(a[3]) if len(a) > 3 else 1300, int(a[4]) if len(a) > 4 else 1, int(a[5]) if len(a) > 5 else None)
