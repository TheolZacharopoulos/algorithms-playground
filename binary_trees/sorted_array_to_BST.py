# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
# Time complexity O(n)
from binary_trees.bst_operations.BST import BSTNode


def sorted_array_to_BST(nums):
        return to_BST(nums, 0, len(nums) - 1)


def to_BST(nums, low, high):
        if low > high:
            return None

        mid = (low + high) / 2
        n = BSTNode(nums[int(mid)])

        n.left = to_BST(nums, low, mid - 1)
        n.right = to_BST(nums, mid + 1, high)
        return n


array = [1, 2, 3, 4, 5, 6, 7, 8]
t = sorted_array_to_BST(array)
