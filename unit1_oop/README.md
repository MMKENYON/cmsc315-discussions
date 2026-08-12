# unit 1 discussion: python oop namespaces and copying

## overview

i made a small household and school task program to practice object oriented programming

## completed requirements

- todo 1  i created the `HouseholdTask` parent class with a class variable and instance variables for the task name due date and steps

- todo 2  i created the `SchoolTask` child class which inherited from `HouseholdTask` and added the course name and priority

- todo 3  i made two school task objects and showed the class and instance namespaces with `__dict__`

- todo 4  i made shallow and deep copies of a task and changed its nested steps list to show the difference

- todo 5  i created and tested parent and child objects inside `main()`

- todo 6  i added `add_step()` and `change_priority()` as my own methods

## design approach

i used `HouseholdTask` for information that every task needed and used `SchoolTask` for the extra information that only a school task needed  the child class reused the parent class and changed `display_info()` so it also showed the course and priority

## edge case

i tested a task with a blank name and the program caught the `ValueError` instead of making the task

## real world use

the example represented a basic family calendar because the school task reused the things that every household task already had

## how to run

i ran the program from the main project folder with this command

```text
python3 unit1_oop/unit1_discussion.py
```

## discussion board reflection

from this assignment i learned that a class is like a blueprint and an object is one thing made from it  inheritance let my school task use things from the household task without me writing the same code again  the part i had the most trouble with was understanding class variables and instance variables  printing `__dict__` helped because i could actually see which information belonged to each object

the shallow and deep copy part was also new to me  at first i thought both copies would be separate  when i changed the nested steps list the shallow copy changed too but the deep copy did not  seeing the output made that difference a lot easier to understand

procedural programing feels like following functions one after another while oop keeps the information and actions together inside classes  i think that can make a program easier to read and update  reusing the parent class also means less repeated code and less work if something changes later  my example is small but i could see the same idea being used in a family calendar or school planner  i am still new to this but the ideas make more sense now
