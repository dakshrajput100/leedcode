#case1
class Solution:
    def hIndex(self, citations):
        N = len(citations)
        index = 0
        while index < N and N - index > citations[index]:
            index += 1
        return N - index



def h_index(citations):
    left = 0
    right = len(citations) - 1
    N = len(citations)
    while left <= right:
        h = left + (right - left) // 2
        if citations[h] == N - h:
            return N - h
        elif citations[h] > N - h:
            right = h - 1
        else:
            left = h + 1
    return N - left
