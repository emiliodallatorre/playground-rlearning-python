from numpy import ndarray
from matplotlib import pyplot as plt
import terrain
import road

terrain: ndarray = terrain.get_terrain_matrix()

terrain_with_road: ndarray = road.draw_road(terrain)

plt.imshow(terrain_with_road)
plt.show()
