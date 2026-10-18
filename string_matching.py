"""Naive vs Rabin-Karp string matching (standard library only)."""
import random
import sys
import time

D = 256  # alphabet size
Q = 101  # prime modulus


def naive_search(T, P):
    n, m = len(T), len(P)
    positions, cmp = [], 0
    for s in range(n - m + 1):
        j = 0
        while j < m:
            cmp += 1
            if T[s + j] != P[j]:
                break
            j += 1
        if j == m:
            positions.append(s)
    return positions, cmp


def rabin_karp_search(T, P):
    n, m = len(T), len(P)
    positions, cmp, hash_matches, spurious = [], 0, 0, 0
    if m > n:
        return positions, cmp, hash_matches, spurious
    h = pow(D, m - 1, Q)
    p = t = 0
    for i in range(m):
        p = (D * p + ord(P[i])) % Q
        t = (D * t + ord(T[i])) % Q
    for s in range(n - m + 1):
        if p == t:
            hash_matches += 1
            j = 0
            while j < m:
                cmp += 1
                if T[s + j] != P[j]:
                    break
                j += 1
            if j == m:
                positions.append(s)
            else:
                spurious += 1
        if s < n - m:
            t = (D * (t - ord(T[s]) * h) + ord(T[s + m])) % Q
    return positions, cmp, hash_matches, spurious


def timed(fn, T, P, runs=3):
    total = 0.0
    for _ in range(runs):
        a = time.perf_counter()
        fn(T, P)
        total += time.perf_counter() - a
    return total / runs


def compare(T, P):
    np_, nc = naive_search(T, P)
    rp, rc, hm, sp = rabin_karp_search(T, P)
    tn, tr = timed(naive_search, T, P), timed(rabin_karp_search, T, P)
    print(f"  n = {len(T)}, m = {len(P)}")
    print(f"  Naive       : {nc} comparisons, {tn:.6f} s")
    print(f"  Rabin-Karp  : {rc} comparisons, {hm} hash matches, {sp} spurious, {tr:.6f} s")
    print(f"  Positions   : {np_[:20]}")
    print(f"  Same positions found: {np_ == rp}")


def random_text(n, seed=42):
    r = random.Random(seed)
    return "".join(r.choice("ABCD") for _ in range(n))


def known_examples():
    for T, P in [("AABAACAADAABAABA", "AABA"), ("GEEKS FOR GEEKS", "GEEK"), ("ABCDEFGH", "XYZ")]:
        print(f"\nText: {T}  Pattern: {P}")
        compare(T, P)


def single_random():
    n = int(input("n: ")); m = int(input("m: "))
    T = random_text(n)
    P = T[n // 2: n // 2 + m]
    compare(T, P)


def benchmark():
    print("\nBenchmark A: random text over {A,B,C,D}, m = 8 (average of 3 runs)")
    print(f"{'n':>8}{'Naive cmp':>12}{'RK cmp':>10}{'Spurious':>10}{'Naive(s)':>11}{'RK(s)':>11}  Same")
    for n in (1000, 5000, 10000, 50000, 100000):
        T = random_text(n); P = T[n // 2: n // 2 + 8]
        a, nc = naive_search(T, P); b, rc, _, sp = rabin_karp_search(T, P)
        print(f"{n:>8}{nc:>12}{rc:>10}{sp:>10}{timed(naive_search, T, P):>11.6f}"
              f"{timed(rabin_karp_search, T, P):>11.6f}  {a == b}")

    print("\nBenchmark B (worst case for Naive): text = 'A' * n, pattern = 'A' * (m-1) + 'B'")
    print(f"{'n':>8}{'m':>5}{'Naive cmp':>12}{'RK cmp':>10}{'Naive(s)':>11}{'RK(s)':>11}  Same")
    for n, m in [(1000, 10), (5000, 20), (10000, 50), (50000, 50)]:
        T = "A" * n; P = "A" * (m - 1) + "B"
        a, nc = naive_search(T, P); b, rc, _, _ = rabin_karp_search(T, P)
        print(f"{n:>8}{m:>5}{nc:>12}{rc:>10}{timed(naive_search, T, P):>11.6f}"
              f"{timed(rabin_karp_search, T, P):>11.6f}  {a == b}")

    print("\nBenchmark C (worst case for Rabin-Karp): text = 'A' * n, pattern = 'A' * m")
    print(f"{'n':>8}{'m':>5}{'Matches':>9}{'Naive cmp':>12}{'RK cmp':>10}{'Naive(s)':>11}{'RK(s)':>11}  Same")
    for n, m in [(1000, 10), (5000, 20), (10000, 50), (50000, 50)]:
        T = "A" * n; P = "A" * m
        a, nc = naive_search(T, P); b, rc, _, _ = rabin_karp_search(T, P)
        print(f"{n:>8}{m:>5}{len(a):>9}{nc:>12}{rc:>10}{timed(naive_search, T, P):>11.6f}"
              f"{timed(rabin_karp_search, T, P):>11.6f}  {a == b}")


def own_input():
    T = input("Text: "); P = input("Pattern: ")
    if not P or len(P) > len(T):
        print("Pattern must be non-empty and not longer than the text."); return
    compare(T, P)


def main():
    print(f"Python {sys.version.split()[0]} | alphabet size d = {D} | prime q = {Q}")
    while True:
        print("\n1. Known examples (Naive vs Rabin-Karp)\n2. Single run with random text (enter n and m)")
        print("3. Benchmark (best / worst cases)\n4. Enter your own text and pattern\n5. Exit")
        c = input("Choose an option (1-5): ").strip()
        if c == "1": known_examples()
        elif c == "2": single_random()
        elif c == "3": benchmark()
        elif c == "4": own_input()
        elif c == "5": break


if __name__ == "__main__":
    main()
