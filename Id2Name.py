from dataclasses import dataclass

@dataclass
class STUDENT:
    id: int
    name: str
    def __init__(self, id, name):
        self.id = id
        self.name = name 

stuList = []

# Đường dẫn đến file MSSV cần chuyển đổi
FILE = "input.csv"

def binarySearch(arr: list, target: int):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid].id == target:
            return arr[mid].name
        elif arr[mid].id < target:
            left = mid+1
        else:
            right = mid
    return -1

with open("dataK21.csv", mode = "r", newline = '', encoding = "utf-8") as f:
    f.readline()
    for line in f:
        data = line.strip().split("|")
        stuList.append(STUDENT(int(data[0]),data[2]))

def getName():
    with open(FILE, mode = "r", newline = '', encoding = "utf-8") as inf:
        with open("output.csv", mode = "w", newline = '', encoding = "utf-8") as outf:
            outf.write("MSSV,Họ tên\n")
            for line in inf:
                id = int(line)
                stuName = binarySearch(stuList, id)
                outf.write(f"{id},{stuName}\n")

getName()