import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 3, 400)
mus = [0, 1, 2, 3]
colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']

def L(mu, x):
    return x**2 + mu * (1 - x)

fig, ax = plt.subplots(figsize=(7, 5))

for mu, c in zip(mus, colors):
    ax.plot(x, L(mu, x), color=c, label=rf'$\mu={mu}$')
    # minimizer x(mu) = mu/2 (from dL/dx = 2x - mu = 0)
    x_min = mu / 2
    L_min = L(mu, x_min)        
    ax.plot(x_min, L_min, 'o', color=c, markersize=8,
            markeredgecolor='k', zorder=5)
    ax.annotate(rf'$x({mu})={x_min:.1f}$', (x_min, L_min),
                textcoords='offset points', xytext=(0, -18),
                ha='center', color=c)

# locus of the minimizers: L_min = 2x - x^2
xl = np.linspace(0, 1.5, 100)
ax.plot(xl, 2 * xl - xl**2, 'k--', lw=1, label='locus of minimizers')

# constraint boundary x = 1
ax.axvline(1, color='gray', ls=':', lw=1.2)
ax.text(1.02, 5.2, r'$x=1$ (constraint boundary)', color='gray')

ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$L(\mu,x)=x^2+\mu(1-x)$')
ax.set_title(r'Lagrangian $L(\mu,x)$ for $\mu=0,1,2,3$')
ax.set_ylim(-0.5, 6)
ax.grid(alpha=0.3)
ax.legend()
plt.tight_layout()
plt.savefig('fig1a.pdf')   
plt.savefig('fig1a.png', dpi=300)
plt.show()