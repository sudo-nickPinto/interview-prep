# Interview Prep

Daily coding-interview practice (NeetCode / LeetCode in Python) plus beginner system design.
Built one topic at a time, with spaced repetition so old topics stay fresh.

## Start here

1. **Read [`00-python-basics/`](00-python-basics/README.md)**: the Python you need for interviews, plus Big-O.
2. **Open [`01-arrays-hashing/`](01-arrays-hashing/README.md)**: read the primer, then study the worked example [`0001_two_sum.py`](01-arrays-hashing/0001_two_sum.py).
3. **Solve your first problem.** Copy [`templates/problem_template.py`](templates/problem_template.py) into the topic folder and work through the warm-ups in order.
4. **Log every attempt** with `python3 review.py add <num> <clean|hint|fail>` so it comes back for review.

Then follow the daily routine below. See [ROADMAP.md](ROADMAP.md) for the topic order.

## Daily routine (~1 hour)

| Time | What |
|------|------|
| 10–15 min | `python3 review.py`: redo whatever is due, from scratch, no peeking |
| 35–40 min | 1–2 new problems from the current topic using **UPI** (below) |
| 5 min | Explain your solution out loud as if to an interviewer; write a [log](log/README.md) entry |

**Weekends:** one [system design](system-design/README.md) lesson plus a mixed review of older topics.

**Stuck rule:** if you have no working approach after ~20 minutes, watch the NeetCode explanation.
Close it, then write the code yourself. Log it as `fail`. It comes back tomorrow, and that's the point.

## How to solve a problem: UPI (from CodePath)

1. **Understand.** Restate the problem, ask clarifying questions, and write 2–3 examples, including edge cases (empty input, one element, duplicates, negatives).
2. **Plan.** Describe the approach in plain English or pseudocode *before* coding. Name the pattern. Estimate the Big-O.
3. **Implement.** Write the code, then **review** it: trace an example by hand, run the asserts, and state the final time and space complexity.

## Spaced repetition

`review.py` tracks every attempt in `review.csv`:

| Result | Meaning | Comes back |
|--------|---------|-----------|
| `fail` | couldn't solve it / needed the answer | tomorrow |
| `hint` | solved with a hint or after a long struggle | in 3 days |
| `clean` | solved alone, confidently | 7 days, then 21 days, then retired |

```bash
python3 review.py                 # what's due today
python3 review.py add 1 fail      # log an attempt at LeetCode #1
python3 review.py list            # every problem and when it's next due
```

## Layout

```
00-python-basics/     Python + Big-O primer
01-arrays-hashing/    current topic (more folders added as each topic is unlocked)
templates/            starting file to copy for each new problem
system-design/        system design notes and practice designs
log/                  daily notes
review.py / .csv      spaced-repetition tracker
codepath/             CodePath TIP102 course material (local only, gitignored)
```
