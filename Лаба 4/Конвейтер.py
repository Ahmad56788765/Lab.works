# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input1.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r") as f:
        with open(OUTPUT_FILENAME, "w") as f1:
            csvd = csv.DictReader(f, delimiter=',', quotechar='\n')
            s = [i for i in csvd]
            x = json.dump(s, f1, indent=4)
    return x





    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
