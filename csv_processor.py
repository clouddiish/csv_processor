import csv


def read_file(filename):
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]
            return data
    except FileNotFoundError:
        print(f"File {filename} does not exist")


def main():
    data = read_file("data.csv")
    if data:
        for elem in data:
            print(elem)
    else:
        print("File is empty or its content is not valid csv")


if __name__ == "__main__":
    main()
