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

schema.py
"""

# =============================================================================
# IMPORTS
# =============================================================================

from typing import List, Literal

from pydantic import BaseModel, Field


class MathProblem(BaseModel):

    id: str = Field(pattern=r"^problem_\d+$")

    domain: Literal["mathematics", "physics", "computer_science"]

    subdomain: str = Field(min_length=2)

    task_type: Literal["proof", "computation", "classification", "counterexample"]

    problem: str = Field(min_length=10)

    solution: str = Field(min_length=10)

    source: Literal["human-written", "synthetic", "translated"]

    authors: List[str] = Field(min_length=1)

    license: str
