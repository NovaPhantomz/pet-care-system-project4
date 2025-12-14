# Testing Documentation

## 1. Overview

This document describes the full testing process for the **Pet Care Tracker** Project 4, including unit tests, integration tests, system tests, expected behaviors, and test data used during evaluation.

---

## 2. Testing Strategy

The testing strategy is built around three layers of verification:

### **2.1 Unit Testing**

Each class was tested individually to ensure that attributes, methods, and error handling behave correctly. Unit tests focus on:

* Owner class creation and pet management
* Pet class attribute handling
* CareTask class recurrence and date logic
* FileManager save and load operations
* CSV import parsing
* JSON export formatting

### **2.2 Integration Testing**

Integration tests verify that multiple classes interact correctly:

* Owners correctly store multiple pets
* Pets correctly store multiple tasks
* FileManager correctly loads nested owners+pets+tasks
* CSV import writes tasks to correct pets
* Task filtering functions correctly determine which tasks are due

### **2.3 System Testing**

System tests validate the full CLI workflow from the user's perspective:

* Adding owners, pets, and tasks through prompts
* Viewing due tasks
* Saving and loading the full dataset
* Exporting JSON summaries
* Exiting and re-entering the program without losing data

---

## 3. Unit Tests

Below is a summary of the major unit tests used.

### **3.1 Owner Class Tests**

* Test owner creation with valid and invalid names
* Test adding a pet to an owner
* Test removing a pet
* Test retrieving pet list

### **3.2 Pet Class Tests**

* Test pet creation with various types (dog, cat, etc.)
* Test adding tasks to a pet
* Test removing tasks
* Test fetching tasks due today

### **3.3 CareTask Class Tests**

* Test task creation with recurrence types (daily, weekly, monthly)
* Test marking a task as completed
* Test next due date calculation
* Test edge cases (invalid dates, recurrence types)

### **3.4 FileManager Tests**

* Test saving the full dataset to data.json
* Test loading the dataset back into objects
* Test JSON output for each pet
* Test CSV import with valid/invalid rows

---

## 4. Integration Tests

### **4.1 Owner + Pet Integration Tests**

* Ensure pets added to an owner appear in the returned list
* Ensure pet deletion correctly updates the owner's pet list

### **4.2 Pet + CareTask Integration Tests**

* Verify that multiple tasks store correctly under a pet
* Verify task filtering returns only due tasks

### **4.3 FileManager + Data Model Integration Tests**

* Load a dataset and confirm the structure is recreated identically
* After CSV import, confirm new tasks attach to the correct pet

---

## 5. System Tests

System tests simulate full user interactions.

### **5.1 Adding Owners and Pets**

1. Start program
2. Add owner "Amar Hassan"
3. Add pet "Milo" (dog)
4. Confirm both appear when listed

**Expected Result:** Entries appear correctly.

### **5.2 Adding Tasks**

1. Select "Milo"
2. Add task "Feed" (daily)
3. Add task "Walk" (daily)
4. Display tasks

**Expected Result:** Both tasks appear with correct recurrence type.

### **5.3 Persisting Data**

1. Add owner, pet, and tasks
2. Exit program (auto-save)
3. Restart program
4. Load data.json

**Expected Result:** All owners, pets, and tasks reappear.

### **5.4 Exporting JSON**

1. Export pet summaries
2. Verify JSON file structure

**Expected Result:** JSON contains correct fields and nested structure.

---

## 6. Test Data Used

### **Owners:**

* "Amar Hassan"
* "John Doe"

### **Pets:**

* Milo (Dog)
* Luna (Cat)

### **Tasks:**

* Feed — daily
* Walk — daily
* Clean litter — weekly
* Vet check — monthly

### **CSV Import Example:**

```
pet_name,task_name,recurrence,due_date
Milo,Brush,daily,2025-01-01
Luna,Trim nails,monthly,2025-01-10
```

---

## 7. Known Issues / Edge Cases

* CSV rows missing fields are skipped
* Invalid recurrence types default to "daily"
* If pets have identical names under different owners, CSV import requires manual disambiguation

---

## 8. Conclusion

Testing confirms that the Pet Care Tracker meets all functional requirements for Project 4. The system successfully supports owners, pets, tasks, saving, loading, and full application workflows.
