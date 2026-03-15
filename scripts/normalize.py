#!/usr/bin/env python3
"""
normalize.py

Normalizes Bible translation JSON files to a unified schema.
Reads from data/00_raw/, writes to data/01_structured/.

Input schemas handled:
  A) {translation, books[{name, chapters[{chapter, verses[{verse, text}]}]}]}
  B) [{abbrev, chapters[[strings]]}]  (no book name, verses are plain strings)
  C) [{abbrev, name, chapters[[strings]]}]  (has book name, verses are plain strings)

Output schema (always):
  {translation, books[{name, chapters[{chapter, verses[{verse, text}]}]}]}

Usage:
    python scripts/normalize.py
    python scripts/normalize.py --dry-run
"""

import argparse
import json
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
RAW_DIR = REPO_ROOT / "data" / "00_raw"
OUT_DIR = REPO_ROOT / "data" / "01_structured"

ABBREV_TO_NAME = {
    "Gn": "Genesis", "Ex": "Exodus", "Lv": "Leviticus", "Nm": "Numbers",
    "Dt": "Deuteronomy", "Js": "Joshua", "Jd": "Judges", "Rt": "Ruth",
    "1Sm": "1 Samuel", "2Sm": "2 Samuel", "1Rs": "1 Kings", "2Rs": "2 Kings",
    "1Cr": "1 Chronicles", "2Cr": "2 Chronicles", "Ed": "Ezra", "Ne": "Nehemiah",
    "Et": "Esther", "Jó": "Job", "Sl": "Psalms", "Pv": "Proverbs",
    "Ec": "Ecclesiastes", "Ct": "Song of Solomon", "Is": "Isaiah",
    "Jr": "Jeremiah", "Lm": "Lamentations", "Ez": "Ezekiel", "Dn": "Daniel",
    "Os": "Hosea", "Jl": "Joel", "Am": "Amos", "Ob": "Obadiah", "Jn": "Jonah",
    "Mq": "Micah", "Na": "Nahum", "Hc": "Habakkuk", "Sf": "Zephaniah",
    "Ag": "Haggai", "Zc": "Zechariah", "Ml": "Malachi",
    "Mt": "Matthew", "Mc": "Mark", "Lc": "Luke", "Jo": "John", "At": "Acts",
    "Rm": "Romans", "1Co": "1 Corinthians", "2Co": "2 Corinthians",
    "Gl": "Galatians", "Ef": "Ephesians", "Fp": "Philippians", "Cl": "Colossians",
    "1Ts": "1 Thessalonians", "2Ts": "2 Thessalonians",
    "1Tm": "1 Timothy", "2Tm": "2 Timothy", "Tt": "Titus", "Fm": "Philemon",
    "Hb": "Hebrews", "Tg": "James", "1Pe": "1 Peter", "2Pe": "2 Peter",
    "1Jo": "1 John", "2Jo": "2 John", "3Jo": "3 John", "Ap": "Revelation",
    "Ge": "Genesis", "Le": "Leviticus", "Nu": "Numbers", "De": "Deuteronomy",
    "Jos": "Joshua", "Jud": "Judges", "Ru": "Ruth", "1Sa": "1 Samuel",
    "2Sa": "2 Samuel", "1Ki": "1 Kings", "2Ki": "2 Kings", "1Ch": "1 Chronicles",
    "2Ch": "2 Chronicles", "Ezr": "Ezra", "Es": "Esther", "Job": "Job",
    "Ps": "Psalms", "Pr": "Proverbs", "Ecc": "Ecclesiastes", "So": "Song of Solomon",
    "Isa": "Isaiah", "Jer": "Jeremiah", "La": "Lamentations", "Eze": "Ezekiel",
    "Da": "Daniel", "Ho": "Hosea", "Joe": "Joel", "Jon": "Jonah", "Mic": "Micah",
    "Nah": "Nahum", "Hab": "Habakkuk", "Zep": "Zephaniah", "Hag": "Haggai",
    "Zec": "Zechariah", "Mal": "Malachi", "Mr": "Mark", "Lu": "Luke",
    "Joh": "John", "Ac": "Acts", "Ro": "Romans", "Ga": "Galatians",
    "Eph": "Ephesians", "Php": "Philippians", "Col": "Colossians",
    "1Th": "1 Thessalonians", "2Th": "2 Thessalonians", "1Ti": "1 Timothy",
    "2Ti": "2 Timothy", "Tit": "Titus", "Phm": "Philemon", "Heb": "Hebrews",
    "Jas": "James", "Jude": "Jude", "Re": "Revelation",
}


def normalize_file(raw_path: Path, out_path: Path, dry_run: bool) -> str:
    with open(raw_path, encoding="utf-8") as f:
        data = json.load(f)

    version = raw_path.stem

    if isinstance(data, dict) and "books" in data and "translation" in data:
        if not dry_run:
            out_path.parent.mkdir(parents=True, exist_ok=True)
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        n_books = len(data["books"])
        n_verses = sum(
            len(ch.get("verses", []))
            for b in data["books"]
            for ch in b.get("chapters", [])
        )
        return f"Schema A (copy) — {n_books} books, {n_verses} verses"

    if isinstance(data, list):
        books = []
        for book_data in data:
            abbrev = book_data.get("abbrev", "")
            name = book_data.get("name", ABBREV_TO_NAME.get(abbrev, abbrev))
            chapters = []
            for ch_idx, ch_data in enumerate(book_data.get("chapters", []), 1):
                if isinstance(ch_data, list):
                    verses = [
                        {"verse": i, "text": text}
                        for i, text in enumerate(ch_data, 1)
                    ]
                    chapters.append({"chapter": ch_idx, "verses": verses})
                elif isinstance(ch_data, dict):
                    chapters.append(ch_data)
            books.append({"name": name, "chapters": chapters})

        normalized = {"translation": version, "books": books}
        n_verses = sum(len(ch["verses"]) for b in books for ch in b["chapters"])

        if not dry_run:
            out_path.parent.mkdir(parents=True, exist_ok=True)
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(normalized, f, ensure_ascii=False, indent=2)

        return f"Converted — {len(books)} books, {n_verses} verses"

    return "Unknown schema"


def main():
    parser = argparse.ArgumentParser(description="Normalize Bible JSONs to unified schema")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    print(f"{'[DRY RUN] ' if args.dry_run else ''}Normalizing {RAW_DIR} -> {OUT_DIR}")

    for lang_dir in sorted(RAW_DIR.iterdir()):
        if not lang_dir.is_dir():
            continue
        print(f"\n{lang_dir.name}/")
        for f in sorted(lang_dir.glob("*.json")):
            out = OUT_DIR / lang_dir.name / f.name
            result = normalize_file(f, out, args.dry_run)
            print(f"  {f.name}: {result}")


if __name__ == "__main__":
    main()
