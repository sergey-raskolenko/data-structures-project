class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        :param next_node: следующие данные узла
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Инициализация пустого стэка класса Stack"""
        self.top = None


    def push(self, data_to_stack: Node):
        """
        Метод для добавления элемента на вершину стека

        :param data_to_stack: данные, которые будут добавлены на вершину стека
        """
        node_in_stack = Node(data= data_to_stack)
        node_in_stack.next_node = self.top
        self.top = node_in_stack

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        data_to_return = self.top
        self.top = self.top.next_node
        return data_to_return.data
