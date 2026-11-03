def write_notes(filename):
    lines = []
    for _ in range(3):
        lines.append(input("Строка: ") )

    with open(filename, "a", encoding="utf-8") as f:
        f.writelines(lines)


def read_notes(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def main():
    write_notes("notes.txt")
    print(read_notes("notes.txt"))


if __name__ == "__main__":
    main()