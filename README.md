# Stuck Pipe Mechanism Identifier (V2.0)

During drilling operations, a pipe is considered stuck if it cannot be freed from the hole without damaging the pipe or exceeding the drilling rig’s maximum allowed hook load.

Pipe sticking is generally classified under two main categories: **differential pressure pipe sticking** and **mechanical pipe sticking** (which includes *Pack-off / Bridge-off* and *Wellbore Geometry*).

## Why is it important to determine the stuck pipe mechanism?

Identifying the root cause of a stuck pipe event is critical because each mechanism requires a completely different freeing action. Applying the wrong procedure can worsen the situation—and potentially leave your drill string stuck in the hole permanently.

Many field engineers, including myself, rely on the industry-standard guidelines from Amoco’s **TRUE** (*Training to Reduce Unscheduled Events*) stuck pipe prevention manual.

## What is this program about?

**Stuck Pipe Mechanism Identifier** is an interactive command-line tool written in Python that digitizes the classic stuck pipe decision matrix. By answering four quick operational questions, the program calculates the score vectors and immediately identifies the most likely stuck pipe mechanism (including tie-breaking detection).

## Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/JRicardi08/Stuck_Pipe_Program-V1.0
   cd Stuck_Pipe_Program-V1.0
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the program:**
   ```bash
   python main.py
   ```

## Example Output

```text
Q-1: Pipe motion prior to sticking?
  (a) Move Up
  (b) Rotating Up
  (c) Move Down
  (d) Rotating Down
  (e) Static
Your answer: a

=============================================
FINAL SCORE BREAKDOWN
=============================================
  Pack-off / Bridge off    : 6 points
  Differential Sticking    : 0 points
  Wellbore Geometry        : 4 points
---------------------------------------------
Most likely mechanism(s): Pack-off / Bridge off
=============================================
```

## Changelog

* **V2.0 (Current):** Refactored into an Object-Oriented design (`StuckPipeQuiz` class) eliminating global variables, added per-question input validation, vectorized score calculation with NumPy, and implemented tie detection.
* **V1.1:** Initial release using standalone functions, global variables, and a shared validation tuple.

