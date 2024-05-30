from utilities.loader import load_input
import os
import pytest

class TestLoader:
    def test_load_existing_file(self):
        existing_path = os.path.dirname(os.path.realpath(__file__))
        filename = "existing_file.txt"
        res = load_input(existing_path, filename)
        assert res == ['one', 'two', 'three']

    def test_load_non_existing_file(self):
        existing_path = os.path.dirname(os.path.realpath(__file__))
        filename = "non_existing_file.txt"

        with pytest.raises(RuntimeError) as e:
            load_input(existing_path, filename)



