from itertools import permutations
s1, s2, s3 = input("Enter three words (space-separated): ").split()
letters = set(s1 + s2 + s3)
if len(letters) > 10:
    print("Too many unique letters.")
else:
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if (mapping[s1[0]] != 0 and mapping[s2[0]] != 0 and mapping[s3[0]] != 0 and
            sum(mapping[c] for c in s1) + sum(mapping[c] for c in s2) == sum(mapping[c] for c in s3)):
            print("Solution found:", mapping)
            break