"""Test merge sort."""


import random


def test_mergesort_sorts_list():
    """Test mergesort sorts list."""
    from mergesort import mergesort
    unsorted_list = [3, 4, 2, 1, 5, 19]
    assert mergesort(unsorted_list) == [1, 2, 3, 4, 5, 19]


def test_mergesort_on_long_list():
    """Test mergesort on long list."""
    from mergesort import mergesort
    unsorted_list = []
    for i in range(100):
        unsorted_list.append(random.randint(0, 1000))

    sorted_list = mergesort(unsorted_list)

    assert sorted_list == sorted(unsorted_list)
