# schedule.py
from datetime import date, timedelta


class Schedule:
    """
    Represents a recurring schedule for a care task.
    Handles:
    - every N days recurrence
    - last completed date
    - next due date logic
    - serialization for saving/loading
    """

    def __init__(self, every_days: int, start: date, last_completed: date = None):
        if every_days <= 0:
            raise ValueError("Recurrence must be at least 1 day.")
        if not isinstance(start, date):
            raise ValueError("Start must be a date object.")

        self._every_days = every_days
        self._start = start
        self._last_completed = last_completed

    # ---------------------------------------------------------
    # Logic
    # ---------------------------------------------------------

    def mark_completed(self, on: date):
        if not isinstance(on, date):
            raise ValueError("Completion date must be a date.")
        self._last_completed = on

    def next_due(self) -> date:
        if self._last_completed is None:
            return self._start
        return self._last_completed + timedelta(days=self._every_days)

    def is_due(self, on: date) -> bool:
        if not isinstance(on, date):
            raise ValueError("Check date must be a date.")
        return on >= self.next_due()

    # ---------------------------------------------------------
    # Serialization
    # ---------------------------------------------------------

    def to_dict(self) -> dict:
        return {
            "every_days": self._every_days,
            "start": self._start.isoformat(),
            "last_completed": (
                self._last_completed.isoformat() if self._last_completed else None
            ),
        }

    @classmethod
    def from_dict(cls, data: dict):
        every = data["every_days"]
        start = date.fromisoformat(data["start"])
        last = (
            date.fromisoformat(data["last_completed"])
            if data.get("last_completed")
            else None
        )
        return cls(every, start, last)

    # ---------------------------------------------------------

    def __str__(self):
        if self._last_completed:
            return f"every {self._every_days} day(s), last completed {self._last_completed}"
        return f"every {self._every_days} day(s), starting {self._start}"
