set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set1.update(set2 - set1)  # Add only unique items from set2
print("Updated set1:", set1)
