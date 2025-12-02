#!/usr/bin/env python3
"""Starter script for the Python Text Processing assignment.

Features:
- Count lines, words, characters
- Show top-N most common words (case-insensitive, basic punctuation stripping)
- Simple find-and-replace that writes to an output file

Usage examples:
    python3 starter-code.py sample_text.txt --top 5
    python3 starter-code.py sample_text.txt --replace old new --out replaced.txt
"""

import argparse
import collections
import re
from pathlib import Path


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def basic_stats(text: str) -> dict:
    lines = text.splitlines()
    words = re.findall(r"\b\w+\b", text.lower())
    chars = len(text)
    return {"lines": len(lines), "words": len(words), "chars": chars}


def top_n_words(text: str, n: int = 10):
    words = re.findall(r"\b\w+\b", text.lower())
    counter = collections.Counter(words)
    return counter.most_common(n)


def find_replace(text: str, old: str, new: str) -> str:
    return text.replace(old, new)


def main():
    parser = argparse.ArgumentParser(description="Text processing starter script")
    parser.add_argument("file", help="Text file to process")
    parser.add_argument("--top", type=int, default=0, help="Show top N words")
    parser.add_argument("--replace", nargs=2, metavar=("OLD","NEW"), help="Find and replace OLD with NEW")
    parser.add_argument("--out", help="Output file for replaced text")
    args = parser.parse_args()

    path = Path(args.file)
    if not path.exists():
        print(f"File not found: {path}")
        return

    text = load_text(path)
    stats = basic_stats(text)
    print(f"Lines: {stats['lines']} | Words: {stats['words']} | Characters: {stats['chars']}")

    if args.top and args.top > 0:
        top = top_n_words(text, args.top)
        print("Top words:")
        for word, count in top:
            print(f"  {word}: {count}")

    if args.replace:
        old, new = args.replace
        out_text = find_replace(text, old, new)
        out_path = Path(args.out) if args.out else path.with_name(path.stem + "_replaced" + path.suffix)
        out_path.write_text(out_text, encoding="utf-8")
        print(f"Wrote replaced text to: {out_path}")


if __name__ == "__main__":
    main()
