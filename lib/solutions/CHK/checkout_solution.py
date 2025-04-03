# noinspection PyUnusedLocal
# skus = unicode string

from collections import Counter
def checkout(skus):
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10,
        'G': 20
    }

    if not skus:
        return 0
    
    item_counts = Counter(skus)

    if not all(item in prices for item in item_counts):
        return -1
    
    total = 0

    count_a = item_counts.get("A",0)
    total += (count_a // 5) * 200
    count_a %= 5
    total += (count_a // 3) * 130
    count_a %= 3
    total += count_a * 50

    count_e = item_counts['E']
    free_b = count_e // 2
    total += count_e * 40

    count_b = max(0, item_counts["B"] - free_b)

    total += (count_b // 2) * 45
    count_b %= 2
    total += count_b * 30

    count_f = item_counts.get("F",0)
    payable_f = (count_f // 3) * 2 + (count_f % 3)
    total += payable_f * 10

    total += item_counts["C"] * 20
    total += item_counts["D"] * 15

    total += item_counts["G"] * prices['G']

    count_h = item_counts.get("H",0)
    total += (count_a // 10) * 80
    count_h %= 10
    total += (count_a // 5) * 45
    count_h %= 5
    total += count_h * 10

    total += item_counts["I"] * 35

    total += item_counts["J"] * 60

    count_k = item_counts["K"]
    total += (count_a // 2) * 150
    count_k %= 2
    total += count_k * 80

    total += item_counts["L"] * 90

    count_n = item_counts['N']
    free_M = count_n // 3
    total += count_n * 40

    count_M = max(0, item_counts["M"] - free_M)

    total += count_M * 15

    total += item_counts["O"] * 10


    count_p = item_counts["P"]
    total += (count_p // 5) * 200
    count_b %= 5
    total += count_b * 50

    count_r = item_counts['R']
    free_q = count_r // 3
    total += count_n * 50

    count_M = max(0, item_counts["M"] - free_M)






    
    return total





