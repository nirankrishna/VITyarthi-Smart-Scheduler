Project Title  
Smart Study Scheduler & Reminder

Problem Definition

Let’s face it—juggling a bunch of classes, assignments, and deadlines can get overwhelming fast. You end up stressed, scrambling to keep track, and sometimes things just slip through the cracks. This project steps in to help. The idea is simple: give students a straightforward tool to keep their tasks organized and stay on top of what matters.

Objectives & Expected Outcomes

1. Build a Task class using object-oriented programming to manage tasks.
2. Make sure tasks don’t disappear by saving and loading them as CSV files.
3. Sort tasks so the most urgent and important ones show up first. We’ll use both priority (HIGH, MEDIUM, LOW) and due date to decide what needs attention.
4. When it’s done, you’ll have a command-line app where you can add, manage, and track all your assignments and deadlines.

Concepts and Techniques Applied

- Object-Oriented Programming: Everything centers around the Task class, with details like name, due date, and priority, plus handy methods for string conversion and CSV formatting.
- Data Structures: All your tasks live in a simple Python list.
- File I/O: The app uses Python’s csv module to save and load your work, so nothing gets lost.
- Algorithms: There’s a custom sort in place—first by date, then by priority—so you always know what’s next.
- Date/Time Handling: The datetime module keeps all your due dates accurate and easy to work with.

How to Run the Project

1. Clone the Repository:
   git clone https://github.com/nirankrishna/VITyarthi-Smart-Scheduler

   cd Smart-Scheduler-Project

2. Run the Script:
   python scheduler.py

   