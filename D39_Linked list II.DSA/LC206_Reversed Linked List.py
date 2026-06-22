class Solution:
    def reverseList(self, head):

        # reversed part is empty initially
        prev = None

        # current starts from first node
        curr = head

        # loop runs until curr becomes None
        while curr:

            # save next node
            # example: if curr = 1 then nxt = 2
            nxt = curr.next

            # reverse arrow direction
            # example: 1 -> None
            curr.next = prev

            # move prev forward
            # prev now becomes 1
            prev = curr

            # move curr forward
            # curr now becomes 2
            curr = nxt

        # prev becomes new head
        return prev