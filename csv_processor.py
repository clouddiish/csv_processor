import csv


def read_file(filename):
    """
    Reads a CSV file and returns its content as a list of dictionaries.

    Args:
        filename (str): The name of the CSV file to read.

    Returns:
        list[dict]: A list of dictionaries containing the rows of the CSV file.
        None: If the file is not found or an error occurs.

    Raises:
        FileNotFoundError: If the file does not exist.
        Exception: For any other unexpected errors.
    """
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
    """
    Checks if a given value is numeric (float or int).

    Args:
        value (str): The value to check.

    Returns:
        bool: True if the value is numeric, False otherwise.

    Raises:
        Exception: For any unexpected errors during validation.
    """
    try:
        float(value)
        return True

    except ValueError:
        return False

    except Exception as e:
        print(f"Error: {e}")


def process_data(dict):
    """
    Processes the input data by filtering rows with numeric values for 'Age'
    and 'Salary', converting 'Name' to uppercase, rounding 'Salary', and
    calculating 'Tax'.

    Args:
        dict (list[dict]): A list of dictionaries representing the data.

    Returns:
        list[dict]: A list of processed dictionaries with 'Name', 'Salary',
                    and 'Tax' columns modified or added.

    Raises:
        KeyError: If required columns ('Age', 'Salary', or 'Name') are missing.
        TypeError: If the input data is not a list of dictionaries.
        Exception: For any other unexpected errors.
    """
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
    """
    Writes processed data to a CSV file.

    Args:
        filename (str): The name of the output CSV file.
        data (list[dict]): The processed data to write, where each dictionary
                           represents a row.

    Raises:
        Exception: For any unexpected errors during file writing.
    """
    try:
        with open(filename, "w", newline="") as f:
            headers = list(data[0].keys())
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writerows(data)
    except Exception as e:
        print(f"Error: {e}")


def main():
    """
    Main function that orchestrates the reading, processing, and writing
    of CSV data.

    Reads data from a CSV file, processes the data, and writes the results
    to a new CSV file.

    Raises:
        Exception: For any unexpected errors during execution.
    """
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
