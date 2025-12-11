# vetrecord.py


class VetRecord:
    """
    Stores a pet's vet history:
    - vaccinations
    - vet appointments
    Includes serialization for persistence.
    """

    def __init__(self, vaccinations=None, appointments=None):
        self._vaccinations = vaccinations if vaccinations else []
        self._appointments = appointments if appointments else []

    # ---------------------------------------------------------
    # Add records
    # ---------------------------------------------------------

    def add_vaccination(self, name: str):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Vaccination name must be a non-empty string.")
        self._vaccinations.append(name.strip())

    def add_appointment(self, note: str):
        if not isinstance(note, str) or not note.strip():
            raise ValueError("Appointment note must be a non-empty string.")
        self._appointments.append(note.strip())

    # ---------------------------------------------------------
    # Properties
    # ---------------------------------------------------------

    @property
    def vaccinations(self):
        return self._vaccinations

    @property
    def appointments(self):
        return self._appointments

    # ---------------------------------------------------------
    # Serialization
    # ---------------------------------------------------------

    def to_dict(self) -> dict:
        return {
            "vaccinations": self._vaccinations,
            "appointments": self._appointments,
        }

    @classmethod
    def from_dict(cls, data: dict):
        vaccinations = data.get("vaccinations", [])
        appointments = data.get("appointments", [])
        return cls(vaccinations, appointments)

    # ---------------------------------------------------------

    def __str__(self):
        return f"{len(self._vaccinations)} vaccination(s), {len(self._appointments)} appointment(s)"
