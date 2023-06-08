import math
import random
import matplotlib.pyplot as plt
import numpy as np


def exact_value(x, mode='test'):
    if mode == 'test':
        return x ** 2 + 1
    elif mode == 'main':
        return np.exp(x ** 2)
    else:
        raise ValueError('Invalid mode')



def generate_random_point(a, b, f, mode):
    x = random.uniform(a, b)
    y = random.uniform(0, max(f(np.array([a, b]), mode=mode)))
    return x, y


def monte_carlo_integration(f, a, b, num_samples=100000, mode='main'):
    total_area = (b - a) * max(f(np.array([a, b]), mode=mode))
    num_points_inside = 0
    points_inside = []

    for i in range(num_samples):
        x, y = generate_random_point(a, b, f, mode)
        if y <= f(x, mode=mode):
            num_points_inside += 1
            points_inside.append((x, y))

    integral = total_area * (num_points_inside / num_samples)
    return integral, points_inside, total_area


a = 1
b = 2
c = 0
d = 1
exact_integral = monte_carlo_integration(exact_value, a, b, num_samples=500000, mode = 'main')[0]
exact_test_integral = monte_carlo_integration(exact_value, c, d, num_samples=500000, mode = 'test')[0]

x = np.linspace(a, b, 1000)
y = exact_value(x, mode='main')

num_samples = 10000
integral, points_inside, total_area = monte_carlo_integration(exact_value, a, b, num_samples=num_samples, mode='main')
print(f"Monte Carlo approximation of the main integral: {integral}")

integral_test, points_inside_test, total_area_test = monte_carlo_integration(exact_value, c, d, num_samples=num_samples, mode='test')
print(f"Monte Carlo approximation of the test integral: {integral_test}")

print(f"Exact main integral value: {exact_integral}")
print(f"Exact test integral value: {exact_test_integral}")
if integral != 0:
    error_abs = abs(exact_integral - integral)
    if exact_integral == 0:
        error_rel = 0
    else:
        error_rel = error_abs / abs(exact_integral)
    print(f"Absolute main error: {error_abs}")
    print(f"Relative main error: {error_rel}")
else:
    print("The approximation is zero. The relative error is undefined.")

if integral != 0:
    error_abs = abs(exact_test_integral - integral_test)
    if exact_test_integral == 0:
        error_rel = 0
    else:
        error_rel = error_abs / abs(exact_test_integral)
    print(f"Absolute test error: {error_abs}")
    print(f"Relative test error: {error_rel}")
else:
    print("The approximation is zero. The relative error is undefined.")

points_outside = [(x, y) for x, y in zip([random.uniform(a, b) for _ in range(num_samples)], [random.uniform(0, total_area) for _ in range(num_samples)]) if y > exact_value(x, mode='main')]

plt.plot(x, y, label='Exact function')
plt.fill_between(x, y, color='gray', alpha=0.2, label='Area')
plt.scatter([p[0] for p in points_outside], [p[1] for p in points_outside], s=1, color='green', label='Points outside')
plt.scatter([p[0] for p in points_inside], [p[1] for p in points_inside], s=1, label='Points inside')
plt.legend()
plt.show()

x_test = np.linspace(c, d, 1000)
y_test = exact_value(x_test, mode='test')



points_outside_test = [(x, y) for x, y in zip([random.uniform(c, d) for _ in range(num_samples)], [random.uniform(0, total_area_test) for _ in range(num_samples)]) if y > exact_value(x, mode='test')]

plt.plot(x_test, y_test, label='Exact function (test)')
plt.fill_between(x_test, y_test, color='gray', alpha=0.2, label='Area (test)')
plt.scatter([p[0] for p in points_outside_test], [p[1] for p in points_outside_test], s=1, color='green', label='Points outside (test)')
plt.scatter([p[0] for p in points_inside_test], [p[1] for p in points_inside_test],color='red', s=1, label='Points inside (test)')
plt.legend()
plt.show()

def exact_func_value(x):
    return math.exp(x**2)

point = 2
exact_point_value = exact_value(point, mode = "main")
print(f"Точне значення підінтегральної функції в точці {point}: {exact_point_value}")