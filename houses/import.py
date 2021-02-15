import csv
from sys import exit, argv
import cs50

db = cs50.SQL("sqlite:///students.db")


def main():

    file_csv = verify_args()
    read_csv(file_csv)


def verify_args():
    if len(argv) != 2:  # check for entreance of datas
        print("Usage: python import.py characters.csv")
        exit(1)
    return argv[1]


def read_csv(base):
    FIRST_NAME = "null"
    MIDDLE_NAME = "null"
    LAST_NAME = "null"
    with open(base, "r") as studens_line:

        reader = csv.DictReader(studens_line)
        for row in reader:

            name = row["name"].split(" ")
            house = row["house"]
            birth = row["birth"]
            length = len(name)

            FIRST_NAME = name[0]
            if length == 3:

                MIDDLE_NAME = name[1]
                LAST_NAME = name[2]

            else:
                MIDDLE_NAME = None
                LAST_NAME = name[1]

            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)",
                       FIRST_NAME, MIDDLE_NAME, LAST_NAME, house, birth)


main()
