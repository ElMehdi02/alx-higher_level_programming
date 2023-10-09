#!/usr/bin/python3
"""defines an inherited list class Mylist."""


class Mylist(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
