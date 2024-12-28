import csv


def read_file(filename):
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]
            return data

    except FileNotFoundError:
        print(f"File {filename} does not exist")

    except Exception as e:
        print(f"Error: {e}")


def is_num(value):
    try:
        float(value)
        return True

    except ValueError:
        return False

    except Exception as e:
        print(f"Error: {e}")


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

    except Exception as e:
        print(f"Error: {e}")


def write_file(filename, data):
    try:
        with open(filename, "w", newline="") as f:
            headers = list(data[0].keys())
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writerows(data)
    except Exception as e:
        print(f"Error: {e}")


def main():
    input_file = "data.csv"
    output_file = "output_data.csv"

    data = read_file(input_file)

    if not data:
        print("File is empty or its content is not valid csv")
        return

    processed_data = process_data(data)

    if not processed_data:
        print("No data to process")
        return

    write_file(output_file, processed_data)
    print(f"Processed data saved to {output_file}")


if __name__ == "__main__":
    main()
