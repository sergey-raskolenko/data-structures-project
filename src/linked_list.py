from src.node import Node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        """Инициализирует пустой односвязный список"""
        self.head = None
        self.tail = None

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        data_to_ll = Node(data=data)
        if self.tail is None:
            self.head = data_to_ll
            self.tail = data_to_ll
        else:
            self.head, self.head.next_node = data_to_ll, self.head

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        data_to_ll = Node(data=data)
        if self.head is None:
            self.head = data_to_ll
            self.tail = data_to_ll
        else:
            old_tail = self.tail
            old_tail.next_node = data_to_ll
            self.tail = data_to_ll





