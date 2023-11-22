import timeit


def yaml2json(input_file, output_file):
    with open(input_file, 'r', encoding='utf8') as in_file:
        data = in_file.readlines()
        numb_lines = len(data)

    out_file = open(output_file, 'w', encoding='utf8')
    out_file.write("{\n")

    lst = ["Пятница:\n", " Расписание:\n", "  Пара1:\n", "  Пара2:\n"]

    for i in range(0, numb_lines):
        if data[i] in ["Пятница:\n"]:
            if data[0] == data[i]:
                sup_string = data[i].lstrip().split(':', maxsplit=1)
                out_file.write('"' + sup_string[0] + '":' + sup_string[1])
            else:
                sup_string = data[i].lstrip().split(':', maxsplit=1)
                out_file.write(' }\n }\n\n"' + sup_string[0] + '":' + sup_string[1])

        elif data[i] in [" Расписание:\n"]:
            sup_string = data[i].lstrip().split(':', maxsplit=1)
            out_file.write('\t{\n')
            out_file.write('\t"' + sup_string[0] + '":' + sup_string[1])
            out_file.write('\t\t{\n')

        elif data[i] in ["  Пара1:\n", "  Пара2:\n"]:
            sup_string = data[i].lstrip().split(':', maxsplit=1)
            out_file.write('\t\t"' + sup_string[0] + '":' + sup_string[1])
            out_file.write('\t\t\t{\n')

        else:
            if i + 1 == numb_lines:
                sup_string = data[i].lstrip().split(':', maxsplit=1)
                a = sup_string[1].split("\n")
                out_file.write('\t\t\t\t"' + sup_string[0] + '":' + a[0].lstrip() + "\n")
            elif i + 1 != numb_lines and (data[i + 1] in lst):
                sup_string = data[i].lstrip().split(':', maxsplit=1)
                a = sup_string[1].split("\n")
                out_file.write('\t\t\t\t"' + sup_string[0] + '":' + a[0].lstrip() + "\n")
            else:
                sup_string = data[i].lstrip().split(':', maxsplit=1)
                a = sup_string[1].split("\n")
                out_file.write('\t\t\t\t"' + sup_string[0] + '":' + a[0].lstrip() + ",\n")
            if i + 1 != numb_lines and data[i + 1] in lst:
                out_file.write('\t\t\t},\n')

    out_file.write("\t\t\t}\n\t\t}\n\t}\n}"'\n')
    out_file.close()


YAML_IN = r"data\yaml_in.yaml"
JSON_OUT = r"data\json_out.json"


print("Время стократного выполнения, используя собственный парсер ", timeit.timeit(lambda: yaml2json(YAML_IN, JSON_OUT), number=100))
