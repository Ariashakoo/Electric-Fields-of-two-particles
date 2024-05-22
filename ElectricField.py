import numpy as np
import matplotlib.pyplot as plt

# Constants
k = 8.99e9  
charge_positive = 1e-6 
charge_negative = -1e-6 

# Force
def electric_field(q, r0, x, y):
    r = np.sqrt((x - r0[0])**2 + (y - r0[1])**2)
    return k * q / r**2 * (x - r0[0]) / r, k * q / r**2 * (y - r0[1]) / r

# Set up grid and compute field
nx, ny = 64, 64
x = np.linspace(50, 250, nx)
y = np.linspace(100, 200, ny)
X, Y = np.meshgrid(x, y)


Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx))
positions = [(100, 150), (200, 150)]

for charge, position in zip([charge_positive, charge_negative], positions):
    ex, ey = electric_field(charge, position, X, Y)
    Ex += ex
    Ey += ey


fig, ax = plt.subplots(figsize=(8, 6))


ax.scatter(*positions[0], color='red', label='Positive Charge', s=100)
ax.scatter(*positions[1], color='blue', label='Negative Charge', s=100)


color = np.log(np.sqrt(Ex**2 + Ey**2))
ax.streamplot(X, Y, Ex, Ey, color=color, linewidth=1, cmap=plt.cm.inferno,
              density=2, arrowstyle='->', arrowsize=1.5)


ax.set_title('Electric Field between Positive and Negative Charges')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend()
ax.set_aspect('equal')
plt.grid(True)
plt.show()