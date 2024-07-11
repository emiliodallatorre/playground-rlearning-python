from numpy import ndarray, zeros


TERRAIN_SIZE: tuple = 256, 256


def get_terrain_matrix() -> ndarray:
    return zeros(TERRAIN_SIZE, dtype=int)
