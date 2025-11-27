from typing import Any

class Node:
    """
    Вспомогательный класс узлов для реализации очереди
    """
    def __init__(self, value: Any, next_node=None):
        self.value = value
        self.next = next_node

class Queue:
    """
    Класс очередей
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def enqueue(self, x: Any) -> None:
        """
        Добавляет элемент в конец очереди
        :param x: Значение добавляемого элемента
        :return: Данная функция ничего не возвращает
        """
        new_node = Node(x)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def dequeue(self) -> Any:
        """
        Удаляет и возвращает элемент из начала очереди
        :return: Значение удаленного элемента
        """
        if self.is_empty():
            raise IndexError("Очередь пуста")
        
        value = self.head.value
        self.head = self.head.next
        self.size -= 1

        if self.head is None:
            self.tail = None
        
        return value
    
    def front(self) -> Any:
        """
        Возвращает элемент из начала очереди без удаления
        :return: Значение первого элемента в очереди
        """
        if self.is_empty():
            raise IndexError("Очередь пуста")
        
        return self.head.value
    
    def is_empty(self) -> bool:
        """
        Проверяет, пуста ли очередь
        :return: Пуста ли очередь
        """
        return self.head is None
    
    def __len__(self) -> int:
        """
        Возвращает количество элементов в очереди
        :return: Размер очереди
        """
        return self.size