import json
input1 = "input.json"
def task() -> float:
    with open(input1, encoding='utf-8') as f:
        x = json.load(f)
        t =[i["score"]*i["weight"] for i in x]
    return round(sum(t), 3)



print(task())
