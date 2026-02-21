# Week 2 - File Handling & Data Management Systems

**Duration:** 7 days (Feb 14-20, 2026)  
**Focus:** File persistence, JSON/CSV operations, CRUD systems, Data validation

---

## 📌 Overview

This week focused on building production-ready data management systems with file persistence. All projects implement proper validation, error handling, and user-friendly interfaces.

**Key Achievement:** Transitioned from basic scripts to complete systems that businesses can actually use.

---

## 🎯 Projects Built

### 1️⃣ Library Management System
**File:** `BookLibarary_.py`

A complete library book tracking system with member management and issue/return functionality.

#### Features:
- ✅ Add new books with unique Book ID
- ✅ View all books with availability status
- ✅ Remove books from system
- ✅ Issue books to members
- ✅ Return books and update status
- ✅ Search books by ID
- ✅ Duplicate book ID prevention
- ✅ Timestamp tracking for all entries

#### Technical Implementation:
```python
Data Structure: JSON
Fields: name, author, bookId, available, issued_to, created_at
Storage: Persistent file storage with automatic save
Validation: Required fields, duplicate prevention
Error Handling: File not found, invalid input, book already issued
```

#### Sample Usage:
```
Add book → Issue to member → Track availability → Return → Update status
```

#### Code Highlights:
- Clean function separation (Single Responsibility)
- Proper state management (available/issued)
- Timestamp tracking with datetime
- Comprehensive error messages

---

### 2️⃣ Contact Management System
**File:** `contact_Management_System.py`

Professional contact manager with full CRUD operations and smart search functionality.

#### Features:
- ✅ Add contacts with validation
- ✅ View all contacts (alphabetically sorted)
- ✅ Search by name/phone/email
- ✅ Update contact information
- ✅ Remove contacts
- ✅ Duplicate phone number prevention
- ✅ Email format validation
- ✅ Phone number validation (digits only)

#### Technical Implementation:
```python
Data Structure: JSON
Fields: name, phone_no, gmail, created_at
Storage: Persistent JSON with auto-save
Validation: Email format, phone digits, required fields
Sorting: Lambda function for case-insensitive alphabetical sort
```

#### Advanced Features:
- Partial search (search "Am" finds "Aman")
- Multi-field search (name OR phone OR email)
- Sorted display for better UX
- Update without re-entering all fields

#### Code Highlights:
```python
# Smart search implementation
if (keyword in contact["name"].lower() or
    keyword in contact["phone_no"] or
    keyword in contact["gmail"].lower()):
```

---

### 3️⃣ Expense Tracker
**File:** `Expense_tracker.py`

Daily expense tracking system with category management and CSV export.

#### Features:
- ✅ Add expenses with date, category, amount
- ✅ View all expenses in table format
- ✅ Calculate total expenses
- ✅ CSV storage for easy Excel import
- ✅ Amount validation (must be number)
- ✅ Automatic file initialization

#### Technical Implementation:
```python
Data Structure: CSV
Fields: Date, Category, Amount, Description
Storage: CSV file with headers
Validation: Amount must be numeric, required fields
Calculations: Sum of all expenses
```

#### Why CSV?
- Easy to open in Excel/Google Sheets
- Human-readable format
- Lightweight and fast
- Universal compatibility

#### Sample Output:
```
Date        Category    Amount    Description
10-02-2026  Food        500       Lunch
11-02-2026  Transport   200       Auto
```

#### Code Highlights:
```python
# Safe amount conversion
try:
    amount = float(amount)
except ValueError:
    print("Amount must be a number!")
```

---

### 4️⃣ Student Grade Calculator
**File:** `gradeCalculatorAndStoreData.py`

Automated grade calculation and student record management system.

#### Features:
- ✅ Add student with multiple subject marks
- ✅ Calculate average and assign grades (A-F)
- ✅ View all students sorted by name
- ✅ Persistent JSON storage
- ✅ Automatic grade assignment
- ✅ Support for multiple students

#### Grading System:
```
90-100: Grade A
80-89:  Grade B
70-79:  Grade C
60-69:  Grade D
Below 60: Failed
```

#### Technical Implementation:
```python
Data Structure: JSON
Fields: name, marks (array)
Storage: Persistent JSON file
Calculations: Average from marks array, grade assignment
Sorting: Alphabetical by student name
```

#### Sample Workflow:
```
Add student → Enter 3 subject marks → Auto-calculate average → 
Assign grade → Store in JSON → View results
```

#### Code Highlights:
```python
# Dynamic average calculation
total = sum(marks)
average = total / len(marks)

# Grade assignment
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
# ...
```

---

## 🎓 Key Learnings

### Technical Skills Mastered:

**File Operations:**
- Reading and writing JSON files
- Working with CSV module
- File existence checking
- Directory creation and management

**Data Validation:**
- Input sanitization
- Type checking
- Required field validation
- Format validation (email, phone)
- Duplicate prevention

**Error Handling:**
- Try-except blocks
- FileNotFoundError handling
- JSONDecodeError handling
- ValueError handling
- User-friendly error messages

**Code Organization:**
- Function separation
- Single Responsibility Principle
- Clean code structure
- Consistent naming conventions
- Comment documentation

**Data Structures:**
- Lists of dictionaries
- Nested data structures
- Lambda functions for sorting
- List comprehensions

---

## 📊 Code Statistics

```
Total Projects:        4
Total Lines of Code:   ~600
Total Functions:       20+
File Formats Used:     JSON, CSV
Data Validations:      15+
Error Handlers:        10+
```

---

## 🔧 Technologies Used

- **Language:** Python 3.11+
- **Libraries:**
  - `os` - File system operations
  - `json` - JSON data handling
  - `csv` - CSV file operations
  - `datetime` - Timestamp generation
- **Concepts:**
  - File I/O
  - CRUD operations
  - Data persistence
  - Input validation
  - Error handling
  - Lambda functions

---

## 🚀 How to Run

### Prerequisites:
```bash
python --version  # Should be 3.8+
```

### Running Projects:

**Library Management:**
```bash
python BookLibarary_.py
```

**Contact Management:**
```bash
python "contact_Management_System.py"
```

**Expense Tracker:**
```bash
python Expense_tracker.py
```

**Grade Calculator:**
```bash
python gradeCalculatorAndStoreData.py
```

### Data Storage:
All projects create a `Data/` or `data/` folder automatically to store files.

---

## 💡 Project Highlights

### What Makes These Projects Different:

**1. Production-Ready Code:**
- Not just tutorials - actual usable systems
- Proper error handling
- Data validation
- User-friendly messages

**2. Real-World Applications:**
- Library Management → Schools, personal libraries
- Contact Management → Small businesses, freelancers
- Expense Tracker → Personal finance, small shops
- Grade Calculator → Teachers, coaching centers

**3. Code Quality:**
- Clean structure
- Proper comments
- Consistent formatting
- Modular functions

---

## 🎯 Challenges Faced & Solutions

### Challenge 1: File Persistence
**Problem:** Data lost when program closes  
**Solution:** Implemented JSON/CSV storage with save/load functions

### Challenge 2: Data Validation
**Problem:** Users entering invalid data  
**Solution:** Added comprehensive validation before saving

### Challenge 3: Duplicate Prevention
**Problem:** Same book ID or phone number added twice  
**Solution:** Loop-based duplicate checking before insert

### Challenge 4: Sorted Display
**Problem:** Contacts/students not in order  
**Solution:** Used `sorted()` with lambda for case-insensitive sorting

---

## 📝 Code Quality Improvements

**From Week 1 to Week 2:**

| Aspect | Week 1 | Week 2 |
|--------|--------|--------|
| **File Handling** | None | JSON + CSV |
| **Validation** | Basic | Comprehensive |
| **Error Handling** | Minimal | Extensive |
| **Code Structure** | Simple | Modular |
| **Data Persistence** | No | Yes |
| **User Experience** | Basic | Professional |

---

## 🔄 Future Enhancements

Potential improvements for these projects:

**Library Management:**
- [ ] Due date tracking
- [ ] Late fee calculation
- [ ] Multiple book copies
- [ ] Member database

**Contact Management:**
- [ ] Group/category support
- [ ] Birthday reminders
- [ ] Export to VCF
- [ ] Email integration

**Expense Tracker:**
- [ ] Monthly reports
- [ ] Category-wise breakdown
- [ ] Budget limits
- [ ] Visual graphs

**Grade Calculator:**
- [ ] Multiple semesters
- [ ] GPA calculation
- [ ] Report card generation
- [ ] Student comparison

---

## 🎓 Learnings Applied

### Design Patterns:
- **CRUD Pattern:** Create, Read, Update, Delete in all systems
- **Validation Pattern:** Check before save
- **Error Handling Pattern:** Try-except for user inputs

### Best Practices:
- Don't trust user input
- Always validate
- Provide helpful error messages
- Save frequently
- Check file existence
- Use meaningful variable names

---

## 📈 Progress Tracking

**Week 1:** Basic Python (Calculator, Games, File Organizer)  
**Week 2:** Data Management Systems (This week) ✅  
**Week 3:** APIs & Web Integration (Coming next)

**Skills Growth:**
- Week 1: Python basics
- Week 2: File operations, data structures, validation
- Cumulative projects: 11
- Lines of code written: 1100+

---

## 🙏 Acknowledgments

Built as part of my self-learning journey in Python development and AI/ML preparation.

All projects created independently using:
- Official Python documentation
- Best practices from industry standards
- Problem-solving and debugging skills

---

## 📞 Contact

**GitHub:** [@RitikChoudhary01](https://github.com/RitikChoudhary01)  
**LinkedIn:** [Your LinkedIn]  
**Email:** [Your Email]

---

## 📄 License

MIT License - Feel free to use these projects for learning purposes.

---

<div align="center">

**⭐ If you found this helpful, please star the repository!**

**Building in Public | One Week at a Time**

</div>

---

*Last Updated: February 20, 2026*  
*Week 2 Status: ✅ Complete*  
*Next Milestone: Week 3 - APIs & Web Integration*
