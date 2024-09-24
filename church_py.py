# church_py.py

# Декораторы
def благословение(молитва):
    def wrapper(*args, **kwargs):
        print("Начало молитвы...")
        результат = молитва(*args, **kwargs)
        print("Молитва завершена.")
        return результат
    return wrapper

def святая_служба(декоратор):
    def wrapper(*args, **kwargs):
        print("Начало службы...")
        результат = декоратор(*args, **kwargs)
        print("Служба завершена.")
        return результат
    return wrapper

# Условные конструкции
def если_воля_Божья(условие):
    if условие:
        print("Да будет воля Божья.")
        return True
    else:
        print("Иначе по воле Божьей.")
        return False

def иначе_если_воля_Божья(условие):
    return elif_wrapper(условие)

def иначе_по_воле_Божьей():
    return else_wrapper()

# Циклы
def всякий(коллекция, функция):
    for элемент in коллекция:
        функция(элемент)

def доколе(условие_func, действие):
    while условие_func():
        действие()

# Обработка исключений
class ГреховоеИсключение(Exception):
    pass

def пытаться(блок):
    try:
        блок()
    except Exception as e:
        print(f"Греховое исключение: {e}")
        raise ГреховоеИсключение(e)

def ловить(исключение, обработчик):
    return except_wrapper(исключение, обработчик)

# Классы
class Класс:
    def __init__(self, имя, базовый=None):
        self.имя = имя
        self.базовый = базовый
        self.методы = {}

    def добавить_метод(self, имя, функция):
        self.методы[имя] = функция

    def создать_объект(self, *args, **kwargs):
        объект = Объект(self, *args, **kwargs)
        return объект

class Объект:
    def __init__(self, класс_, *args, **kwargs):
        self.класс_ = класс_
        for имя, значение in kwargs.items():
            setattr(self, имя, значение)
    
    def вызвать_метод(self, имя, *args, **kwargs):
        метод = self.класс_.методы.get(имя)
        if метод:
            return метод(self, *args, **kwargs)
        else:
            print(f"Метод {имя} не найден в классе {self.класс_.имя}")

# Модули и пакеты
def импортировать(модуль):
    import importlib
    return importlib.import_module(модуль)

# Вспомогательные функции
def печать(*args, **kwargs):
    print(*args, **kwargs)

# Пример использования ключевых слов elif и else
def elif_wrapper(условие):
    return lambda: условие

def else_wrapper():
    return lambda: None
