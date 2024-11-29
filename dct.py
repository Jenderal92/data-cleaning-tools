# -*- coding: utf-8 -*-
import csv
import re

def print_banner():
    banner = """
    ###############################################
    #          DATA CLEANING TOOLS                #
    #            Created by Python 2.7            #
    ###############################################
    """
    print(banner)
    
def read_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

def write_csv(file_path, data):
    with open(file_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def remove_empty_rows(data):
    cleaned_data = [row for row in data if all(row)]
    return cleaned_data

def remove_duplicates(data):
    seen = set()
    cleaned_data = []
    for row in data:
        row_tuple = tuple(row)
        if row_tuple not in seen:
            seen.add(row_tuple)
            cleaned_data.append(row)
    return cleaned_data

def normalize_text(data):
    cleaned_data = []
    for row in data:
        cleaned_row = [re.sub(r'[^a-zA-Z0-9\s]', '', cell).strip().lower() for cell in row]
        cleaned_data.append(cleaned_row)
    return cleaned_data

def clean_dataset(input_file, output_file):
    print("• Membaca dataset...")
    data = read_csv(input_file)

    print("• Menghapus baris kosong...")
    data = remove_empty_rows(data)

    print("• Menghapus baris duplikat...")
    data = remove_duplicates(data)

    print("• Normalisasi teks...")
    data = normalize_text(data)

    print("• Menulis dataset bersih ke file...")
    write_csv(output_file, data)
    print("\nProses selesai! Dataset bersih telah disimpan di: {}".format(output_file))

if __name__ == "__main__":
    print_banner()
    input_file = raw_input("Masukkan nama file dataset mentah (misal: tes.csv): ")
    output_file = raw_input("Masukkan nama file untuk hasil dataset bersih (misal: done.csv): ")
    try:
        clean_dataset(input_file, output_file)
    except Exception as e:
        print("\nTerjadi kesalahan: {}".format(str(e)))
