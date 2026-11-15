# MIL-001: Baseline and framework alignment

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S02 | Initial version; accepted with the Go verdict of the review record (autonomous, not independent) | pending |

---

## Purpose

This gate decides whether Followers has a complete, reviewed baseline: documents, wiki, README and metadata, merged to the default branch with a green build.

## Deliverable

A merged pull request that holds: the accepted Business Case, Stakeholder Analysis, Project Plan and this milestone with their review records; the traceability matrix; the wiki in English, Danish and Malay; the README in the framework template with a licence statement; and the framework release adopted by the project.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | BC-001, SA-001, PP-001 and MIL-001 each have an `Accepted` Version History row and a review record with the verdict `Go` | All four | Any missing or `Go-with-conditions` |
| 2 | `python -m py_compile src/main.py` runs | Exit code 0 | Any failure |
| 3 | `docs/wiki/` has `_Sidebar.md` and the pages Home, Getting-Started and Project-Documents in en, da and ms | 9 pages and the sidebar | A page or language missing |
| 4 | `framework/scripts/check-readme.sh` and `framework/scripts/check-languages.sh` run | Exit code 0 | Any finding |
| 5 | The README License section names the licence and links `LICENSE` | Both present | Either missing |
| 6 | All CI (continuous integration) checks of the pull request | Green | Red or pending |

## Dependencies

| Depends on | Reason |
| --- | --- |
| none | This is the first and only gateway of the baseline |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1 | Criteria 2 and 6 |
| O2 | Criteria 1 and 4 |
| O3 | Criterion 3 |
| O4 | Criterion 5 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S02 |

## Target Date

2026-11-22: one week after the start, as the Business Case constraint requires.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Adopt the framework release | Track the `framework/` submodule and `.gitmodules`, install the skills, hooks and `.editorconfig`, and track `.env.example` so the project follows the same rules as the other projects of the portfolio. | No | |
| 2 | Write and review the baseline documents | Create the Business Case, Stakeholder Analysis, Project Plan, this milestone and the traceability matrix, review each against its QC checklist and accept them on a `Go`, so the plan-first gate is met. | No | |
| 3 | Publish the wiki in English, Danish and Malay | Write the pages Home, Getting-Started and Project-Documents and the sidebar in `docs/wiki/`, so a visitor can learn what the exercise is and how to run it in their own language. | No | |
| 4 | Restore the README to the framework template | Bring back the original text of the README inside the template's sections and the document appendix, with the project links, so the README is complete and checkable. | No | |
| 5 | State the licence in the README and the wiki | Name the licence of the `LICENSE` file in the README License section and on the wiki page Getting-Started, so a visitor sees it without opening the file. | No | |

---

[BC-001]: ../business-case.md
