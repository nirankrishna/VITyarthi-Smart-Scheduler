
# Project Title
# Smart Study Scheduler & Reminder

## 📝 Problem Definition

Students often face challenges managing multiple tasks, subjects, and varying deadlines. This leads to stress, poor prioritization, and potential failure to meet submission dates. This project aims to solve this by providing a simple, structured tool for task management.

## 🎯 Objectives & Expected Outcomes

1.  **Objective:** Implement an OOP-based data model for tasks (Task class).
2.  **Objective:** Provide persistence by saving and loading task data using File I/O (CSV format).
3.  **Objective:** Develop a robust sorting algorithm that prioritizes tasks by **Priority** (HIGH, MEDIUM, LOW) and **Due Date**.
4.  **Outcome:** A functional command-line application that allows users to manage, prioritize, and track the completion of their academic tasks.

## 🛠️ Concepts and Techniques Applied

* **Object-Oriented Programming (OOP):** Using the `Task` class to encapsulate data (name, date, priority) and behavior (`__str__`, `to_csv_row`).
* **Data Structures:** Using a Python `list` to hold all `Task` objects.
* **File I/O:** Reading and writing data using Python's built-in `csv` module for persistent storage.
* **Algorithm Development:** Implementing a custom **stable sort** to first sort by date, and then sort by a custom priority order.
* **Date/Time Handling:** Using the `datetime` module for date validation and comparison.

## ▶️ How to Run the Project

1.  **Clone the Repository:**
    ```bash
    git clone [YOUR-GITHUB-REPO-URL]
    cd Smart-Scheduler-Project
    ```
2.  **Run the Script:**
    ```bash
    python scheduler.py
    ```

## 🖼️ Screenshots

Screenshots of the application's interface can be found in the `/screenshots` directory.