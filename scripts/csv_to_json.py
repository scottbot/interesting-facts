#!/usr/bin/env python3
"""Extract only verified facts for the public site."""

import argparse
import csv
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file", type=Path)
    parser.add_argument("json_file", type=Path)
    args = parser.parse_args()

    with args.csv_file.open(encoding="utf-8-sig", newline="") as source:
        rows = list(csv.DictReader(source))

    facts = []
    excluded = 0
    for row in rows:
        if row["Accuracy"].strip().lower() != "accurate":
            excluded += 1
            continue
        facts.append(
            {
                "fact": row["Fact (verbatim)"],
                "name": row["Name"],
                "handle": row["Bluesky account"],
            }
        )

    args.json_file.parent.mkdir(parents=True, exist_ok=True)
    args.json_file.write_text(
        json.dumps(facts, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"Wrote {len(facts)} accurate facts to {args.json_file}; "
        f"excluded {excluded} rows not marked accurate."
    )


if __name__ == "__main__":
    main()
