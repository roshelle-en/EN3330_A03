import numpy as np

def d(mu):
    return mu - mu**2 / 4

p_star = 1.0
print(f"{'mu':>4} {'d(mu)':>8} {'p*':>6} {'d(mu) <= p*':>12}")
for mu in [0, 1, 2, 3]:
    print(f"{mu:>4} {d(mu):>8.2f} {p_star:>6.1f} {str(d(mu) <= p_star):>12}")