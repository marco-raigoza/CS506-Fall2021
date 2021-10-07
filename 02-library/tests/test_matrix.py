# import pytest
import random

from cs506 import matrix


def test_matrix():
    assert matrix.get_determinate([[4,6],[3,8]]) == 14
    assert matrix.get_determinate([[6,1,1],[4,-2,5],[2,8,7]]) == -306
    # edge case of 5 x 5 matrix
    assert matrix.get_determinate([[1,3,5,5,5],[0,9,8,6,5],[8,6,5,6,9],[7,6,7,9,7],[5,7,97,5,4]]) == 80276