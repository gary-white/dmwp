import matplotlib.pyplot as plt


def draw_graph(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('Distance in meters')
    plt.ylabel('Gravitational force in newtons')
    plt.title('Gravitational force and distance')
    plt.show()


def generate_f_r():
    # Generate values for r
    r = range(100, 1001, 50)
    # Empty list to store the calculated values of F
    f = []
    # Constant, G
    g = 6.674 * (10 ** -11)
    # Two masses
    m1 = 0.5
    m2 = 1.5
    # Calculate force and add it to the list, F
    for dist in r:
        force = g * (m1 * m2) / (dist ** 2)
        f.append(force)

    print(f)

    # Call the draw_graph function
    draw_graph(r, f)


if __name__ == '__main__':
    generate_f_r()
