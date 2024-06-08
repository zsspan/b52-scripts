import itertools

def find_prob(num):
    prob_of_x = []

    for outcome in itertools.product(range(1, 7), repeat=num):
        if len(set(outcome)) == 3 and len(set(outcome[: num - 1])) == 2:
            prob_of_x.append(outcome)
            # print(outcome)

    outcomes = len(prob_of_x)

    print(f"Total outcomes with Y = {num}: {outcomes}")
    return (outcomes/(6 ** num))

prob = 0
for i in range(10):
    prob += find_prob(i)
print(f"Total probability: {prob}")
