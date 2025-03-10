import pygame
from .. data_models.base_world import WorldConfig
from .. data_models.cars import Car
from .. configs.file_path import CAR_FIG

class CarManager:
    def __init__(self) -> None:
        self.cars: list[Car] = []
        self.cell_size = WorldConfig.get_cell_size()
        self.car_image = pygame.image.load(CAR_FIG)
        self.car_image = pygame.transform.scale(self.car_image, (self.cell_size, self.cell_size))
        self.grid_rows = WorldConfig.get_grid_rows()
        self.grid_cols = WorldConfig.get_grid_cols()

    def add_car(self, car: Car) -> None:
        self.cars.append(car)

    def update_cars(self, blocks: set[tuple[int, int]]) -> None:
        for car in self.cars:
            car.move(self.grid_cols, self.grid_rows, blocks)

    def draw_cars(self, screen: pygame.Surface) -> None:
        for car in self.cars:
            car_pixel_x = car.grid_pos[0] * self.cell_size
            car_pixel_y = car.grid_pos[1] * self.cell_size
            screen.blit(self.car_image, (car_pixel_x, car_pixel_y))