# test_schedule.py
import unittest
from datetime import date, timedelta

from model.schedule import Schedule


class TestSchedule(unittest.TestCase):

    def test_initial_next_due_equals_start(self):
        s = Schedule(every_days=3, start=date(2025, 1, 1))
        self.assertEqual(s.next_due(), date(2025, 1, 1))

    def test_next_due_after_completion(self):
        s = Schedule(2, date(2025, 1, 1))
        s.mark_completed(date(2025, 1, 3))
        self.assertEqual(s.next_due(), date(2025, 1, 5))

    def test_is_due_true(self):
        s = Schedule(1, date(2025, 1, 1))
        self.assertTrue(s.is_due(date(2025, 1, 2)))

    def test_is_due_false(self):
        s = Schedule(5, date(2025, 1, 1))
        self.assertFalse(s.is_due(date(2025, 1, 2)))

    def test_serialization_round_trip(self):
        s = Schedule(3, date(2025, 1, 1))
        s.mark_completed(date(2025, 1, 4))
        d = s.to_dict()
        restored = Schedule.from_dict(d)
        self.assertEqual(restored.next_due(), s.next_due())


if __name__ == "__main__":
    unittest.main()
