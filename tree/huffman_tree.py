from binary_tree import BinaryTreeNode
from heap.binary_heap import BinaryHeap


class HuffmanTree(BinaryTreeNode):
    """
    Huffman Tree implementation
    """
    def construct(self, array):
        binary_heap = BinaryHeap(len(array))
        for i in array:
            binary_heap.insert(i)

        while not binary_heap.is_empty():
            first_key = binary_heap.delete_min()
            first_node = BinaryTreeNode(first_key, None, None, None)
            second_key = binary_heap.delete_min()
            second_node = BinaryTreeNode(second_key, None, None, None)
            new_key = first_key + second_key
            new_node = BinaryTreeNode(new_key, None, first_node, second_node)
            binary_heap.insert(new_key)
