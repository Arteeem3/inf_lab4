import json
import timeit
import yaml

YAML_IN = r"data\yaml_in.yaml"
JSON_LIB = r"data\json_lib.json"


def yaml2json_libs(yaml_in, json_out):
    with open(YAML_IN, 'r', encoding='utf8') as yaml_in, open(JSON_LIB, "w") as json_out:
        yaml_object = yaml.safe_load(yaml_in)
        json.dump(yaml_object, json_out, ensure_ascii=False)

print("Время стократного выполнения с помощью библиотек ", timeit.timeit(lambda: yaml2json_libs(YAML_IN, JSON_LIB), number=100))
