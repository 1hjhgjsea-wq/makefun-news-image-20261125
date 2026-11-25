"""Entry point for the 25 November 2026 world-news image.

Builds the front-page infographic with draw_infographic.py and writes it
to /output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png). Deterministic:
no network, no clock, no randomness, so repeated runs are byte-identical.
Standard library plus Pillow only.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from draw_infographic import build

MAX_BYTES = 1048576  # 1 MiB, per the kit's rules
EXPECTED_SIZE = (1024, 1024)
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def validate(path):
    """Enforce the kit's image constraints at run time.

    Raises ValueError when the file is not a whole 1024x1024 PNG within
    the 1 MiB limit, so a bad image can never be submitted silently.
    """
    with open(path, "rb") as fh:
        data = fh.read()
    if data[:8] != PNG_MAGIC:
        raise ValueError("entry.png is not a PNG file")
    if len(data) > MAX_BYTES:
        raise ValueError(
            "entry.png is %d bytes, over the 1 MiB limit" % len(data))
    from PIL import Image
    with Image.open(path) as img:
        if img.size != EXPECTED_SIZE:
            raise ValueError(
                "entry.png is %s, expected 1024x1024" % (img.size,))
        img.load()  # proves every chunk and its checksums are intact
    return len(data)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    img = build()
    img.save(out_path, format="PNG")
    size = validate(out_path)
    print("wrote %s (%d bytes, 1024x1024 PNG)" % (out_path, size))


if __name__ == "__main__":
    main()
