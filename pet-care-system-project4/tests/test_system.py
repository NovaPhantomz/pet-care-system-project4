# test_system.py
import unittest
import os
from datetime import date

from storage import StorageManager
from model.tracker import Tracker, Owner
from model.pets import Dog
from model.schedule import Schedule
from model.tasks import CareTask


class TestSystem(unittest.TestCase):

    def setUp(self):
        self.test_path = "data/test_system.json"
        self.store = StorageManager(self.test_path)

        # Ensure directory exists
        os.makedirs("data", exist_ok=True)

        # Build full system
        self.tracker = Tracker()

        owner = Owner("Amar")
        dog = Dog("Luna", "Lab", 10, 3)

        schedule = Schedule(1, date(2025, 1, 1))
        task = CareTask("Feed", schedule)

        dog.add_task(task)
        owner.add_pet(dog)
        self.tracker.register_owner(owner)

    def tearDown(self):
        # Clean up test files
        if os.path.exists(self.test_path):
            os.remove(self.test_path)
        if os.path.exists(self.test_path + ".bak"):
            os.remove(self.test_path + ".bak")

    def test_full_system_save_load(self):
        """
        Tests full system behavior:
        - save Tracker to file
        - load Tracker from file
        - verify all data persisted
        """
        # Save system
        saved = self.store.save(self.tracker)
        self.assertTrue(saved)

        # Load system
        loaded = self.store.load()
        self.assertIsNotNone(loaded)

        # Verify round-trip data
        self.assertIn("Amar", loaded.owners)
        self.assertIn("Luna", loaded.owners["Amar"].pets_map)

        restored_task_labels = [
            t.label for t in loaded.owners["Amar"].pets_map["Luna"].all_tasks()
        ]

        self.assertIn("Feed", restored_task_labels)


if __name__ == "__main__":
    unittest.main()

