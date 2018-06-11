import os
import subprocess
import json

import pytest

# File to be tested
from labs.IPO_L2 import TT18_L2_Wilson as ipo_lab

# Absolute Path to module to be tested
ipo_labs_path = os.path.abspath(ipo_lab.__file__)


@pytest.fixture
def ipo_fixture():

    def _run_ipo_lab(option_number, input_list):
        """A reusable fixture for running the IPO lab

        Args:
            option_number (int): This is the opening option number selected
                used to select which part of the program to run.
            input_list (list): The list of input values based on what
                ``option_number`` was given
        """
        return [option_number, input_list]

    return _run_ipo_lab


def test_mpg_calculation(ipo_fixture):
    # Ask for and get the vehicle make and model. These are separate items.
    # Ask for and get the amount of miles traveled.
    # Ask for and get the number of gallons used.
    # Calculate the gas mileage.
    # Output the results.
    # Include: vehicle make and model, miles traveled, gallons used, mileage.

    result = ipo_fixture(3, [1, 2, 3])

    assert result == [3, [1, 2, 3]]
