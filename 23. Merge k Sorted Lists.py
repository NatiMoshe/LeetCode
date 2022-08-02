# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        
        for list in lists: 
            if list is None: 
                continue
                
            values.append(list.val)
            
            while list.next != None:
                list = list.next 
                values.append(list.val)
        
        values.sort()
        values.reverse()
        
        final_node = None
        next = None
        
        for num in values:
            node = ListNode(num)
            node.next = next
            next = node
            final_node = node 
            
        return final_node