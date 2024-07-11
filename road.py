from numpy import ndarray, array, linspace
from numpy.random import randint
from scipy.interpolate import splprep, splev
from scipy.ndimage import gaussian_filter


ROAD_WIDTH: int = 10


def draw_road(terrain: ndarray) -> ndarray:
    # Determine terrain size
    max_x, max_y = terrain.shape

    # Generate random points, ensuring start and end points are at the edges
    x = array([0 + ROAD_WIDTH] + list(randint(ROAD_WIDTH + 1,
              max_x - 1 - ROAD_WIDTH, 3)) + [max_x - 1 - ROAD_WIDTH])
    y = array([0 + ROAD_WIDTH] + list(randint(ROAD_WIDTH + 1,
              max_y - 1 - ROAD_WIDTH, 3)) + [max_y - 1 - ROAD_WIDTH])

    # Interpolate points to create a smooth curve
    tck, u = splprep([x, y], s=0)
    unew = linspace(0, 1.0, 1000)
    out = splev(unew, tck)

    # Draw the curve over the matrix
    for i in range(len(out[0]) - 1):
        x0, y0 = int(out[0][i]), int(out[1][i])
        x1, y1 = int(out[0][i + 1]), int(out[1][i + 1])

        if x0 >= 0 and x0 < max_x and y0 >= 0 and y0 < max_y:
            terrain[x0, y0] = 1

        if x1 >= 0 and x1 < max_x and y1 >= 0 and y1 < max_y:
            terrain[x1, y1] = 1

        for j in range(-ROAD_WIDTH // 2, ROAD_WIDTH//2):
            for k in range(-ROAD_WIDTH // 2, ROAD_WIDTH//2):
                if x0 + j >= 0 and x0 + j < max_x and y0 + k >= 0 and y0 + k < max_y:
                    terrain[x0 + j, y0 + k] = 1

                if x1 + j >= 0 and x1 + j < max_x and y1 + k >= 0 and y1 + k < max_y:
                    terrain[x1 + j, y1 + k] = 1

    for px, py in zip(x, y):
        terrain[px, py] += 1

    return terrain
