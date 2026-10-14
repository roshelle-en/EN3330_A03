import numpy as np
import matplotlib.pyplot as plt

def d(mu):
    # dual function d(mu) = min_x L(mu, x) = mu - mu^2/4
    return mu - mu**2 / 4

mu = np.linspace(0, 4, 400)

mu_star = 2.0
d_star = d(mu_star)      # = 1

fig, ax = plt.subplots(figsize=(7, 5))

ax.plot(mu, d(mu), color='tab:blue', lw=2, label=r'$d(\mu)=\mu-\mu^2/4$')

# maximizer and dual optimal value
ax.plot(mu_star, d_star, 'o', color='tab:red', markersize=9,
        markeredgecolor='k', zorder=5)
ax.annotate(rf'$\mu^*={mu_star:.0f},\ d^*={d_star:.0f}$', (mu_star, d_star),
            textcoords='offset points', xytext=(10, -25), color='tab:red')

# primal optimal value p* = f(x*) = 1

ax.axvline(mu_star, color='gray', ls=':', lw=1)

ax.set_xlabel(r'$\mu$')
ax.set_ylabel(r'$d(\mu)$')
ax.set_title(r'Dual function $d(\mu)=\min_x L(\mu,x)$')
ax.grid(alpha=0.3)
ax.legend(loc='lower center')
plt.tight_layout()
plt.savefig('Figure_2.png', dpi=300)
plt.show()