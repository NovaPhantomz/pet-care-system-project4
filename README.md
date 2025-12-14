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

▶️ How to Run the Application
1. Move into the project folder:
cd pet-care-system-project4
2. Run the program:
python3 src/main.py
You will see:
A splash screen
Main menu
Options to add/view owners, pets, tasks
Import/Export tools
Save/load options
🧪 How to Run All Tests
From the project root:
python3 -m unittest discover -s tests
The tests cover:
Schedule logic
Task completion rules
Pet inheritance + serialization
Owner/Tracker integration
Storage save/load + corrupted file recovery
Multi-step integration flows
Full system save → load verification
All tests should pass.
📤 Importing Tasks via CSV
CSV must follow this format:
owner,pet,task_label,every_days,start_date,notes
Amar,Luna,Feed,1,2025-01-01,Morning feeding
Amar,Luna,Walk,1,2025-01-01,30-minute walk
To import:
Open the main menu
Select “Import Tasks (CSV)”
Enter the file path
📥 Exporting Pet Summaries
Exports a pet’s details to a JSON file.
Includes:
Name
Breed
Age
Weight
All care tasks
Veterinary record
🗄️ Data Persistence
The system stores all data in:
data/data.json
A backup is created automatically:
data/data.json.bak
If the main file becomes corrupted, the backup is used automatically.
🎥 Project Presentation Video
Insert the link to your video presentation here:
[Add link before submission]
🧑‍💻 Notes on AI Collaboration
AI assistance was used for:
Initial file structure planning
Drafting documentation
Helping generate testing scaffolds
All code was reviewed, understood, and validated before being included.
✅ Final Notes
This capstone project demonstrates:
Strong OOP design
Real file persistence
CLI-based workflows
A complete integration-tested system