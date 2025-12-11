# test_tracker.py
import unittest
from datetime import date

from model.tracker import Tracker, Owner
from model.pets import Dog
from model.schedule import Schedule
from model.tasks import CareTask


class TestTracker(unittest.TestCase):

    def test_register_owner(self):
        t = Tracker()
        o = Owner("Amar")
        t.register_owner(o)
        self.assertIn("Amar", t.owners)

    def test_find_due_tasks(self):
        t = Tracker()
        owner = Owner("A")
        dog = Dog("Luna", "Lab", 10, 2)

        schedule = Schedule(1, date(2025, 1, 1))
        task = CareTask("Feed", schedule)
        dog.add_task(task)

        owner.add_pet(dog)
        t.register_owner(owner)

        due = t.all_due(date(2025, 1, 1))
        self.assertEqual(len(due), 1)
        self.assertEqual(due[0], ("A", "Luna", "Feed"))

    def test_tracker_serialization_round_trip(self):
        t = Tracker()
        owner = Owner("A")
        dog = Dog("Luna", "Lab", 10, 2)

        schedule = Schedule(1, date(2025, 1, 1))
        task = CareTask("Feed", schedule)
        dog.add_task(task)

        owner.add_pet(dog)
        t.register_owner(owner)

        data = t.to_dict()
        restored = Tracker.from_dict(data)

        self.assertIn("A", restored.owners)
        self.assertIn("Luna", restored.owners["A"].pets_map)


if __name__ == "__main__":
    unittest.main()

