import os
import sys


def find_test_files(directory):
    file_list = []
    for root, _, files in os.walk(directory):
        for file_name in files:

            file_path = os.path.join(root, file_name)
            file_list.append(file_path)
    return file_list


if len(sys.argv) < 2:
    print('Please provide one of the allowed options.test file path  as an argument to run specific file or "all" to run all tests.\n')
    print("'file path' (example: file, folder.file/ without .py extension, runs specified python test)")
    print("all (runs all python tests)")
    print("cpp (runs all cpp tests)")
    sys.exit(1)
else:
    if (sys.argv[1] == "cpp"):
        files = find_test_files("./tests/cpp")
        for f in files:
            new_f = f.replace(
                "\\", "/")
            os.system(f"g++ -o cpp_test {new_f}")
            os.system(f".\cpp_test.exe")
        sys.exit(1)
    if (sys.argv[1] == "all"):

        directory_path = "./tests/python"

        files = find_test_files(directory_path)
        files_filtered = []
        for f in files:
            if "__init__.py" in f:
                continue
            if "__pycache__" in f:
                continue
            new_f = f.replace(".py", "").replace(
                "/", ".").replace("\\", ".")[2:]
            files_filtered.append(new_f)

        ff_string = ' '.join(files_filtered)

        os.system(f"python -m unittest {ff_string}")
    else:
        test = sys.argv[1]
        os.system(
            f"python -m unittest tests.python.{test}")
