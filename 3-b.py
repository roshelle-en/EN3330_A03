import numpy as np
import matplotlib.pyplot as plt

def L(mu, x):
    return x**2 + mu * (1 - x)

mu = np.linspace(0, 4, 400)
xs = [0, 1, 2]
colors = ['tab:blue', 'tab:orange', 'tab:green']

fig, ax = plt.subplots(figsize=(7, 5))

lines = []
for x, c in zip(xs, colors):
    y = L(mu, x)
    lines.append(y)
    ax.plot(mu, y, color=c, lw=1.5, label=rf'$x={x}$')

# lower envelope of the three lines
envelope = np.min(lines, axis=0)
ax.plot(mu, envelope, 'k', lw=3, label='lower envelope')

# true dual function 
ax.plot(mu, mu - mu**2 / 4, 'r--', lw=1.5, label=r'true $d(\mu)=\mu-\mu^2/4$')

ax.set_xlabel(r'$\mu$')
ax.set_ylabel(r'$L(\mu,x)$')
ax.set_title(r'$L(\mu,x)$ against $\mu$ for $x=0,1,2$')
ax.set_ylim(-3, 5)
ax.grid(alpha=0.3)
ax.legend(fontsize=9)
plt.tight_layout()
plt.savefig('Figure_5.png', dpi=300)
plt.show()