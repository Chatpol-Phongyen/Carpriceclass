from contextvars import copy_context
from dash._callback_context import context_value
from dash._utils import AttributeDict
import random
import numpy as np


# Import the names of callback functions you want to test
from app import features_size, output_size

max_power1 = random.sample(sorted(np.arange(0, 500.02, 0.02)), 1)[0]
mileage1 = random.sample(sorted(np.arange(0, 80.02, 0.02)), 1)[0]
km_driven1 = random.sample(sorted(np.arange(0, 10000001)), 1)[0]
year1 = random.sample(sorted(np.arange(2011, 2024)), 1)[0]

def test_size_input_callback():
    expected_input = features_size(max_power1, mileage1, km_driven1, year1)
    assert expected_input == f'Shape of inputs is (4, 1)'

def test_size_output_callback():
    size_output = output_size(max_power1, mileage1, km_driven1, year1)
    assert size_output == f'Shape of output is (1,)'