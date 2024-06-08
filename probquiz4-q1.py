import itertools


def find_prob(num):
    outcomes_X = []

    for outcome in itertools.product(range(1, 4), repeat=3):
        if sum(outcome) == num:
            outcomes_X.append(outcome)
            # print("outcome:", outcome, "sum:", sum(outcome))

    outcomes = len(outcomes_X)

    print(f"Total outcomes with X = {num}: {outcomes}")
    return outcomes / (27)


prob = 0
for i in range(3, 10):  # values of X are in [3, 9]
    prob += find_prob(i)

print(f"Total probability: {prob}")
