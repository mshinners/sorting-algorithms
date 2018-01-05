"""Test Quick sort."""

import random


def test_quicksort_with_lots_of_random_lists():
    """Test quicksort with many random lists."""
    from quicksort import quicksort

    for i in range(100):
        list_length = random.randint(0, 100)
        unsorted_list = []
        for x in range(list_length):
            unsorted_list.append(random.randint(0, 100))
        assert quicksort(unsorted_list) == sorted(unsorted_list)
