# test_vetrecord.py
import unittest
from model.vetrecord import VetRecord


class TestVetRecord(unittest.TestCase):

    def test_add_vaccination(self):
        v = VetRecord()
        v.add_vaccination("Rabies")
        self.assertIn("Rabies", v.vaccinations)

    def test_add_appointment(self):
        v = VetRecord()
        v.add_appointment("Checkup")
        self.assertIn("Checkup", v.appointments)

    def test_serialization_round_trip(self):
        v = VetRecord(["Rabies"], ["Checkup"])
        d = v.to_dict()
        restored = VetRecord.from_dict(d)

        self.assertEqual(restored.vaccinations, ["Rabies"])
        self.assertEqual(restored.appointments, ["Checkup"])


if __name__ == "__main__":
    unittest.main()

