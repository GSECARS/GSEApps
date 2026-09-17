# SPDX-License-Identifier: MIT

from argparse import ArgumentParser
from importlib.metadata import EntryPoint, entry_points, version

__all__ = ["cmd_list", "cmd_make", "make_parser"]


COMMAND_GROUP = "gseapps.commands"
MAKE_ICONS_GROUP = "gseapps.make_icons"


def make_parser() -> ArgumentParser:
    """Builds the gseapps argument parser."""
    parser = ArgumentParser("gseapps")
    parser.add_argument("-v", "--version", action="version", version=f"gseapps {version('gseapps')}")
    parser.add_argument("-t", "--test", action="store_true", help="runs the test suite")
    parser.add_argument("-m", "--make-icons", action="store_true", help="creates desktop shortcuts for all apps in a 'GSE Apps' folder")

    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("list", help="lists available commands")

    return parser


def _load_commands() -> dict[str, EntryPoint]:
    """Returns the plugin commands registered under gseapps.commands."""
    return {ep.name: ep for ep in entry_points(group=COMMAND_GROUP)}


def _print_rows(rows: list[tuple[str, str]]) -> None:
    """Prints left-aligned name/description rows."""
    width = max(len(name) for name, _ in rows)
    for name, description in rows:
        print(f"  {name:<{width}}  {description}")


def cmd_make() -> int:
    """Creates desktop shortcuts for all installed apps in a 'GSE Apps' folder."""
    makers = {ep.name: ep for ep in entry_points(group=MAKE_ICONS_GROUP)}
    if not makers:
        print("No apps with shortcut support installed.")
        return 0

    print(f"GSE Apps {version('gseapps')}\n")
    for name, ep in sorted(makers.items()):
        ep.load()(folder="GSE Apps")
        print(f"Created shortcut: {name}")

    return 0


def cmd_list() -> int:
    """Prints built-in and installed plugin commands."""
    commands = _load_commands()
    rows = [("list", "lists available commands")]
    rows.extend((name, "") for name in sorted(commands))

    print(f"GSE Apps {version('gseapps')}\n")
    _print_rows(rows)
    if not commands:
        print("\nNo plugins installed.")

    return 0
