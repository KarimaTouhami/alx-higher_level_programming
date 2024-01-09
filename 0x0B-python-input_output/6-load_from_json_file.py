#!/usr/bin/python3
"""Module for load_from_json_file method."""
import json


def load_from_json_file(filename):
    """ func """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
