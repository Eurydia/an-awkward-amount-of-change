from ctypes import Union
import json
import math
from typing import Dict, List
from collections import Counter
from itertools import combinations


def make_awkward(
    original_amount: int,
    awkward_amount: int,
    usable_units: List[int],
) -> List[int]:

    """This create an awkward way to get to an arbitary amount.
    In this case "awkward way" means that the other party
    has to provide all of the change themselves.

    For example, I owe you $12. If I were to give you
    one $10 and three $1s, you will simply return the extra $1 back to me.
    However, if I give you one $10 and one $5, you now have to find
    two $1s to give me as change.

    This function ensure that the second case happens
    if it cannot happen the it will return and empty list instead
    of a list of integers

    Args:
        original_amount (int): The original amount of money
        awkward_amount (int): The awkward ammount of money to get to
        usable_units (List[int]): A list containing the units currency available

    Returns:
        List[int]: A list of integers containing awkward amount of change
    """
    res: List[int] = []
    for unit in usable_units:
        while True:
            res.append(unit)
            if (
                sum(res) == original_amount
                or sum(res) > awkward_amount
            ):
                res.pop(-1)
                break

    if sum(res) <= original_amount:
        return []

    return res


def main():
    # The amount of money you have to pay someone
    # change to match your
    AMOUNT = 51

    # Get units of currency from JSON file
    # change to match yours
    with open("unit.json", "r") as f:
        UNITS: List[int] = json.load(f)
        UNITS.sort(reverse=True)

    # Dictionary to the store the result
    res: Dict[int, Dict[int, int]] = {}

    for unit in UNITS:
        if AMOUNT % unit != 0:
            ceiling = math.ceil(AMOUNT / unit)
            amount_over = unit * ceiling

            if (
                not closest_amount_over
                or amount_over - AMOUNT < closest_amount_over
            ):
                closest_amount_over = amount_over

            if amount_over not in res:
                res[amount_over] = {unit: ceiling}

    # The usable units are the ones that are strictly less than
    # the pay amount.
    # This is to ensure the most amount of awkwardness.
    usable_units: List[int] = [u for u in UNITS if u < AMOUNT]

    # Iterate in the range of pay amount + 1
    # to the nearest amount that is over - 1
    for awkward_amount in range(AMOUNT + 1, min(res.keys())):
        awkward_result = make_awkward(
            AMOUNT, awkward_amount, usable_units
        )

        if awkward_result:
            combs = combinations(
                awkward_result, len(awkward_result) - 1
            )
            # All combinations of awkward result with length of n - 1
            # should be strictly less than the pay amount
            if all(sum(comb) < AMOUNT for comb in combs):
                # Finally add the result to the res dict
                res[awkward_amount] = dict(
                    Counter(awkward_result)
                )

    with open("result.json", "w") as f:
        json.dump(res, f)

    print('Your result will appear in "result.json!"')


if __name__ == "__main__":
    main()
