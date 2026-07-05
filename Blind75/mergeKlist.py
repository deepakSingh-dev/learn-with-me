from typing import List, Optional
import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        # push initial heads
        for i, node in enumerate(lists):
            if node:
                # (value, list_index, node) -> list_index breaks ties when values equal
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        tail = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        tail.next = None  # optional safety
        return dummy.next