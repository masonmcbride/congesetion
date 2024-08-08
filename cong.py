import numpy as np
num_of_players = 2

def divisors_gen(k: int):
    return (d for d in range(1,k+1) if k % d == 0)

def u(ki, kjs):
    return sum(sum(kj % d != 0 for d in divisors_gen(ki)) for kj in kjs)

def phi(strategy):
    uu = 0
    for i in range(len(strategy)):
        ki, kjs = split(strategy, i)
        uu += u(ki, kjs)
    return uu

def best_response(kjs):
    br = np.argmax([u(i, kjs) for i in range(1000)])
    return br

def solve(l):
    while l != (new_l:=[best_response(l[:i] + l[i+1:]) for i in range(len(l))]):
        print(f"{new_l=}")

        l = new_l 
    return l

from itertools import product
from random import choice
from collections import defaultdict
all_combos = list(product(range(1000),repeat=num_of_players))
results = defaultdict(int)
print("starting")
for i,combo in enumerate(all_combos):
    if i % 1000 == 0:
        print(f"run {i}")
    br = [best_response(combo[:i] + combo[i+1:]) for i in range(len(combo))]
    results[str(br)] += 1
print(results)
#initial_state = list(np.random.choice(1000, num_of_players))
#print(f"{initial_state=}")
#nash = solve(initial_state)
#print(f"a nash equilibrium: {nash}")
#total_utility = phi(nash)
#print(f"total utility {total_utility}")
