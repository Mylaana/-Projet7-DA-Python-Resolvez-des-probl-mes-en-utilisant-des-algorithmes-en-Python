"""
bruteforce solution for the best share's value combination
"""
from itertools import combinations
from csv_loader import get_list_from_csv

MAX_COST = 500


def get_shares_total_profit(share_combo: tuple, share_list_info: list) -> float:
    """
    gets :
        -Tuple: share index combo
        -List: the total share list
    returns:
        -Float: sum of profit value, 0 if total cost exceeds the maximum cost
    """
    value = 0
    cost = 0
    for share_index in share_combo:
        for share_info in share_list_info:
            if share_info["index"] == share_index:
                cost += share_info["cost"]
                value += share_info["rate"] * share_info["cost"]
                break

    if cost > MAX_COST:
        value = 0

    return value


share_list: list = get_list_from_csv("test shares", MAX_COST)
share_list_index = []
best_combo: tuple = None
best_combo_profit: float = 0.0

for line in share_list:
    share_list_index.append(line["index"])

for i in range(len(share_list_index)):
    combinations_pool = combinations(share_list_index, i)

    for combo in combinations_pool:
        combo_profit = get_shares_total_profit(combo, share_list)

        if combo_profit > best_combo_profit:
            best_combo_profit = combo_profit
            best_combo = combo

print("meilleur combo : " + str(best_combo))
print("profit total : " + str(round(best_combo_profit, 2)) + "€")
