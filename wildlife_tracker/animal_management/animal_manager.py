from typing import Optional
from wildlife_tracker.animal_management.animal import Animal

class AnimalManager:

    def __init__(self) -> None:
        animals: dict[int, Animal] = {}

    def get_animal_by_id(self, animal_id: int) -> Optional[Animal]:
        return self.animals.get(animal_id)

    def register_animal(self, Animal) -> None:
        animal_id = len(self.animals) + 1
        self.animals[animal_id] = animal

    def remove_animal(self, animal_id: int) -> None:
        if(animal_id in self.animals):
            del self.animals[animal_id]