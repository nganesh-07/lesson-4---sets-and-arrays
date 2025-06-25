set1 = {"brown", "spain", "orange"}
set2 = {"greece", "white", "brown"}

print("set 1:", set1)
print("set 2:", set2)

print("The values that are contrast between these two sets are:")
set3 = set1.symmetric_difference(set2)
print(set3)