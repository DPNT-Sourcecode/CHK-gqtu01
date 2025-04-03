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

    
    
    return total


