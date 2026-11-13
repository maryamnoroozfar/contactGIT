import csv 
import os 
import uuid
import ctypes

def get_user(*headers):
    user = dict()
    for header in headers:
        if header == "id":
            user[header] = str(uuid.uuid4())
        else:
            user[header] = input("enter" + header.title() + ":")
    return user


def save_user(file_path : str, user: dict):
    with open(file_path, "a", encoding="utf-8")as file:
        writer = csv.DictWriter(file, user.keys())
        writer.writerow(user)


def file_opener(path, flags):
    fd = os.open(path, flags, mode = 0o600)
    return fd


def creat_file(file_name: str, headers: list):
        try:
            if file_name.endswith(".csv"):
                new_name = file_name + ".csv"
                os.rename(file_name, new_name)
                file_name = new_name
        except FileExistsError as error:
            with open(file_name, "w", opener = file_opener)as file:
                writer = csv.writer(file)
                writer.writerow(headers)


def search_user(file_path: str,enter_user: str):
    if not os.path.exists(file_path):
        print("FILE NOT EXISTS")
        return
    else:
        with open(file_path, "r")as file:
            headers = file.readline()
        while True:
            user_tell = file.tell()
            user_line = file.readline()
            line_list = list(user_line.split(","))
            if enter_user.lower() in user_line.lower():
                print(f"{repr(user_line)} and tell is {user_tell}")
                print(ctypes.c_long.from_address(id(line_list)).value)
                print(id(line_list))
                print(hex(id(line_list)))


def main():
    headers = ["id", "name", "email", "phone"]
    file_path = "contact.csv"
    enter_user = input("ENTER UR CHAR")
    while True:
        if os.path.exists(file_path):
            user = get_user(*headers)
            save_user(user)
            search_user(file_path, enter_user)
        else:
            creat_file(file_path, headers)
        next_turn = input("do u want continu?").lower()
        if next_turn != "yes":
            break


if __name__ == "__main__":
    main()
