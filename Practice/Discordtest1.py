sample= list(range(2,100))
filtered_sample= [x for x in sample if x % 3 or x==3]
print(filtered_sample)
print(sample[::3])