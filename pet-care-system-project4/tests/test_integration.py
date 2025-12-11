# test_integration.py
import unittest
from datetime import date

from model.tracker import Tracker, Owner
from model.pets import Dog
from model.schedule import Schedule
from model.tasks import CareTask


class TestIntegration(unittest.TestCase):

    def test_add_owner_pet_task_flow(self):
        """
        Tests a full workflow:
        - create tracker
        - add owner
        - add pet
        - add task
        - verify due tasks
        """
        tracker = Tracker()

        # Step 1: Owner
        owner = Owner("Amar")
        tracker.register_owner(owner)

        # Step 2: Pet
        dog = Dog("Luna", "Lab", 10, 5)
        owner.add_pet(dog)

        # Step 3: Task
        schedule = Schedule(1, date(2025, 1, 1))
        task = CareTask("Feed", schedule)
        dog.add_task(task)

        # Step 4: Query tasks due
        due_tasks = tracker.all_due(date(2025, 1, 1))

        self.assertEqual(len(due_tasks), 1)
        self.assertEqual(due_tasks[0], ("Amar", "Luna", "Feed"))

    def test_multiple_pets_and_tasks(self):
        tracker = Tracker()
        owner = Owner("A")
        tracker.register_owner(owner)

        dog = Dog("Max", "Husky", 20, 3)
        cat = Dog("Bella", "Lab", 15, 4)  # using Dog just for test variety

        owner.add_pet(dog)
        owner.add_pet(cat)

        schedule1 = Schedule(1, date(2025, 1, 1))
        schedule2 = Schedule(2, date(2025, 1, 1))

        dog.add_task(CareTask("Walk", schedule1))
        cat.add_task(CareTask("Feed", schedule2))

        due = tracker.all_due(date(2025, 1, 1))

        self.assertEqual(len(due), 1)
        self.assertEqual(due[0], ("A", "Max", "Walk"))


if __name__ == "__main__":
    unittest.main()
