from typing import List, Literal

from pydantic import BaseModel, Field


class MathProblem(BaseModel):

    id: str = Field(
        pattern=r"^problem_\d+$"
    )

    domain: Literal[
        "mathematics",
        "physics",
        "computer_science"
    ]

    subdomain: str = Field(
        min_length=2
    )

    task_type: Literal[
        "proof",
        "computation",
        "classification",
        "counterexample"
    ]

    problem: str = Field(
        min_length=10
    )

    solution: str = Field(
        min_length=10
    )

    source: Literal[
        "human-written",
        "synthetic",
        "translated"
    ]

    authors: List[str] = Field(
        min_length=1
    )

    license: str

