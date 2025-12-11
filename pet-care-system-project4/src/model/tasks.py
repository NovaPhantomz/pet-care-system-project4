# tasks.py
from datetime import date
from model.schedule import Schedule


class CareTask:
    """
    Represents a care task assigned to a pet.
    Includes:
    - label (e.g., "Feed", "Walk")
    - schedule (recurrence logic)
    - optional notes
    - serialization support
    """

    def __init__(self, label: str, schedule: Schedule, notes: str = ""):
        if not isinstance(label, str) or not label.strip():
            raise ValueError("Task label must be a non-empty string.")
        if not isinstance(schedule, Schedule):
            raise ValueError("schedule must be a Schedule instance.")

        self._label = label.strip()
        self._schedule = schedule
        self._notes = notes

    # ---------------------------------------------------------
    # Core logic
    # ---------------------------------------------------------

    def complete(self, on: date):
        """Mark task completed on a specific date."""
        self._schedule.mark_completed(on)

    def is_due(self, on: date) -> bool:
        """Return True if task is due on the given date."""
        return self._schedule.is_due(on)

    def next_due(self) -> date:
        """Return the next date when this task is due."""
        return self._schedule.next_due()

    # ---------------------------------------------------------
    # Properties
    # ---------------------------------------------------------

    @property
    def label(self) -> str:
        return self._label

    @property
    def notes(self) -> str:
        return self._notes

    @property
    def schedule(self) -> Schedule:
        return self._schedule

    # ---------------------------------------------------------
    # Serialization
    # ---------------------------------------------------------

    def to_dict(self) -> dict:
        return {
            "label": self._label,
            "notes": self._notes,
            "schedule": self._schedule.to_dict(),
        }

    @classmethod
    def from_dict(cls, data: dict):
        schedule = Schedule.from_dict(data["schedule"])
        return cls(
            label=data["label"],
            schedule=schedule,
            notes=data.get("notes", "")
        )

    # ---------------------------------------------------------

    def __str__(self):
        return f"{self._label} — next due {self.next_due()}"
