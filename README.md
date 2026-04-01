# 🧠 AI Meeting Notes (Offline Version)

## 🚀 Overview

AI Meeting Notes is a full-stack web application that allows users to upload files (CSV/Text) and automatically generate:

* 📄 Summary
* ✅ Action Points
* 🧾 PDF Report

This version is built **without OpenAI API** (fully free & offline logic-based processing).

---

## 🏗️ Project Structure

```
ai-meeting-notes/
│
├── backend/
│   ├── main.py
│   ├── ai_utils.py
│   ├── models.py
│   ├── database.py
│   ├── uploads/
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
```

---

## ⚙️ Features

### ✅ Core Features

* File Upload (CSV / TXT)
* Automatic Data Processing
* Summary Generation (Rule-based)
* Action Points Extraction
* PDF Generation
* Data Storage (SQLite)
* API Documentation (Swagger UI)

---

### 🔥 Advanced Features

* FastAPI Backend
* REST API Endpoints
* Frontend-Backend Integration
* Error Handling (Invalid Data Skip)
* CORS Enabled

---

## 🧠 How It Works

1. User uploads a file from frontend
2. File is sent to backend via API
3. Backend reads file content
4. Data is processed using Python logic
5. Summary + Action Points generated
6. PDF is created
7. Data stored in database
8. Response sent back to frontend

---

## 🌐 API Endpoints

### 📤 Upload File

```
POST /upload/
```

### 📥 Get Meetings

```
GET /meetings/
```

---

## 🖥️ Running Locally

### Backend

```
cd backend
uvicorn main:app --reload
```

### Frontend

```
cd frontend
python -m http.server 5500
```

---

## ⚠️ Important Notes

* Upload only **proper CSV files**
* Invalid rows are skipped automatically
* No AI API required (completely free)

---

## 👨‍💻 Author

Developed by Deepanshu 🚀

---

## ⭐ Support

If you like this project:

* Star the repo ⭐
* Share with others 🔥
