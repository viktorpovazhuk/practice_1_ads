import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# matplotlib.use('Qt5Agg')

def visualize(powers, power_timing, power_operations, num_exp):
    algo_names = ['selection_sort', 'insertion_sort', 'shell_sort', 'merge_sort']

    # times

    plt.yscale('log', base=2)
    plt.xlabel('array size, powers of 2')
    plt.ylabel('time, ms')

    for name in algo_names:
        x = np.array(powers)
        y = np.array(power_timing[name])

        plt.plot(x, y, label=name)
    plt.legend()

    plt.savefig(f'exp_{num_exp}_times.png')

    # operations

    plt.clf()

    plt.yscale('log', base=2)

    for name in algo_names:
        x = np.array(powers)
        y = np.array(power_operations[name])

        plt.plot(x, y, label=name)
    plt.legend()

    plt.xlabel('array size, powers of 2')
    plt.ylabel('operations')

    plt.savefig(f'exp_{num_exp}_ops.png')


if __name__ == '__main__':
    visualize([], {}, {}, 1)
