# 017-followers

Day 17 of the Udemy *100 Days of Code* course: a small example of how to define and use a Python class.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

This is a demonstration only. It has no tests and no dependencies.

### What it shows

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

### Layout

| Path | Purpose |
| --- | --- |
| `src/main.py` | The `User` class and the demo that uses it |

## 📋 Requirements

Python 3. There are no dependencies.

## 🛠️ Setup

No installation is needed: the program uses only the Python standard library. Clone the repository and run the program from its root.

## ▶️ Run

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

## 🧪 Tests

The project has no automated tests. Check that the program compiles:

```bash
python -m py_compile src/main.py
```

## 📄 License

This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0). See [LICENSE][license].

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

The documents a newcomer needs, in reading order.

| Document | What it tells you |
| --- | --- |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Traceability matrix][TM-001] | How the artifacts link and when each was last reviewed |

---

[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/017-followers
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/017-followers/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/017-followers/issues
[license]: ./LICENSE
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[TM-001]: ./docs/sqa/traceability-matrix.md
