# TODO решите задачу
import json
input1 = "input.json"
def task() -> float:
    with open(input1, encoding='utf-8') as f:
        x = json.load(f)
        t =[i["score"] for i in x]
        t1 = [i["weight"] for i in x]
        t2 = [t[i]*t1[i] for i in range(len(t))]

    return round(sum(t2), 3)



print(task())
