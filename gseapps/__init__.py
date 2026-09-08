# SPDX-License-Identifier: MIT

from importlib.metadata import version

from gseapps.utils import cmd_list, make_parser

__version__ = version("gseapps")
__all__ = ["__version__", "main"]


def main() -> None:
    """Runs the gseapps CLI."""

    parser = make_parser()
    args = parser.parse_args()

    if args.test:
        import pytest

        raise SystemExit(pytest.main([]))

    if args.command == "list":
        raise SystemExit(cmd_list())

    parser.print_help()
