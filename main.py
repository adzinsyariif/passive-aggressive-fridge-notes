#!/usr/bin/env python3
"""Writes the fridge note entry to /output/entry.txt."""

import os

LINE = "I've counted 11 door opens to check if the leftover rice changed its mind. It hasn't. Kept at 3°C for your optimism."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
