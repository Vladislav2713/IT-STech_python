def parse_logs(file_path):
    errors = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if "ERROR" in line.upper():
                    errors += 1
        return errors
    except FileNotFoundError:
        return -1

file_path = input("Enter log file path: ")
error_count = parse_logs(file_path)
if error_count == -1:
    print("File not found!")
else:
    print(f"Number of errors: {error_count}")