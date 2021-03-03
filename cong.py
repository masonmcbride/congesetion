import numpy as np
num_of_players = 5

def divisors_gen(k):
    d = 1
    while d <= k:
        if k % d == 0:
            yield d
        d += 1

def u(ki, kjs):
    return sum([sum([1 if kj % d != 0 else 0 for d in divisors_gen(ki)]) for kj in kjs])

def phi(strategy):
    uu = 0
    for i in range(len(strategy)):
        ki, kjs = split(strategy, i)
        uu += u(ki, kjs)
    return uu

def split(strategy, i=0):
    ki = strategy[i]
    kjs = strategy[:i] + strategy[i+1:]
    return ki, kjs

def step(ki, kjs):
    new_ki = np.argmax([u(i, kjs) for i in range(1000)])
    changed = new_ki != ki
    return new_ki, changed

def solve(l=list(np.random.choice(1000, num_of_players))):
    
    count = 0
    any_changed = True
    while any_changed:
        any_changed = False
        for i in range(len(l)):
            ki, kjs = split(l, i)
            new_ki, changed = step(ki, kjs)
            if changed: 
                any_changed = True
                l[i] = new_ki
        count += 1
    return l

nash = solve()
print(f"a nash equilibrium: {nash}")
total_utility = phi(nash)
print(f"total utility {total_utility}")
