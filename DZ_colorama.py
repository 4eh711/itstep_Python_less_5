import colorama
import inspect

# Включаем поддержку ANSI-цветов в Windows
colorama.init()

# Пример функции с использованием colorama
def colored_print(text, color):
    colors = {
        'red': colorama.Fore.RED,
        'green': colorama.Fore.GREEN,
        'blue': colorama.Fore.BLUE,
        'yellow': colorama.Fore.YELLOW,
    }

    if color in colors:
        print(colors[color] + text + colorama.Style.RESET_ALL)
    else:
        print(text)

# Выводим список функций модуля colorama
print("Functions in colorama module:")
for name, obj in inspect.getmembers(colorama):
    if inspect.isfunction(obj):
        print(name)

# Используем функцию colored_print для вывода цветного текста
colored_print("This is red text", "red")
colored_print("This is green text", "green")
colored_print("This is blue text", "blue")
colored_print("This is yellow text", "yellow")

# Выводим список методов объекта Style из colorama
print("\nMethods in colorama.Style:")
style_methods = inspect.getmembers(colorama.Style, predicate=inspect.ismethod)
for name, _ in style_methods:
    print(name)

# Отключаем поддержку ANSI-цветов
colorama.deinit()