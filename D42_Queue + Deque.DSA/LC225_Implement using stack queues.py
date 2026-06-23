from collections import deque


class MyStack:

    def __init__(self):

        # create an empty queue
        self.q = deque()


    def push(self, x: int) -> None:

        # add new element into queue
        self.q.append(x)

        # EXAMPLE:
        #
        # before push:
        # [1,2]
        #
        # after append(3):
        # [1,2,3]
        #
        # but stack needs newest element at FRONT
        #
        # expected:
        # [3,1,2]
        #
        # so rotate old elements behind 3


        # loop only old(previous) elements
        #
        # len(self.q) = 3
        #
        # 3 - 1 = 2
        #
        # so loop runs 2 times
        #
        # because old elements are:
        # 1 and 2

        for _ in range(len(self.q) - 1):


            # self.q.popleft()
            #
            # remove front element
            #
            # queue:
            # [1,2,3]
            #
            # remove 1
            #
            # remaining:
            # [2,3]


            # self.q.append(...)
            #
            # add removed element at rear
            #
            # after append(1):
            # [2,3,1]

            self.q.append(self.q.popleft())


            # second rotation:
            #
            # remove 2
            # append 2 at rear
            #
            # final:
            # [3,1,2]
            #
            # newest element 3 comes front
            #
            # now queue behaves like stack


    def pop(self) -> int:

        # remove front element
        #
        # front contains latest pushed element
        #
        # because rotations already arranged queue like stack
        #
        # example:
        # [3,1,2]
        #
        # remove:
        # 3

        return self.q.popleft()


    def top(self) -> int:

        # return front element
        #
        # front is stack top
        #
        # example:
        # [3,1,2]
        #
        # top = 3

        return self.q[0]


    def empty(self) -> bool:

        # check queue empty or not
        #
        # if length = 0
        # stack is empty

        return len(self.q) == 0