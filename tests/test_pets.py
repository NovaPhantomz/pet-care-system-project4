# test_pets.py
import unittest
from datetime import date

from model.pets import Dog, Cat, Bird
from model.schedule import Schedule
from model.tasks import CareTask


class TestPets(unittest.TestCase):

    def test_dog_food_amount(self):
        d = Dog("Buddy", "Lab", 10, 5)
        self.assertEqual(d.daily_food_amount(), 400)

    def test_cat_food_amount(self):
        c = Cat("Kitty", "Tabby", 4, 3)
        self.assertEqual(c.daily_food_amount(), 120)

    def test_bird_food_amount(self):
        b = Bird("Tweety", "Canary", 1, 1)
        self.assertEqual(b.daily_food_amount(), 20)

    def test_add_task(self):
        d = Dog("Buddy", "Lab", 10, 5)
        schedule = Schedule(1, date(2025, 1, 1))
        task = CareTask("Feed", schedule)
        d.add_task(task)
        self.assertIn("Feed", d.tasks_map)

    def test_pet_serialization_round_trip(self):
        d = Dog("Buddy", "Lab", 10, 5)
        schedule = Schedule(1, date(2025, 1, 1))
        task = CareTask("Feed", schedule)
        d.add_task(task)

        data = d.to_dict()
        restored = Dog.from_dict(data)

        self.assertEqual(restored.name, "Buddy")
        self.assertIn("Feed", restored.tasks_map)


if __name__ == "__main__":
    unittest.main()

