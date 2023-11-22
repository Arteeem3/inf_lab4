import timeit
import json
from typing import Any

def parse_yaml_value(value: str) -> Any:
    """ Вспомогательная функция для конвертации YAML строки в python data types"""
    value = value.strip()
    if not value:
        return None

    try:
        if '.' in value:
            return float(value)
        elif value.isdigit() or (value[1:].isdigit() and value[0] in '+-'):
            return int(value)
        elif value.lower() == 'true':
            return True
        elif value.lower() == 'false':
            return False
        elif value.lower() in ['null', '~']:
            return None
    except ValueError:
        pass

    return value

def parse_yaml(data: str) -> Any:
    """ Парсит YAML и возвращает dict """
    obj = {}
    if type(data) is str:
        lines = data.splitlines()
    else:
        lines = data
    if not lines:
        return obj
    for i, line in enumerate(lines):
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            if value.strip() == '':
                j = i + 1
                sublines = []
                while j < len(lines) and lines[j].startswith('  '):
                    sublines.append(lines[j].strip())
                    j += 1
                if sublines and sublines[0].startswith('- '):
                    obj[key] = [parse_yaml([item[2:]]) for item in sublines if item.startswith('- ')]
                else:
                    obj[key] = parse_yaml(sublines)
            else:
                obj[key] = parse_yaml_value(value)
    return obj


def to_json(value):
    if isinstance(value, dict):
        json_string = "{"
        json_string += ", ".join(
            f'"{key}": {to_json(val)}' for key, val in value.items()
        )
        json_string += "}"
        return json_string
    elif isinstance(value, list):
        json_string = "["
        json_string += ", ".join(to_json(item) for item in value)
        json_string += "]"
        return json_string
    elif isinstance(value, str):
        return f'{value}'
    elif isinstance(value, bool):
        return "true" if value else "false"
    elif value is None:
        return "null"
    elif isinstance(value, (int, float)):
        return str(value)
    else:
        raise TypeError(f"Type {type(value)} not serializable")

def yaml2json_task3(file_in, OUT_FILE):
    with open(file_in, "r", encoding="utf-8") as f:
        line = f.read()
    data = parse_yaml(line)
    json = to_json(data)
    with open(OUT_FILE, "w") as f:
        f.write(json)


test1 = r"data\test1.yaml"
test2 = r"data\test2.yaml"
OUT_FILE = r"data\add_task3.json"



print("Время стократного выполнения доп. задания 3 (тест 1) ", timeit.timeit(lambda: yaml2json_task3(test1, OUT_FILE), number=100))
print("Время стократного выполнения доп. задания 3 (тест 2) ", timeit.timeit(lambda: yaml2json_task3(test2, OUT_FILE), number=100))
yaml2json_task3(test1, OUT_FILE)