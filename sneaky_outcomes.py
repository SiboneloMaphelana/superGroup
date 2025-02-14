def find_duplicates(outcomes):
    counts = {}
    duplicates = []

    for outcome in outcomes:
        if outcome in counts:
            counts[outcome] += 1
            if counts[outcome] == 2:  # Found a duplicate
                duplicates.append(outcome)
        else:
            counts[outcome] = 1

    return duplicates


outcomes = [123456, 234567, 123347, 456789, 567890, 678901, 789012, 890123, 901234, 112233, 223344, 334455, 789012, 222234, 123347]
duplicates = find_duplicates(outcomes)
print(duplicates) 
