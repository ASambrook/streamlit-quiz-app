import csv

CSV_FILE = "results.csv"

def save_result(name: str, score: int) -> None:
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, score])


def load_results() -> list:
    results = []
    try:
        with open(CSV_FILE, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                results.append(row)
    except FileNotFoundError:
        pass  
    return results


