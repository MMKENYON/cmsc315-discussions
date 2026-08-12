"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class HouseholdTask:
    category = "household"

    def __init__(self, task_name, due_date):
        # a task should have a name so blank tasks are not saved
        if not task_name.strip():
            raise ValueError("task name cannot be empty")

        self.task_name = task_name
        self.due_date = due_date
        self.steps = []

    def add_step(self, step_name):
        if not step_name.strip():
            raise ValueError("step name cannot be empty")
        self.steps.append({"step": step_name, "done": False})

    def display_info(self):
        return (
            f"task: {self.task_name}, due: {self.due_date}, "
            f"category: {self.category}, steps: {self.steps}"
        )


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class SchoolTask(HouseholdTask):
    task_type = "school"

    def __init__(self, task_name, due_date, course_name, priority):
        super().__init__(task_name, due_date)
        self.course_name = course_name
        self.priority = priority

    def change_priority(self, new_priority):
        allowed_priorities = ["low", "medium", "high"]
        if new_priority.lower() not in allowed_priorities:
            raise ValueError("priority must be low medium or high")
        self.priority = new_priority.lower()

    def display_info(self):
        # this overrides the parent method and adds the school details
        return (
            f"task: {self.task_name}, due: {self.due_date}, "
            f"course: {self.course_name}, priority: {self.priority}, "
            f"type: {self.task_type}, steps: {self.steps}"
        )


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== namespace demonstration ===")

    first_task = SchoolTask("read chapter", "friday", "cmsc 315", "medium")
    second_task = SchoolTask("finish discussion", "sunday", "cmsc 315", "high")

    print("class variable through the class:", SchoolTask.task_type)
    print("class variable through an object:", first_task.task_type)

    # this reminder only belongs to first_task
    first_task.reminder = "review notes before starting"

    print("first object namespace:", first_task.__dict__)
    print("second object namespace:", second_task.__dict__)
    print("school task class namespace keys:", list(SchoolTask.__dict__.keys()))


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== copy demonstration ===")

    original = HouseholdTask("prepare for class", "monday")
    original.add_step("read the learning resources")

    shallow_copy = copy(original)
    deep_copy = deepcopy(original)

    # the shallow copy shares the nested steps list
    # the deep copy gets its own nested steps list
    original.steps[0]["done"] = True
    original.add_step("check the assignment instructions")

    print("original steps:", original.steps)
    print("shallow copy steps:", shallow_copy.steps)
    print("deep copy steps:", deep_copy.steps)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== unit 1 oop assignment ===")

    print("\n=== parent object ===")
    grocery_task = HouseholdTask("make grocery list", "saturday")
    grocery_task.add_step("check the pantry")
    print(grocery_task.display_info())

    print("\n=== child object and inheritance ===")
    discussion_task = SchoolTask(
        "complete unit 1 discussion", "sunday", "cmsc 315", "medium"
    )
    # add_step is inherited from HouseholdTask
    discussion_task.add_step("read the textbook section")
    discussion_task.add_step("test the python program")
    discussion_task.change_priority("high")
    print(discussion_task.display_info())

    print("\n=== edge case test ===")
    try:
        HouseholdTask("", "friday")
    except ValueError as error:
        print("the blank task was not created:", error)

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
