# Curation records

This folder documents how each value in `data/` was entered and checked. It is a provenance log: the records are
kept as they were produced, so that every decision can be traced. One folder per work step, named by date and
subject.

## What a folder contains

| file | content |
|---|---|
| `task.md`, `instruction.md`, `INSTRUCTIONS.md`, `questions.md` | the task as it was given to the readers |
| `reading1*`, `reading2*`, `answers1.md`, `answers2.md` | the two readings, made blind to each other |
| `comparison.md` | every difference between the two readings |
| `resolution.md`, `changes.csv`, `rows_entered.csv` | the decision taken for each difference and the rows that changed |
| `report.md` | summary of the step: sources, method, result, open points |
| `build_rows.py` | script that derived rows from a transcription, where one was used |

## How to read the records

- The readings are machine readings (`CURATION.md`, rule 2). Reading reports are written by the reader and may use
  the first person; task files address the reader directly. They are working records, not prose for publication.
- Paths of the form `<workdir>/...` refer to the reader's working directory at the time and are not part of this
  repository.
- "Internal review" refers to reviews of analyses built on the collection; they are not part of this repository.
- "Referees" and "referee readings" are runs of the same AI model that were asked to check a text, an archive or an
  analysis. They are not peer reviewers.
- Most records are in English. Some readings of 23 November 2026 (`answers1.md`, `answers2.md`) and one report of 7 November 2026
  (`report_de.md`, with an English translation beside it) are in German, the working language of the curator; the
  reports that summarise them are in English.
- Quotations from the primary sources are limited to a few words each and stay with their rightsholders.
- The check of a sample by a person is in `2026-11-11_person_check/`.

The authoritative data are the tables in `data/`; `CHANGELOG.md` lists every change with date and time.
