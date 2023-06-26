"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue

class QueueTestCase(unittest.TestCase):
	def test__init__(self):
		queue = Queue()
		self.assertEqual(str(queue), '')
		self.assertIsInstance(queue, Queue)
		self.assertEqual(queue.tail, None)
		self.assertEqual(queue.head, None)

	def test__str__(self):
		queue = Queue()
		queue.enqueue(1)
		queue.enqueue(2)
		queue.enqueue(3)
		self.assertEqual(str(queue),"1\n2\n3")

	def test_enqueue(self):
		queue = Queue()
		queue.enqueue(1)
		queue.enqueue(2)
		queue.enqueue(3)
		self.assertEqual(queue.head.data, 1)
		self.assertEqual(queue.head.next_node.data, 2)
		self.assertEqual(queue.tail.data, 3)
		self.assertEqual(queue.tail.next_node, None)
		self.assertRaises(AttributeError)

	def test_dequeue(self):
		queue = Queue()
		queue.enqueue(1)
		queue.enqueue(2)
		queue.enqueue(3)
		self.assertEqual(queue.dequeue(), 1)
		self.assertEqual(str(queue), "2\n3")
		self.assertEqual(queue.dequeue(), 2)
		self.assertEqual(str(queue), "3")
		self.assertEqual(queue.dequeue(), 3)
		self.assertEqual(str(queue), '')
		self.assertEqual(queue.dequeue(), None)
		self.assertEqual(str(queue), '')




if __name__ == "__main__":
	unittest.main()
