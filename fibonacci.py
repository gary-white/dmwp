import matplotlib.pyplot as plt


def first_n(n):

    if n == 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]

    series = [1, 1]

    for i in range(2, n):
        s = series[i-2] + series[i-1]
        series.append(s)

    return series


series = []
fib = first_n(100)
for n in range(1, len(fib)):
    series.append(fib[n] / fib[n-1])

plt.title('Ratio between consecutive Fibonacci numbers')
plt.xlabel('Number')
plt.ylabel('Ratio')
plt.plot(range(1, 100), series)
plt.show()
