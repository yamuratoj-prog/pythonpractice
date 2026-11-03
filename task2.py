def ask_int(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Please enter an integer.")


def main():
    print(ask_int("Enter a number: "))

if __name__ == "__main__":
    main()