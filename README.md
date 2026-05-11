
[![issues](https://img.shields.io/github/issues/juniors90/human-math-llm-dataset?color=teal)](https://github.com/juniors90/human-math-llm-dataset/issues)
[![GitHub contributors](https://img.shields.io/github/contributors/juniors90/human-math-llm-dataset?color=green)](https://github.com/juniors90/human-math-llm-dataset/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/juniors90/human-math-llm-dataset)](https://github.com/juniors90/human-math-llm-dataset/stargazers)
[![star](https://img.shields.io/github/stars/juniors90/human-math-llm-dataset?color=yellow)](https://github.com/juniors90/human-math-llm-dataset/network/members)

# The human-math-llm-dataset

A high-quality dataset for training and evaluating mathematical large language models (LLMs), focused on abstract algebra problems and rigorous human-style solutions inspired by Hungerford's Abstract Algebra.

The dataset emphasizes:

- Step-by-step proofs
- Formal mathematical reasoning
- Algebraic structures and theorem proving
- Human-readable derivations
- Fine-tuning data for math-focused LLMs

Designed for research in:

- Mathematical reasoning
- Proof generation
- Formalization
- AI-assisted mathematics
- Symbolic reasoning systems

# Developers

```
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements/dev.txt
```

## usage

```py
python scripts/build_dataset.py
```

```py
python scripts/validate_dataset.py
```

```py
python scripts/build_messages.py data/train.jsonl data/messages_train.jsonl
python scripts/build_messages.py data/test.jsonl data/messages_test.jsonl
python scripts/build_messages.py data/validation.jsonl data/messages_validation.jsonl
```

## Contact

TODO: add info on how to contact you and/or how to report issues with your
project


## Contributors

Credits goes to these peoples:

<a href="https://github.com/juniors90/human-math-llm-dataset/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=juniors90/human-math-llm-dataset" />
</a>

## License

TODO: Provide information on the license of your project.
