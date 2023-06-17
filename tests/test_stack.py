"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack
class TestStack(unittest.TestCase):
	def test__init__(self):
		stack = Stack()
		self.assertIsInstance(stack, Stack)
		self.assertEqual(stack.top, None)
	def test__str__(self):
		stack = Stack()
		stack.push(True)
		stack.push('data2')
		stack.push(3)
		self.assertEqual(stack.__str__(), '3\ndata2\nTrue')
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
		self.assertEqual(data, 'data2')
		self.assertEqual(stack.top.data, 'data1')


if __name__ == '__main__':
	unittest.main()
