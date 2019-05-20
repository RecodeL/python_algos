# python version of FreqQuery leveraging defauldict, much quicker

from collections import defaultdict

# Complete the freqQuery function below.
def freq_query(queries):
    a = defaultdict(int) # n:cnt
    b = defaultdict(int) # cnt:occurence
    res = []
    for query in queries:
        op, data = query[0], query[1]
        if op == 1:
            if data in a:
                b[a[data]] -= 1
            a[data] += 1
            b[a[data]] += 1
        elif op == 2:
            if data in a:
                b[a[data]] -= 1
                a[data] -= 1
                b[a[data]] += 1
                a[data] = 0 if a[data] < 0 else a[data] # reset the negative count
        elif op == 3:
            res.append('1' if data in b and b[data] > 0 else '0')
    return res


if __name__ == '__main__':
    queries = [[1, 2], [1, 2], [3, 1], [1, 3], [2, 2], [3, 1]]
    ans = freq_query(queries)
    print ans == ['0', '1'] # expects it to print [0, 1]
    queries = [[1, 2], [1, 2], [3, 2], [1, 3], [2, 2], [3, 1], [3, 2]]
    ans = freq_query(queries)
    print ans == ['1', '1', '0']
    queries = [[1, 5], [1, 2], [2, 10], [3, 1], [2, 4], [2,5], [3, 1]]
    ans = freq_query(queries)
    print ans == ['1', '1']
