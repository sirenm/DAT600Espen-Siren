import math
import matplotlib.pyplot as plt
import matplotlib as mpl
from IPython.display import clear_output

def generate_sort_algorithm_plot(sort_func, time_complexity):
    mpl.rcParams['figure.figsize'] = [16,4]

    fig, ax = plt.subplots(1, 2)
    fig.suptitle('Counted steps and Asymptotic running time')

    B = [5, 2, 4, 6, 1, 3]
    points = 12  # plotting points, originally 13, changed to 12 for quicksort due to exhausion
    x, y, ref, c = [], [], [], []

    for i in range(points):
        clear_output(wait=True)
        print(f"{i + 1}/{points}")

        #Supposed to be steps = sort_func(B.copy()), but added extra parameters for QuickSort specifically. Use steps = sort_func(B.copy()) for all others.
        steps = sort_func(B.copy(), 0, len(B.copy())-1)
        #steps = sort_func(B.copy())

        # Increase the size of the list based on algorithm
        if time_complexity == "O(N^2)":
            B = B * 2
        elif time_complexity == "O(N log N)":
            B = B + B

        x.append(len(B))
        y.append(steps)

        # Calculate 'c' based on time complexity
        if time_complexity == "O(N^2)":
            c.append(steps / (len(B) ** 2))
        elif time_complexity == "O(N log N)":
            c.append(steps / (len(B) * math.log(len(B))))

    for v in x:
        if time_complexity == "O(N^2)":
            ref.append(v ** 2 * c[6])
        elif time_complexity == "O(N log N)":
            ref.append(v * math.log(v) * c[6])

    ax[0].plot(x, y, color="red", label="Counted steps")
    ax[0].plot(x, ref, color="green", label=f"{round(c[6], 2)}{time_complexity}")
    ax[0].set_xlabel("Size of n")
    ax[0].set_ylabel("Computation steps")
    ax[0].legend()

    ax[1].scatter(x, c, label="Approximation of c")
    ax[1].set_xlabel("Size of n")
    ax[1].set_ylabel("c factor")

    plt.show()