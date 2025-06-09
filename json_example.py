import json
def save_user (data, file_path):
    try:
        with open (file_path, 'w') as f:
            json.dump (data, f, indent=4)
            return True
    except Exception as e:
        print (f"Error saving: {e}")
        return False
def load_user(file_path):
    try:
        with open (file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print ("File not found!")
        return None
    except json.JSONDecodeError:
        print("Invalid JSON format!")
        return None
user = {"name": "Alice", "age": 25, "scores": [85, 90]}
if save_user (user, 'user.json'):
    print("User saved!")
loaded_user = load_user('wrong.json')
if loaded_user:
    print ("Loaded user:", loaded_user)