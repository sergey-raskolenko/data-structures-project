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
    def test_to_list(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})
        lst = ll.to_list()
        self.assertEqual(len(lst), 4)
        self.assertEqual(lst[0], {'id': 0, 'username': 'serebro'})
        self.assertEqual(lst[1], {'id': 1, 'username': 'lazzy508509'})
        self.assertEqual(lst[2], {'id': 2, 'username': 'mik.roz'})
        self.assertEqual(lst[3], {'id': 3, 'username': 'mosh_s'})

    def test_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        self.assertEqual(ll.get_data_by_id(1), {'id': 1, 'username': 'lazzy508509'})


if __name__ == '__main__':
    unittest.main()
