import csv

def read_csv(file_path):
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return [row for row in reader]
    except FileNotFoundError:
        return []

def filter_by_column(data, column, value):
    return [row for row in data if row.get(column) == value]