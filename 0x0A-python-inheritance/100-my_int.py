#!/usr/bin/python3
"""Creates a class that inherits from int."""


class MyInt(int):
    """Defines class inheriting from int"""

    def __eq__(self, other):
        """Override == op with != op"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override != op with == op"""
        return super().__eq__(other)
