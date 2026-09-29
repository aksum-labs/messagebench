from itertools import combinations, permutations

from aksum_messagebench.errors import PRECEDENCE, aggregate_exit


def test_all_exit_combinations_and_order_independence():
    assert aggregate_exit([]) == 3
    for size in range(1, 7):
        for subset in combinations(PRECEDENCE, size):
            for order in permutations(subset):
                assert aggregate_exit(list(order)) == subset[0]
