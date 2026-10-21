# 00 · Python for Interviews + Big-O

You don't need all of Python, just this subset. Try each snippet by typing `python3`
in a terminal to open the interactive shell.

## Core types

```python
# list: ordered, mutable, indexed from 0
nums = [3, 1, 4]
nums.append(1)          # [3, 1, 4, 1]       O(1)
nums.pop()              # removes last        O(1)
nums[0], nums[-1]       # first, last         O(1)
nums[1:3]               # slice -> [1, 4]     O(k) for k items copied
4 in nums               # linear scan         O(n)  <-- slow for lists!
len(nums)               #                     O(1)

# dict (hashmap): key -> value, average O(1) lookup/insert/delete
ages = {"ana": 30}
ages["bo"] = 25
ages.get("cy", 0)       # default if missing, no KeyError
"ana" in ages           # O(1)
for name, age in ages.items(): ...

# set: unique values, O(1) membership
seen = set()
seen.add(5)
5 in seen               # O(1)  <-- why sets/dicts beat lists for lookups

# string: immutable sequence of characters
s = "Hello"
s.lower(), s[::-1]      # "hello", "olleH"
s.split(","), ",".join(["a", "b"])
# Building strings in a loop: append parts to a list, then "".join(parts) at the end
```

## Looping idioms

```python
for i in range(len(nums)): ...          # by index
for x in nums: ...                      # by value
for i, x in enumerate(nums): ...        # both (use this one a lot)
for a, b in zip(list1, list2): ...      # two lists in parallel
squares = [x * x for x in nums]         # list comprehension
evens = [x for x in nums if x % 2 == 0]
```

## Sorting

```python
sorted(nums)                     # new list, O(n log n)
nums.sort(reverse=True)          # in place
sorted(words, key=len)           # sort by a computed key
sorted(pairs, key=lambda p: p[1])
```

## The `collections` toolbox

```python
from collections import Counter, defaultdict, deque

Counter("banana")                # {'a': 3, 'n': 2, 'b': 1}
Counter(nums).most_common(2)     # top 2 (value, count) pairs

groups = defaultdict(list)       # missing keys start as []
groups["fruit"].append("apple")

q = deque([1, 2, 3])             # fast at both ends (queues, BFS)
q.appendleft(0); q.popleft()     # O(1)

import heapq                     # min-heap on a plain list
heapq.heappush(h, x); heapq.heappop(h)
```

Other handy built-ins: `float("inf")` (a value bigger than any number), `max()` / `min()` / `sum()`,
`abs()`, `divmod()`, and integer division with `//`.

## Big-O in one page

Big-O describes how work grows as the input size **n** grows. Drop constants and keep the biggest term.

| Big-O | Name | Typical code |
|-------|------|--------------|
| O(1) | constant | dict/set lookup, list index |
| O(log n) | logarithmic | binary search; halving each step |
| O(n) | linear | one loop over the input |
| O(n log n) | linearithmic | sorting |
| O(n²) | quadratic | a loop inside a loop over the same input |
| O(2ⁿ) | exponential | trying every subset |

**Space complexity** is the extra memory you create. A new dict holding up to n items is O(n) space.

Rough feel: with n = 100,000, O(n²) is too slow and O(n log n) is fine.
Interviewers almost always ask "can you do better?" after a brute-force answer. The usual answer is to
**trade space for time**: store things in a dict or set so lookups are O(1).

## Learn more
- CodePath Unit 1 cheatsheet: `codepath/unit-01/cheatsheet.md` (local only)
- [Python docs: built-in types](https://docs.python.org/3/library/stdtypes.html)
- [Python docs: collections](https://docs.python.org/3/library/collections.html)
- [Big-O cheat sheet](https://www.bigocheatsheet.com/)
