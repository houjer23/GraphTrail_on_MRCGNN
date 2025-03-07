#!/usr/bin/env python3
import pickle
import sys

def load_pickle(file_path):
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
        return data
    except Exception as e:
        print(f"Error loading pickle file: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 load_pickle.py <path_to_pickle_file>")
        sys.exit(1)
    file_path = sys.argv[1]
    data = load_pickle(file_path)
    print("Data loaded from pickle file:")
    print(data)
