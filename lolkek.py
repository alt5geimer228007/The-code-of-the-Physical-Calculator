# Продвинутый калькулятор - с выбором языка и дополнительными функциями
# Advanced Calculator - with language selection and extra functions

constants = {}

# Языковые настройки / Language settings
current_lang = None

# Режим дополнительных функций / Extra functions mode
extra_mode = False

# Русские тексты
ru = {
    'welcome': "\n" + "=" * 50 + "\n     ПРОДВИНУТЫЙ КАЛЬКУЛЯТОР\n" + "=" * 50,
    'lang_prompt': "\nВыберите язык / Select language:",
    'lang_ru': "   1 - Русский",
    'lang_en': "   2 - English",
    'lang_choice': ">>> ",
    'lang_error': "[ОШИБКА] Введите 1 или 2",
    'commands_title': "\nОСНОВНЫЕ КОМАНДЫ:",
    'cmd_add': "   add     - Добавить константу",
    'cmd_show': "   show    - Показать все константы",
    'cmd_delete': "   delete  - Удалить константу",
    'cmd_clear': "   clear   - Удалить ВСЕ константы",
    'cmd_extra': "   extra   - Дополнительные функции (%, !, ^, sqrt, sin, cos и т.д.)",
    'cmd_help': "   help    - Показать это меню",
    'cmd_exit': "   exit    - Выйти из калькулятора",
    'extra_title': "\nДОПОЛНИТЕЛЬНЫЕ ФУНКЦИИ (режим extra):",
    'extra_cmd': "   normal  - Вернуться в обычный режим",
    'extra_examples': "\nПРИМЕРЫ В РЕЖИМЕ EXTRA:",
    'ex_percent': "   50% of 100 - процент от числа (50% от 100 = 50)",
    'ex_factorial': "   5!      - факториал (5! = 120)",
    'ex_power': "   2^8     - степень (2^8 = 256)",
    'ex_sqrt': "   sqrt(16) - квадратный корень (sqrt(16) = 4)",
    'ex_sin': "   sin(90)  - синус в градусах (sin(90) = 1)",
    'ex_cos': "   cos(0)   - косинус в градусах (cos(0) = 1)",
    'ex_tan': "   tan(45)  - тангенс в градусах (tan(45) = 1)",
    'ex_log': "   log(100) - десятичный логарифм (log(100) = 2)",
    'ex_ln': "   ln(20)   - натуральный логарифм",
    'ex_abs': "   abs(-5)  - модуль числа (abs(-5) = 5)",
    'examples_title': "\nПРИМЕРЫ ОБЫЧНОЙ МАТЕМАТИКИ:",
    'ex_normal': "   25 + 75 * 2",
    'ex_const': "   С константами: сначала 'add', потом 'pi * 10'",
    'ex_multi': "   (100 + 50) / 3 ** 2",
    'separator': "\n" + "=" * 50 + "\n",
    'add_prompt': "Введите имя константы: ",
    'add_value': "Введите значение для '",
    'add_value_end': "': ",
    'add_ok': "[OK] Константа '{}' = {} добавлена",
    'add_error': "[ОШИБКА] Это не число",
    'no_constants': "[ИНФО] Нет констант. Используйте 'add' чтобы добавить.",
    'constants_header': "\n[КОНСТАНТЫ]",
    'total_constants': "  Всего: {} констант(а)\n",
    'nothing_to_delete': "[ИНФО] Нечего удалять. Сначала добавь константы.",
    'delete_prompt': "Введите имя константы для удаления: ",
    'delete_ok': "[OK] Константа '{}' удалена",
    'delete_error': "[ОШИБКА] Константа '{}' не найдена",
    'clear_ok': "[OK] Все константы удалены",
    'clear_empty': "[ИНФО] Нет констант для удаления",
    'goodbye': "\nДо свидания!",
    'extra_mode_on': "\n[РЕЖИМ EXTRA ВКЛЮЧЁН] Доступны: %, !, ^, sqrt(), sin(), cos(), tan(), log(), ln(), abs()",
    'normal_mode_on': "\n[ОБЫЧНЫЙ РЕЖИМ]",
    'help_menu': "\n" + "=" * 50 + "\nОСНОВНЫЕ КОМАНДЫ:\n   add     - Добавить константу\n   show    - Показать все константы\n   delete  - Удалить конкретную константу\n   clear   - Удалить ВСЕ константы\n   extra   - Включить дополнительные функции\n   help    - Показать это меню\n   exit    - Выйти из калькулятора\n\nПРИМЕРЫ МАТЕМАТИКИ:\n   15 + 30\n   100 - 45\n   12 * 8\n   144 / 12\n   2 ** 10 (возведение в степень)\n   (10 + 5) * 2\n   100 / 3\n\nПРИМЕР С КОНСТАНТАМИ:\n   add -> имя: pi -> значение: 3.14\n   потом пишем: pi * 10\n\nДОПОЛНИТЕЛЬНЫЕ ФУНКЦИИ (команда 'extra'):\n   50% of 100 (проценты)\n   5! (факториал)\n   2^8 (степень)\n   sqrt(16) (корень)\n   sin(90) (синус)\n   cos(0) (косинус)\n   tan(45) (тангенс)\n   log(100) (логарифм)\n   ln(20) (натуральный логарифм)\n   abs(-5) (модуль)\n" + "=" * 50 + "\n",
    'error_division': "[ОШИБКА] Деление на ноль",
    'error_unknown_const': "[ОШИБКА] Неизвестная константа. Используй 'show' чтобы увидеть доступные константы, потом 'add' чтобы добавить",
    'error_invalid': "[ОШИБКА] Неверное выражение. Напиши 'help' если застрял",
    'error_percent': "[ОШИБКА] Неправильный формат процентов. Используй: число% от число",
    'result_prefix': "= "
}

# English texts
en = {
    'welcome': "\n" + "=" * 50 + "\n     ADVANCED CALCULATOR\n" + "=" * 50,
    'lang_prompt': "\nSelect language:",
    'lang_ru': "   1 - Русский",
    'lang_en': "   2 - English",
    'lang_choice': ">>> ",
    'lang_error': "[ERROR] Enter 1 or 2",
    'commands_title': "\nMAIN COMMANDS:",
    'cmd_add': "   add     - Add constant",
    'cmd_show': "   show    - Show all constants",
    'cmd_delete': "   delete  - Delete constant",
    'cmd_clear': "   clear   - Delete ALL constants",
    'cmd_extra': "   extra   - Extra functions (%, !, ^, sqrt, sin, cos, etc.)",
    'cmd_help': "   help    - Show this menu",
    'cmd_exit': "   exit    - Exit calculator",
    'extra_title': "\nEXTRA FUNCTIONS (extra mode):",
    'extra_cmd': "   normal  - Return to normal mode",
    'extra_examples': "\nEXAMPLES IN EXTRA MODE:",
    'ex_percent': "   50% of 100 - percentage (50% of 100 = 50)",
    'ex_factorial': "   5!      - factorial (5! = 120)",
    'ex_power': "   2^8     - power (2^8 = 256)",
    'ex_sqrt': "   sqrt(16) - square root (sqrt(16) = 4)",
    'ex_sin': "   sin(90)  - sine in degrees (sin(90) = 1)",
    'ex_cos': "   cos(0)   - cosine in degrees (cos(0) = 1)",
    'ex_tan': "   tan(45)  - tangent in degrees (tan(45) = 1)",
    'ex_log': "   log(100) - base-10 logarithm (log(100) = 2)",
    'ex_ln': "   ln(20)   - natural logarithm",
    'ex_abs': "   abs(-5)  - absolute value (abs(-5) = 5)",
    'examples_title': "\nREGULAR MATH EXAMPLES:",
    'ex_normal': "   25 + 75 * 2",
    'ex_const': "   With constants: first 'add', then 'pi * 10'",
    'ex_multi': "   (100 + 50) / 3 ** 2",
    'separator': "\n" + "=" * 50 + "\n",
    'add_prompt': "Enter constant name: ",
    'add_value': "Enter value for '",
    'add_value_end': "': ",
    'add_ok': "[OK] Constant '{}' = {} added",
    'add_error': "[ERROR] That's not a number",
    'no_constants': "[INFO] No constants yet. Use 'add' to create one.",
    'constants_header': "\n[CONSTANTS]",
    'total_constants': "  Total: {} constant(s)\n",
    'nothing_to_delete': "[INFO] Nothing to delete. Add some constants first.",
    'delete_prompt': "Enter constant name to delete: ",
    'delete_ok': "[OK] Constant '{}' deleted",
    'delete_error': "[ERROR] Constant '{}' not found",
    'clear_ok': "[OK] All constants deleted",
    'clear_empty': "[INFO] No constants to delete",
    'goodbye': "\nGoodbye!",
    'extra_mode_on': "\n[EXTRA MODE ON] Available: %, !, ^, sqrt(), sin(), cos(), tan(), log(), ln(), abs()",
    'normal_mode_on': "\n[NORMAL MODE]",
    'help_menu': "\n" + "=" * 50 + "\nMAIN COMMANDS:\n   add     - Add constant\n   show    - Show all constants\n   delete  - Delete a specific constant\n   clear   - Delete ALL constants\n   extra   - Enable extra functions\n   help    - Show this menu\n   exit    - Exit calculator\n\nMATH EXAMPLES:\n   15 + 30\n   100 - 45\n   12 * 8\n   144 / 12\n   2 ** 10 (power)\n   (10 + 5) * 2\n   100 / 3\n\nEXAMPLE WITH CONSTANTS:\n   add -> name: pi -> value: 3.14\n   then type: pi * 10\n\nEXTRA FUNCTIONS (command 'extra'):\n   50% of 100 (percentage)\n   5! (factorial)\n   2^8 (power)\n   sqrt(16) (square root)\n   sin(90) (sine)\n   cos(0) (cosine)\n   tan(45) (tangent)\n   log(100) (logarithm)\n   ln(20) (natural log)\n   abs(-5) (absolute value)\n" + "=" * 50 + "\n",
    'error_division': "[ERROR] Division by zero",
    'error_unknown_const': "[ERROR] Unknown constant. Use 'show' to see available constants, then 'add' to create one",
    'error_invalid': "[ERROR] Invalid expression. Type 'help' if you're stuck",
    'error_percent': "[ERROR] Invalid percentage format. Use: number% of number",
    'result_prefix': "= "
}


def factorial(n):
    """Вычисление факториала / Calculate factorial"""
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, int(n) + 1):
        result *= i
    return result


def calculate_extra(expression):
    """Вычисление выражений с дополнительными функциями / Calculate expressions with extra functions"""
    import math
    import re

    try:
        expr = expression.strip()

        # Обработка процентов / Handle percentages (например: 50% of 100)
        if '%' in expr and ' of ' in expr:
            parts = expr.split(' of ')
            if len(parts) == 2:
                percent_part = parts[0].strip()
                if percent_part.endswith('%'):
                    percent = float(percent_part[:-1])
                    number = float(parts[1].strip())
                    result = (percent / 100) * number
                    # Возвращаем как есть, без округления
                    return result

        # Обработка факториала / Handle factorial
        if '!' in expr and expr.count('!') == 1:
            num = float(expr.replace('!', '').strip())
            if num == int(num):
                return factorial(int(num))
            else:
                return None

        # Обработка степени через ^ / Handle power with ^
        if '^' in expr and 'sqrt' not in expr and 'log' not in expr:
            parts = expr.split('^')
            if len(parts) == 2:
                base = float(parts[0].strip())
                exponent = float(parts[1].strip())
                return base ** exponent

        # Функция для конвертации градусов в радианы
        def deg_to_rad(match):
            func = match.group(1)
            value = float(match.group(2))
            rad_value = math.radians(value)
            return f"math.{func}({rad_value})"

        # Заменяем sin(градусы), cos(градусы), tan(градусы)
        expr = re.sub(r'(sin|cos|tan)\(([^)]+)\)', deg_to_rad, expr)

        expr = expr.replace('sqrt', 'math.sqrt')
        expr = expr.replace('log', 'math.log10')
        expr = expr.replace('ln', 'math.log')
        expr = expr.replace('abs', 'abs')

        # Вычисляем / Evaluate
        allowed_globals = {
            '__builtins__': None,
            'math': math,
            'abs': abs,
            'round': round,
            'pow': pow
        }

        result = eval(expr, allowed_globals, {})

        return result

    except ZeroDivisionError:
        return "division_by_zero"
    except Exception:
        return None


def calculate_standard(expression):
    """Вычисление стандартных выражений / Calculate standard expressions"""
    try:
        expr = expression

        # Заменяем константы / Replace constants
        for const_name, const_value in constants.items():
            import re
            pattern = r'\b' + re.escape(const_name) + r'\b'
            expr = re.sub(pattern, str(const_value), expr)

        # Вычисляем / Evaluate
        allowed_globals = {
            '__builtins__': None,
            'abs': abs,
            'round': round,
            'pow': pow
        }

        result = eval(expr, allowed_globals, {})

        # Форматируем результат красиво / Format result nicely
        if isinstance(result, float):
            return format_result(result)
        else:
            return str(result)

    except ZeroDivisionError:
        return "division_by_zero"
    except NameError:
        return "unknown_constant"
    except Exception:
        return None


def add_constant():
    """Добавить свою константу / Add your own constant"""
    global current_lang
    texts = ru if current_lang == 'ru' else en

    name = input(texts['add_prompt']).strip().lower()
    try:
        value = float(input(f"{texts['add_value']}{name}{texts['add_value_end']}"))
        constants[name] = value
        print(texts['add_ok'].format(name, value))
    except ValueError:
        print(texts['add_error'])


def show_constants():
    """Показать все сохранённые константы / Show all saved constants"""
    global current_lang
    texts = ru if current_lang == 'ru' else en

    if not constants:
        print(texts['no_constants'])
    else:
        print(texts['constants_header'])
        for name, value in constants.items():
            if value == int(value):
                print(f"  {name} = {int(value)}")
            else:
                print(f"  {name} = {value}")
        print(texts['total_constants'].format(len(constants)))


def delete_constant():
    """Удалить константу / Delete constant"""
    global current_lang
    texts = ru if current_lang == 'ru' else en

    if not constants:
        print(texts['nothing_to_delete'])
        return

    show_constants()
    name = input(texts['delete_prompt']).strip().lower()
    if name in constants:
        del constants[name]
        print(texts['delete_ok'].format(name))
    else:
        print(texts['delete_error'].format(name))


def format_result(value):
    """Форматирует результат, убирая мусор плавающей точки / Format result to avoid floating point garbage"""
    if abs(value - round(value)) < 0.0000000001:
        return str(int(round(value)))

    rounded = round(value, 10)
    str_value = str(rounded)
    if '.' in str_value:
        str_value = str_value.rstrip('0').rstrip('.')

    return str_value


def calculator():
    global current_lang, extra_mode

    # Выбор языка / Language selection
    print("\n" + "=" * 50)
    print("     CALCULATOR / КАЛЬКУЛЯТОР")
    print("=" * 50)
    print(ru['lang_prompt'] + " / " + en['lang_prompt'])
    print(ru['lang_ru'])
    print(ru['lang_en'])

    while True:
        choice = input(ru['lang_choice']).strip()
        if choice == '1':
            current_lang = 'ru'
            break
        elif choice == '2':
            current_lang = 'en'
            break
        else:
            print(ru['lang_error'] + " / " + en['lang_error'])

    texts = ru if current_lang == 'ru' else en

    # Основное меню / Main menu
    print(texts['welcome'])
    print(texts['commands_title'])
    print(texts['cmd_add'])
    print(texts['cmd_show'])
    print(texts['cmd_delete'])
    print(texts['cmd_clear'])
    print(texts['cmd_extra'])
    print(texts['cmd_help'])
    print(texts['cmd_exit'])
    print(texts['examples_title'])
    print(texts['ex_normal'])
    print(texts['ex_const'])
    print(texts['ex_multi'])
    print(texts['separator'])

    while True:
        if extra_mode:
            prompt = "[extra] >>> "
        else:
            prompt = ">>> "

        user_input = input(prompt).strip().lower()

        if user_input == 'exit':
            print(texts['goodbye'])
            break

        elif user_input == 'help':
            print(texts['help_menu'])

        elif user_input == 'add':
            add_constant()

        elif user_input == 'show':
            show_constants()

        elif user_input == 'delete':
            delete_constant()

        elif user_input == 'clear':
            if constants:
                constants.clear()
                print(texts['clear_ok'])
            else:
                print(texts['clear_empty'])

        elif user_input == 'extra':
            if not extra_mode:
                extra_mode = True
                print(texts['extra_mode_on'])
            else:
                print("[INFO] " + (
                    "Уже в режиме extra. Используй 'normal' чтобы выйти." if current_lang == 'ru' else "Already in extra mode. Use 'normal' to exit."))

        elif user_input == 'normal':
            if extra_mode:
                extra_mode = False
                print(texts['normal_mode_on'])
            else:
                print("[INFO] " + ("Уже в обычном режиме." if current_lang == 'ru' else "Already in normal mode."))

        elif user_input == '':
            continue

        else:
            if extra_mode:
                # Режим с дополнительными функциями / Extra functions mode
                result = calculate_extra(user_input)

                if result == "division_by_zero":
                    print(texts['error_division'])
                elif result is not None:
                    # Форматируем результат
                    if isinstance(result, float):
                        formatted = format_result(result)
                        print(f"{texts['result_prefix']}{formatted}")
                    else:
                        print(f"{texts['result_prefix']}{result}")
                else:
                    # Пробуем как обычное выражение
                    std_result = calculate_standard(user_input)
                    if std_result == "division_by_zero":
                        print(texts['error_division'])
                    elif std_result == "unknown_constant":
                        print(texts['error_unknown_const'])
                    elif std_result is not None:
                        print(f"{texts['result_prefix']}{std_result}")
                    else:
                        print(texts['error_invalid'])
            else:
                # Обычный режим / Normal mode
                result = calculate_standard(user_input)

                if result == "division_by_zero":
                    print(texts['error_division'])
                elif result == "unknown_constant":
                    print(texts['error_unknown_const'])
                elif result is not None:
                    print(f"{texts['result_prefix']}{result}")
                else:
                    print(texts['error_invalid'])


if __name__ == "__main__":
    calculator()