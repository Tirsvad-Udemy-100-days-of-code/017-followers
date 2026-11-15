# Business Case: Followers

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial version; accepted with the Go verdict of the review record (autonomous, not independent) | [a86c2ef] |

---

## Executive Summary

Followers is a small demonstration of how to define and use a Python class: a `User` class with follower and following counters and a `follow` method. It is day 17 of the Udemy course *100 Days of Code: The Complete Python Pro Bootcamp* and is kept in a repository of its own so that the learner's progress is visible and each exercise can be reused. The program already works. What is missing is a written purpose, scope, owner and plan, a wiki that a visitor can read in English, Danish and Malay, and the common project baseline of the SQA and QC framework that the other projects of the portfolio follow. This Business Case justifies one short baseline project that adds those documents and metadata. It changes no behaviour of the program. The recommendation is to proceed.

## Methodological and Standards Foundation

The project follows the SQA (software quality assurance) and QC (quality control) framework mounted at `framework/`: artifact templates, QC checklists and the review process. Every QC criterion is tagged with an ISO/IEC 25010:2023 quality characteristic, and each review record gives evidence per criterion. Use cases and design artifacts follow Larman's *Applying UML and Patterns*; this baseline needs none, because it adds no behaviour. The Product Owner's language is English and the domain is education.

## Problem Statement

- The repository holds a working exercise, but nothing states why it exists, what is in and out of scope, who owns it or how its quality is judged.
- A visitor who does not read English finds only English text.
- The repository does not yet follow the common project baseline (framework submodule, `.gitmodules`, `.env.example`, `.editorconfig`, registry), so it differs from the projects that already follow it.
- The licence is stated only in the `LICENSE` file; the README and the wiki do not name it (the project has no `pyproject.toml`).

## Business Opportunity

A documented, framework-aligned repository makes the exercise easy to understand, review and reuse, shows the learner's progress as a portfolio, and lets the same checks run on every project of the course. Wiki pages in three languages make the exercise readable to a wider audience of learners.

## Objectives

- **O1.** Keep Followers working: the exercise file compiles and starts from the documented command (the project has no automated tests).
- **O2.** Record the purpose, scope, stakeholders and plan of the project in a Business Case, a Stakeholder Analysis, a Project Plan and one milestone, each reviewed and accepted.
- **O3.** Publish a wiki in English, Danish and Malay that explains what the exercise is, how to run it and where its documents are.
- **O4.** State the licence clearly in the README and the wiki, next to the `LICENSE` file, and adopt the current framework release.

## Scope

### In Scope

- Adopting the framework release in use across the portfolio (submodule, installed skills, hooks, `.gitmodules`, `.env.example`, `.editorconfig`).
- The baseline documents: Business Case, Stakeholder Analysis, Project Plan, one milestone, the traceability matrix and their review records.
- The wiki in English, Danish and Malay (`docs/wiki/`).
- The README, restored to the framework's README template.
- A licence statement in the README and the wiki.

### Out of Scope

- Any change to the behaviour of the program or to the layout of `src/`.
- A review of the existing source code against the Python QC checklist, and adding automated tests (kept as an open issue of the Project Plan).
- Translating text that the program prints while it runs.
- Use cases, design artifacts and a domain dictionary.

## Expected Benefits

### Tangible Benefits

- One accepted Business Case, Stakeholder Analysis, Project Plan and milestone, with a review record for each.
- A wiki of three pages in each of three languages.
- A README that has every section of the framework template.
- A licence statement in the README and the wiki that names the licence of the `LICENSE` file.

### Intangible Benefits

- A visitor understands the purpose and scope within minutes.
- The learner can show the exercise in a portfolio that looks the same for every project.
- Reviewing the project later is easier because every decision has a document.

## Strategic Alignment

The repository is the learner's portfolio of the 100 days of the course. The strategic goal is a portfolio in which every project is understandable, tested, licensed and documented in the same way. This project brings Followers to that level.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | The exercise file compiles (O1) | 0 errors | `python -m py_compile src/main.py` exits with code 0 |
| 2 | The baseline documents are accepted (O2) | 4 of 4 documents `Accepted` with a `Go` review | Version History status and `RC-*` verdict of BC-001, SA-001, PP-001 and MIL-001 |
| 3 | The wiki exists in three languages (O3) | 3 languages with the same 3 pages, plus the sidebar | Files in `docs/wiki/` and the `QC-WIKI-001` review |
| 4 | The README follows the template (O2) | 0 findings | `framework/scripts/check-readme.sh` exits with code 0 |
| 5 | The licence is stated (O4) | The README License section names the licence and links `LICENSE` | `README.md` and `LICENSE` |
| 6 | The change is merged with a green build (O1, O2) | 100 % of the CI (continuous integration) checks on the pull request pass | Status of the pull request on the git host |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The documents drift from the code as the exercise changes | Readers get wrong information | The scope states that the program does not change; a later change reopens the documents (a new Version History row and a review) |
| The reviewer is also the author, so the review is not independent | A defect is missed | Every review record says `Mode: autonomous, not independent`, and the end-of-run summary lists it for challenge |
| A translation is wrong or unclear | Danish or Malay readers are misled | English is the authoritative text; the translations follow it page by page and are open to correction by a native reader |
| The wiki publication fails after the merge | The wiki is empty | The publication is checked on the host after the merge, and a failure is reported |

## Assumptions

- The Product Owner is the learner, who also reviews and merges (S01, S02).
- The course exercise is complete; no further course step is planned for this project.
- The git host's scoped workflow publishes `docs/wiki/` to the repository wiki after a merge.
- The people the exercise is for cannot be asked for interviews; their concerns are inferred from the course.

## Constraints

- The baseline is finished within one week, by 2026-11-22.
- Metadata keys, headings, IDs and statuses stay in English; the content is English (the Product Owner's language).
- The framework is private, so project documents do not link to its files in the README appendix.
- The repository is public, so the AI prompt log is ignored by git.

## Cost–Benefit Assessment

A qualitative assessment is justified: the project is unpaid, has one person, and its benefits (clarity, portfolio value, reuse) have no market price.

| Costs | Benefits |
| --- | --- |
| About one day of the author's and the AI assistant's time | Reviewed documents that explain the project |
| Reviewer time to read the end-of-run summary | A wiki in three languages |
| Upkeep of the documents when the exercise changes | A portfolio entry that matches the other projects |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Owns the project and wants a documented, working portfolio entry |
| S02 | Reviews every document and merges the pull request |
| S03 | Wants to understand and run the exercise in their own language |
| S04 | Sets the exercise whose faithful solution the project shows |

## Recommendation

Proceed. The cost is small, the risk is low and the benefit is a documented, reviewable and multilingual portfolio entry.

---

[SA-001]: ./stakeholder-analysis.md
[a86c2ef]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/017-followers/commit/a86c2ef435fbe2f3f21d5178625603b669cc2e16
