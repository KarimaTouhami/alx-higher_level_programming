#!/usr/bin/python3
"""Module for write_file method."""


def write_file(filename="", text=""):
    """ func """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
