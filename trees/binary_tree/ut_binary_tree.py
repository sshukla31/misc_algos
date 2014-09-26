import unittest
import binary_tree



class TH(binary_tree.BinaryTree):
    def __init__(self):
        super(TH, self).__init__()

class BinaryTreeTest(unittest.TestCase):

    def setUp(self):
        self.bt = TH()
        for value in [5, 2, 1, 9, 10, 0, 6]:
            self.bt.insert(value)

    def tearDown(self):
        self.bt.inorder_result = self.bt.preorder_result = self.bt.postorder_result = []


    def test_record_meta(self):
        expected_result = [
            {'right_child': 9, 'node_value': 5, 'sibling': None, 'found': True, 'left_child': 2, 'parent_node': None},
            {'right_child': None, 'node_value': 0, 'sibling': None, 'found': True, 'left_child': None, 'parent_node': 1},
            {'right_child': 10, 'node_value': 9, 'sibling': 2, 'found': True, 'left_child': 6, 'parent_node': 5},
            {'right_child': None, 'node_value': 1, 'sibling': None, 'found': True, 'left_child': 0, 'parent_node': 2}
        ]
        actual_result = [self.bt.record_meta_data(value) for value in [5, 0, 9, 1]]
        for val in actual_result:
            val['parent_node'] = getattr(val['parent_node'], 'data', None)
            val['node_value'] = val['node_value'].data

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
