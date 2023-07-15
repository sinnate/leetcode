class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        list_event = sorted(events)

        @functools.lru_cache(None)
        def search(i, k):
            if k == 0 or i == len(list_event):
                return 0

            # Binary search events to find the first index j s.t. list_event[j][0] > list_event[i][1]
            j = bisect.bisect(list_event, [list_event[i][1], math.inf, math.inf], i + 1)
            return max(search(i + 1, k), list_event[i][2] + search(j, k - 1))

        return search(0, k)