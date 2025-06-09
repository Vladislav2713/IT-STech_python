from csv_utils import read_csv, filter_by_column

data = read_csv('sample.csv')
if not data:
    print("File not found or empty!")
else:
    print("All data:", data)
    filtered = filter_by_column(data, 'category', 'A')
    print("Filtered data (category A):", filtered)