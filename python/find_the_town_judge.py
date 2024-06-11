from typing import Dict, List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = [0 for _ in range (n + 1)] 

        for t in trust:
            people[t[0]] += 1
            people[t[1]] -= 1

        for i in range(len(people)):
            if people[i] == (n-1):
                return i
        return -1
