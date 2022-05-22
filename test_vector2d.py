#
# File: test_vector2d.py
# Author: Annabelle
# Student Id: 518577
# Email Id: 518577@eynesbury.sa.edu.au
# Date: 06/11/2021
# Description: This is my program.
# This is my own work as defined by the University's
# Academic Misconduct policy
import pytest
from game import Vector2D


@pytest.fixture()
def valid_vector2D():
    """This file is for test the Vector2D class
    First fixture Vector2D
    """
    return Vector2D(2, 5)


def test_add(valid_vector2D):
    """Test the add function in Vector2D."""
    other = Vector2D(3, 0)
    v1 = Vector2D(5, 5)
    assert valid_vector2D.add(other) == v1
    with pytest.raises(TypeError):
        valid_vector2D.add('Hello')


def test_subtract(valid_vector2D):
    """Test the subtract function in Vector2D."""
    other = Vector2D(2, 0)
    v1 = Vector2D(0, 5)
    assert valid_vector2D.subtract(other) == v1
    with pytest.raises(TypeError):
        valid_vector2D.subtract(True)


def test_scale(valid_vector2D):
    """Test the scale function in Vector2D."""
    v1 = Vector2D(4, 10)
    assert valid_vector2D.scale(2) == v1
    with pytest.raises(TypeError):
        valid_vector2D.scale(True)


@pytest.fixture()
def valid_vector2D2():
    """fixture Vector2D
    """
    return Vector2D(-31, 5)


def test_length(valid_vector2D):
    """Test the length function in Vector2D.
    """
    assert valid_vector2D.length() == pytest.approx(5.38516)


def test_length2(valid_vector2D2):
    """Test the length function in Vector2D.
    """
    assert valid_vector2D2.length() == pytest.approx(31.4006369)


def test_distance(valid_vector2D):
    """Test the distance function in Vector2D.
    """
    v1 = Vector2D(3, 0)
    assert valid_vector2D.distance(v1) == pytest.approx(5.099019)
    with pytest.raises(TypeError):
        valid_vector2D.distance(True)


def test_normalize(valid_vector2D):
    """Test the normalize function in Vector2D.
    """
    v1 = Vector2D(0.3713906763541037, 0.9284766908852594)
    assert valid_vector2D.normalize() == v1


def test_normalize2(valid_vector2D2):
    """Test the normalize function in Vector2D.
    """
    v1 = Vector2D(-0.9872411207126471, 0.1592324388246205)
    assert valid_vector2D2.normalize() == v1


if __name__ == '__main__':
    pytest.main()
