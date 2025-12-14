# Pet Care Tracker — INST326 Project 4
**Author:** Amar Hassan  
**Course:** INST326 — Object-Oriented Programming  
**Project:** Capstone Integration & Testing (Project 4)

---

## 📌 Overview
The **Pet Care Tracker** is a complete information management system that tracks daily care needs for pets across multiple owners. This capstone project brings together all major concepts from INST326, including:

- Object-oriented design  
- Abstraction, inheritance, and polymorphism  
- Data persistence (save/load)  
- CSV data import  
- JSON export  
- Integration testing and system testing  
- CLI-based interactive application  

This system represents a full end-to-end software application that stores data, loads it back, and supports complete workflows.

---

## 👥 Team & Contributions
This project was completed individually by **Amar Hassan**.  
All system design, implementation, testing, documentation, and presentation were completed by me.


---

## 🐾 What the System Can Do
- Manage **multiple owners**
- Manage **multiple pets per owner**
- Add or remove **pets**
- Add or remove **care tasks**
- Track **recurring tasks** (feed, walk, grooming, etc.)
- View **all tasks due today**
- Import tasks from **CSV**
- Export pet summaries as **JSON**
- Persist all data to disk (data.json)
- Includes full test suite: unit, integration, system

---

## ▶️ How to Run the Application

First, move into the project’s root directory. From there, run the main application file using Python. Once the program starts, you will see a splash screen followed by a main menu. The menu allows you to add and view owners, manage pets, create and track care tasks, import and export data, and save or load the system state.
To run the application:
cd pet-care-system-project4
python3 src/main.py

## 🧪 How to Run All Tests
All tests can be run from the project root directory using Python’s built-in unittest framework. The test suite includes unit tests, integration tests, and system tests that validate the correctness and reliability of the application.
To run the full test suite:
python3 -m unittest discover -s tests
The tests cover schedule logic, task completion rules, pet inheritance and serialization, owner and tracker integration, storage save and load behavior including corrupted file recovery, multi-step integration workflows, and full system save-to-load verification. All tests should pass successfully.

## 📤 Importing Tasks via CSV
The system supports importing care tasks from a CSV file. The CSV file must follow this format:
owner,pet,task_label,every_days,start_date,notes
Amar,Luna,Feed,1,2025-01-01,Morning feeding
Amar,Luna,Walk,1,2025-01-01,30-minute walk
To import tasks, open the main menu, select the option to import tasks from CSV, and enter the file path when prompted. The system validates each row before adding the tasks.

## 📥 Exporting Pet Summaries
The application allows users to export a pet’s information to a JSON file. The exported summary includes the pet’s name, breed, age, weight, all assigned care tasks, and veterinary record information. This feature provides an easy way to generate reports or backups.

## 🗄️ Data Persistence
All application data is stored in a JSON file located at data/data.json. A backup file named data/data.json.bak is created automatically. If the main data file becomes corrupted, the system automatically restores data from the backup to prevent data loss.

🎥 Project Presentation Video
Link to the Project 4 presentation video:
https://drive.google.com/file/d/17gZaNFGEYq-njji1DXCKGRgT8Rbv9emV/view?usp=sharing



## 📁 Project Structure

```plaintext
src/
│   main.py
│   controller.py
│   storage.py
│
└── model/
    pets.py
    tasks.py
    schedule.py
    vetrecord.py
    tracker.py

tests/
    test_schedule.py
    test_vetrecord.py
    test_tasks.py
    test_pets.py
    test_tracker.py
    test_storage.py
    test_integration.py
    test_system.py

data/
    data.json

README.md
architecture.md
testing_documentation.md
requirements.txt
