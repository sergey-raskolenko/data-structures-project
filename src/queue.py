from src.node import Node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор пустой очереди класса Queue"""
        self.tail = None
        self.head = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        data_to_queue = Node(data=data)
        if self.tail is None:
            self.tail = data_to_queue
            self.head = data_to_queue
        else:
            self.tail.next_node = data_to_queue
            self.tail = data_to_queue


    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        pass
    def __str__(self):
        """
        Отображает содержимое очереди с головы до хвоста
        """
        queue_output = []
        node_in_queue = self.head
        while node_in_queue != None:
            queue_output.append(str(node_in_queue.data))
            node_in_queue = node_in_queue.next_node
        return '\n'.join(queue_output)
