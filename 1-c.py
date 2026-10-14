import numpy as np
import matplotlib.pyplot as plt

def L(mu, x):
    return x**2 + mu * (1 - x)

x = np.linspace(-1, 3, 400)

fig, ax = plt.subplots(figsize=(8, 5.5))


mus = [0, 1, 2, 5, 10, 20]
for mu in mus:
    ax.plot(x, L(mu, x), lw=1, alpha=0.5, label=rf'$\mu={mu}$')


#   feasible   (x >= 1): g(x) = x^2
#   infeasible (x <  1): g(x) = +infinity
x_feas = x[x >= 1]
x_inf = x[x < 1]

ax.plot(x_feas, x_feas**2, color='k', lw=3, label=r'$g(x)=x^2$ (feasible, $x\geq 1$)')


y_top = 12
ax.axvline(1, color='tab:red', lw=3, ymax=1,
           label=r'$g(x)=+\infty$ (infeasible, $x<1$)')
ax.annotate('', xy=(0.5, y_top), xytext=(0.5, 8),
            arrowprops=dict(arrowstyle='->', color='tab:red', lw=2))
ax.text(-0.9, 10, r'$g(x)=+\infty$ for $x<1$', color='tab:red', fontsize=11)

# shade the infeasible region
ax.axvspan(-1, 1, color='tab:red', alpha=0.08)

# mark the minimizer of g
ax.plot(1, 1, 'o', color='k', markersize=9, markeredgecolor='k', zorder=6)
ax.annotate(r'$x^*=1,\ g(x^*)=1$', (1, 1), textcoords='offset points',
            xytext=(15, -20))

ax.set_ylim(-1, y_top)
ax.set_xlim(-1, 3)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$g(x)$,  $L(\mu,x)$')
ax.set_title(r'Primal function $g(x)=\max_{\mu\geq 0}L(\mu,x)$')
ax.grid(alpha=0.3)
ax.legend(loc='upper right', fontsize=8)
plt.tight_layout()
plt.savefig('Figure_3.png', dpi=300)
plt.show()