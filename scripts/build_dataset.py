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
"""

# =============================================================================
# META
# =============================================================================

__version__ = "1.0.0"

# =============================================================================
# IMPORTS
# =============================================================================

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NOTES = ROOT / "notes"
PROBLEMS = NOTES / "problem"
SOLUTIONS = NOTES / "solution"
DATA = ROOT / "data"

PROBLEMS = ROOT / "notes" / "problem"


def generar_ids_numericos(problems_path, train_ratio=0.8, valid_ratio=0.1):
    """
    Automatically generates numeric IDs for train/valid/test based on the
    number of files in the problems folder.

    Args:
        problems_path (Path): Folder where the problems are located.
        train_ratio (float): Percentage of files for training.
        valid_ratio (float): Percentage of files for validation.

    Returns:
        tuple: (TRAIN_IDS, VALID_IDS, TEST_IDS)
    """
    archivos = sorted(problems_path.glob("*.tex"))  # Lista de archivos .tex
    total = len(archivos)

    # Crear IDs numéricos con 3 dígitos
    ids = [f"{i+1:03}" for i in range(total)]

    n_train = int(total * train_ratio)
    n_valid = int(total * valid_ratio)
    n_test = total - n_train - n_valid

    TRAIN_IDS = set(ids[:n_train])
    VALID_IDS = set(ids[n_train : n_train + n_valid])
    TEST_IDS = set(ids[n_train + n_valid :])

    return TRAIN_IDS, VALID_IDS, TEST_IDS


# Use
train_ids, valid_ids, test_ids = generar_ids_numericos(
    PROBLEMS, train_ratio=0.8, valid_ratio=0.1
)

print("TRAIN_IDS =", train_ids)
print("VALID_IDS =", valid_ids)
print("TEST_IDS =", test_ids)


TRAIN_IDS = train_ids
VALID_IDS = valid_ids
TEST_IDS = test_ids  # set()


def read_tex(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


splits = {"train": [], "validation": [], "test": []}

problems = sorted(PROBLEMS.glob("problem_*.tex"))

for prob_path in problems:
    idx = prob_path.stem.replace("problem_", "")
    sol_path = SOLUTIONS / f"solution_{idx}.tex"

    if not sol_path.exists():
        raise FileNotFoundError(f"Missing solution for {prob_path.name}")

    record = {
        "id": f"problem_{idx}",
        "domain": "mathematics",
        "subdomain": "algebra",
        "task_type": "proof",
        "problem": read_tex(prob_path),
        "solution": read_tex(sol_path),
        "source": "human-written",
        "authors": ["Juan David Ferreira"],
        "license": "CC-BY-4.0",
    }

    if idx in TRAIN_IDS:
        splits["train"].append(record)
    elif idx in VALID_IDS:
        splits["validation"].append(record)
    elif idx in TEST_IDS:
        splits["test"].append(record)
    else:
        raise ValueError(f"ID {idx} not assigned to any split")

DATA.mkdir(exist_ok=True)

for split, records in splits.items():
    out_path = DATA / f"{split}.jsonl"
    with open(out_path, "w", encoding="utf-8") as f:
        for r in records:
            json.dump(r, f, ensure_ascii=False)
            f.write("\n")

print("Generated dataset:")
for split, records in splits.items():
    print(f"  {split}: {len(records)} examples")
