# FitMetrix 🏋️‍♂️ – All-in-One Fitness Tracker (Python)

FitMetrix is a comprehensive fitness tracking application designed to help users manage and monitor their health journey. With secure authentication, personalized workout and diet plans, and visual progress tracking, FitMetrix offers a powerful, user-friendly solution to support fitness goals.

---

## 🚀 Features

- **Secure User Authentication**  
  - Register/Login system with MySQL backend for secure user account management.

- **Personalized Diet & Workout Plans**  
  - Interactive menus to search for diet and workout routines based on personal metrics:
    - Weight, height, age, activity level, and dietary preference.
  - Save and manage plans under your profile (revisit or delete at any time).

- **Progress Tracking**  
  - Includes two health calculators:
    - **Body Fat Percentage Calculator**
    - **BMI (Body Mass Index) Calculator**
  - Visualize progress with clear, interactive bar charts using **matplotlib**.

- **Database Architecture**  
  - Fully normalized relational database built in **SQLite3**.
  - Uses cross-table parameterized queries and aggregate functions for efficient data operations.

- **Graphical User Interface**  
  - Built using **Tkinter** for an intuitive and responsive GUI.
  - Modular design using **Object-Oriented Programming** principles such as:
    - Composition
    - Inheritance

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python     | Core language |
| MySQL      | User authentication and account storage |
| SQLite3    | Diet/workout plans and progress data |
| Tkinter    | GUI framework |
| matplotlib | Data visualization |

---

## 📸 Screenshots

*(Insert screenshots here if available, such as UI navigation, plan selection, and progress graphs)*

---

## 📁 Project Structure

```bash
FitMetrix/
│
├── auth/                  # User registration and login modules
├── gui/                   # GUI components built with Tkinter
├── plans/                 # Diet and workout plan logic
├── progress/              # Calculators and progress visualizations
├── database/              # SQLite3 schema and queries
├── assets/                # Static files (if any)
├── main.py                # Entry point of the application
└── README.md              # This file
