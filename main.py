from src.data_models.cars import Car
from src.maps.world import World
from src.registers.car_manager import CarManager
from src.data_models.base_world import WorldConfig

if __name__ == "__main__":

    world_config = WorldConfig()

    car_manager = CarManager()
    # TODO register cars in db 
    car1 = Car(name="test_vehicle_1", color=(255, 0, 0), grid_pos=[0, 0])
    car2 = Car(name="test_vehicle_2", color=(0, 255, 0), grid_pos=[15, 15])
    car3 = Car(name="test_vehicle_3", color=(0, 255, 255), grid_pos=[24, 24])
    car_manager.add_car(car1)
    car_manager.add_car(car2)
    car_manager.add_car(car3)

    my_world = World(world_config, car_manager)
    my_world.init_world()
    
