import unittest
from src.node import Node
class TestNode(unittest.TestCase):

	def test__init__(self):
		n1 = Node(5, None)
		n2 = Node('a', n1)
		self.assertIsInstance(n1, Node)
		self.assertIsInstance(n2, Node)
		self.assertEqual(n1.data, 5)
		self.assertEqual(n2.data, 'a')
		self.assertEqual(n1, n2.next_node)

if __name__ == '__main__':
	unittest.main()