import matplotlib.pyplot as plt
import csv
import matplotlib.animation as animation


class Visualization:
    def __init__(self, cities, sol):
        self.cities = cities
        self.sol = sol

        self.paused = False
        self.animation = None

    def __order(self):
        new_cities = []
        for idx in range(len(cities)):
            new_cities.append(cities[self.sol[idx]])
        new_cities.append(cities[0])
        return new_cities

    def show(self):
        x = []
        y = []
        ordered_cities = self.__order()

        for city in ordered_cities:
            x.append(float(city[0]))
            y.append(float(city[1]))
        # print(x)

        # Create a figure object and add a subplot
        fig, ax = plt.subplots()

        # Plot the data on the subplot
        line, = ax.plot([], [], marker='o', markersize=1.5,
                        markerfacecolor='red', markeredgecolor='red')
        line.set_linewidth(0.3)
        # Add a title and axis labels
        ax.set_title(
            'Travelling salesman problem - Click to pause/resume the animation')
        ax.set_xlabel('Horizontal')
        ax.set_ylabel('Vertical')

        # Set the limits of the x- and y-axes
        ax.set_xlim([0, 100])
        ax.set_ylim([0, 100])

        self.animation = animation.FuncAnimation(fig, self.animate, frames=len(x)+1,
                                                 fargs=[x, y, line], interval=1, blit=False, repeat=False)

        # # Pause / Resume
        # fig.canvas.mpl_connect('button_press_event', self.toggle_pause)
        # # Save file
        # self.animation.save('visualization.gif')
        # plt.savefig('visualization.png')
        plt.show()

    def animate(self, i, x, y, line):
        print(i)
        # Get the x and y data for the line up to the ith point
        line.set_data(x[:i], y[:i])

        # Return the line object
        return line,

    def toggle_pause(self, *args, **kwargs):
        if self.paused:
            self.animation.resume()
        else:
            self.animation.pause()
        self.paused = not self.paused


cities = []
# get TSP city map
with open('2023_AI_TSP.csv', mode='r', newline='', encoding='utf-8-sig') as tsp:
    # read TSP city map
    reader = csv.reader(tsp)
    for row in reader:
        cities.append(row)

sol = []
# 1. get solution sequence and reordering (sort from 0)
with open('./greedy_solution.csv', mode='r', newline='') as solution:

    # read solution sequence
    reader = csv.reader(solution)
    for row in reader:
        sol.append(int(row[0]))

    # reordering solution sequence
    idx = sol.index(0)

    front = sol[idx:]
    back = sol[0:idx]

    sol = front + back

    # expand 0 city (start) for simplicity
    sol.append(int(0))

# Usage
visual = Visualization(cities, sol)
visual.show()
