"""Здесь надо написать тесты с использованием unittest для модуля stack."""
from src.stack import Stack
from src.node import Node
import unittest

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

	def test_str_stuck(self):
		stack = Stack()
		stack.push(True)
		stack.push('data2')
		stack.push(3)
		self.assertEqual(str(stack), '3\ndata2\nTrue')


if __name__ == '__main__':
	unittest.main()
