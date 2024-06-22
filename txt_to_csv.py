import tkinter as tk
from tkinter import filedialog
import csv
import os
import pandas as pd


def choose_txt_file():
    # Erstelle ein unsichtbares Hauptfenster
    root = tk.Tk()
    root.withdraw()  # Verstecke das Hauptfenster

    # Öffne eine Datei-Auswahl-Dialogbox und filtere nach .txt Dateien
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    return file_path


def convert_txt_to_csv(txt_file_path):
    # Lies den Inhalt der .txt Datei
    with open(txt_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Erstelle den Pfad für die neue .csv Datei
    csv_file_path = os.path.splitext(txt_file_path)[0] + ".csv"

    # Schreibe die Daten in die .csv Datei
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)

        for line in lines:
            # Teile die Zeile an jedem ';' und entferne das Trennzeichen
            columns = line.strip().split(';')
            # Schreibe die gesplitteten Zeilen in die CSV Datei
            writer.writerow(columns)

    print(f"Datei {csv_file_path} erfolgreich erstellt!")


def main():
    print("Bitte wählen Sie eine .txt Datei aus:")
    txt_file_path = choose_txt_file()

    if txt_file_path:
        print(f"Ausgewählte Datei: {txt_file_path}")
        convert_txt_to_csv(txt_file_path)
    else:
        print("Keine Datei ausgewählt. Programm wird beendet.")


def load_csv(file_path):
    """Lädt eine CSV-Datei."""
    if not os.path.isfile(file_path):
        print(f"Datei {file_path} nicht gefunden.")
        return None
    try:
        df = pd.read_csv(file_path)
        print(f"\nCSV-Datei {file_path} erfolgreich geladen:")
        print(df.head())  # Zeigt die ersten paar Zeilen der CSV-Datei zur Kontrolle
        return df
    except Exception as e:
        print(f"Fehler beim Laden der Datei {file_path}: {e}")
        return None


def remove_sec(file_path, output_path):
    """Entfernt die zweite Spalte einer CSV-Datei und speichert das Ergebnis."""
    df = load_csv(file_path)
    if df is None:
        print("Das DataFrame konnte nicht geladen werden.")
        return

    if len(df.columns) < 2:
        print("Die CSV-Datei hat weniger als zwei Spalten. Es gibt keine zweite Spalte zu entfernen.")
        return

    # Entfernen der zweiten Spalte
    df = df.drop(df.columns[1], axis=1)
    print(f"Die zweite Spalte wurde entfernt. Hier sind die ersten paar Zeilen des aktualisierten DataFrames:")
    print(df.head())  # Zeigt die ersten paar Zeilen des modifizierten DataFrames

    # Speichern der aktualisierten CSV-Datei
    try:
        df.to_csv(output_path, index=False)
        print(f"Die modifizierte CSV-Datei wurde erfolgreich unter {output_path} gespeichert.")
    except Exception as e:
        print(f"Fehler beim Speichern der Datei {output_path}: {e}")

    # Spalten alphabetisch anordnen


def sortcsv():

    # Pfad zur Eingabedatei und zur Ausgabedatei
    input_file_path = 'sonnenschein_dauer.csv'  # Ersetze durch den tatsächlichen Pfad der Eingabedatei
    output_file_path = 'cleanSonnenscheinDauer.csv'  # Ersetze durch den gewünschten Pfad der Ausgabedatei


    # Spalten, die entfernt werden sollen (ersetze durch die gewünschten Spalten)
    columns_to_remove = ['Thueringen/Sachsen-Anhalt', 'Deutschland']

    # Spalte, die dupliziert und umbenannt werden soll
    column_to_duplicate = 'Hamburg'
    new_column_name = 'Bremen'

    # CSV-Datei einlesen
    df = pd.read_csv(input_file_path)

    # Ausgewählte Spalten entfernen
    df.drop(columns=columns_to_remove, inplace=True, errors='ignore')

    # Spalte duplizieren und umbenennen
    df[new_column_name] = df[column_to_duplicate]

    # Spalten alphabetisch sortieren
    #sorted_columns = sorted(df.columns)

    # DataFrame mit sortierten Spalten neu anordnen
   # sorted_df = df[sorted_columns]

    # Sortierte CSV-Datei speichern
    df.to_csv(output_file_path, index=False)

    print(f"Die CSV-Datei wurde erfolgreich unter '{output_file_path}' gespeichert.")


# csv neu anordnen
def reorganize_csv(file_path, output_path):
    # Einlesen der CSV-Datei
    df = pd.read_csv(file_path)

    # Alle Spalten außer "Jahr" alphabetisch sortieren
    cols = sorted([col for col in df.columns if col != 'Jahr'])

    # "Jahr" als erste Spalte setzen
    sorted_cols = ['Jahr'] + cols

    # DataFrame neu ordnen
    df = df[sorted_cols]

    # Speichern der reorganisierten CSV-Datei
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    reorganize_csv("cleanSonnenscheinDauer.csv", "cleanSonnenscheinDauer.csv")