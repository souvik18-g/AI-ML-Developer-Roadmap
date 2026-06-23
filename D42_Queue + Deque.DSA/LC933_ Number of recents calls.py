from collections import deque

class RecentCounter:

    def __init__(self):

        # create an empty queue
        # this queue stores all request times
        self.q = deque()

    def ping(self, t):

        # add current request time into queue
        self.q.append(t)

        # remove old requests
        # keep only requests inside:
        # [t - 3000, t]

        while self.q[0] < t - 3000:

            # remove old timestamp from front
            self.q.popleft()

        # remaining queue size
        # = number of recent requests
        return len(self.q)
