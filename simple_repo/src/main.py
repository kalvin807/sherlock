from queue import PriorityQueue
from typing import List, Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        node_queue: PriorityQueue[Tuple[int, int, ListNode]] = PriorityQueue(len(lists))
        # Use counter to diff same value nodes.
        counter = 1
        for node in lists:
            if node:
                node_queue.put((node.val, counter, node))
                counter += 1

        dummy_node = ListNode(0, None)
        current = dummy_node

        while not node_queue.empty():
            _, _, min_node = node_queue.get()
            current.next = min_node
            current = current.next
            if min_node.next:
                node_queue.put((-min_node.next.val, counter, min_node.next))
                counter += 1

        return dummy_node.next


test_list1 = ListNode(1, ListNode(4, ListNode(5)))
test_list2 = ListNode(1, ListNode(3, ListNode(4)))
test_list3 = ListNode(2, ListNode(6))

ans = Solution().mergeKLists([test_list1, test_list2, test_list3])

current = ans
ans_list = []
while current:
    ans_list.append(current.val)
    current = current.next

print(ans_list)
