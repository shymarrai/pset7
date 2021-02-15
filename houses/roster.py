import sys
import cs50

db = cs50.SQL("sqlite:///students.db")


def main():

    house = verify_args()
    read_database(house)


def verify_args():
    if len(sys.argv) != 2:  # check for entreance of datas
        print("Usage: python roster.py house")
        sys.exit(1)
    return sys.argv[1]


def read_database(house):

    data = db.execute("SELECT * FROM students WHERE house = ? ORDER BY last, first", house)

    for student in data:

        if student['middle'] == None:
            print(f"{student['first']} {student['last']}, born {student['birth']}")
        else:
            print(f"{student['first']} {student['middle']} {student['last']}, born {student['birth']}")


main()