import json

with open("json_example.json") as j:
    data = json.load(j)

    for i in data.keys():
        print(i, data[i])


if __name__ == "__main__":
    print("PyCharm")