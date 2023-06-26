"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
from src.linked_list import LinkedList
import unittest

class TestLinkedList(unittest.TestCase):
    def test_init(self):
        ll = LinkedList()
        self.assertEqual(isinstance(ll, LinkedList), True)
        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})
        self.assertEqual(str(ll), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")

if __name__ == '__main__':
    unittest.main()
