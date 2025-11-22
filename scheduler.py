import csv
from datetime import datetime
from operator import attrgetter

# --- 1. Task Class (Object-Oriented Programming) ---
class Task:
    """Represents a single task with attributes and methods."""
    def __init__(self, name, subject, due_date_str, priority, is_completed=False):
        self.name = name
        self.subject = subject
        self.priority = priority.upper()  # Ensure consistency: HIGH, MEDIUM, LOW
        self.is_completed = is_completed
        try:
            # Store date as a datetime object for easy sorting and comparison
            self.due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
            self.due_date_str = due_date_str
        except ValueError:
            print("Error: Invalid date format. Please use YYYY-MM-DD.")
            raise

    def __str__(self):
        """String representation for viewing tasks."""
        status = "✅ COMPLETE" if self.is_completed else "❌ PENDING"
        return f"[{status}] {self.name} (Subject: {self.subject}) | Due: {self.due_date_str} | Priority: {self.priority}"

    def to_csv_row(self):
        """Returns a list of task attributes for saving to CSV."""
        return [
            self.name,
            self.subject,
            self.due_date_str,
            self.priority,
            'True' if self.is_completed else 'False'
        ]

# --- 2. Data Management (File I/O) ---
TASK_FILE = 'tasks.csv'

def load_tasks():
    """Loads tasks from the CSV file into a list of Task objects."""
    tasks = []
    try:
        with open(TASK_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 5:
                    name, subject, date_str, priority, completed_str = row
                    is_completed = completed_str.lower() == 'true'
                    try:
                        tasks.append(Task(name, subject, date_str, priority, is_completed))
                    except ValueError:
                        # Skip task with bad date format
                        print(f"Skipping task due to bad date format: {name}")
    except FileNotFoundError:
        print("Task file not found. Starting with an empty task list.")
    return tasks

def save_tasks(tasks):
    """Saves the current list of Task objects to the CSV file."""
    with open(TASK_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        for task in tasks:
            writer.writerow(task.to_csv_row())
    print("\nTasks saved successfully.")

# --- 3. Core Logic (Algorithm Development) ---
def add_task(tasks):
    """Prompts the user for task details and adds a new Task object."""
    print("\n--- Add New Task ---")
    name = input("Task Name: ")
    subject = input("Subject: ")
    # Basic date validation
    while True:
        due_date_str = input("Due Date (YYYY-MM-DD): ")
        try:
            datetime.strptime(due_date_str, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    
    # Basic priority validation
    while True:
        priority = input("Priority (HIGH, MEDIUM, LOW): ").upper()
        if priority in ['HIGH', 'MEDIUM', 'LOW']:
            break
        print("Invalid priority. Choose HIGH, MEDIUM, or LOW.")

    try:
        new_task = Task(name, subject, due_date_str, priority)
        tasks.append(new_task)
        print(f"Task '{name}' added.")
    except Exception as e:
        print(f"Could not add task: {e}")

def view_tasks(tasks):
    """Displays all pending tasks, sorted by due date and then by priority."""
    pending_tasks = [t for t in tasks if not t.is_completed]
    
    if not pending_tasks:
        print("\n🎉 No pending tasks! Time for a break. 🎉")
        return

    # Sort tasks: 1. By Priority (Custom Order), 2. By Due Date
    priority_order = {'HIGH': 0, 'MEDIUM': 1, 'LOW': 2}
    
    # Python's list.sort() is stable, so we sort by the secondary key first
    # Sort by Due Date (Ascending)
    pending_tasks.sort(key=attrgetter('due_date')) 
    # Sort by Priority (Custom Order)
    pending_tasks.sort(key=lambda task: priority_order[task.priority])
    
    print("\n--- PENDING TASKS (Sorted by Priority & Date) ---")
    for i, task in enumerate(pending_tasks):
        print(f"{i+1}. {task}")
    print(f"\nTotal Pending: {len(pending_tasks)}")

def mark_complete(tasks):
    """Allows user to select a task and mark it as completed."""
    pending_tasks = [t for t in tasks if not t.is_completed]
    if not pending_tasks:
        print("\nNo pending tasks to complete.")
        return

    print("\n--- Mark Task as Complete ---")
    for i, task in enumerate(pending_tasks):
        print(f"{i+1}. {task.name} (Due: {task.due_date_str})")

    while True:
        try:
            choice = int(input("Enter the number of the task to complete (0 to cancel): "))
            if choice == 0:
                return
            if 1 <= choice <= len(pending_tasks):
                # Find the corresponding object in the main tasks list and update it
                task_to_complete = pending_tasks[choice - 1]
                
                # We need to find the *original* task object reference in the 'tasks' list
                # to ensure the save_tasks function works correctly on the whole list.
                for task in tasks:
                    if task is task_to_complete: # Check if they are the same object instance
                        task.is_completed = True
                        print(f"\nTask '{task.name}' marked as complete! Well done.")
                        save_tasks(tasks)
                        return
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# --- 4. Main Program / User Interface ---
def display_menu():
    """Displays the main menu options."""
    print("\n\n=== Smart Study Scheduler ===")
    print("1. Add New Task")
    print("2. View Pending Tasks (Sorted)")
    print("3. Mark Task as Complete")
    print("4. Save & Exit")
    print("5. View All Tasks (Including Completed)")

def main():
    """Main function to run the application."""
    tasks = load_tasks() # Load existing tasks at startup

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_complete(tasks)
        elif choice == '5':
            print("\n--- ALL TASKS ---")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
            if not tasks:
                 print("No tasks recorded yet.")
        elif choice == '4':
            save_tasks(tasks)
            print("Exiting Scheduler. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
