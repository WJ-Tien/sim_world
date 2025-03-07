import pygame
import sys
from data_models.base_world import WorldConfig
from registers.car_manager import CarManager


class World:

    def __init__(self, world_config: WorldConfig, car_manager: CarManager) -> None:
        pygame.init()
        self.world_config = world_config
        self.cell_size = self.world_config.cell_size
        self.width = self.world_config.grid_cols * self.world_config.cell_size
        self.height = self.world_config.grid_rows * self.world_config.cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.car_manager = car_manager

    def draw_grid(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, (200, 200, 200), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, (200, 200, 200), (0, y), (self.width, y))
    
    def init_world(self) -> None:
        pygame.display.set_caption("Simulation World")
        move_event = pygame.USEREVENT + 1
        pygame.time.set_timer(move_event, self.world_config.frame_update_interval)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == move_event:
                    self.car_manager.update_cars(self.world_config.grid_cols, self.world_config.grid_rows)

            self.screen.fill((255, 255, 255))
            self.draw_grid()
            self.car_manager.draw_cars(self.screen, self.world_config.cell_size)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()