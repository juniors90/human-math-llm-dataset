#!/usr/bin/env python3
"""
build_messages.py

Convierte archivos JSONL de problema/solución a JSONL de mensajes de chat.
Cada línea en input es un JSON:
{"id": "...", "domain": "...", "problem": "...", "solution": "...", ...}

Cada línea en output será:
{"messages": [{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}
"""

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

    assistant_content = problem_json.get('solution', '')

    return {
        "messages": [
            {"role": "user", "content": user_content},
            {"role": "assistant", "content": assistant_content}
        ]
    }

def main(input_path, output_path):
    input_file = Path(input_path)
    output_file = Path(output_path)

    if not input_file.exists():
        print(f"Error: {input_file} does not exist.")
        sys.exit(1)

    with open(input_file, "r", encoding="utf-8") as fin, \
         open(output_file, "w", encoding="utf-8") as fout:
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

    print(f"Mensajes generados en {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python build_messages.py data/train.jsonl data/messages_train.jsonl")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
