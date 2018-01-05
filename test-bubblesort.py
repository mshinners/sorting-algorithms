"""Test bubblesort."""

import random


def test_bubblesort_sorts_list():
    """Test bubblesort sorts list of vals."""
    from bubblesort import bubblesort
    unsorted_list = [3, 4, 2, 1, 5, 19]
    assert bubblesort(unsorted_list) == [1, 2, 3, 4, 5, 19]


def test_bubblesort_on_long_list():
    """Test bubblesort on a long list."""
    from bubblesort import bubblesort
    unsorted_list = []
    for i in range(100):
        unsorted_list.append(random.randint(0, 1000))

    sorted_list = bubblesort(unsorted_list)

    assert sorted_list == sorted(unsorted_list)
