import tkinter as tk
from tkinter import filedialog
import json
import os


def choose_txt_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    return file_path


def convert_txt_to_json(txt_file_path):
    with open(txt_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    if len(lines) < 3:
        raise ValueError("The file does not contain enough lines to process.")

    # Extract metadata from the first line
    metadata_line = lines[0].strip()
    metadata_parts = metadata_line.split(',')
    metadata = {
        "description": metadata_parts[0].strip(),
        "creation_date": metadata_parts[1].strip().split(': ')[1]
    }

    # Extract column headers from the second line
    headers = lines[1].strip().split(';')

    # Process the data rows
    data = []
    for line in lines[2:]:
        values = line.strip().split(';')
        row_dict = {headers[i]: float(values[i]) if i > 1 else values[i] for i in range(len(headers))}
        data.append(row_dict)

    # Create the JSON structure
    json_structure = {
        "metadata": metadata,
        "data": data
    }

    json_file_path = os.path.splitext(txt_file_path)[0] + ".json"

    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(json_structure, json_file, ensure_ascii=False, indent=4)

    print(f"Datei {json_file_path} erfolgreich erstellt!")


def main():
    print("Bitte wählen Sie eine .txt Datei aus:")
    txt_file_path = choose_txt_file()

    if txt_file_path:
        print(f"Ausgewählte Datei: {txt_file_path}")
        convert_txt_to_json(txt_file_path)
    else:
        print("Keine Datei ausgewählt. Programm wird beendet.")

if __name__ == "__main__":
    main()
