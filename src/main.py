# main.py
import os
from controller import Controller, Color
from storage import StorageManager


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def splash_screen():
    clear()
    print(Color.HEADER + "========================================" + Color.RESET)
    print(Color.HEADER + "         PET CARE TRACKER SYSTEM        " + Color.RESET)
    print(Color.DIM + "            INST326 • Project 4" + Color.RESET)
    print(Color.DIM + "                Amar Hassan" + Color.RESET)
    print(Color.HEADER + "========================================\n" + Color.RESET)

    input(Color.DIM + "Press Enter to continue..." + Color.RESET)


def main():
    # Show startup splash screen
    splash_screen()

    # Initialize system with storage manager
    storage = StorageManager(filepath="data/data.json")
    controller = Controller(storage)

    # Run main menu
    try:
        controller.main_menu()
    except KeyboardInterrupt:
        print(Color.WARNING + "\nExiting due to keyboard interrupt." + Color.RESET)
    except Exception as e:
        print(Color.ERROR + f"\nUnexpected error: {e}" + Color.RESET)


if __name__ == "__main__":
    main()
