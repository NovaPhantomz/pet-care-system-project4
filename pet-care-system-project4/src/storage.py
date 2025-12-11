# storage.py

import json
import os
from pathlib import Path
from typing import Optional
from datetime import date

import csv

from model.tracker import Tracker
from model.tasks import CareTask
from model.schedule import Schedule


class StorageManager:
    """
    Handles saving/loading the entire Tracker system to a single JSON file.
    Also supports CSV import and JSON export.
    """

    def __init__(self, filepath: str = "data/data.json"):
        self.filepath = Path(filepath)
        self.filepath.parent.mkdir(parents=True, exist_ok=True)

    # ---------------------------------------------------------
    # SAVE SYSTEM STATE
    # ---------------------------------------------------------

    def save(self, tracker: Tracker) -> bool:
        """Save system as one JSON file."""
        try:
            data = tracker.to_dict()
            json_text = json.dumps(data, indent=4)

            # Backup before overwrite
            if self.filepath.exists():
                backup_path = self.filepath.with_suffix(".bak")
                backup_path.write_text(self.filepath.read_text())

            self.filepath.write_text(json_text)
            return True

        except Exception as e:
            print(f"Error saving data: {e}")
            return False

    # ---------------------------------------------------------
    # LOAD SYSTEM STATE
    # ---------------------------------------------------------

    def load(self) -> Optional[Tracker]:
        """Load system from JSON. Return Tracker or None."""
        if not self.filepath.exists():
            print("No save file found — starting fresh.")
            return None

        try:
            raw = self.filepath.read_text()
            data = json.loads(raw)
            return Tracker.from_dict(data)

        except json.JSONDecodeError:
            print("Error: data.json is corrupted.")
            print("Attempting backup recovery...")

            backup = self.filepath.with_suffix(".bak")
            if backup.exists():
                try:
                    raw_backup = backup.read_text()
                    data = json.loads(raw_backup)
                    print("Recovered using backup file.")
                    return Tracker.from_dict(data)
                except:
                    print("Backup also corrupted.")
                    return None
            else:
                print("No backup available.")
                return None

        except Exception as e:
            print(f"Unexpected load error: {e}")
            return None

    # ---------------------------------------------------------
    # IMPORT TASKS FROM CSV
    # ---------------------------------------------------------

    def import_tasks_csv(self, tracker: Tracker, csv_path: str):
        """
        Imports tasks from CSV.
        CSV format:
            owner,pet,task_label,every_days,start_date,notes
        """
        count = 0

        try:
            with open(csv_path, newline="") as f:
                reader = csv.DictReader(f)

                for row in reader:
                    owner_name = row["owner"]
                    pet_name = row["pet"]
                    label = row["task_label"]
                    every_days = int(row["every_days"])
                    start_date = date.fromisoformat(row["start_date"])
                    notes = row.get("notes", "")

                    owner = tracker.get_owner(owner_name)
                    if not owner:
                        print(f"Skipping: owner {owner_name} not found.")
                        continue

                    pet = owner.pets_map.get(pet_name)
                    if not pet:
                        print(f"Skipping: pet {pet_name} not found.")
                        continue

                    schedule = Schedule(every_days, start_date)
                    task = CareTask(label, schedule, notes)

                    try:
                        pet.add_task(task)
                        count += 1
                    except ValueError:
                        print(f"Duplicate task skipped: {label}")

            return count

        except FileNotFoundError:
            print("CSV file not found.")
            return 0
        except Exception as e:
            print(f"CSV import error: {e}")
            return 0

    # ---------------------------------------------------------
    # EXPORT PET SUMMARY AS JSON
    # ---------------------------------------------------------

    def export_pet_summary(self, owner_name: str, pet_name: str, tracker: Tracker, out_path: str) -> bool:
        """Export one pet's details as JSON."""
        try:
            owner = tracker.get_owner(owner_name)
            if not owner:
                print("Owner not found.")
                return False

            pet = owner.pets_map.get(pet_name)
            if not pet:
                print("Pet not found.")
                return False

            summary = pet.to_dict()
            Path(out_path).write_text(json.dumps(summary, indent=4))
            return True

        except Exception as e:
            print(f"Export error: {e}")
            return False
