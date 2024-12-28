import csv


def read_file(filename):
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]
            return data
    except FileNotFoundError:
        print(f"File {filename} does not exist")


def is_num(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def process_data(dict):
    try:
        filtered = [row for row in dict if is_num(row["Age"]) and is_num(row["Salary"])]

        processed = [
            {
                **row,
                "Name": row["Name"].upper(),
                "Salary": round(float(row["Salary"]), 2),
                "Tax": round(0.1 * float(row["Salary"]), 2),
            }
            for row in filtered
        ]

        return processed

    except KeyError:
        print("Missing required column in csv file")

    except TypeError:
        print("Provided data must be a dictionary")


def main():
    data = read_file("data.csv")
    if data:
        print(process_data(data))

    else:
        print("File is empty or its content is not valid csv")


if __name__ == "__main__":
    main()
