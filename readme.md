# Naive String Matching and Rabin-Karp String Matching Performance Comparison

**Savitribai Phule Pune University**  
**Modern Education Society's Wadia College of Engineering, Pune**  
19, Bund Garden, V.K. Joag Path, Pune – 411001  
Accredited by NBA and NAAC with A++ Grade

**Department of Computer Engineering**

## A Mini-Project Report

**Subject:** Design and Analysis of Algorithms (DAA)  
**Academic Year:** 2026–27  
**Programme:** B.E. Computer Engineering

**Submitted by:** Prachi Kumar Nailkar  
**College PRN No.:** F23111054

---

## 1. Abstract

This mini-project implements the Naive String Matching algorithm and the Rabin-Karp algorithm in Python using only the standard library. Both algorithms search a text `T` for every occurrence of a pattern `P`. Execution time is measured using `time.perf_counter()`, while character comparisons, hash matches, and spurious hits are counted.

In every recorded experiment, both algorithms reported identical match positions. For the 16-character example, the Naive algorithm performed 30 character comparisons, whereas Rabin-Karp performed 12. On random text over a four-letter alphabet, Rabin-Karp required substantially fewer character comparisons but was approximately 1.5 times slower because of rolling-hash computation. For repetitive text with long partial matches, Rabin-Karp was approximately 20 times faster for `n = 50000` and `m = 50`. When every shift is a genuine match, both algorithms perform O(nm) character comparisons.

## 2. Introduction

String matching determines the positions at which a pattern of length `m` occurs in a text of length `n`.

The Naive algorithm slides the pattern over the text one position at a time and compares characters at each shift. Its worst-case time complexity is O(nm).

The Rabin-Karp algorithm calculates hash values for the pattern and text windows. It compares characters only when the window hash equals the pattern hash. A rolling hash calculates the next window's hash in constant time, avoiding complete hash recomputation.

This project implements both algorithms and compares their correctness, character comparisons, hash matches, spurious hits, and execution times using identical inputs.

## 3. Problem Statement

Implement the Naive String Matching and Rabin-Karp algorithms. Observe and compare their working on the same inputs.

## 4. Objectives

1. Implement both string matching algorithms in Python.
2. Run both algorithms on identical text and pattern inputs.
3. Verify that both algorithms report the same match positions.
4. Count character comparisons, hash matches, and spurious hits.
5. Measure execution time using `time.perf_counter()`.
6. Analyse their performance in best-case, average-case, and worst-case scenarios.

## 5. Scope

- Texts over the alphabet `{A, B, C, D}`, generated using random seed `42`, and repetitive texts containing only `A`.
- Benchmark text lengths from 1,000 to 100,000 and pattern lengths from 8 to 50.
- Support for custom text and pattern inputs.
- Python standard library only.
- Rabin-Karp parameters: alphabet size `d = 256` and prime modulus `q = 101`.
- KMP, Boyer-Moore, and multiple-pattern search are outside the project scope.

## 6. System and Software Requirements

| Item | Details |
|---|---|
| Programming language | Python 3 |
| Libraries | `time`, `random`, `sys` |
| Source file | `string_matching.py` |
| Execution environment | Python 3.12.3 |
| Alphabet size | `d = 256` |
| Prime modulus | `q = 101` |

### Program Menu

1. Known examples
2. Single random run
3. Benchmark
4. Custom text and pattern
5. Exit

## 7. Methodology

Both algorithms receive exactly the same text and pattern to ensure a fair comparison.

1. **Known examples:** Run the algorithms on examples such as `AABAACAADAABAABA` with pattern `AABA`, and verify the output manually.
2. **Random benchmark:** Generate random text over `{A, B, C, D}` using seed `42`.
3. **Benchmark B:** Use a text containing only `A` and a pattern ending in `B` to create long partial matches for the Naive algorithm.
4. **Benchmark C:** Use a text and pattern containing only `A` to make every shift a genuine match.
5. **Repeated execution:** Run each case three times and calculate average execution times.
6. **Correctness verification:** Compare the match-position lists returned by both algorithms.

The time ratio is defined as:

`Time Ratio = Naive Execution Time / Rabin-Karp Execution Time`

- Ratio greater than 1: Rabin-Karp is faster.
- Ratio less than 1: Naive is faster.
- Ratio approximately equal to 1: Similar execution times.

## 8. Naive String Matching Algorithm

For a text `T[0...n-1]` and pattern `P[0...m-1]`, the algorithm examines every shift from `0` to `n-m`.

At each shift `s`, it compares `P[j]` with `T[s+j]` until a mismatch occurs or all pattern characters match.

A shift is valid if:

`T[s+j] = P[j]` for every `j = 0, 1, ..., m-1`.

**Advantages**
- Simple to implement and understand.
- Requires no preprocessing.
- Uses O(1) auxiliary space.
- Performs well when mismatches occur early.

**Limitation:** It may repeat many character comparisons at adjacent shifts.

## 9. Rabin-Karp String Matching Algorithm

Rabin-Karp represents each window of length `m` using a numeric hash calculated in base `d` modulo a prime `q`.

The pattern hash `p` and first-window hash `t₀` are calculated in O(m) time.

The rolling hash for the next window is calculated using:

\[
t_{s+1} = \left(d(t_s-T[s]h)+T[s+m]\right)\bmod q
\]

where:

\[
h=d^{m-1}\bmod q
\]

The algorithm compares characters only when the current window hash equals the pattern hash.

If the hashes match but the strings differ, the event is called a **spurious hit**, caused by a hash collision. Character verification ensures that hash collisions do not produce incorrect match positions.

Project parameters:

- Alphabet size: `d = 256`
- Prime modulus: `q = 101`

**Advantages**
- Avoids character-by-character verification when hashes differ.
- Can significantly reduce character comparisons.
- Supports efficient rolling-hash computation.
- Can be useful for searching multiple patterns with suitable extensions.

**Limitation:** Hash collisions require verification, and hashing overhead can make the algorithm slower on inputs where the Naive algorithm fails quickly.

## 10. Algorithm Pseudocode

### Algorithm 1: Naive String Matching

```text
NAIVE-SEARCH(T, P)
    n = length(T)
    m = length(P)

    for s = 0 to n - m:
        j = 0

        while j < m and T[s + j] == P[j]:
            j = j + 1

        if j == m:
            report valid shift s
```

### Algorithm 2: Rabin-Karp String Matching

```text
RABIN-KARP-SEARCH(T, P, d, q)
    n = length(T)
    m = length(P)
    h = d^(m-1) mod q
    p = 0
    t = 0

    for i = 0 to m-1:
        p = (d*p + P[i]) mod q
        t = (d*t + T[i]) mod q

    for s = 0 to n-m:
        if p == t:
            if T[s : s+m] == P[0 : m]:
                report valid shift s
            else:
                count spurious hit

        if s < n-m:
            t = (d*(t - T[s]*h) + T[s+m]) mod q
```

## 11. Complexity Analysis

| Measure | Naive | Rabin-Karp |
|---|---|---|
| Preprocessing | None | O(m) |
| Best-case time | O(n), for early mismatches | Expected O(n+m) under suitable hashing assumptions |
| Average-case time | Often near O(n) for random text | Expected O(n+m) under suitable hashing assumptions |
| Worst-case time | O(nm) | O(nm) |
| Auxiliary space | O(1), excluding output | O(1), excluding output |

The Naive algorithm can be efficient when mismatches occur early. Rabin-Karp can reduce character comparisons substantially, but hash computation adds arithmetic overhead at every shift.

A small modulus such as `q = 101` makes collisions more visible in the experiments. Consequently, fewer character comparisons do not necessarily imply lower execution time.

## 12. Working on the Same Input

**Text:** `AABAACAADAABAABA`  
**Pattern:** `AABA`  
**Text length:** 16  
**Pattern length:** 4  
**Number of shifts:** 13  
**Pattern hash:** 79

Both algorithms identify the match positions `[0, 9, 12]`.

### Table 3: Shift-by-Shift Trace

| Shift | Window | Naive comparisons | Window hash | Hash match? | Rabin-Karp character comparisons | Result |
|---:|---|---:|---:|---|---:|---|
| 0 | AABA | 4 | 79 | Yes | 4 | Match |
| 1 | ABAA | 2 | 12 | No | 0 | — |
| 2 | BAAC | 1 | 32 | No | 0 | — |
| 3 | AACA | 3 | 32 | No | 0 | — |
| 4 | ACAA | 2 | 100 | No | 0 | — |
| 5 | CAAD | 1 | 38 | No | 0 | — |
| 6 | AADA | 3 | 86 | No | 0 | — |
| 7 | ADAA | 2 | 87 | No | 0 | — |
| 8 | DAAB | 1 | 41 | No | 0 | — |
| 9 | AABA | 4 | 79 | Yes | 4 | Match |
| 10 | ABAA | 2 | 12 | No | 0 | — |
| 11 | BAAB | 1 | 31 | No | 0 | — |
| 12 | AABA | 4 | 79 | Yes | 4 | Match |
| **Total** | | **30** | | **3 hash matches** | **12** | **3 matches** |

The Naive algorithm performs 30 character comparisons. Rabin-Karp performs 12 character comparisons because only three windows have hashes equal to the pattern hash. All three hash matches are genuine matches, so this example has no spurious hits.

## 13. Performance Analysis

### Benchmark A: Random Text

Random text is generated over `{A, B, C, D}`, with pattern length `m = 8`.

The Naive algorithm typically stops after one or two character comparisons. Rabin-Karp performs substantially fewer character comparisons, but rolling-hash arithmetic makes it slower in the recorded runs.

For `n = 100000`, the Naive algorithm performs 133,614 comparisons, while Rabin-Karp performs 1,316 character comparisons and records 988 spurious hits.

### Benchmark B: Worst Case for Naive

The text contains only `A` characters, and the pattern consists of `A` characters followed by `B`.

The Naive algorithm compares almost the entire pattern at every shift before detecting the final mismatch.

For `n = 50000` and `m = 50`:

- Naive comparisons: 2,497,550
- Rabin-Karp character comparisons: 0
- Naive execution time: 0.218568 seconds
- Rabin-Karp execution time: 0.010841 seconds
- Time ratio: approximately 20.16

Rabin-Karp is approximately 20 times faster in this recorded experiment because no window hash equals the pattern hash.

### Benchmark C: Worst Case for Rabin-Karp

Both the text and pattern contain only `A` characters. Every window is a genuine match.

For `n = 50000` and `m = 50`:

- Number of matches: 49,951
- Naive comparisons: 2,497,550
- Rabin-Karp character comparisons: 2,497,550
- Naive execution time: 0.223424 seconds
- Rabin-Karp execution time: 0.247447 seconds
- Time ratio: approximately 0.90

Both algorithms perform the same number of character comparisons. Rabin-Karp is slightly slower because of its additional hashing operations.

## 14. Results

### Table 4: Known Examples and Single Random Run

| Text → Pattern | n | m | Naive comparisons | Rabin-Karp comparisons | Hash matches | Spurious hits | Same positions |
|---|---:|---:|---:|---:|---:|---:|---|
| `AABAACAADAABAABA` → `AABA` | 16 | 4 | 30 | 12 | 3 | 0 | True |
| `GEEKS FOR GEEKS` → `GEEK` | 15 | 4 | 18 | 8 | 2 | 0 | True |
| `ABCDEFGH` → `XYZ` | 8 | 3 | 6 | 0 | 0 | 0 | True |
| Random text, pattern from text | 5000 | 8 | 6729 | 74 | 51 | 50 | True |

### Table 5: Benchmark A — Random Text, m = 8

| n | Naive comparisons | Rabin-Karp comparisons | Spurious hits | Naive time (s) | Rabin-Karp time (s) | Time ratio | Same |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1000 | 1311 | 25 | 14 | 0.000127 | 0.000196 | 0.65 | True |
| 5000 | 6669 | 92 | 58 | 0.000656 | 0.001060 | 0.62 | True |
| 10000 | 13385 | 140 | 93 | 0.001347 | 0.002033 | 0.66 | True |
| 50000 | 66494 | 674 | 495 | 0.007249 | 0.010800 | 0.67 | True |
| 100000 | 133614 | 1316 | 988 | 0.014135 | 0.021177 | 0.67 | True |

### Table 6: Benchmark B — Worst Case for Naive

| n | m | Naive comparisons | Rabin-Karp comparisons | Naive time (s) | Rabin-Karp time (s) | Time ratio | Same |
|---:|---:|---:|---:|---:|---:|---:|---|
| 1000 | 10 | 9910 | 0 | 0.000838 | 0.000200 | 4.19 | True |
| 5000 | 20 | 99620 | 0 | 0.008438 | 0.001227 | 6.88 | True |
| 10000 | 50 | 497550 | 0 | 0.050217 | 0.002508 | 20.02 | True |
| 50000 | 50 | 2497550 | 0 | 0.218568 | 0.010841 | 20.16 | True |

### Table 7: Benchmark C — Worst Case for Rabin-Karp

| n | m | Matches | Naive comparisons | Rabin-Karp comparisons | Naive time (s) | Rabin-Karp time (s) | Time ratio | Same |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1000 | 10 | 991 | 9910 | 9910 | 0.000958 | 0.001652 | 0.58 | True |
| 5000 | 20 | 4981 | 99620 | 99620 | 0.009130 | 0.009744 | 0.94 | True |
| 10000 | 50 | 9951 | 497550 | 497550 | 0.042150 | 0.045423 | 0.93 | True |
| 50000 | 50 | 49951 | 2497550 | 2497550 | 0.223424 | 0.247447 | 0.90 | True |

### Correctness Verification

In every recorded experiment, both algorithms reported identical match positions.

For the known example, the expected match positions are `[0, 9, 12]`. For a pattern that does not occur in the text, both algorithms return an empty list.

The timing results are averages of three runs on one machine. They may vary with hardware, Python version, system load, and implementation details.

## 15. Conclusion

- Both algorithms were implemented and tested on identical inputs.
- Both algorithms returned identical match positions in every recorded experiment.
- The Naive algorithm performed 30 character comparisons on the 16-character example, while Rabin-Karp performed 12.
- Rabin-Karp was approximately 20 times faster in the recorded long-partial-match benchmark.
- On random text over a four-letter alphabet, Rabin-Karp reduced character comparisons but was approximately 1.5 times slower.
- When every shift was a genuine match, both algorithms performed O(nm) character comparisons, and Rabin-Karp's additional hashing overhead made it slightly slower.
- The experiments demonstrate that reducing character comparisons does not always reduce execution time.

The project successfully demonstrates the implementation, correctness, and performance differences between Naive String Matching and Rabin-Karp String Matching.

## 16. Screenshots

Add the actual screenshots generated from your program in this section.

- **Figure 4:** Program start-up showing Python version, alphabet size `d = 256`, modulus `q = 101`, and menu option 1.
- **Figure 5:** Menu option 2 showing the random run with `n = 5000` and `m = 8`.
- **Figure 6:** Menu option 3 showing benchmarks A, B, and C, including comparisons, execution times, and correctness results.

To display screenshots in GitHub Markdown, upload the image files to your repository and use paths such as:

```markdown
![Figure 4: Program start-up](screenshots/figure4.png)

![Figure 5: Single random run](screenshots/figure5.png)

![Figure 6: Benchmark results](screenshots/figure6.png)
```

Replace these paths with the actual filenames and locations in your repository.

## References

1. T. H. Cormen, C. E. Leiserson, R. L. Rivest, and C. Stein, *Introduction to Algorithms*, MIT Press. Chapter on string matching.
2. Python Software Foundation, [Python `time` documentation](https://docs.python.org/3/library/time.html).
3. Python Software Foundation, [Python `random` documentation](https://docs.python.org/3/library/random.html).
4. R. M. Karp and M. O. Rabin, “Efficient randomized pattern-matching algorithms,” *IBM Journal of Research and Development*, vol. 31, no. 2, 1987.
