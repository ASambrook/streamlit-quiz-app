import csv

CSV_FILE = "results.csv"

def save_result(name: str, score: int) -> None:
    """
    The function saves a user's name and final socre to `results.csv`.
    `mode="a" allows new data to be added to the csv file instead of overwrting the current data.
    """
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, score])


def load_results() -> list:
    """
    This function loads all the previous user names and scores .
    `mode="r"` allows these results to be read line by line in a list.
    A `try` and `except` is used with the intention to saved the results into a list of rows, yet the `Except` block prevents the web application from crashing if the CSV file cannot be found.
    """
    results = []
    try:
        with open(CSV_FILE, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                results.append(row)
    except FileNotFoundError:
        pass  
    return results


