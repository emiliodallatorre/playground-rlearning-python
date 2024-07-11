from numpy import ndarray
from matplotlib import pyplot as plt
import terrain
import road

terrain_matrix: ndarray = terrain.get_terrain_matrix()
terrain_with_road: ndarray = road.draw_road(terrain_matrix)

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
        terrain_with_road = road.draw_road(terrain_matrix)
