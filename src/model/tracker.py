# tracker.py

from typing import Dict
from datetime import date

from model.pets import Pet, Dog, Cat, Bird


class Owner:
    """
    Represents a pet owner.
    Holds multiple pets.
    Supports serialization + lookup convenience.
    """

    def __init__(self, name: str, email: str = None):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Owner name must be a non-empty string.")

        self._name = name.strip()
        self._email = email
        self._pets: Dict[str, Pet] = {}

    # ---------------------------------------------------------
    # Properties
    # ---------------------------------------------------------

    @property
    def name(self):
        return self._name

    @property
    def pets(self):
        return list(self._pets.values())

    @property
    def pets_map(self):
        return self._pets  # name → Pet

    # ---------------------------------------------------------
    # Pet management
    # ---------------------------------------------------------

    def add_pet(self, pet: Pet):
        if pet.name in self._pets:
            raise ValueError("A pet with this name already exists.")
        self._pets[pet.name] = pet

    def remove_pet(self, name: str):
        if name in self._pets:
            del self._pets[name]

    # ---------------------------------------------------------
    # Serialization
    # ---------------------------------------------------------

    def to_dict(self) -> dict:
        return {
            "name": self._name,
            "email": self._email,
            "pets": [pet.to_dict() for pet in self._pets.values()],
        }

    @classmethod
    def from_dict(cls, data: dict):
        owner = cls(data["name"], data.get("email"))

        for p_data in data.get("pets", []):
            pet = Pet.from_dict(p_data)
            owner.add_pet(pet)

        return owner

    # ---------------------------------------------------------

    def __str__(self):
        return f"{self._name} — {len(self._pets)} pet(s)"


class Tracker:
    """
    Holds all owners.
    Provides:
    - register owner
    - find owners
    - find tasks due on a date
    - serialization (save/load)
    """

    def __init__(self):
        self._owners: Dict[str, Owner] = {}

    # ---------------------------------------------------------
    # Properties
    # ---------------------------------------------------------

    @property
    def owners(self):
        return self._owners  # name → Owner

    # ---------------------------------------------------------
    # Owner management
    # ---------------------------------------------------------

    def register_owner(self, owner: Owner):
        self._owners[owner.name] = owner

    def get_owner(self, name: str):
        return self._owners.get(name)

    def remove_owner(self, name: str):
        if name in self._owners:
            del self._owners[name]

    # ---------------------------------------------------------
    # Task queries
    # ---------------------------------------------------------

    def all_due(self, on: date):
        """Return list of (owner, pet, task_label) tuples for tasks due on this date."""
        results = []
        for owner in self._owners.values():
            for pet in owner.pets:
                for task in pet.due_tasks(on):
                    results.append((owner.name, pet.name, task.label))
        return results

    # ---------------------------------------------------------
    # Serialization
    # ---------------------------------------------------------

    def to_dict(self) -> dict:
        return {
            "owners": [owner.to_dict() for owner in self._owners.values()]
        }

    @classmethod
    def from_dict(cls, data: dict):
        tracker = cls()
        for o_data in data.get("owners", []):
            owner = Owner.from_dict(o_data)
            tracker.register_owner(owner)
        return tracker

    # ---------------------------------------------------------

    def __str__(self):
        return f"Tracker with {len(self._owners)} owner(s)"
