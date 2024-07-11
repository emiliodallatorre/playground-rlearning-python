from numpy import ndarray, zeros


TERRAIN_SIZE: tuple = 128, 128


def get_terrain_matrix() -> ndarray:
    return zeros(TERRAIN_SIZE, dtype=int)
