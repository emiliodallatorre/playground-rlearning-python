from numpy import ndarray, arange
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

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

car: Car = Car(
    position=(road_line[0][0], road_line[0][1]),
    direction=(road_line[1][0] - road_line[0][0],
               road_line[1][1] - road_line[0][1])
)

print(f"Car position: {car.position}")


# Assuming terrain_with_road is a numpy array representing the map
# and car is an instance of the Car class

fig, ax = plt.subplots()
ax.imshow(terrain_with_road)

# Initial car position and direction
car_pos, = ax.plot(car.position[0], car.position[1], 'ro')  # 'ro' for red dot


def update(frame):
    sensor_values: list[int] = []
    for sensor_position in car.get_sensor_positions():
        # print(sensor_position)
        # print(terrain_with_road[sensor_position[0]][sensor_position[1]])
        sensor_values.append(
            terrain_with_road[sensor_position[0]][sensor_position[1]])

    car.move(sensor_values)

    # Update the plot
    car_pos.set_data(car.position[0], car.position[1])
    return car_pos,


# Create animation
ani = FuncAnimation(fig, update, frames=arange(
    0, 100), blit=True, interval=500)

plt.show()
