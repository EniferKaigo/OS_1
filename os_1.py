import os
import psutil
import time
import json
import xml.etree.ElementTree as elementTree
import zipfile as zf


def disks_info():
    d = psutil.disk_partitions()
    print('Информация о диске C:', d[0])
    print('Информация о диске D:', d[1])
    print('Получить поле диска:', d[0][0], d[1][0])
    print('Тип данных:', type(d), '\n')

    p = psutil.disk_usage(d[0][0])  # C диск
    print('Процент использования диска C: ', p)
    p = psutil.disk_usage(d[1][0])  # D disk
    print("D процент использования диска:", p)
    print('Тип данных»', type(p))


class Employee:
    def __init__(self, post: str, name: str, age: int, sex: str):
        self.post = post
        self.name = name
        self.age = age
        self.sex = sex

    def toJson(self):
        return {
            self.post: {
                "name": self.name,
                "age": self.age,
                "sex": self.sex
            }
        }

    def toXmlSet(self):
        return {
            "name": self.name,
            "age": str(self.age),
            "sex": self.sex
        }


class File:
    def __init__(self, filename: str):
        self.filename = filename
        if filename == "":
            self.filename = input("Введи имя нового файла\n") + ".txt"
            f = open(self.filename, "w")
            print("Файл", filename, "успешно создан")
            f.close()

    def write(self, text: str):
        with open(self.filename, "w") as file:
            file.write(text)
            print("Данные записаны")
            file.close()

    def printAll(self):
        with open(self.filename, "r") as file:
            print("Содержимое файла " + self.filename + ":")
            for line in file:
                print(line)
            file.close()

    def delete(self):
        os.remove(self.filename)
        print("Файл " + self.filename + " удалён")


class Json:
    def __init__(self):
        self.filename = "employees.json"

    def write(self, employee: Employee):
        with open(self.filename, "w") as file:
            json.dump(employee.toJson(), file)
            file.close()

    def printAll(self):
        with open(self.filename, "r") as file:
            data: dict = json.load(file)

            print("post:", list(data.keys())[0])
            for i in data.values():
                print("name:", i["name"])
                print("age:", i["age"])
                print("sex:", i["sex"])

    def delete(self):
        os.remove(self.filename)
        print("Файл " + self.filename + " удалён")


class Xml:
    def __init__(self):
        self.filename = "employees.xml"

    def write(self, employee: Employee):
        root = elementTree.Element("Employees")
        elementTree.SubElement(root, employee.post.capitalize(), employee.toXmlSet())
        elementTree.ElementTree(root).write(self.filename)

    def printAll(self):
        tree = elementTree.parse(self.filename)
        root = tree.getroot()

        for child in root:
            print(child.tag, child.attrib)

    def delete(self):
        os.remove(self.filename)
        print("Файл " + self.filename + " удалён")


# disks_info()

print("Создание файла:")
file = File("")

print("Добавление записей в файл")
file.write(input("Введи текст для записи в файл\n"))

time.sleep(2)
print('Вывод содержимого файла на экран')
file.printAll()

# print("\n\nРабота с JSON")
# j = Json()

# post = input("Введи должность сотрудника\n")
# name = input("Введи имя сотрудника\n")
# age = int(input("Введи возраст сотрудника\n"))
# sex = input("Введи пол сотрудника\n")
#
# emp = Employee(post, name, age, sex)
# j.write(emp)
time.sleep(2)

# print("Данные файла json:")
# j.printAll()

time.sleep(2)
# print("Удаление файла")
# j.delete()
# print("Создание файла xml")
# xml = Xml()
#
# print("Запись в xml")
# xml.write(emp)
# print("Данные записаны в xml")
#
# time.sleep(2)
# print("Вывод информации xml")
# xml.printAll()

time.sleep(2)
# xml.delete()

filename = input("Введи имя файла\n")
z = zf.ZipFile(filename + ".zip", "w")
z.write(filename)
z.close()

z1 = zf.ZipFile("test.zip", "r")
z1.printdir()
z1.close()

time.sleep(2)
print("Удаление файла")
file.delete()
