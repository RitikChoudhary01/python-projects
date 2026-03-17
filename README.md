# Python Projects (Learning Journey)

A collection of beginner-to-intermediate Python projects I built while learning Python step-by-step.  
The repo is organized by weeks (fundamentals → file handling → APIs) and also includes a few AI projects powered by **Groq LLM API**.

> **Goal:** Learn by building small, complete projects and improve code quality each week.

---

## 📁 Repository Structure

- `week_1/` → Python fundamentals + small apps (CLI + GUI)
- `WEEK_2/` → File handling, persistence (JSON/CSV), CRUD mini-systems
- `week3/` → Working with APIs (weather/news) and basic web scraping
- `Ai_Projects/` → LLM-based tools (writer assistant, business bot, PDF Q&A bot)

---

## ✅ Week 1 — Python Fundamentals

**What I practiced**
- Variables, loops, functions
- Conditionals and control flow
- Basic error handling
- Simple CLI programs
- Tkinter GUI basics

**Projects**
1. **Simple Calculator (CLI)** — arithmetic operations using `match-case`
2. **GUI Calculator** — Tkinter-based calculator
3. **To-Do List (CLI)** — add/remove/mark tasks
4. **Predict Number Game** — random guessing game
5. **Quiz App** — multiple choice quiz scoring
6. **Rock Paper Scissors** — game against computer

> There is also a `week_1/README.md` in the folder with more details.

---

## ✅ Week 2 — File Handling & Data Management (JSON/CSV)

This week focuses on building “real systems” that save data even after the program closes.

### 1) Library Management System (`WEEK_2/BookLibrary`)
**Features**
- Add/remove books
- Issue/return books
- Search by book ID
- Uses JSON storage (`data/library.json`)

### 2) Contact Management System (`WEEK_2/contactManagent`)
**Features**
- Add/update/remove contacts
- Smart search
- Validation (phone digits, email format)
- Uses JSON storage (`Data/contact.json`)

### 3) Expense Tracker (`WEEK_2/Expense Tracker`)
**Features**
- Add expenses (date, category, amount, description)
- View expenses
- Calculate total expenses
- Uses CSV storage (`Data/ExpenseTrackerDATA.csv`)

### 4) Grade Calculator (`WEEK_2/GradeCalculator`)
**Features**
- Store student marks
- Calculate average and grade (A–F)
- View students sorted by name
- Uses JSON storage (`Data/grade.json`)

> Check `WEEK_2/README.md` for a detailed breakdown.

---

## ✅ Week 3 — APIs & Web Integration

### Weather App (`week3/weather`)
- Uses OpenWeatherMap API
- Displays temperature, humidity, wind speed, sunrise/sunset

### News App (`week3/news`)
- Uses NewsAPI to display top headlines

### Price Tracker / Web Scraping (`week3/price Tracker`)
- Uses `requests` + `BeautifulSoup`
- Extracts product title from a product page (experimental)

---

## 🤖 AI Projects (Groq API)

These projects use Groq’s chat completion API with system prompts.

### AI Writer Assistant (`Ai_Projects/ai_writer.py`)
- Generates blogs/articles/paragraphs
- Can rewrite, expand, summarize, improve grammar
- Streams output in terminal

### Business Customer Support Bot (`Ai_Projects/For Business ChatBot`)
- Acts as support for a sample electronics shop
- Responds using fixed business info and simple rules

### PDF Q&A Bot (`Ai_Projects/PDF RealtedQ&A BOT`)
- Reads PDF text using `pypdf`
- Answers questions using only the PDF context
- Can summarize sections and explain concepts

---

## ⚙️ Setup & Installation

### 1) Clone the repository
```bash
git clone https://github.com/RitikChoudhary01/python-projects.git
cd python-projects
```

### 2) (Recommended) Create a virtual environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3) Install dependencies
Some scripts require extra libraries:
```bash
pip install python-dotenv groq requests beautifulsoup4 pypdf
```

> Tkinter is usually included with Python on Windows/macOS, but on some Linux systems you may need to install it separately.

---

## 🔑 Environment Variables (For AI Projects)

Create a `.env` file in the root of the project:

```env
GROQ_API_KEY=your_api_key_here
```

Then run AI scripts from terminal, e.g.:
```bash
python Ai_Projects/ai_writer.py
```

---

## ▶️ How to Run

Example commands:

```bash
python "week_1/GUI Calculator.py"
python "WEEK_2/Expense Tracker"
python "week3/weather"
python "Ai_Projects/ai_writer.py"
```

> Some file names in this repo contain spaces. If you get an error running them, wrap the path in quotes (as shown above).

---

## 🧠 What I’m Learning From This Repo

- Writing clean, reusable functions
- Input validation and error handling
- Persistent storage using JSON and CSV
- Working with APIs (requests)
- Web scraping basics
- Prompt design and LLM integration

---

## 🗺️ Next Steps (Planned)

- Improve folder naming consistency (`week_2` vs `WEEK_2`)
- Add requirements file (`requirements.txt`)
- Add better CLI UX (argparse, menus)
- Add more AI + API projects (Week 4+)

---

## 📬 Contact

GitHub: **@RitikChoudhary01**

---

## 📄 License

MIT (or add your preferred license)
