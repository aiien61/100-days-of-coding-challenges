from typing import Iterable, Union
from math import pow


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class Singly_Linked_List:
    def __init__(self, data_list: Union[Iterable, None] = None):
        self.head = None
        if data_list:
            self.append_multiple(data_list)


    @property
    def data(self):
        result = []
        node = self.head
        while node:
            result.append(node.data)
            node = node.next
        return result


    def __len__(self):
        return len(self.data)
    

    def append(self, data: int) -> None:
        if not self.head:
            self.head = Node(data)
            return None
        
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(data)
        return None

    
    def append_multiple(self, data_list: Union[Iterable, None]) -> None:
        index = 0
        if not self.head:
            self.head = Node(data_list[index])
            index += 1

        node = self.head
        while node.next:
            node = node.next
        
        for data in data_list[index:]:
            node.next = Node(data)
            node = node.next
        return None


    def rev(self) -> None:
        body = tail = self.head
        new_head = self.head.next
        while new_head:
            tail.next = tail.next.next
            new_head.next = body
            self.head = new_head
            body = new_head
            new_head = tail.next
        return None


class Solution:

    def backward_sum_lists_by_int(self, list_1, list_2) -> Singly_Linked_List:
        num_1 = 0
        for i, num in enumerate(list_1.data):
            num_1 += num * pow(10, i)
        
        num_2 = 0
        for i, num in enumerate(list_2.data):
            num_2 += num * pow(10, i)

        data_list = list(map(int, str(int(num_1 + num_2))[::-1]))
        return Singly_Linked_List(data_list)


    def forward_sum_lists_by_int(self, list_1, list_2) -> Singly_Linked_List:
        num_1 = 0
        for i, num in enumerate(list_1.data[::-1]):
            num_1 += num * pow(10, i)

        num_2 = 0
        for i, num in enumerate(list_2.data[::-1]):
            num_2 += num * pow(10, i)

        data_list = list(map(int, str(int(num_1 + num_2))))
        return Singly_Linked_List(data_list)


    def backward_sum_lists(self, list_1, list_2) -> Singly_Linked_List:
        p1 = list_1.head
        p2 = list_2.head
        sum_list = Singly_Linked_List()
        next_digit = 0
        while p1 or p2:
            if p1:
                next_digit += p1.data
                p1 = p1.next
            
            if p2:
                next_digit += p2.data
                p2 = p2.next
            
            next_digit, this_digit = divmod(next_digit, 10)
            sum_list.append(this_digit)

        if next_digit:
            sum_list.append(next_digit)
        
        return sum_list


    def forward_sum_lists(self, list_1, list_2) -> Singly_Linked_List:
        list_1.rev()
        list_2.rev()

        n1, n2 = len(list_1), len(list_2)
        d = abs(n1 - n2)
        if n1 < n2:
            list_1.append_multiple([0] * d)
        elif n2 < n1:
            list_2.append_multiple([0] * d)


        p1 = list_1.head
        p2 = list_2.head
        sum_list = Singly_Linked_List()
        next_digit = 0
        while p1 or p2:
            if p1:
                next_digit += p1.data
                p1 = p1.next

            if p2:
                next_digit += p2.data
                p2 = p2.next

            next_digit, this_digit = divmod(next_digit, 10)
            sum_list.append(this_digit)

        if next_digit:
            sum_list.append(next_digit)

        sum_list.rev()
        return sum_list
