class Solution:

    def middleNode(self, head):

        # slow pointer starts from first node
        slow = head

        # fast pointer also starts from first node
        fast = head

        # loop runs while fast can move 2 steps safely
        while fast and fast.next:

            # slow moves 1 step
            slow = slow.next

            # fast moves 2 steps
            fast = fast.next.next

        # when fast reaches end
        # slow automatically reaches middle
        return slow                  # here main concept is fast runs two times slow & fast reach end part then slow's position is mid 