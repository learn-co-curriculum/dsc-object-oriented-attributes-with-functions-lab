
# Object Oriented Attributes With Functions - Lab

## Introduction

In the last lesson, you saw what a **domain model** is and how it ties into object-oriented programming. In this lab, you'll be using a school as a domain model.

## Objectives

You will be able to:

* Create a domain model using OOP
* Create instance methods that operate on instance attributes


## Creating a Simple School Class

To start, open up the **school.py** file in your text editor of choice such as Atom, Sublime, or a simple notepad program. Within this file, create a `School()` class definition that will be initialized with the name of the school.

> **Note:** the next cell imports an extension, `autoreload`, from IPython. The autoreload extension reloads any imported packages when methods from that package are called. While this is inefficient for stable packages such as NumPy which will be static while working in a notebook, the `autoreload` extension is quite useful when developing a package yourself. That is, you can update a package such as **school.py** and then test the effects in a notebook; with the `autoreload` extension, you'll see the effects of your changes to the package reflected. 

>> If you still have trouble with cells reflecting updates to the **school.py** file as you go along, go to the *Kernel* tab at the top of the Jupyter notebook and click *Restart & Run All*. This should smoothly run everything up to where you're working.


```python
%load_ext autoreload
%autoreload 2
```


```python
from school import School
```


```python
school = School("Middletown High School")
```

## Updating the __init__ method

Great! Now, update your `School()` definition in **school.py** to also include a `roster` attribute upon initialization. Initialize the `roster` attribute as an empty dictionary. Later, you'll use this empty roster dictionary to list students of each grade. For example, a future entry in the roster dictionary could be `{"9": ["John Smith", "Jane Donahue"]}`).


```python
# You must reinstantiate the object since you've modified the class definition!
school = School("Middletown High School") 
school.roster # {}
```




    {}



## Adding Methods

### Method 1: `add_student()` 

Now add a method `.add_student()` which takes two arguments: a student's full name and their grade level, and updates the roster dictionary accordingly. 


```python
# Again, you must reinstantiate since you've modified the class!
school = School("Middletown High School") 
school.add_student("Peter Piper", 12)
school.roster # {"12": ["Peter Piper"]}
```




    {12: ['Peter Piper']}



> **Hint:** If you're stuck, don't fret; this one's a little tricky. You need to consider two scenarios.
    1. There is no entry for this grade yet in the roster dictionary:
        - Add an entry to roster dictionary with the grade key and a single item list using the name
    2. There is an entry for this grade in the roster dictionary:
        - Append the current name to the list associated with that grade
        
>> Going further: if you're really ambitious, you can actually combine both of these conditions into a single line using the `.get()` method with dictionaries. Here's the docstring for the `.get()` method:  
get(key[, default])  
    Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None, so that this method never raises a KeyError.


To make sure your method works for both scenarios, run the cell below: 


```python
school.add_student("Kelly Slater", 9)
school.add_student("Tony Hawk", 10)
school.add_student("Ryan Sheckler", 10)
school.add_student("Bethany Hamilton", 11)
school.roster # {9: ["Kelly Slater"], 10: ["Tony Hawk", "Ryan Sheckler"], 11: ["Bethany Hamilton"], 12: ["Peter Piper"]}
```




    {12: ['Peter Piper'],
     9: ['Kelly Slater'],
     10: ['Tony Hawk', 'Ryan Sheckler'],
     11: ['Bethany Hamilton']}



### Method 2: `grade()`
Next, define a method called `.grade()`, which should take in an argument of a grade and return a list of all the students in that grade. 


```python
# While annoying, you do need to reinstantiate the updated class and reform the previous methods
school = School("Middletown High School") 
school.add_student("Peter Piper", 12)
school.add_student("Kelly Slater", 9)
school.add_student("Tony Hawk", 10)
school.add_student("Ryan Sheckler", 10)
school.add_student("Bethany Hamilton", 11)
# Testing out your new method:
print(school.grade(10)) # ["Tony Hawk", "Ryan Sheckler"]
print(school.grade(12)) # ["Peter Piper"]
```

    ['Tony Hawk', 'Ryan Sheckler']
    ['Peter Piper']


### Method 3: `sort_roster()` 

Define a method called `.sort_roster()` that returns the school's roster where the strings in the student arrays are sorted alphabetically. For instance:
`{9: ["Kelly Slater"], 10: ["Ryan Sheckler", "Tony Hawk"], 11: ["Bethany Hamilton"], 12: ["Peter Piper"]}}`

>**Note:** since dictionaries are unordered, the order of the keys does not matter here, just the order of the student's names within each list.


```python
school.sort_roster()
```




    {12: ['Peter Piper'],
     9: ['Kelly Slater'],
     10: ['Ryan Sheckler', 'Tony Hawk'],
     11: ['Bethany Hamilton']}



## Summary
In this lab, you continued to pracitce OOP, designing a more complex domain model using a `School()` class with a few instance methods and variables. Soon you'll see that domain models can use other classes, instance methods, and instance variables to create more functionality in your programs.
