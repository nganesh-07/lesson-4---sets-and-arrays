import array as arr

numberarray = arr.array("i", [1, 2, 3, 7, 4, 6, 5, 7, 9, 8])
print("Original array:", str(numberarray))

print("7 occurs in this array", str(numberarray.count(7)), "times.")

numberarray.reverse()
print("The reversed array looks like this:")
print(str(numberarray))