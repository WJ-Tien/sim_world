import pygame
from .. data_models.cars import Car

class CarManager:
    def __init__(self) -> None:
        self.cars: list[Car] = []

    def add_car(self, car: Car) -> None:
        self.cars.append(car)

    def update_cars(self, grid_cols: int, grid_rows: int, blocks: set[tuple[int, int]]) -> None:
        for car in self.cars:
            car.move(grid_cols, grid_rows, blocks)

    def draw_cars(self, screen: pygame.Surface, cell_size: int) -> None:
        for car in self.cars:
            car_pixel_x = car.grid_pos[0] * cell_size
            car_pixel_y = car.grid_pos[1] * cell_size
            pygame.draw.rect(screen, car.color, (car_pixel_x, car_pixel_y, cell_size, cell_size))