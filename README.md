# 🐍 Python Projects

Welcome to my Python Projects repository! This is a structured learning journey through Python — from beginner CLI apps to GUI programs, data-persistence systems, API integrations, and AI-powered tools.

---

## 📁 Repository Structure

```
python-projects/
├── week_1/          # Beginner Python projects (CLI & GUI)
├── WEEK_2/          # Intermediate projects with data persistence
├── week3/           # API integration & web scraping projects
└── Ai_Projects/     # Advanced AI-powered applications
```

---

## 🗓️ Week 1 — Beginner Projects

> Focus: Core Python concepts — functions, loops, conditionals, basic I/O, and GUI basics.

### 1. 🖩 GUI Calculator
A fully functional desktop calculator built with a graphical user interface.

- **Features**: 4×4 button grid (digits 0–9, operators +, −, ×, ÷), clear button, real-time expression display, error handling for invalid operations.
- **Libraries**: `tkinter`
- **Path**: `week_1/GUI Calculator.py`

### 2. 🔢 Predict Number Game
A number-guessing game where the player tries to guess a random number between 1 and 100.

- **Features**: Random number generation, higher/lower hints after each guess, attempt counter.
- **Libraries**: `random`
- **Path**: `week_1/Predict number Game`

### 3. 📝 Quiz App
An interactive multiple-choice quiz in the terminal.

- **Features**: 3 questions with A/B/C/D options, score tracking, instant feedback on each answer, final score summary.
- **Libraries**: Built-in only
- **Path**: `week_1/Quiz app`

### 4. ✊ Rock Paper Scissors Game
Play the classic Rock-Paper-Scissors game against the computer.

- **Features**: Random computer choice, full win/loss/draw logic, replay option.
- **Libraries**: `random`
- **Path**: `week_1/Rcok Paper Scissor game`

### 5. ➕ Simple Calculator
A command-line calculator for basic arithmetic operations.

- **Features**: Supports +, −, ×, ÷, % operations, division-by-zero validation, uses Python 3.10+ `match-case`, continue/exit loop.
- **Libraries**: Built-in only
- **Path**: `week_1/Simple calculator`

### 6. 🗂️ File Organizer
Automatically organizes files in a directory by categorizing them into folders based on file type.

- **Features**: Detects file extensions, creates category folders, moves files to the correct folder.
- **Libraries**: `os`, `shutil`
- **Path**: `week_1/file Organizer`

### 7. ✅ To-Do List
A command-line task management application.

- **Features**: Add tasks, view all tasks with ✅/❌ status, mark tasks as complete, remove tasks, interactive menu.
- **Libraries**: Built-in only
- **Path**: `week_1/to-do-list`

---

## 🗓️ Week 2 — Intermediate Projects

> Focus: Data structures, JSON/CSV file persistence, and full CRUD operations.

### 1. 📚 Book Library Management System
A complete library management system with data persistence.

- **Features**: Add, view, search, and remove books; issue books to members and track who has them; return books; JSON-based storage; timestamps for records.
- **Libraries**: `json`, `os`, `datetime`
- **Data**: `WEEK_2/BookLibrary/data/library.json`
- **Path**: `WEEK_2/BookLibrary`

### 2. 💸 Expense Tracker
Track personal expenses with categories and descriptions.

- **Features**: Add expenses (date, category, amount, description), view all expenses, calculate total spending, ₹ currency display, CSV-based storage.
- **Libraries**: `csv`, `os`
- **Data**: `WEEK_2/Expense Tracker/Data/ExpenseTrackerDATA.csv`
- **Path**: `WEEK_2/Expense Tracker`

### 3. 🎓 Grade Calculator
Calculate and track student grades across subjects.

- **Features**: Add students with marks for 3 subjects, calculate average, assign letter grade (A–F), view all students sorted by name, JSON persistence.
- **Grade Scale**: A (90+), B (80+), C (70+), D (60+), F (<60)
- **Libraries**: `json`, `os`
- **Data**: `WEEK_2/GradeCalculator/Data/grade.json`
- **Path**: `WEEK_2/GradeCalculator`

### 4. 📇 Contact Management System
A full-featured contact manager with validation and search.

- **Features**: Add contacts (name, phone, email), view sorted contact list, search by name/phone/email, update or remove contacts, duplicate phone prevention, email format validation, JSON persistence.
- **Libraries**: `json`, `os`, `datetime`
- **Data**: `WEEK_2/contactManagent/Data/contact.json`
- **Path**: `WEEK_2/contactManagent`

---

## 🗓️ Week 3 — API Integration & Web Scraping

> Focus: HTTP requests, external REST APIs, and web scraping with BeautifulSoup.

### 1. 📰 News Fetcher
Fetch and display today's top news headlines for India.

- **Features**: Connects to NewsAPI, displays top 5 headlines, country-specific filtering, error handling.
- **Libraries**: `requests`
- **API**: [NewsAPI](https://newsapi.org/) — requires a free API key
- **Path**: `week3/news`

### 2. 💰 Price Tracker
Scrape product information and prices from e-commerce URLs.

- **Features**: Web scraping with BeautifulSoup, extracts product title, custom HTTP headers to avoid bot blocking.
- **Libraries**: `requests`, `beautifulsoup4`
- **Target**: Amazon product pages
- **Path**: `week3/price Tracker`

### 3. 🌤️ Weather App
Get real-time weather information for any city worldwide.

- **Features**: Temperature, humidity, wind speed (converted to km/h), weather description, sunrise/sunset times, formatted date and time display.
- **Libraries**: `requests`, `datetime`
- **API**: [OpenWeatherMap](https://openweathermap.org/) — requires a free API key
- **Path**: `week3/weather`

---

## 🤖 AI Projects — Advanced LLM-Powered Applications

> Focus: Groq API integration with LLaMA 3.3 70B for intelligent, context-aware applications.

> **Requirement**: All AI projects need a `GROQ_API_KEY` stored in a `.env` file.
> ```
> GROQ_API_KEY=your_api_key_here
> ```

### 1. 🛒 Business ChatBot
An AI-powered customer support chatbot for an electronics retail store.

- **Features**: Conversational AI with store-specific context (products, hours, delivery policy), streaming responses, professional and polite tone, escalates out-of-scope questions to staff.
- **Store Details**: Ritik's Electronics Store, Warangal | Hours: 10 AM – 9 PM | Free delivery within 10 km
- **Model**: `llama-3.3-70b-versatile` via Groq
- **Libraries**: `groq`, `python-dotenv`, `os`
- **Path**: `Ai_Projects/For Business ChatBot`

### 2. 📄 PDF Q&A Bot
Ask questions about any PDF document and get accurate answers from its content.

- **Features**: Extracts text from PDF files, answers questions based only on document content (no hallucination), generates summaries, explains technical concepts with examples, streaming responses.
- **Model**: `llama-3.3-70b-versatile` via Groq (temperature 0.1 for accuracy)
- **Libraries**: `groq`, `python-dotenv`, `pypdf`, `os`
- **Path**: `Ai_Projects/PDF RealtedQ&A BOT`

### 3. ✍️ AI Writer
An AI-powered writing assistant for content creation and improvement.

- **Features**: Write blog posts or articles, improve grammar and clarity, rewrite text in different tones (formal, casual, persuasive), expand short ideas into full content, summarize long text, interactive conversation mode.
- **Model**: `llama-3.3-70b-versatile` via Groq (temperature 0.8 for creativity)
- **Libraries**: `groq`, `python-dotenv`, `os`
- **Path**: `Ai_Projects/ai_writer.py`

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.10 or higher
- `pip` (Python package manager)

### Install Dependencies

```bash
# For Week 3 projects (API & web scraping)
pip install requests beautifulsoup4

# For AI Projects
pip install groq python-dotenv pypdf
```

### API Keys Setup (Week 3 & AI Projects)

1. **NewsAPI** (week3/news): Get a free key at [newsapi.org](https://newsapi.org/)
2. **OpenWeatherMap** (week3/weather): Get a free key at [openweathermap.org](https://openweathermap.org/)
3. **Groq** (Ai_Projects): Get a free key at [console.groq.com](https://console.groq.com/)

For AI Projects, create a `.env` file inside the `Ai_Projects` folder:
```
GROQ_API_KEY=your_groq_api_key_here
```

### Running a Project

```bash
# Example: run the To-Do List
python "week_1/to-do-list"

# Example: run the Weather App
python "week3/weather"

# Example: run the AI Writer
python "Ai_Projects/ai_writer.py"
```

---

## 📦 Dependency Summary

| Library | Project(s) | Purpose |
|---|---|---|
| `tkinter` | GUI Calculator | Desktop GUI framework |
| `random` | Number Game, Rock-Paper-Scissors | Random number generation |
| `json` | Book Library, Grade Calculator, Contact Manager | Data persistence |
| `csv` | Expense Tracker | CSV file handling |
| `os` / `shutil` | File Organizer, all file-based projects | File & directory operations |
| `datetime` | Book Library, Contact Manager, Weather | Date and time handling |
| `requests` | News, Price Tracker, Weather | HTTP requests |
| `beautifulsoup4` | Price Tracker | HTML parsing / web scraping |
| `groq` | All AI Projects | Groq LLM API client |
| `python-dotenv` | All AI Projects | `.env` environment variables |
| `pypdf` | PDF Q&A Bot | PDF text extraction |

---

## 🚀 Project Progression

| Week | Theme | Skills Learned |
|------|-------|----------------|
| Week 1 | Beginner | Loops, functions, conditionals, `tkinter` GUI |
| Week 2 | Intermediate | CRUD operations, JSON/CSV persistence, input validation |
| Week 3 | API Integration | `requests`, REST APIs, web scraping with BeautifulSoup |
| AI Projects | Advanced AI | Groq LLM API, streaming, PDF parsing, prompt engineering |

---

## 📄 License

This project is licensed under the terms of the [LICENSE](./LICENSE) file.

---

> Feel free to explore, learn, and reach out for any questions! ⭐ Star the repo if you find it useful.