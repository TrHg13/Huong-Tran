# week-10 -> file_properties.py

# This file prints information about a file
import os.path

def main():
    filename = "students.txt"
    abs_file_path = os.path.abspath(filename)  # returns absolute path for the given file
    dir_name = os.path.dirname(abs_file_path)  # returns directory given file is in

    print("Absolute Path:", abs_file_path)
    print("Directory:", dir_name)
    print("Base Name:", os.path.basename(abs_file_path))  # returns filename without directory in front of it
    print("File Size:", os.path.getsize(filename))  # returns the size of the given file in bytes
    print("Is A File?:", os.path.isfile(filename))  # returns 'True' if the given file exists
    print("Is A Directory?:", os.path.isdir(filename))  # returns 'True' if the given directory exists

if __name__ == '__main__':
    main()
