with open("data/unsorted_names.txt", "r") as f:
    unsorted_names = f.read().split()
with open("data/sorted_names.txt", "w") as f:
    f.write("\n".join(sorted(unsorted_names)))
