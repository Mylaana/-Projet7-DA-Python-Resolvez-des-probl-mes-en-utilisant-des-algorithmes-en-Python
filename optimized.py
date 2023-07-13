"""
optimized solution for the best share's value combination
using dynamic programming for the Knapsack problem
"""
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
    for index in share_combo:
        for share_info in share_list_info:
            if share_info["index"] == index:
                cost += share_info["cost"]
                value += share_info["profit"] * share_info["cost"]
                break

    if cost > MAX_COST:
        value = 0

    return value


def main():
    """
    main function
    """
    share_list: list = get_list_from_csv(file_name="test shares", list_length=MAX_COST+1)
    share_list.insert(0, {"name": "Aucun",
                          "index": 0,
                          "cost": 0,
                          "rate": 0,
                          "list_value_at_cost": [0 for i in range(MAX_COST + 1)],
                          "list_combo_at_cost": [[0] for i in range(MAX_COST + 1)]})

    best_combo: tuple = None
    best_combo_profit: float = 0.0
    share_list_index = []
    for line in share_list:
        share_list_index.append(line["index"])

    share_list_index.sort()

    for share_index in share_list_index:
        if share_index == 0:
            continue

        for i in range(MAX_COST + 1):
            share_profit = 0
            remaining_cost = 0
            combo_at_cost = []
            previous_index_remaining_cost_profit = 0

            if i >= share_list[share_index]["cost"]:
                share_profit = share_list[share_index]["cost"] * share_list[share_index]["rate"]
                remaining_cost = i - share_list[share_index]["cost"]

            previous_combo_profit = share_list[share_index - 1]["list_value_at_cost"][i]
            if remaining_cost > 0:
                previous_index_remaining_cost_profit = share_list[
                    share_index - 1]["list_value_at_cost"][remaining_cost]

            if share_profit + previous_index_remaining_cost_profit > previous_combo_profit:

                if previous_index_remaining_cost_profit > 0:
                    combo_at_cost = share_list[share_index - 1]["list_combo_at_cost"][remaining_cost].copy()
                combo_at_cost.append(share_index)

                share_list[share_index]["list_value_at_cost"][i] = share_profit + previous_index_remaining_cost_profit
                share_list[share_index]["list_combo_at_cost"][i] = combo_at_cost.copy()

            else:
                share_list[share_index]["list_value_at_cost"][i] = previous_combo_profit
                share_list[share_index]["list_combo_at_cost"][i] = share_list[
                    share_index - 1]["list_combo_at_cost"][i].copy()

    best_combo = share_list[max(share_list_index)]["list_combo_at_cost"][MAX_COST]
    best_combo_profit = share_list[max(share_list_index)]["list_value_at_cost"][MAX_COST]

    print("meilleur combo : " + str(best_combo))
    print("profit total : " + str(round(best_combo_profit, 2)) + "€")


if __name__ == "__main__":
    main()
