import pygame
import sys
import random
from ..data_models.base_world import WorldConfig
from ..configs.file_path import BLOCK_FIG 
from ..registers.car_manager import CarManager


class World:

    def __init__(self, world_config: WorldConfig, car_manager: CarManager) -> None:
        pygame.init()

        # map/road
        self.world_config = world_config
        self.cell_size = self.world_config.cell_size
        self.width = self.world_config.grid_cols * self.cell_size
        self.height = self.world_config.grid_rows * self.cell_size
        self.block_ratio = self.world_config.block_ratio
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        # car
        self.car_manager = car_manager

        # blocks & block images
        self.road_blocks = set()
        self.gen_road_block()
        self.block_image = pygame.image.load(BLOCK_FIG)
        self.block_image = pygame.transform.scale(self.block_image, (self.cell_size, self.cell_size))  # S

    def gen_road_block(self) -> None:
        """Generate a random block network."""
        for y in range(self.world_config.grid_rows):
            for x in range(self.world_config.grid_cols):
                if random.random() > (1 - self.block_ratio):  # 1 - self.block_ratio% chance of being a road
                    self.road_blocks.add((x, y))

    def draw_roads(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, self.world_config.grid_line_color, (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, self.world_config.grid_line_color, (0, y), (self.width, y))

    def draw_blocks(self) -> None:
        for x, y in self.road_blocks:
            self.screen.blit(self.block_image, (y * self.cell_size, x * self.cell_size))

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
                    self.car_manager.update_cars(self.world_config.grid_cols, self.world_config.grid_rows, self.road_blocks)

            self.screen.fill(self.world_config.map_background_color)
            self.draw_roads()
            self.draw_blocks()
            self.car_manager.draw_cars(self.screen)

            pygame.display.flip()
            self.clock.tick(self.world_config.fps)

        pygame.quit()
        sys.exit()