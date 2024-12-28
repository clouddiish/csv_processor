import csv


def read_file(filename):
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
        return data


def main():
    data = read_file("data.csv")
    for elem in data:
        print(elem)


if __name__ == "__main__":
    main()
