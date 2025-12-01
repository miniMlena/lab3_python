import pytest
from src.queues.queue_class import Queue
from src.queues.queue_commands import queues, create_queue, delete_queue, show_queue, queue_operation
from src.app_errors import AppError

# Тесты для класса очередей
def test_create_empty_queue():
    """Создание пустой очереди"""
    q = Queue()
    assert q.is_empty()
    assert len(q) == 0

def test_enqueue_multiple():
    """Добавление элементов"""
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    
    assert len(q) == 3
    assert q.front() == 1

def test_dequeue_multiple():
    """Удаление элементов"""
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.is_empty()

def test_front():
    """Вызов метода front()"""
    q = Queue()
    q.enqueue(42)
    
    assert q.front() == 42
    assert q.front() == 42
    assert len(q) == 1

def test__empty_queue_errors():
    """Ошибки с пустой очередью"""
    q = Queue()
    
    with pytest.raises(IndexError):
        q.dequeue()
    
    with pytest.raises(IndexError):
        q.front()

def test_len_method():
    """Тестирование __len__"""
    q = Queue()
    assert len(q) == 0
    
    q.enqueue(-1)
    assert len(q) == 1
    
    q.enqueue(-2)
    q.enqueue(-3)
    assert len(q) == 3
    
    q.dequeue()
    assert len(q) == 2

def test_is_empty_method():
    """Тестирование is_empty()"""
    q = Queue()
    assert q.is_empty()
    
    q.enqueue(1)
    assert not q.is_empty()
    
    q.dequeue()
    assert q.is_empty()

# Тесты команд для очередей
def setup_queues():
    """Очищаем очереди перед каждым тестом"""
    global queues
    queues.clear()

def test_create_queue_empty():
    """Создание пустой очереди"""
    create_queue("create q1")
    assert "q1" in queues
    assert queues["q1"].is_empty()

def test_create_queue_with_elements_bracket():
    """Создание очереди с элементами"""
    create_queue("create q2 [1,2,3]")
    assert len(queues["q2"]) == 3
    assert queues["q2"].front() == 1

def test_add_to_queue():
    """Добавление элемента в очередь"""
    create_queue("create q5")
    queue_operation("q5", "add", "q5 add 42")

    assert queues["q5"].front() == 42
    assert len(queues["q5"]) == 1

def test_remove_from_queue():
    """Удаление элемента из очереди"""
    create_queue("create q6 [1,2,3]")
    queue_operation("q6", "remove", "q6 remove")

    assert len(queues["q6"]) == 2
    assert queues["q6"].front() == 2

def test_delete_queue():
    """Удаление очереди"""
    create_queue("create to_delete")
    delete_queue("delete to_delete")

    assert "to_delete" not in queues

def test__queue_errors():
    """Ошибки с очередями"""
    with pytest.raises(AppError):
        create_queue("create q4")
        create_queue("create q4")

    with pytest.raises(IndexError):
        create_queue("create q7")
        queue_operation("q7", "remove", "q7 remove")

    with pytest.raises(AppError):
        show_queue("show not_exist")

    with pytest.raises(AppError):
        delete_queue("delete nonexistent")