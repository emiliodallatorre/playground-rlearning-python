import math


class Car:
    position: tuple = (0, 0)
    direction: tuple = (1, 1)  # This can be any direction, not just cardinal

    sensors: list[tuple] = [(-1, 1), (0, 1), (1, 1)]

    def __init__(self, position: tuple, direction: tuple):
        self.position = position
        self.direction = direction

    def get_sensor_positions(self) -> list:
        result: list = []

        # Calculate the angle of rotation from the upward direction (0, 1) to the car's direction
        up_vector = (0, 1)
        angle = math.atan2(
            self.direction[1] - up_vector[1], self.direction[0] - up_vector[0])

        for sensor in self.sensors:
            # Rotate sensor position
            rotated_x = math.cos(angle) * \
                        sensor[0] - math.sin(angle) * sensor[1]
            rotated_y = math.sin(angle) * \
                        sensor[0] + math.cos(angle) * sensor[1]

            # Translate rotated sensor position to absolute position
            sensor_position = (
                round(self.position[0] + rotated_x), round(self.position[1] + rotated_y))
            result.append(sensor_position)

        return result

    def move(self, sensor_values: list[int]) -> tuple:
        determined_direction: tuple = self.determine_direction(sensor_values)

        # Update car's position and direction
        self.position = (self.position[0] + self.direction[0],
                         self.position[1] + self.direction[1])

        self.direction = determined_direction

        return self.position

    def determine_direction(self, sensor_values: list[int]) -> tuple:
        # Placeholder for actual logic
        return (1, 1)
