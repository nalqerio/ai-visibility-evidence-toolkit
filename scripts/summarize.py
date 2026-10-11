"""Summarize a documented sample; no network or third-party dependencies."""
import argparse
import csv
import json
from pathlib import Path


def ratio(numerator, denominator):
    return {"numerator": numerator, "denominator": denominator,
            "percent": round(100 * numerator / denominator, 2) if denominator else None}


def summarize(rows):
    required = {"question_id", "response_status", "brand_mention", "citation_status", "own_citation_url"}
    for number, row in enumerate(rows, start=2):
        if not required.issubset(row):
            raise ValueError(f"Row {number}: missing required columns")
        if not row["question_id"].strip():
            raise ValueError(f"Row {number}: question_id must not be blank")
        for key, allowed in (
            ("response_status", {"completed", "failed", "missing"}),
            ("brand_mention", {"yes", "no", "unknown"}),
            ("citation_status", {"available", "unavailable"}),
        ):
            if row[key] not in allowed:
                raise ValueError(f"Row {number}: invalid {key}")
        if row["response_status"] != "completed" and row["brand_mention"] != "unknown":
            raise ValueError(f"Row {number}: a failed/missing answer must have unknown brand_mention")
        if row["own_citation_url"].strip() and (row["citation_status"] != "available" or row["response_status"] != "completed"):
            raise ValueError(f"Row {number}: citation URL requires an available completed answer")

    returned = [r for r in rows if r["response_status"] == "completed"]
    evaluable = [r for r in returned if r["brand_mention"] in {"yes", "no"}]
    mentioned = [r for r in evaluable if r["brand_mention"] == "yes"]
    citations = [r for r in returned if r["citation_status"] == "available"]
    return {
        "observations": len(rows),
        "completed_answers": len(returned),
        "failed_or_missing_answers": len(rows) - len(returned),
        "unknown_mention_answers": len(returned) - len(evaluable),
        "answer_mention_rate": ratio(len(mentioned), len(evaluable)),
        "question_coverage": ratio(len({r["question_id"] for r in mentioned}), len({r["question_id"] for r in evaluable})),
        "owned_citation_rate": ratio(sum(bool(r["own_citation_url"].strip()) for r in citations), len(citations)),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", type=Path)
    args = parser.parse_args()
    try:
        with args.csv_file.open(encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)
            required = {"question_id", "response_status", "brand_mention", "citation_status", "own_citation_url"}
            if not required.issubset(reader.fieldnames or []):
                raise ValueError("Missing required CSV headers")
            result = summarize(list(reader))
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
