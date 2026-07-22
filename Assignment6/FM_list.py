grades = [55, 70, 65, 40, 90, 85, 50, 77]

passed_with_bonus = [g * 1.05 for g in grades if g >= 60]

print("Grades after filtering and applying bonus:", passed_with_bonus)