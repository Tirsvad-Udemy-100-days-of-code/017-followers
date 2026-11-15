**English** · [Dansk](Home-da) · [Bahasa Melayu](Home-ms)

# Followers

A small example of how to define and use a Python class.

## What is it?

Day 17 of the Udemy course *100 Days of Code: The Complete Python Pro Bootcamp*. The `User` class in `src/main.py` shows how a class is defined and used. It is a demonstration only: it has no tests and no dependencies.

## What the exercise teaches

- Defining a class with a constructor (`__init__`) that sets attributes with default values
- Instance attributes: `id`, `username`, `followers` and `following`
- Writing a method (`follow`) that changes the state of two objects at once

## What it does

- Creates two users and lets the first follow the second
- When `user_1.follow(user_2)` runs, `user_1.following` and `user_2.followers` each go up by one
- Prints the four counters, so the expected output is 0, 1, 1 and 0

## Next

- [Getting Started](Getting-Started)
- [Project Documents](Project-Documents)
