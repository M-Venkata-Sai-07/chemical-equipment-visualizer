# 📘 Chemical Equipment Parameter Visualizer

### 🌐 Hybrid Web + Desktop Application

### 🧪 FOSSEE Winter Internship 2025 – Screening Task

---

## 🚀 Overview

The **Chemical Equipment Parameter Visualizer** is a hybrid application designed to analyze, visualize, and manage datasets of chemical process equipment. It provides:

* A **Web UI (React.js + Chart.js)**
* A **Desktop UI (PyQt5 + Matplotlib)**
* A **REST API backend (Django + DRF)**
* Support for data uploads, summaries, charts, and PDF reports
* History storage of the last 5 datasets

This project demonstrates **full-stack development**, **data analytics**, **desktop UI development**, and **REST API design** — fulfilling all requirements for the FOSSEE Winter Internship screening task.

---

# 🎯 Features

### 📤 **CSV Upload**

Upload chemical equipment data containing:

* Equipment Name
* Equipment Type
* Flowrate
* Pressure
* Temperature

### 📊 **Summary Analytics**

The backend processes the CSV using **Pandas** to compute:

* Total number of equipment
* Average flowrate
* Average pressure
* Average temperature
* Type-wise equipment distribution

### 📈 **Charts (Web + Desktop)**

Both frontends visualize:

* Bar chart showing equipment distribution by type

Web uses **Chart.js**, Desktop uses **Matplotlib**.

### 🕒 **Upload History**

Backend stores the **last 5 uploaded datasets** in SQLite, enabling:

* Quick access to past summaries
* Fast re-visualization
* Repeat PDF downloads

### 📄 **Auto PDF Report Generation**

A single-click button generates a professional PDF containing:

* File name
* Summary statistics
* Type distribution table

Built using **ReportLab**.

### 💻 **Web + Desktop Frontend**

Both frontends talk to the **same backend API**, demonstrating:

* API reusability
* Multi-platform interface design
* Consistent UX

---

# 🧱 System Architecture

```
                   ┌──────────────────────────┐
                   │     React Web Frontend    │
                   │  (Upload, Chart, Summary) │
                   └─────────────▲─────────────┘
                                 │
                                 │ REST API Calls (Axios)
                                 │
               ┌─────────────────┴──────────────────┐
               │         Django REST Backend         │
               │  Upload → Analyze → Store → Report  │
               └─────────────▲─────────────┬────────┘
                                 │         │
                                 │         │
                                 │         │
                    ┌────────────┘   ┌─────┴──────────┐
                    │                     SQLite DB     │
                    │         (Stores last 5 datasets)  │
                    └───────────────────────────────────┘


                    ┌──────────────────────────────────┐
                    │  PyQt5 Desktop App (Matplotlib)  │
                    │      Upload, Summary, Charts     │
                    └──────────────────────────────────┘
```

---

# 📁 Folder Structure

```
chemical-equipment-visualizer_full/
│
├── backend/                 # Django REST API server
│   ├── api/                 # Upload, summary, history, PDF
│   ├── backend/             # Main config
│   ├── db.sqlite3
│   └── manage.py
│
├── web-frontend/            # React Web UI
│   ├── src/
│   │   ├── components/      # UploadForm, ChartView, Summary, History
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
│
├── desktop-frontend/        # PyQt5 Desktop App
│   ├── api_handler.py
│   ├── main.py
│   └── requirements.txt
│
├── datasets/                # Sample CSV files
├── reports/                 # Generated PDFs
├── screenshots/             # UI screenshots
└── README.md                # Project documentation
```

---

# 🔧 Tech Stack

### 🖥 Backend

* **Django**
* **Django REST Framework**
* **Pandas**
* **ReportLab**
* **SQLite**

### 🌐 Web Frontend

* **React.js**
* **Chart.js**
* **Axios**

### 🖥 Desktop Frontend

* **PyQt5**
* **Matplotlib**
* **Requests**

---

# ⚙️ Setup & Installation Guide

## 1️⃣ Backend Setup (Django)

```bash
cd backend
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Backend runs at:
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 2️⃣ Web Frontend Setup (React)

```bash
cd web-frontend
npm install
npm start
```

Runs at:
👉 [http://localhost:3000/](http://localhost:3000/)

---

## 3️⃣ Desktop Frontend Setup (PyQt5)

```bash
cd desktop-frontend
pip install -r requirements.txt
python main.py
```

---

# 📡 REST API Documentation

### 📤 **Upload CSV**

```
POST /api/upload/
```

Response:

```json
{
  "message": "File uploaded successfully",
  "summary": { ... }
}
```

### 📚 **Get History**

```
GET /api/history/
```

### 📄 **Get PDF Report**

```
GET /api/report/<id>/
```

---

# 🧪 Testing the System

### ✔ Upload CSV in Web

### ✔ Verify Chart displays

### ✔ Open Desktop App

### ✔ Load History

### ✔ Download PDF

### ✔ Check history (max 5 datasets)

All components should communicate flawlessly.

---

# 📦 Deployment (Optional)

You may deploy the backend using:

* Render
* Railway
* PythonAnywhere

And deploy web frontend using:

* Vercel
* Netlify

---

# 🧭 Future Improvements

* JWT authentication
* Role-based dashboards
* Comparison of multiple datasets
* Export charts as PNG
* Add filtering & sorting

---

# 🙌 Credits

This project was developed for:
**FOSSEE Winter Internship 2025 – Web/Software Development Screening Task**

Developer: **Venkata Sai Mallavarapu**
College: **RVR & JC College of Engineering**
Track: **Hybrid Web + Desktop Applications**

---

# 🎉 Conclusion

This project fully satisfies the requirements of the FOSSEE internship task by delivering:

✔ A unified, production-ready backend
✔ A modern web client
✔ A fully functional desktop application
✔ Data visualization + analytics
✔ PDF reporting
✔ Clean architecture + reusable API

---

If you want, I can now generate:
📌 **Demo video script**
📌 **GitHub release**
📌 **Architecture diagram image**
📌 **Final ZIP for submission**

Just tell me!
