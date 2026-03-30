# Tutorial 11 — Teaching Guide

## Overview

Tutorial 11 covers **Python Modules**, **CSV processing**, a brief intro to **Pandas**, and **OOP with file I/O**. It is designed for Week 12 of APS106.

### Prerequisites (what students already know)

| Topic | Covered in |
|---|---|
| `open()` / `.close()`, `for line in file`, `strip()` | Tutorial 9 |
| `__init__`, `self`, methods, constructors | Tutorial 10 |
| Basic class design | Tutorial 10 |

### What's new in this tutorial

- **Python Modules**: `import`, `from ... import`, `import ... as`, creating custom `.py` modules
- **CSV module**: `csv.reader`, `csv.writer`, `next()` for skipping headers, `newline=''`
- **`__str__` method**: customizing how objects print
- **Class composition**: using one class inside another (Book inside Library)
- **OOP + CSV integration**: reading/writing CSV inside class methods (SensorReader)
- **Pandas**: brief intro only — not on exam

---

## In-Class Plan (~60 minutes)

| Time | Problem | Topic | Difficulty |
|---|---|---|---|
| 0:00–0:05 | **M1** — Using Imports | Modules | Easy |
| 0:05–0:15 | **C1** — Reading and Processing a CSV | CSV | Easy |
| 0:15–0:30 | **C2** — Student Grades Analysis | CSV | Medium-Hard |
| 0:30–0:32 | **O1** — Quick `__str__` demo | OOP | Easy (demo only) |
| 0:32–0:47 | **O2** — SensorReader (OOP + CSV) | OOP + CSV + Modules | Medium |
| 0:47–0:50 | **O3** — Library System intro | OOP + File I/O | Hard (explain only) |
| 0:50–0:55 | **P1** — Pandas brief demo | Pandas | Medium (demo only) |
| 0:55–1:00 | **E1/E2/E3** — Exam-style overview | Exam prep | Point students to these |

### Take-home problems

M2, O1, O3, P1, E1, E2, E3

---

## Per-Problem Teaching Notes

### M1: Using Imports (Easy, ~5 min)

**Key teaching point:** Show the three import styles side-by-side. Students often confuse `import X` vs `from X import Y` vs `import X as alias`.

- Have students open `math_helpers.py` first so they can see what they're importing.
- Emphasize that the `.py` file must be in the **same folder** as the notebook.
- Quick live-coding — call each import style and run it.

### C1: Reading and Processing a CSV (Easy, ~10 min)

**Key teaching points:**
- **`next(csv_reader)`** to skip the header row. Many students don't know this pattern.
- **All CSV values are strings.** Stress the need for `int()` / `float()` conversion. This is the #1 source of bugs.
- Walk through the loop logic step-by-step, printing each `row` to show it's a list.

**Common mistake:** Students try to do `int("John")` because they forget which column index is which.

### C2: Student Grades Analysis (Medium-Hard, ~15 min)

**Key teaching points:**
- Multi-step problem — walk through one step at a time. Don't let students get overwhelmed.
- **`newline=''`** in `open()` for CSV writing — explain that without it, Windows adds extra blank lines.
- Show `next(csv_reader)` again to skip the header.
- When computing averages, remind students to convert strings to floats first.

**Common mistake:** Forgetting `newline=''` when writing CSV. Students also mix up `csv_reader` (iterable) with the raw file object.

### O1: Student Class (Easy, ~2 min demo)

**Key teaching point:** The `__str__` "aha moment."

- Show printing an object **without** `__str__` first → ugly `<__main__.Student object at 0x...>`.
- Then add `__str__` and print again → clean output.
- This is a quick demo; students implement the full class at home.

### O2: SensorReader — OOP + CSV + Modules (Medium, ~15 min)

**This is the centerpiece problem.** It ties together all three core topics: modules, CSV, and OOP.

**Key teaching points:**
- Walk through the workflow: write class in `.py` → import in notebook → use it.
- **Kernel restart**: After editing `my_classes.py`, students MUST restart the kernel for changes to take effect. Demo this live — it's the most common source of confusion.
- Show the `__str__` output after `read_data()` so students see their class working.
- For `save_filtered_data`, emphasize writing the header row separately from data rows.

**Suggested approach:**
1. Show the starter `my_classes.py` with TODOs.
2. Implement `read_data()` together as a class.
3. Have students try `__str__` on their own (2 min).
4. Implement `save_filtered_data()` together.
5. Run the notebook cell to verify.

### O3: Library System (Hard, ~3 min intro)

- Just explain the problem and the concept of **class composition** (Book objects stored inside Library).
- Point out that `Library.load_books_from_csv()` creates `Book` objects — one class using another.
- Leave as take-home. Students who finish early can start in class.

### P1: Sensor Data with Pandas (Medium, ~5 min demo)

- **Not on exam.** Make this explicit.
- Quick demo: `pd.read_csv()`, `.head()`, `.iloc[0]`, bracket filtering.
- Show how Pandas does in 2 lines what took 15 lines with the `csv` module.
- Leave the full problem as take-home.

### E1/E2/E3: Exam-style Questions (~5 min overview)

- Point students to these for exam prep.
- **E1 (Level Crossing)** is the most approachable — recommend starting there.
- **E2 (Weighted Moving Average)** requires careful index math — similar to real exam difficulty.
- **E3 (Data Anomaly Detector)** is new — combines nested loops, boundary handling, and list building.
- Don't solve these in class. Just explain what each one asks.

---

## Common Pitfalls (across all problems)

| Pitfall | Where it occurs | Fix |
|---|---|---|
| Forgetting to restart kernel after editing `.py` file | O2, O3 | Demo this live. Tell students to restart kernel every time they edit `my_classes.py`. |
| Missing `newline=''` in `open()` for CSV | C2, O2, O3 | Explain this causes extra blank lines on Windows. Always include it. |
| CSV values are strings, not numbers | C1, C2 | Show `type(row[1])` → `<class 'str'>`. Must use `int()` / `float()`. |
| Forgetting `self` in method definitions | O1, O2, O3 | Remind students every method's first parameter is `self`. |
| Confusing `import X` vs `from X import Y` | M1 | Show both side-by-side. With `import X`, you need `X.func()`. With `from X import func`, you use `func()` directly. |
| Using `==` to check `None` | O3 | Use `is None` instead of `== None` (good practice). |

---

## Files in This Directory

| File | Purpose |
|---|---|
| `tutorial11_complete.ipynb` | Complete notebook with all solutions |
| `tutorial11_starter.ipynb` | Student version with TODO placeholders |
| `my_classes.py` | Starter OOP module (TODOs for SensorReader, Book, Library) |
| `my_classes_complete.py` | Complete OOP module (solutions) |
| `math_helpers.py` | Support file for M1 (modules practice) |
| `data.csv` | Small dataset for C1 |
| `student_grades.csv` | Student grades for C2 |
| `sensor_data.csv` | Sensor readings for O2, P1 |
| `library_books.csv` | Book catalog for O3 |
| `_archive/` | Archived previous versions (not distributed to students) |

---

## Distributing to Students

Give students the following files:
- `tutorial11_starter.ipynb`
- `my_classes.py` (starter version with TODOs)
- `math_helpers.py`
- `data.csv`, `student_grades.csv`, `sensor_data.csv`, `library_books.csv`

**Do NOT distribute:** `tutorial11_complete.ipynb`, `my_classes_complete.py`, `TEACHING_GUIDE.md`, `_archive/`
