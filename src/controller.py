# controller.py
import os
from datetime import date

from storage import StorageManager
from model.tracker import Tracker, Owner
from model.pets import Dog, Cat, Bird
from model.tasks import CareTask
from model.schedule import Schedule


# -------------------------------------------------------
# COLOR CLASS (subtle professional palette)
# -------------------------------------------------------
class Color:
    HEADER = "\033[95m"
    OK = "\033[96m"
    SUCCESS = "\033[92m"
    WARNING = "\033[93m"
    ERROR = "\033[91m"
    RESET = "\033[0m"
    DIM = "\033[90m"


# -------------------------------------------------------
# CONTROLLER
# -------------------------------------------------------
class Controller:
    """
    The Controller orchestrates:
    - menus
    - user interaction
    - calling Tracker
    - saving/loading via StorageManager
    """

    def __init__(self, storage: StorageManager):
        self.storage = storage
        loaded = self.storage.load()
        self.tracker = loaded if loaded else Tracker()

    # ---------------------------------------------------
    # HELPER FUNCTIONS
    # ---------------------------------------------------
    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def pause(self):
        input(Color.DIM + "\nPress Enter to continue..." + Color.RESET)

    # ---------------------------------------------------
    # MAIN MENU
    # ---------------------------------------------------
    def main_menu(self):
        while True:
            self.clear()
            print(Color.OK + "==== PET CARE TRACKER ====" + Color.RESET)
            print("1. Manage Owners")
            print("2. Manage Pets")
            print("3. Manage Tasks")
            print("4. Import Tasks (CSV)")
            print("5. Export Pet Summary")
            print("6. Save System")
            print("7. Quit")

            choice = input(Color.DIM + "\nChoose an option: " + Color.RESET).strip()

            if choice == "1":
                self.menu_owners()
            elif choice == "2":
                self.menu_pets()
            elif choice == "3":
                self.menu_tasks()
            elif choice == "4":
                self.import_csv_menu()
            elif choice == "5":
                self.export_menu()
            elif choice == "6":
                self.save_system()
            elif choice == "7":
                print(Color.WARNING + "Exiting program..." + Color.RESET)
                return
            else:
                print(Color.ERROR + "Invalid choice." + Color.RESET)
                self.pause()

    # ---------------------------------------------------
    # OWNERS MENU
    # ---------------------------------------------------
    def menu_owners(self):
        while True:
            self.clear()
            print(Color.OK + "==== OWNERS ====" + Color.RESET)

            print("Owners:")
            for name in self.tracker.owners:
                print(" -", name)

            print("\n1. Add Owner")
            print("2. Remove Owner")
            print("3. Back")

            choice = input(Color.DIM + "\nChoose: " + Color.RESET).strip()

            if choice == "1":
                self.add_owner()
            elif choice == "2":
                self.remove_owner()
            elif choice == "3":
                return
            else:
                print(Color.ERROR + "Invalid choice." + Color.RESET)
                self.pause()

    def add_owner(self):
        name = input("Enter owner name: ").strip()
        if not name:
            print(Color.ERROR + "Name cannot be empty." + Color.RESET)
            self.pause()
            return

        try:
            owner = Owner(name)
            self.tracker.register_owner(owner)
            print(Color.SUCCESS + "Owner added." + Color.RESET)
        except Exception as e:
            print(Color.ERROR + f"Error: {e}" + Color.RESET)

        self.pause()

    def remove_owner(self):
        name = input("Enter owner name to remove: ").strip()
        if name in self.tracker.owners:
            self.tracker.remove_owner(name)
            print(Color.SUCCESS + "Owner removed." + Color.RESET)
        else:
            print(Color.ERROR + "Owner not found." + Color.RESET)
        self.pause()

    # ---------------------------------------------------
    # PETS MENU
    # ---------------------------------------------------
    def menu_pets(self):
        while True:
            self.clear()
            print(Color.OK + "==== PETS ====" + Color.RESET)

            print("Owners:")
            for name in self.tracker.owners:
                print(" -", name)

            print("\n1. Add Pet")
            print("2. Remove Pet")
            print("3. Back")

            choice = input(Color.DIM + "\nChoose: " + Color.RESET).strip()

            if choice == "1":
                self.add_pet()
            elif choice == "2":
                self.remove_pet()
            elif choice == "3":
                return
            else:
                print(Color.ERROR + "Invalid choice." + Color.RESET)
                self.pause()

    def select_owner(self) -> Owner:
        """Helper: ask for owner name and return Owner or None."""
        name = input("Owner name: ").strip()
        return self.tracker.get_owner(name)

    def add_pet(self):
        owner = self.select_owner()
        if not owner:
            print(Color.ERROR + "Owner not found." + Color.RESET)
            self.pause()
            return

        name = input("Pet name: ").strip()
        breed = input("Breed: ").strip()
        try:
            weight = float(input("Weight (kg): ").strip())
            age = float(input("Age: ").strip())
        except:
            print(Color.ERROR + "Invalid number." + Color.RESET)
            self.pause()
            return

        print("Pet type:")
        print("1. Dog")
        print("2. Cat")
        print("3. Bird")
        type_choice = input("Choose: ").strip()

        if type_choice == "1":
            pet = Dog(name, breed, weight, age)
        elif type_choice == "2":
            pet = Cat(name, breed, weight, age)
        elif type_choice == "3":
            pet = Bird(name, breed, weight, age)
        else:
            print(Color.ERROR + "Invalid pet type." + Color.RESET)
            self.pause()
            return

        try:
            owner.add_pet(pet)
            print(Color.SUCCESS + "Pet added." + Color.RESET)
        except Exception as e:
            print(Color.ERROR + f"Error: {e}" + Color.RESET)

        self.pause()

    def remove_pet(self):
        owner = self.select_owner()
        if not owner:
            print(Color.ERROR + "Owner not found." + Color.RESET)
            self.pause()
            return

        pet_name = input("Pet to remove: ").strip()
        if pet_name in owner.pets_map:
            owner.remove_pet(pet_name)
            print(Color.SUCCESS + "Pet removed." + Color.RESET)
        else:
            print(Color.ERROR + "Pet not found." + Color.RESET)

        self.pause()

    # ---------------------------------------------------
    # TASKS MENU
    # ---------------------------------------------------
    def menu_tasks(self):
        while True:
            self.clear()
            print(Color.OK + "==== TASKS ====" + Color.RESET)

            print("1. Add Task")
            print("2. Show Tasks Due Today")
            print("3. Back")

            choice = input(Color.DIM + "\nChoose: " + Color.RESET).strip()

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.show_due_today()
            elif choice == "3":
                return
            else:
                print(Color.ERROR + "Invalid choice." + Color.RESET)
                self.pause()

    def add_task(self):
        owner = self.select_owner()
        if not owner:
            print(Color.ERROR + "Owner not found." + Color.RESET)
            self.pause()
            return

        pet_name = input("Pet name: ").strip()
        pet = owner.pets_map.get(pet_name)

        if not pet:
            print(Color.ERROR + "Pet not found." + Color.RESET)
            self.pause()
            return

        label = input("Task label: ").strip()
        notes = input("Notes (optional): ").strip()

        try:
            every_days = int(input("Every how many days? ").strip())
            start = date.fromisoformat(input("Start date (YYYY-MM-DD): ").strip())
        except:
            print(Color.ERROR + "Invalid input." + Color.RESET)
            self.pause()
            return

        task = CareTask(label, Schedule(every_days, start), notes)

        try:
            pet.add_task(task)
            print(Color.SUCCESS + "Task added." + Color.RESET)
        except Exception as e:
            print(Color.ERROR + f"Error: {e}" + Color.RESET)

        self.pause()

    def show_due_today(self):
        today = date.today()
        due = self.tracker.all_due(today)

        self.clear()
        print(Color.OK + f"==== TASKS DUE {today} ====" + Color.RESET)

        if not due:
            print(Color.DIM + "No tasks due today." + Color.RESET)
        else:
            for owner, pet, task in due:
                print(f"{owner} → {pet} → {task}")

        self.pause()

    # ---------------------------------------------------
    # IMPORT/EXPORT/SAVE
    # ---------------------------------------------------

    def import_csv_menu(self):
        path = input("CSV path: ").strip()
        count = self.storage.import_tasks_csv(self.tracker, path)
        print(Color.SUCCESS + f"Imported {count} tasks." + Color.RESET)
        self.pause()

    def export_menu(self):
        owner_name = input("Owner name: ").strip()
        pet_name = input("Pet name: ").strip()
        out_path = input("Output JSON path: ").strip()

        ok = self.storage.export_pet_summary(owner_name, pet_name, self.tracker, out_path)
        if ok:
            print(Color.SUCCESS + "Pet summary exported." + Color.RESET)
        else:
            print(Color.ERROR + "Export failed." + Color.RESET)

        self.pause()

    def save_system(self):
        if self.storage.save(self.tracker):
            print(Color.SUCCESS + "System saved." + Color.RESET)
        else:
            print(Color.ERROR + "Save failed." + Color.RESET)
        self.pause()

