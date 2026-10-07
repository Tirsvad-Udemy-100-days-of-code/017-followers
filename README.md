# 017-followers

Day 17 of the Udemy *100 Days of Code* course: a small example of how to
define and use a Python class.

This is a demonstration only. It has no plan, no tests and no dependencies.

## What it shows

The `User` class in [src/main.py](src/main.py) demonstrates:

- a constructor (`__init__`) that sets attributes with default values
- instance attributes (`id`, `username`, `followers`, `following`)
- a method (`follow`) that changes the state of two objects at once

```python
class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1
```

When `user_1.follow(user_2)` runs, `user_1.following` goes up by one and
`user_2.followers` goes up by one.

## Run it

```bash
python src/main.py
```

Expected output:

```text
0
1
1
0
```

The four lines are `user_1.followers`, `user_1.following`,
`user_2.followers` and `user_2.following`.

## Layout

| Path | Purpose |
| --- | --- |
| `src/main.py` | The `User` class and the demo that uses it |
