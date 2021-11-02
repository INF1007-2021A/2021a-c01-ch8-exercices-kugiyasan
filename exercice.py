#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}



def exercice1(filename1: str, filename2: str) -> None:
    i = 1
    with open(filename1) as f1:
        with open(filenane2) as f2:
            for line1 in f1.readlines():
                line2 = f2.readline()
                if line1 != line2:
                    raise ValueError(f"Line {i} differs")
                i += 1


def exercice2(source: str, dest: str) -> None:
    with open(source) as f1:
        with open(dest, "w") as f2:
            f2.write(f1.readlines().replace(" ", "   "))


def main() -> None:
    f1 = "exemple.txt"
    f2 = "notes.txt"
    f3 = "dest.txt"
    exercice1(f1, f2)
    exercice2(f1, f3)


if __name__ == '__main__':
    main()
