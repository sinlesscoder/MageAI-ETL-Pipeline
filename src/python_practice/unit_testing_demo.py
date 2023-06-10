import pytest
import pandas as pd

# Test: Is the number odd?

some_value = 4

df = pd.DataFrame.from_dict({'key_1': ['value_1', 'value_2'], 'key_2': ['value_3', 'value_4']})

# Unit Tests
def test_isodd():
    # Assertion
    assert some_value % 2 != 0

def test_key3():
    # Assertion
    assert 'key_2' in df.columns

