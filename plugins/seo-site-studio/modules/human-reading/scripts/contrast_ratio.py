#!/usr/bin/env python3
import argparse
import re
from pathlib import Path
from PIL import Image


def parse_hex(value):
    value = value.strip()
    if not value.startswith("#"):
        value = "#" + value
    if not re.fullmatch(r"#[0-9a-fA-F]{6}", value):
        raise argparse.ArgumentTypeError(f"Expected #RRGGBB, got {value}")
    return tuple(int(value[i:i+2], 16) for i in (1, 3, 5))


def rel_luminance(rgb):
    vals = []
    for channel in rgb:
        c = channel / 255.0
        vals.append(c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * vals[0] + 0.7152 * vals[1] + 0.0722 * vals[2]


def contrast_ratio(fg, bg):
    l1 = rel_luminance(fg)
    l2 = rel_luminance(bg)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def classify(ratio):
    if ratio >= 7:
        return "PASS enhanced / small text"
    if ratio >= 4.5:
        return "PASS normal text"
    if ratio >= 3:
        return "PASS large text only"
    return "FAIL"


def parse_point(value):
    parts = value.split(",")
    if len(parts) != 2:
        raise argparse.ArgumentTypeError("Expected x,y")
    return int(parts[0]), int(parts[1])


def sample_pixel(image_path, point):
    image = Image.open(image_path).convert("RGB")
    x, y = point
    if x < 0 or y < 0 or x >= image.width or y >= image.height:
        raise ValueError(f"Point {point} outside image {image.width}x{image.height}")
    return image.getpixel((x, y))


def print_result(label, fg, bg):
    ratio = contrast_ratio(fg, bg)
    print(f"{label}: fg rgb{fg} on bg rgb{bg} -> {ratio:.2f}:1 [{classify(ratio)}]")


def main():
    parser = argparse.ArgumentParser(description="Compute WCAG contrast ratio for text and background colors.")
    parser.add_argument("--fg", type=parse_hex, help="Foreground text color as #RRGGBB")
    parser.add_argument("--bg", type=parse_hex, help="Background color as #RRGGBB")
    parser.add_argument("--pairs", nargs="*", help="Pairs as '#foreground,#background'")
    parser.add_argument("--sample", type=Path, help="Image file to sample")
    parser.add_argument("--fg-point", type=parse_point, help="Foreground sample point x,y")
    parser.add_argument("--bg-point", type=parse_point, help="Background sample point x,y")
    args = parser.parse_args()

    did_work = False
    if args.fg and args.bg:
        print_result("direct", args.fg, args.bg)
        did_work = True

    for index, pair in enumerate(args.pairs or [], start=1):
        parts = pair.split(",")
        if len(parts) != 2:
            raise SystemExit(f"Invalid pair {pair!r}; expected '#fg,#bg'")
        print_result(f"pair {index}", parse_hex(parts[0]), parse_hex(parts[1]))
        did_work = True

    if args.sample or args.fg_point or args.bg_point:
        if not (args.sample and args.fg_point and args.bg_point):
            raise SystemExit("--sample requires --fg-point and --bg-point")
        fg = sample_pixel(args.sample, args.fg_point)
        bg = sample_pixel(args.sample, args.bg_point)
        print_result("sample", fg, bg)
        did_work = True

    if not did_work:
        parser.print_help()


if __name__ == "__main__":
    main()
