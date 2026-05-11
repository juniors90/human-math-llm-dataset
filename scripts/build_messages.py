#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of the human-math-llm-dataset Project
#    (https://github.com/juniors90/human-math-llm-dataset/).
# Copyright (c) 2026, Ferreira Juan David
# License: MIT
# Full Text:
#    https://github.com/juniors90/human-math-llm-dataset/blob/master/LICENSE

# =============================================================================
# DOCS
# =============================================================================

"""human-math-llm-dataset

A high-quality dataset for training and evaluating
mathematical large language models (LLMs), focused on
abstract algebra problems and rigorous human-style
solutions inspired by Hungerford's Abstract Algebra.

build_messages.py

Converts JSONL problem/solution files to JSONL chat message files.
Each line in the input field is JSON:
{"id": "...", "domain": "...", "problem": "...", "solution": "...", ...}

Each line in output will be:
{"messages": [{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}
"""

# =============================================================================
# IMPORTS
# =============================================================================

import json
import sys
from pathlib import Path


def build_message(problem_json):
    user_content = (
        f"Domain: {problem_json.get('domain','')}\n"
        f"Subdomain: {problem_json.get('subdomain','')}\n"
        f"Task type: {problem_json.get('task_type','')}\n\n"
        f"{problem_json.get('problem','')}"
    )

    assistant_content = problem_json.get("solution", "")

    return {
        "messages": [
            {"role": "user", "content": user_content},
            {"role": "assistant", "content": assistant_content},
        ]
    }


def main(input_path, output_path):
    input_file = Path(input_path)
    output_file = Path(output_path)

    if not input_file.exists():
        print(f"Error: {input_file} does not exist.")
        sys.exit(1)

    with (
        open(input_file, "r", encoding="utf-8") as fin,
        open(output_file, "w", encoding="utf-8") as fout,
    ):
        for line in fin:
            line = line.strip()
            if not line:
                continue
            try:
                problem_json = json.loads(line)
                messages_json = build_message(problem_json)
                fout.write(json.dumps(messages_json, ensure_ascii=False) + "\n")
            except json.JSONDecodeError as e:
                print(f"Skipping line due to JSON error: {e}")
                continue

    print(f"Messages generated in {output_file}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            "Use: python build_messages.py data/train.jsonl data/messages_train.jsonl"
        )
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
