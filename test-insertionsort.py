"""Test insertion sort."""

import random


def test_insertionsort_sorts_list():
    """Test insertionsort sorts list of vals."""
    from insertionsort import insertionsort
    unsorted_list = [3, 4, 2, 1, 5, 19]
    assert insertionsort(unsorted_list) == [1, 2, 3, 4, 5, 19]


def test_insertionsort_on_long_list():
    """Test insertionsort on long list."""
    from insertionsort import insertionsort
    unsorted_list = []
    for i in range(100):
        unsorted_list.append(random.randint(0, 1000))

    sorted_list = insertionsort(unsorted_list)

    assert sorted_list == sorted(unsorted_list)
