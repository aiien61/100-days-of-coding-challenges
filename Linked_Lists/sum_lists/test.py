import unittest
from main import Solution, Singly_Linked_List


class Test(unittest.TestCase):
    sol = Solution()

    backward_data_lists = [
        [[4, 0, 9], [3, 0, 9], [7, 0, 8, 1]],
        [[7, 1, 6], [5, 9, 2], [2, 1, 9]],
        [[4, 0, 9], [3, 0, 9, 1], [7, 0, 8, 2]],
        [[2, 2, 2], [8, 7, 7], [0, 0, 0, 1]]
    ]

    forward_data_lists = [
        [[4, 0, 9], [3, 0, 9], [7, 1, 8]],
        [[6, 1, 7], [2, 9, 5], [9, 1, 2]],
        [[4, 0, 9], [1, 3, 0, 9], [1, 7, 1, 8]],
        [[2, 2, 2], [7, 7, 8], [1, 0, 0, 0]]
    ]

    def test_backward_data_lists(self):
        for data_list_1, data_list_2, expected in self.backward_data_lists:
            list_1 = Singly_Linked_List(data_list_1)
            list_2 = Singly_Linked_List(data_list_2)
            result = self.sol.backward_sum_lists(list_1, list_2)
            self.assertEqual(result.data, expected)
    
    def test_backward_sum_lists_by_int(self):
        for data_list_1, data_list_2, expected in self.backward_data_lists:
            list_1 = Singly_Linked_List(data_list_1)
            list_2 = Singly_Linked_List(data_list_2)
            result = self.sol.backward_sum_lists_by_int(list_1, list_2)
            self.assertEqual(result.data, expected)
    
    def test_forward_sum_lists(self):
        for data_list_1, data_list_2, expected in self.forward_data_lists:
            list_1 = Singly_Linked_List(data_list_1)
            list_2 = Singly_Linked_List(data_list_2)
            result = self.sol.forward_sum_lists(list_1, list_2)
            self.assertEqual(result.data, expected)
    
    def test_forward_sum_lists_by_int(self):
        for data_list_1, data_list_2, expected in self.forward_data_lists:
            list_1 = Singly_Linked_List(data_list_1)
            list_2 = Singly_Linked_List(data_list_2)
            result = self.sol.forward_sum_lists_by_int(list_1, list_2)
            self.assertEqual(result.data, expected)


if __name__ == "__main__":
    unittest.main()
