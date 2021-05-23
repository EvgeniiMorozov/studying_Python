from time import time

# Структуры данных ч.2

# Связный список (deque)


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, x):
        if self.first is None:
            self.first = self.last = Node(x)
        else:
            self.last.next = self.last = Node(x)

    def push(self, x):
        if self.first is None:
            self.first = self.last = Node(x)
        else:
            self.first = Node(x, self.first)

    def insert(self, i, x):
        if self.first is None:
            self.push(x)
        else:
            if i == 0:
                self.push(x)
            else:
                current_node = self.first
                curr_i_node = 0
                while current_node is not None:
                    curr_i_node += 1
                    if curr_i_node == i:
                        current_node.next = Node(x, current_node.next)
                        if current_node.next.next is None:
                            self.last = current_node.next
                        break
                    current_node = current_node.next

    def __str__(self):
        if self.first is not None:
            current = self.first
            printed_result = str(current.value)
            while current.next is not None:
                current = current.next
                printed_result += ' ' + str(current.value)
            return f'LinkedList [ {printed_result} ]'
        return 'LinkedList []'


class Stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        self.data.pop()

    def __str__(self):
        return str(self.data)


class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, x):
        self.data.append(x)

    def dequeue(self):
        self.data.pop(0)


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_print(self.root)
        elif traversal_type == 'inorder':
            return self.inorder_print(self.root)
        elif traversal_type == 'postorder':
            return self.postorder_print(self.root)

    def preorder_print(self, start, traversal_order=''):
        if start:
            traversal_order += str(start.value) + '->'
            traversal_order = self.preorder_print(start.left, traversal_order)
            traversal_order = self.preorder_print(start.right, traversal_order)
        return traversal_order

    def inorder_print(self, start, traversal_order=''):
        if start:
            traversal_order = self.preorder_print(start.left, traversal_order)
            traversal_order += str(start.value) + '->'
            traversal_order = self.preorder_print(start.right, traversal_order)
        return traversal_order

    def postorder_print(self, start, traversal_order=''):
        if start:
            traversal_order = self.preorder_print(start.left, traversal_order)
            traversal_order = self.preorder_print(start.right, traversal_order)
            traversal_order += str(start.value) + '->'
        return traversal_order


def main():
    # linked_list = LinkedList()
    # linked_list.add(0)
    # linked_list.add(1)
    # linked_list.add(2)
    # print(linked_list)
    #
    # linked_list.push(3)
    # print(linked_list)
    #
    # linked_list.insert(0, 10)
    # linked_list.insert(1, 100)
    # print(linked_list)

    # N = 10000000
    # insert_i = N // 2
    # simple_arr = [i for i in range(N)]
    # linked_list = LinkedList()
    # for i in range(N):
    #     linked_list.add(i)
    #
    # start_time = time()
    # simple_arr.insert(insert_i, -100)
    # print(f'Время добавления эл-та в начало списка: {time() - start_time} сек')
    #
    # start_time = time()
    # linked_list.insert(insert_i, -100)
    # print(f'Время добавления эл-та в начало связного списка: {time() - start_time} сек')

    # Stack

    # stack = Stack()
    # stack.push(0)
    # stack.push(1)
    # stack.push(2)
    # print(stack)
    #
    # stack.pop()
    # print(stack)

    tree = BinaryTree(0)
    tree.root.left = TreeNode(1)
    tree.root.right = TreeNode(2)
    tree.root.left.right = TreeNode(4)
    tree.root.left.left = TreeNode(3)
    tree.root.right.right = TreeNode(6)
    tree.root.right.left = TreeNode(5)

    print(tree.print_tree('preorder'))
    print(tree.print_tree('inorder'))
    print(tree.print_tree('postorder'))


if __name__ == '__main__':
    main()
