# 📚 RAG Chatbot — Atomic Habits

A simple **Retrieval-Augmented Generation (RAG)** chatbot built using **Groq LLM + LangChain + ChromaDB + HuggingFace embeddings**.
This chatbot reads a PDF (*Atomic Habits*) and answers questions **only from the document context**.

---

## 🚀 Features

* 📄 Load and process PDF documents
* 🧠 Convert text into embeddings using HuggingFace
* 🗂 Store embeddings in Chroma vector database
* 🔍 Retrieve relevant chunks using similarity search
* 🤖 Generate answers using Groq LLM (LLaMA 3.3)
* 💾 Persistent vector storage (no need to rebuild every time)

---

## 🛠️ Tech Stack

* Python
* LangChain
* ChromaDB
* HuggingFace Embeddings (`all-MiniLM-L6-v2`)
* Groq API (LLaMA 3.3 model)

---

## 📂 Project Structure

```
project/
│── docs/
│   └── atomicHabits.pdf
│
│── vector_hf_v2/        # Auto-generated vector DB
│
│── main.py              # Your script
│── .env                 # API key file
│── README.md
```

---

## 🔑 Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd <your-project>
```

---

### 2️⃣ Create Virtual Environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install langchain langchain-community langchain-huggingface \
chromadb groq python-dotenv pypdf
```

---

### 4️⃣ Add Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

### 5️⃣ Add PDF

Place your PDF inside:

```
./docs/atomicHabits.pdf
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 💡 How It Works

1. 📄 PDF is loaded using `PyPDFLoader`
2. ✂️ Text is split into chunks
3. 🧠 Each chunk is converted into embeddings
4. 💾 Stored in Chroma vector database
5. 🔍 User query → similarity search → relevant chunks
6. 🤖 LLM generates answer based only on retrieved context

---

## 🧪 Example

```
👉 You: What is habit stacking?

🤖 AI: Habit stacking is a method where you attach a new habit to an existing one...
```

---

## ⚡ Smart Optimization

* If vector DB exists → loads instantly ⚡
* If not → builds automatically 🏗️

---

## ⚠️ Notes

* Answers are **strictly based on PDF content**
* If context is missing → model may return incomplete answer
* First run may take time (embedding creation)

---

## 🔮 Future Improvements

* Add Streamlit UI 🌐
* Support multiple PDFs 📚
* Add chat history memory 🧠
* Deploy as web app 🚀

---

## 👨‍💻 Author

Built by RITIK_CHOUDARY01_CHOUDARY — on a journey to master AI, coding, and build powerful systems.

---

## ⭐ Tip

Consistency > Motivation
Keep building daily 🚀
