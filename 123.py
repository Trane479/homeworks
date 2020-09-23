import main
import matplotlib.pyplot as plt

x = []
y = []
k = []
z = []
free_space = range(-10, 11)
for number in list(free_space):
    x.append(number)
    y.append(main.f(number))
    k.append(number)
    z.append(main.g(number))
# print(x, y)
plt.title('f(x) & g(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.plot(x, y, k, z)
plt.show()



