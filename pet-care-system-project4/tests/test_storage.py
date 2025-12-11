# test_storage.py
import unittest
import os
from datetime import date

from storage import StorageManager
from model.tracker import Tracker, Owner
from model.pets import Dog
from model.schedule import Schedule
from model.tasks import CareTask


class TestStorage(unittest.TestCase):

    def setUp(self):
        # Use a temp file for safety
        self.test_file = "data/test_data.json"
        self.store = StorageManager(self.test_file)

        self.tracker = Tracker()
        owner = Owner("Amar")
        dog = Dog("Luna", "Lab", 10, 5)
        schedule = Schedule(1, date(2025, 1, 1))
        task = CareTask("Feed", schedule)

        dog.add_task(task)
        owner.add_pet(dog)
        self.tracker.register_owner(owner)

        # Ensure data directory exists
        os.makedirs("data", exist_ok=True)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.test_file + ".bak"):
            os.remove(self.test_file + ".bak")

    def test_save_and_load(self):
        self.store.save(self.tracker)
        loaded = self.store.load()

        self.assertIsNotNone(loaded)
        self.assertIn("Amar", loaded.owners)
        self.assertIn("Luna", loaded.owners["Amar"].pets_map)

    def test_corrupted_file_recovery(self):
        # Save a valid file
        self.store.save(self.tracker)

        # Corrupt it
        with open(self.test_file, "w") as f:
            f.write("THIS IS NOT JSON")

        # Now load should try backup
        loaded = self.store.load()

        # Valid backup should restore Tracker
        self.assertIsNotNone(loaded)
        self.assertIn("Amar", loaded.owners)


if __name__ == "__main__":
    unittest.main()
