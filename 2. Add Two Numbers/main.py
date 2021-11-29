# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        result = ListNode()
        current_result = result

        current1 = l1
        current2 = l2
        carry = 0

        while current1 and current2:
            full_sum = current1.val + current2.val + carry

            if len(str(full_sum)) > 1:
                str_sum = str(full_sum)

                first_digit = int(str_sum[:1])
                carry = int(str_sum[1:])

                sum_node = ListNode(first_digit)
            else:
                sum_node = ListNode(full_sum)
                carry = 0

            current_result.next = sum_node
            current_result = current_result.next

        if carry:
            sum_node = ListNode(carry)
            current_result.next = sum_node

        return result


#[2,4,3]
#[5,6,4]
if __name__ == "__main__":
    first_list = [2, 4, 3]
    second_list = [5, 6, 4]

    l1 = ListNode(2)
    l2 = ListNode(5)

    current1 = l1
    current2 = l2

    for i in range(len(first_list)):
        if i:
            node = ListNode(first_list[i])
            l1.next = node
            current1 = l1.next

            node = ListNode(second_list[i])
            l2.next = node
            current2 = l2.next

    print(l1)