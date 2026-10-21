# 01 · Arrays & Hashing

## The idea in plain English

An **array** (a Python `list`) is a row of boxes you reach by position. Reading `nums[i]` is instant,
but *finding* a value means checking box after box, which is O(n).

A **hashmap** (`dict`) and a **hash set** (`set`) fix that. They jump straight to a value
in O(1) on average. Most problems in this topic follow one move:

> *"I'm about to loop inside a loop to find something. Instead, store what I've seen in a dict or set,
> so finding it is O(1)."*

That turns O(n²) into O(n), at the cost of O(n) extra memory.

## Recognize it

The problem says or implies: *duplicate, count, frequency, anagram, pair that sums to, group by, seen before,
most common, unique*.

## Patterns and templates

**1. Seen-set: "have I seen this before?"**
```python
seen = set()
for x in nums:
    if x in seen:
        return True          # duplicate found
    seen.add(x)
return False
```

**2. Complement lookup: "is the partner I need already stored?"** (Two Sum)
```python
index_of = {}                # value -> index
for i, x in enumerate(nums):
    need = target - x
    if need in index_of:
        return [index_of[need], i]
    index_of[x] = i
```

**3. Frequency count**
```python
from collections import Counter
counts = Counter(s)          # or: counts[c] = counts.get(c, 0) + 1
return Counter(s) == Counter(t)   # anagram check
```

**4. Group by a key**
```python
from collections import defaultdict
groups = defaultdict(list)
for word in words:
    groups["".join(sorted(word))].append(word)   # anagrams share a sorted key
return list(groups.values())
```

**5. Prefix sums: precompute running totals so any range sum is O(1)**
```python
prefix = [0]
for x in nums:
    prefix.append(prefix[-1] + x)
# sum of nums[i..j] == prefix[j + 1] - prefix[i]
```

## Problems

Do them in order. Copy `templates/problem_template.py`, name it `NNNN_problem_name.py`, and log each attempt
with `python3 review.py add NNNN <clean|hint|fail>`.

**Warm-ups (Easy). Get comfortable with lists, strings, and dicts.**

- [ ] [1929. Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/)
- [ ] [58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/)
- [ ] [1299. Replace Elements with Greatest Element on Right Side](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/)
- [ ] [392. Is Subsequence](https://leetcode.com/problems/is-subsequence/)
- [ ] [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)
- [ ] [169. Majority Element](https://leetcode.com/problems/majority-element/)
- [ ] [724. Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) (prefix sums)
- [ ] [290. Word Pattern](https://leetcode.com/problems/word-pattern/)

**NeetCode 150 core (the ones interviews actually ask)**

- [ ] [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/): Easy, seen-set
- [ ] [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/): Easy, frequency count
- [ ] [1. Two Sum](https://leetcode.com/problems/two-sum/): Easy, complement lookup ([worked example](0001_two_sum.py). Read it, then re-solve it from a blank file the next day)
- [ ] [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/): Medium, group by key
- [ ] [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/): Medium, count + bucket sort
- [ ] [271. Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/): Medium, length prefixing
- [ ] [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/): Medium, prefix/suffix
- [ ] [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/): Medium, sets per row/col/box
- [ ] [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/): Medium, set + sequence starts

**Extra practice (CodePath mock interview list: Lists + Dictionaries)**

- [ ] [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- [ ] [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- [ ] [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)
- [ ] [383. Ransom Note](https://leetcode.com/problems/ransom-note/)
- [ ] [205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/)
- [ ] [350. Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)

**Ready for the next topic when:** you can do the core 9 `clean` without notes, and explain out loud
why a dict lookup is O(1) while `x in list` is O(n).

## Learn more
- [NeetCode: Arrays & Hashing videos](https://neetcode.io/roadmap) (watch after you attempt, not before)
- [VisuAlgo: Hash Table](https://visualgo.net/en/hashtable) shows hashing visually
- CodePath Unit 1 sessions + cheatsheet: `codepath/unit-01/` (local only)
