from src.node import Node
class Stack:
    """Класс для стека"""
    def __init__(self):
        """Инициализация пустого стэка класса Stack"""
        self.top = None
    def __str__(self) -> str:
        """
        Отображает содержимое стэка от вершины
        """
        stack_output = []
        node_in_stack = self.top
        while node_in_stack != None:
            stack_output.append(str(node_in_stack.data))
            node_in_stack = node_in_stack.next_node
        return '\n'.join(stack_output)
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
