"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from src.stack import Node, Stack
import unittest

class TestNode(unittest.TestCase):

	def test__init__(self):
		n1 = Node(5, None)
		n2 = Node('a', n1)
		self.assertIsInstance(n1, Node)
		self.assertIsInstance(n2, Node)
		self.assertEqual(n1.data, 5)
		self.assertEqual(n2.data, 'a')
		self.assertEqual(n1, n2.next_node)

class TestStack(unittest.TestCase):

	def test_push_to_stack(self):
		stack = Stack()
		stack.push('data1')
		stack.push('data2')
		stack.push('data3')
		self.assertEqual(stack.top.data, 'data3')
		self.assertEqual(stack.top.next_node.data, 'data2')
		self.assertEqual(stack.top.next_node.next_node.data, 'data1')
		self.assertEqual(stack.top.next_node.next_node.next_node, None)
		with self.assertRaises(AttributeError):
			print(stack.top.next_node.next_node.next_node.data)

	def test_pop_from_stuck_1(self):
		stack = Stack()
		stack.push('data1')
		data = stack.pop()
		self.assertEqual(stack.top, None)
		self.assertEqual(data, 'data1')

	def test_pop_from_stuck_2(self):
		stack = Stack()
		stack.push('data1')
		stack.push('data2')
		data = stack.pop()
		self.assertEqual(stack.top.data, 'data1')
		self.assertEqual(data, 'data2')



if __name__ == '__main__':
	unittest.main()
