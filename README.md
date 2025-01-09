# pycounts

`pycounts` is a Python package for counting words in a text file. It is lightweight, easy to use, and ideal for quick word frequency analysis.

## Installation

You can install the latest version of `pycounts` from TestPyPI:

```bash
pip install -i https://test.pypi.org/simple/ pycounts
```

Or, for local development, clone the repository and install it in editable mode:

```bash
git clone https://github.com/Shell-human/pycounts.git
cd pycounts
pip install -e .
```

## Usage

To use `pycounts`, first prepare a text file (e.g., `zen.txt`) with the content you want to analyze. Then, use the `count_words` function to get word frequencies:

```python
from pycounts import count_words

# Analyze word frequency in a text file
result = count_words("zen.txt")
print(result)
```

Sample output:
```
Counter({
    'is': 10,
    'better': 8,
    'than': 8,
    'the': 6,
    ...
})
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`pycounts` was created by Shell. It is licensed under the terms of the MIT license.

## Credits

`pycounts` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
```