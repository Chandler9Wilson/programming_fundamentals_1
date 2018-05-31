import os
import subprocess
import json

import pytest

# File to be tested
from labs.print_errors_L1 import TT18_L1_Wilson as print_errors

# File to compare against
path_to_expected = 'labs/print_errors_L1/test/expected_output.json'

# Absolute Path to module to be tested
print_errors_path = os.path.abspath(print_errors.__file__)


def run_and_split():
    print_result = subprocess.run(
        ['python', print_errors_path], stdout=subprocess.PIPE)
    print_output = print_result.stdout

    output_list = print_output.splitlines()

    return output_list


def load_json(path_to_expected):
    with open(path_to_expected) as expected:
        expected_output = json.load(expected)

    return expected_output


def test_prints():
    output_list = run_and_split()
    expected_output = load_json(path_to_expected)

    for index, print_line in enumerate(output_list):
        assert str(print_line, 'utf-8') == expected_output[index]
