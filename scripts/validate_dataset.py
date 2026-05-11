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

validate_dataset.py
"""

import json
import sys
from pathlib import Path

from pydantic import ValidationError

# Add the project's root directory to the PYTHONPATH
directory = Path(__file__).resolve()
sys.path.append(str(directory.parent.parent))

from schema import MathProblem

DATASET_FILES = [
    Path("data/train.jsonl"),
    Path("data/validation.jsonl"),
    Path("data/test.jsonl"),
]


def validate_file(filepath: Path):

    print(f"\nValidating: {filepath}")

    valid_examples = 0
    invalid_examples = 0

    ids = set()

    with open(filepath, "r", encoding="utf-8") as f:

        for line_number, line in enumerate(f, start=1):

            try:

                data = json.loads(line)

                problem = MathProblem.model_validate(data)

                # duplicate id check
                if problem.id in ids:
                    raise ValueError(f"Duplicate id detected: {problem.id}")

                ids.add(problem.id)

                valid_examples += 1

            except ValidationError as e:

                invalid_examples += 1

                print(f"\n[VALIDATION ERROR]")
                print(f"File: {filepath}")
                print(f"Line: {line_number}")

                print(e)

            except Exception as e:

                invalid_examples += 1

                print(f"\n[ERROR]")
                print(f"File: {filepath}")
                print(f"Line: {line_number}")

                print(e)

    print("\n-------------------------")
    print(f"Valid examples:   {valid_examples}")
    print(f"Invalid examples: {invalid_examples}")
    print("-------------------------")


def main():

    for filepath in DATASET_FILES:

        if filepath.exists():
            validate_file(filepath)
        else:
            print(f"Missing file: {filepath}")


if __name__ == "__main__":
    main()
