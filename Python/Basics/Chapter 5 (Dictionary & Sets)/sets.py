set = {2, 31 ,43 ,5 ,13}

# for empty sets use
# s = set()  as s = {} will form dictionary and not set


# =================== Set methods ======================
set.add(23)
set.add(55) # adds
set.discard(2)  # removes
set.pop() # removes random item form set
print(set)

print(len(set))


set1 = {1,32,42,34,5,6}
set2 = {1,43,54,42,5,31}

print(set1.intersection(set2))
print(set1.union(set2))