# pets.py

from abc import ABC, abstractmethod
from datetime import date
from typing import Dict

from model.tasks import CareTask
from model.vetrecord import VetRecord


class Pet(ABC):
    """
    Abstract Pet class with:
    - name, breed, weight, age
    - tasks
    - vet record
    - serialization
    - abstract species-specific methods
    """

    def __init__(self, name: str, breed: str, weight_kg: float, age: float):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Pet must have a name.")
        if weight_kg <= 0:
            raise ValueError("Weight must be positive.")
        if age < 0:
            raise ValueError("Age cannot be negative.")

        self._name = name.strip()
        self._breed = breed
        self._weight_kg = float(weight_kg)
        self._age = float(age)

        self._tasks: Dict[str, CareTask] = {}
        self._vet_record = VetRecord()

    # ---------------------------------------------------------
    # Properties
    # ---------------------------------------------------------

    @property
    def name(self):
        return self._name

    @property
    def breed(self):
        return self._breed

    @property
    def weight_kg(self):
        return self._weight_kg

    @property
    def age(self):
        return self._age

    @property
    def tasks_map(self):
        return self._tasks  # dict of label → CareTask

    @property
    def vet_record(self):
        return self._vet_record

    # ---------------------------------------------------------
    # Task management
    # ---------------------------------------------------------

    def add_task(self, task: CareTask):
        if task.label in self._tasks:
            raise ValueError("Task already exists for this pet.")
        self._tasks[task.label] = task

    def all_tasks(self):
        return list(self._tasks.values())

    def due_tasks(self, on: date):
        return [t for t in self._tasks.values() if t.is_due(on)]

    # ---------------------------------------------------------
    # Serialization
    # ---------------------------------------------------------

    def to_dict(self) -> dict:
        return {
            "type": self.__class__.__name__,
            "name": self._name,
            "breed": self._breed,
            "weight_kg": self._weight_kg,
            "age": self._age,
            "tasks": [t.to_dict() for t in self._tasks.values()],
            "vet_record": self._vet_record.to_dict(),
        }

    @classmethod
    def from_dict(cls, data: dict):
        pet_type = data["type"]
        name = data["name"]
        breed = data["breed"]
        weight = data["weight_kg"]
        age = data["age"]

        # Pick subclass dynamically
        if pet_type == "Dog":
            pet = Dog(name, breed, weight, age)
        elif pet_type == "Cat":
            pet = Cat(name, breed, weight, age)
        elif pet_type == "Bird":
            pet = Bird(name, breed, weight, age)
        else:
            raise ValueError(f"Unknown pet type: {pet_type}")

        # Load tasks
        for tdata in data.get("tasks", []):
            task = CareTask.from_dict(tdata)
            pet.add_task(task)

        # Load vet record
        pet._vet_record = VetRecord.from_dict(data.get("vet_record", {}))

        return pet

    # ---------------------------------------------------------
    # Abstract species methods
    # ---------------------------------------------------------

    @abstractmethod
    def daily_food_amount(self) -> float:
        pass

    @abstractmethod
    def daily_exercise_minutes(self) -> int:
        pass

    @abstractmethod
    def sound(self) -> str:
        pass


# -------------------------------------------------------------
# SUBCLASSES
# -------------------------------------------------------------

class Dog(Pet):
    def daily_food_amount(self):
        return self._weight_kg * 40

    def daily_exercise_minutes(self):
        return 60

    def sound(self):
        return "Woof!"

    def __str__(self):
        return f"{self._name} the {self._breed} (Dog)"


class Cat(Pet):
    def daily_food_amount(self):
        return self._weight_kg * 30

    def daily_exercise_minutes(self):
        return 20

    def sound(self):
        return "Meow!"

    def __str__(self):
        return f"{self._name} the {self._breed} (Cat)"


class Bird(Pet):
    def daily_food_amount(self):
        return self._weight_kg * 20

    def daily_exercise_minutes(self):
        return 10

    def sound(self):
        return "Chirp!"

    def __str__(self):
        return f"{self._name} the {self._breed} (Bird)"
