<h1 align="center">
  &nbsp;GSEApps
</h1>

[![License](https://img.shields.io/badge/License-MIT-teal.svg)](LICENSE.txt) [![Python](https://img.shields.io/badge/Python-3.14-22558a.svg?logo=python&color=22558a)](https://www.python.org/)
[![Tests](https://github.com/gsecars/gseapps/actions/workflows/test.yml/badge.svg)](https://github.com/gsecars/gseapps/actions/workflows/test.yml)

GSEApps is a collection of scientific tools and applications used at GSECARS. Each tool is a standalone Python package that can be installed on its own, or together through this CLI package.
Plugins register as subcommands once their package is installed. This way GSECARS applications stay in their own repositories.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contribution](#contribution)
- [License](#license)

## Installation
To set up the project for development, clone the repository and install the development group. The pre-commit hooks need to be installed as well. The following command assumes that
`uv` is used for development. See the [uv installation guide](https://docs.astral.sh/uv/getting-started/installation/).

```bash
git clone https://github.com/gsecars/gseapps.git && cd gseapps && git checkout development && uv sync --group dev && uv run pre-commit install
```

## Usage
```bash
uv run gseapps --help
uv run gseapps --version
uv run gseapps --test
uv run gseapps list
```

A plugin is a separate package. It registers an entry point under `gseapps.commands` and can also ship its own command. This repository only declares optional extras, for example `gseapps[all]`,
when those packages exist.

## Contribution
Read more [here](CONTRIBUTING.md) for contribution guidance.

## License
GSEApps is distributed under the MIT License. You should have received a [copy](LICENSE.txt) of the MIT License along with this program. If not, see https://mit-license.org/ for additional details.

