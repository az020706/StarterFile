d1 = 1.11 - 1.10
d2 = 2.11 - 2.10
print('d1=', d1, ' d2=', d2)
diff = d1-d2  # Compute difference
if diff < 0:  # Compute absolute vale
    diff = -diff
if diff <0.00000001:  # Are values similar enough?
    print('Same values')
else:
    print('Different values')