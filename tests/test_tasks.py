# test_tasks.py
import unittest
from datetime import date

from model.tasks import CareTask
from model.schedule import Schedule


class TestTasks(unittest.TestCase):

    def test_task_due_logic(self):
        schedule = Schedule(2, date(2025, 1, 1))
        task = CareTask("Feed", schedule)
        self.assertTrue(task.is_due(date(2025, 1, 1)))

    def test_task_completion_updates_next_due(self):
        schedule = Schedule(2, date(2025, 1, 1))
        task = CareTask("Walk", schedule)
        task.complete(date(2025, 1, 3))
        self.assertEqual(task.next_due(), date(2025, 1, 5))

    def test_task_serialization_round_trip(self):
        schedule = Schedule(1, date(2025, 1, 1))
        task = CareTask("Brush", schedule, "Daily brushing")
        d = task.to_dict()
        restored = CareTask.from_dict(d)

        self.assertEqual(restored.label, "Brush")
        self.assertEqual(restored.notes, "Daily brushing")


if __name__ == "__main__":
    unittest.main()

