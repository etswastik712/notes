"""Render a PDF of page images into numbered contact sheets for quick visual triage.

usage: contact_sheet.py <pdf> <out_prefix> [cols=4] [rows=3] [thumb_w=520]
Writes <out_prefix>-01.jpg, <out_prefix>-02.jpg, ...  (page numbers are PDF page indices, 1-based)
"""
import sys

import fitz  # PyMuPDF
from PIL import Image, ImageDraw


def main(pdf, prefix, cols=4, rows=3, tw=520):
    doc = fitz.open(pdf)
    thumbs = []
    for i, page in enumerate(doc, 1):
        zoom = tw / page.rect.width
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
        im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        d = ImageDraw.Draw(im)
        d.rectangle((0, 0, 46, 26), fill=(0, 0, 0))
        d.text((6, 6), f"p{i}", fill=(255, 255, 0))
        thumbs.append(im)
    th = max(t.height for t in thumbs)
    per = cols * rows
    for s in range(0, len(thumbs), per):
        sheet = Image.new("RGB", (cols * tw, rows * th), (30, 30, 30))
        for k, t in enumerate(thumbs[s:s + per]):
            sheet.paste(t, ((k % cols) * tw, (k // cols) * th))
        out = f"{prefix}-{s // per + 1:02d}.jpg"
        sheet.save(out, quality=70)
        print(out)


if __name__ == "__main__":
    a = sys.argv
    main(a[1], a[2], *(int(x) for x in a[3:]))
