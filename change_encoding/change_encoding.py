#!/usr/bin/env python3

import os
import sys

def convert_file_encoding(input_file, output_file, from_encoding, to_encoding):
    try:
        # Read the file with the specified source encoding
        with open(input_file, 'r', encoding=from_encoding) as infile:
            content = infile.read()
        
        # Write the file with the specified target encoding
        with open(output_file, 'w', encoding=to_encoding) as outfile:
            outfile.write(content)
        
        print(f"Converted: {input_file} -> {output_file} ({from_encoding} -> {to_encoding})")
    except Exception as e:
        print(f"Error processing {input_file}: {e}")

def process_folder(folder_path, from_encoding, to_encoding):
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory.")
        return
    
    output_folder = os.path.join(folder_path, to_encoding)
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.srt'):
            input_file = os.path.join(folder_path, file_name)
            output_file = os.path.join(output_folder, file_name)
            convert_file_encoding(input_file, output_file, from_encoding, to_encoding)

    print(f"All files processed. Converted files are saved in {output_folder}")

def main():
    if len(sys.argv) < 2:
        print("Usage: chenc <folder_path> [from_encoding] [to_encoding]")
        sys.exit(1)

    folder_path = sys.argv[1]
    from_encoding = sys.argv[2] if len(sys.argv) > 2 else "windows-1250"
    to_encoding = sys.argv[3] if len(sys.argv) > 3 else "utf-8"

    process_folder(folder_path, from_encoding, to_encoding)

if __name__ == "__main__":
    main()

