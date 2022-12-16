# Author: philip0000000
# Simple python 3 script to displays statistics about files and amount of lines
# contained in files for various programing languages in working folder and subfolders.
import os

# Programing language and file type associated with it
prog_files = {
               "Batch file": [".bat", ".cmd", "btm"],
               "C": [".c", ".h"],
               "C#": [".cs"],
               "C++": [".cpp", ".hpp"],
               "CUDA": [".cu"],
               "Go": [".go"],
               "Haskell": [".hs"],
               "HTML": [".html", ".htm"],
               "Java": [".java"],
               "JavaScript": [".js"],
               "JSON": [".json"],
               "Julia": [".jl"],
               "Kotlin": [".kt"],
               "Lua": [".lua"],
               "PHP": [".php"],
               "Perl": [".pl", ".pm"],
               "Python": [".py", ".pyw"],
               "R": [".R"],
               "Ruby": [".rb"],
               "Rust": [".rs"],
               "Scala": [".scala"],
               "Shell": [".sh"],
               "Swift": [".swift"],
               "Text": [".txt"],
               "TypeScript": [".ts"],
               "XML": [".xml"]
            }
other_files = {
               "BMP": [".bmp"],
               "GIF": [".gif"],
               "JPEG": [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi"],
               "PNG": [".png"],
               "WebP": [".webp"],
               "ZIP": [".zip"]
}

# Dictionary to store language statistics
files_found = {}

# Get the path of the current working directory
directory = os.getcwd()

# Check if the extension is a programming language we want to track
def get_number_of_lines_in_file(file):
    # Open the file in reading mode
    try:
        with open(file, "r", encoding="utf-8") as f:
            # Initialize the count to 0
            count = 0
            # Iterate over the lines of the file
            for line in f:
                # Increment the count for each line
                count += 1
            return count
    except Exception as e:
        return 0

def is_filename_extension_a_prog_file(filename_extension):
    for key, value in prog_files.items():
        if filename_extension in value:
            return True
    return False

# Use os.walk() to traverse the directory tree and collect all filenames
total_files = 0
for root, dirs, files in os.walk(directory):
    for file in files:
        total_files += 1
        extension = file.rsplit(".", 1)[-1] # Get filename extension
        if extension and not extension.isspace() and len(extension) > 0: # String is not empty
            if "." in file:
                extension = "." + extension
                if extension in files_found:
                    files_found[extension][0] += 1
                else:
                    files_found[extension] = [ 1, 0 ]
                if is_filename_extension_a_prog_file(extension) == True:
                    files_found[extension][1] += get_number_of_lines_in_file(f"{root}\\{file}")
            else: # File has no filename extension
                if "No filename extension" in files_found.values():
                    files_found["No filename extension"][0] += 1
                else:
                    files_found["No filename extension"] = [ 1, 0 ]

def list_value_in_dict_exist(list, dict):
    for val in list:
        if val in dict:
            return True
    return False

def print_dict(dict):
    print("-----------------------------------------------")
    print(" {}{:>21}{:>13}".format("Language", "File(s)", "Line(s)"))
    print("-----------------------------------------------")
    for prog_lang, list_exts in prog_files.items():
        if list_value_in_dict_exist(list_exts, dict) == True:
            print(f"{prog_lang}:")
            for val in list_exts:
                if val in dict:
                    print(" {:<22}{:<13}{:<1}".format(val, (dict[val])[0], (dict[val])[1]))
                    del dict[val]

    print("-----------------------------------------------")
    print(" {}{:>18}".format("Other files", "File(s)"))
    print("-----------------------------------------------")
    for file_type, list_exts in other_files.items():
        if list_value_in_dict_exist(list_exts, dict) == True:
            print(f"{file_type}:")
            for val in list_exts:
                if val in dict:
                    print(" {:<22}{:<13}".format(val, (dict[val])[0]))
                    del dict[val]

    print("-----------------------------------------------")
    print(" {}".format("Unknown file extensions", "File(s)"))
    print("-----------------------------------------------")
    for key, value in dict.items():
        print(" {:<22}{:<13}".format(key, value[0]))
    print(f"Total files: {total_files}")

if len(files_found) > 0:
    print_dict(files_found)
