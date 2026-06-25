import json

student = {
    "name": "Abin",
    "age": 24
}

with open("student.json", "w") as file:
    json.dump(student, file)

with open("student.json", "r") as file:
    data = json.load(file)

print(data)