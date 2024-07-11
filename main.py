from numpy import ndarray, arange
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.cm as cm

import terrain
import road
from car import Car

terrain_matrix: ndarray = terrain.get_terrain_matrix()
terrain_with_road, road_line = road.draw_road(terrain_matrix)

map_accepted: bool = False

while not map_accepted:
    plt.imshow(terrain_with_road)
    plt.show(block=False)

    response: str = input("Are you happy with the given map? (Y/n): ")

    if response.lower() in ["", "y", "yes"]:
        map_accepted = True
    else:
        plt.close('all')
        terrain_matrix = terrain.get_terrain_matrix()
        terrain_with_road, road_line = road.draw_road(terrain_matrix)

plt.close('all')

# Working on the car
car: Car = Car(
    position=(road_line[0][0], road_line[0][1]),
    direction=(road_line[1][0] - road_line[0][0],
               road_line[1][1] - road_line[0][1])
)

fig, ax = plt.subplots()
ax.imshow(terrain_with_road)

# Initial car position and direction
car_pos, = ax.plot(car.position[0], car.position[1], 'ro')

# Create a list to store the sensor plots
plt.close('all')

sensor_plots = []


def update(frame):
    global sensor_plots

    sensor_values: list[int] = []
    for sensor_position in car.get_sensor_positions():
        sensor_values.append(
            terrain_with_road[sensor_position[0]][sensor_position[1]])

    car.move(sensor_values)

    # Remove old sensor plots
    for sensor_plot in sensor_plots:
        sensor_plot.remove()
    sensor_plots = []

    # Plot sensor positions with color based on sensor values
    for sensor_position, sensor_value in zip(car.get_sensor_positions(), sensor_values):
        sensor_plot, = ax.plot(sensor_position[0], sensor_position[1], 'o', color=cm.jet(sensor_value))
        sensor_plots.append(sensor_plot)

    # Update the car plot
    car_pos.set_data([car.position[0]], [car.position[1]])

    return car_pos, *sensor_plots

# Create animation
ani = FuncAnimation(fig, update, frames=arange(
    0, 100), blit=True, interval=200)

plt.show()
