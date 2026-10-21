"""Spaced-repetition tracker for practice problems.

usage:
    python3 review.py                      show problems due today
    python3 review.py add <num> <result>   log an attempt (result: clean | hint | fail)
    python3 review.py list                 show every problem and its next review date

Attempts are appended to review.csv. Each problem's next review date is computed from
its full history, so the CSV is the only saved state.
"""
import csv
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).parent
CSV_PATH = ROOT / "review.csv"
FIELDS = ["date", "problem", "result"]
RESULTS = ("clean", "hint", "fail")
CLEAN_LADDER = [7, 21]  # days until next review after the 1st and 2nd consecutive clean solve


def load():
    if not CSV_PATH.exists():
        return []
    with CSV_PATH.open(newline="") as f:
        return list(csv.DictReader(f))


def next_review(attempts):
    """Return the next review date for one problem's attempts, or None if retired."""
    last = date.fromisoformat(attempts[-1]["date"])
    result = attempts[-1]["result"]
    if result == "fail":
        return last + timedelta(days=1)
    if result == "hint":
        return last + timedelta(days=3)
    streak = 0  # consecutive clean solves ending at the last attempt
    for a in reversed(attempts):
        if a["result"] != "clean":
            break
        streak += 1
    if streak > len(CLEAN_LADDER):
        return None
    return last + timedelta(days=CLEAN_LADDER[streak - 1])


def schedule(rows):
    """Map problem -> next review date (None means retired)."""
    by_problem = {}
    for row in rows:
        by_problem.setdefault(row["problem"], []).append(row)
    return {p: next_review(a) for p, a in by_problem.items()}


def problem_name(num):
    """Find the solution file for a problem number, e.g. 01-arrays-hashing/0001_two_sum.py."""
    matches = sorted(ROOT.glob(f"*/{int(num):04d}_*.py"))
    return str(matches[0].relative_to(ROOT)) if matches else f"#{num}"


def main(argv, today=None):
    today = today or date.today()

    if argv[:1] == ["add"]:
        if len(argv) != 3 or not argv[1].isdigit() or argv[2] not in RESULTS:
            sys.exit("usage: python3 review.py add <num> <clean|hint|fail>")
        problem = str(int(argv[1]))
        is_new = not CSV_PATH.exists()
        with CSV_PATH.open("a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            if is_new:
                writer.writeheader()
            writer.writerow({"date": today.isoformat(), "problem": problem, "result": argv[2]})
        due = schedule(load())[problem]
        print(f"logged {problem_name(problem)}: {argv[2]} -> next review {due or 'retired'}")
        return

    plan = schedule(load())
    if argv[:1] == ["list"]:
        for p, due in sorted(plan.items(), key=lambda kv: kv[1] or date.max):
            print(f"{str(due or 'retired'):>10}  {problem_name(p)}")
        return

    due = sorted((d, p) for p, d in plan.items() if d is not None and d <= today)
    if not due:
        print("Nothing due today. Pick a new problem from the current topic.")
    for d, p in due:
        overdue = (today - d).days
        print(problem_name(p) + (f"  (overdue {overdue}d)" if overdue else ""))


if __name__ == "__main__":
    main(sys.argv[1:])
