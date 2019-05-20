# Solution is coded in python2.7

import os
import sys


def find_best_match_pattern(raw_path, patterns):
    """
        Return the best match pattern where the least # of wildcards are used
        running time for this method is O(n^2logn)
    :param raw_path: raw path to look for
    :param patterns: a list of patterns
    :return: 'NO MATCH' if not found, else return the best Match
    """

    # strip the strip - use os.sep to make it cross-OS compatible
    path = raw_path.strip(os.sep).split(os.sep)

    best_match = 'NO MATCH'
    best_match_num_of_wildcards = sys.maxint

    # sort the patterns in descending order O(nlogn)
    # because we're only dealing with ASCII so * will come after after alpha-numeric characters e.g. a,*,* appears before *,*,a
    for raw_pattern in sorted(patterns, reverse=True):
        pattern = raw_pattern.split(',')

        # simple base cases
        if len(pattern) != len(path):
            continue
        if path == pattern:
            best_match = raw_pattern
            break

        pattern_matched = True
        num_of_wildcards = 0
        for i in xrange(len(pattern)):
            if pattern[i] == '*':
                num_of_wildcards += 1
                # unworthy to compare if the number of wildcards is greater than the best match
                if num_of_wildcards > best_match_num_of_wildcards:
                    break
            elif pattern[i] != path[i]:
                pattern_matched = False
                break

        # update best match
        if pattern_matched and num_of_wildcards < best_match_num_of_wildcards:
            best_match_num_of_wildcards, best_match = num_of_wildcards, raw_pattern
    return best_match


if __name__ == '__main__':
    n_patterns = int(raw_input())
    patterns = [raw_input().strip() for i in xrange(n_patterns)]
    n_paths = int(raw_input())
    for i in xrange(n_paths):
        path = raw_input()
        print find_best_match_pattern(path, patterns)
