import numpy as np
import matplotlib.pyplot as plt

x_star, mu_star = 1.0, 2.0

def L(mu, x):
    return x**2 + mu * (1 - x)

L_star = L(mu_star, x_star)   # = 1

fig, axes = plt.subplots(1, 2, figsize=(10, 4))


mu = np.linspace(0, 4, 200)
axes[0].plot(mu, L(mu, x_star), color='tab:blue', lw=2,
             label=r'$L(\mu,x^*)=1$')
axes[0].plot(mu_star, L_star, 'o', color='tab:red', markersize=9,
             markeredgecolor='k', zorder=5)
axes[0].annotate(r'$L(\mu^*,x^*)=1$', (mu_star, L_star),
                 textcoords='offset points', xytext=(-30, 15), color='tab:red')
axes[0].set_xlabel(r'$\mu$')
axes[0].set_ylabel(r'$L(\mu,x^*)$')
axes[0].set_title(r'$L(\mu,x^*)$ against $\mu$')
axes[0].set_ylim(0, 2)
axes[0].grid(alpha=0.3)
axes[0].legend()


x = np.linspace(-1, 3, 400)
axes[1].plot(x, L(mu_star, x), color='tab:green', lw=2,
             label=r'$L(\mu^*,x)=(x-1)^2+1$')
axes[1].plot(x_star, L_star, 'o', color='tab:red', markersize=9,
             markeredgecolor='k', zorder=5)
axes[1].annotate(r'$L(\mu^*,x^*)=1$', (x_star, L_star),
                 textcoords='offset points', xytext=(15, -25), color='tab:red')
axes[1].set_xlabel(r'$x$')
axes[1].set_ylabel(r'$L(\mu^*,x)$')
axes[1].set_title(r'$L(\mu^*,x)$ against $x$')
axes[1].grid(alpha=0.3)
axes[1].legend()

plt.tight_layout()
plt.savefig('Figure_4.png', dpi=300)
plt.show()