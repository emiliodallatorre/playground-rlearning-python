from numpy import ndarray, zeros


TERRAIN_SIZE: tuple = 1024, 1024


def get_terrain_matrix() -> ndarray:
    return zeros(TERRAIN_SIZE, dtype=int)
