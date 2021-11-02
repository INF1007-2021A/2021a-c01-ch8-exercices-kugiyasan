#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}



def exercice1(filename1: str, filename2: str) -> None:
    with open(filename1) as f1:
        with open(filename2) as f2:
            for i, line1 in enumerate(f1.readlines()):
                line2 = f2.readline()
                if line1 != line2:
                    print(f"Line {i + 1} differs")

            if f2.readline():
                print("The second line has more lines")


def exercice2(source: str, dest: str) -> None:
    with open(source) as f1:
        with open(dest, "w") as f2:
            f2.write(f1.readlines().replace(" ", "   "))


def exercice3() -> None:
    filename = "notes.txt"
    dest = "notes2.txt"
    with open(filename) as f1:
        with open(dest) as f2:
            for line in f1.readlines():
                n = int(line)
                for k, v in PERCENTAGE_TO_LETTER.items():
                    if n in range(*v):
                        grade = k
                        break
                f2.write(f"{line} {grade}")


def exercice4():
    pass


def main() -> None:
    f1 = "exemple.txt"
    f2 = "notes.txt"
    f3 = "dest.txt"
    exercice1(f1, f2)
    exercice2(f1, f3)
    exercice3()
    exercice4()


if __name__ == '__main__':
    main()
