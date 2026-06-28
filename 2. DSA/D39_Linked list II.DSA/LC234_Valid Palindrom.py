class Solution:
    def isPalindrome(self, head):

        # create two pointers
        # both start from first node
        slow = head
        fast = head

        # fast moves 2 steps
        # slow moves 1 step
        # when fast reaches end
        # slow reaches middle
        while fast and fast.next:

            # move slow 1 step
            slow = slow.next

            # move fast 2 steps
            fast = fast.next.next

        # reverse second half starts here

        # reversed part initially empty
        prev = None

        # reverse linked list from middle to end
        while slow:

            # save next node
            nxt = slow.next

            # reverse arrow direction
            slow.next = prev

            # move prev forward
            prev = slow

            # move slow forward
            slow = nxt

        # compare first half and reversed second half

        # left starts from beginning
        left = head

        # right starts from reversed second half
        right = prev

        # loop until second half ends
        while right:

            # if values are different
            # linked list is not palindrome
            if left.val != right.val:
                return False

            # move left forward
            left = left.next

            # move right forward
            right = right.next

        # if all values matched
        # linked list is palindrome
        return True