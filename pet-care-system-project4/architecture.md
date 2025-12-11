# Architecture Documentation  
**Pet Care Tracker – INST326 Project 4**  
**Author:** Amar Hassan  

---

## 1. System Overview
The Pet Care Tracker follows a modular, object-oriented architecture designed around core software engineering principles such as abstraction, encapsulation, inheritance, and separation of concerns.

The system is divided into four major layers:

1. **Model Layer** – All core classes and logic  
2. **Storage Layer** – Saving and loading system data  
3. **Controller Layer** – User interaction logic  
4. **Interface Layer (CLI)** – Menus and user prompts (main.py)

This organization keeps logic clean, reduces coupling, and makes the system easier to maintain and test.

---

## 2. Major Components & Class Responsibilities

### **2.1 Model Layer (`src/model/`)**
This layer contains all domain logic.

---

### **`pets.py`**
Defines the base class **Pet**, which includes:
- Name, breed, age, weight  
- Methods for food calculation, exercise needs  
- Task management  
- Veterinary record  
- Serialization (to/from dictionary)

Three subclasses extend Pet:
- **Dog**
- **Cat**
- **Bird**

Inheritance allows different species to override:
- `daily_food_amount()`  
- `daily_exercise_minutes()`  
- `sound()`

This demonstrates polymorphism because each subclass behaves differently.

---

### **`tasks.py`**
Defines the **CareTask** class:
- A task label ("Feed", "Walk", etc.)
- A recurrence schedule
- Optional notes
- Logic for checking if a task is due
- Serialization support

---

### **`schedule.py`**
Defines the **Schedule** class:
- Controls recurrence (every X days)
- Tracks the last completion date
- Computes next due date
- Provides clean serialization for persistence

---

### **`vetrecord.py`**
Stores:
- Vaccination history  
- Appointment notes  

Used by the Pet class.  
Supports JSON serialization.

---

### **`tracker.py`**
Top-level container for the entire system:
- Stores all owners  
- Provides global “tasks due today” search  
- Handles full-system serialization

---

### **`Owner` class (inside tracker.py)**
Each owner:
- Has a name and optional email  
- Stores multiple pets  
- Provides lookup and add functions

---

## 3. Storage Layer (`src/storage.py`)

Handles persistence of the entire system.

Responsibilities:
- Save tracker data to `data/data.json`
- Load tracker data back into objects
- Create automatic backup (`data.json.bak`)
- Recover from corrupted files
- Validate file existence and JSON structure

Tools used:
- `json` module  
- `pathlib`  
- Centralized `StorageManager` class  

This layer completely separates file I/O from business logic.

---

## 4. Controller Layer (`src/controller.py`)

This layer manages how users interact with the system.

### Controller responsibilities:
- Display menus  
- Interpret user choices  
- Call model methods  
- Call storage save/load  
- Handle errors and invalid input  
- Provide clean CLI formatting (color class included)

This layer keeps the CLI interface out of model logic, improving separation of concerns.

---

## 5. Interface Layer (`src/main.py`)

Entry point of the program.

Responsibilities:
- Show splash screen  
- Initialize `StorageManager`  
- Create or load the main `Tracker` instance  
- Start the controller’s main menu loop  
- Provide safe exception handling  

---

## 6. Data Flow Summary

### **Application Startup**
1. User runs `main.py`  
2. StorageManager loads data.json → Tracker object  
3. Controller launches main menu  

---

### **Adding a Pet**
1. Controller asks user for owner + pet details  
2. Controller creates Pet object  
3. Pet is added to Owner  
4. Owner stored inside Tracker  
5. Data saved to JSON  

---

### **Adding a Task**
1. Controller collects task info  
2. Create Schedule → CareTask  
3. Add task to a Pet  
4. Save to JSON  

---

### **Listing Tasks Due Today**
1. Controller calls `tracker.all_due(date)`  
2. Tracker collects due tasks across all pets  
3. Controller prints results  

---

### **Saving Data**
Controller → StorageManager → JSON file

### **Loading Data**
StorageManager → JSON → Rebuild model objects

---

## 7. Key Design Decisions

### **7.1 Separation of Concerns**
Model classes contain no user input code.  
Controller contains no business logic.  
Storage contains no domain rules.

This separation keeps the project clean and testable.

---

### **7.2 Serialization in All Classes**
Every model class implements:
- `to_dict()`
- `@classmethod from_dict()`

This allows:
- Simple JSON persistence  
- Easy import/export  
- Rebuilding full systems from files  

---

### **7.3 Backup File Protection**
A `.bak` file is automatically created.  
If `data.json` becomes corrupted:
- System loads from backup  
- Protects user data  

---

### **7.4 Full Testing Coverage**
The design supports testing at three levels:
- Unit tests (models)
- Integration tests (multiple classes interacting)
- System tests (save → load → workflow)

---

## 8. Known Limitations & Future Improvements
- No GUI (CLI only)
- Tasks cannot currently “expire”
- No database support (JSON only)
- No user authentication

Possible future enhancements:
- Add mobile app or web interface  
- Add reminders with real-time notifications  
- Add more species and task categories  

---

## ✔️ Conclusion
This architecture follows clean object-oriented principles, is easy to maintain, and demonstrates full integration of course concepts from INST326. It supports persistence, testing, and multi-component workflows, making it a strong capstone-level project.
