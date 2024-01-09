#!/usr/bin/python3
"""Module for append_write method."""


def append_write(filename="", text=""):
    """ func """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
