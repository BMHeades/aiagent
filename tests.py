from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

# dir info
# # 1
# print(get_files_info("calculator", "."))

# # 2
# print(get_files_info("calculator", "pkg"))

# # 3
# print(get_files_info("calculator", "/bin"))

# # 4
# print(get_files_info("calculator", "../"))



# file contents
# print(get_file_content("calculator", "lorem.txt"))

# print(get_file_content("calculator", "pkg/calculator.py"))
# print(get_file_content("calculator", "main.py"))
# print(get_file_content("calculator", "/bin/cat"))
# print(get_file_content("calculator", "pkg/does_not_exist.py") )


# write file
# print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
# print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
# print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))


# run python
print(run_python_file("calculator", "main.py"))
print(run_python_file("calculator", "main.py", ["3 + 5"]))
print(run_python_file("calculator", "tests.py"))
print(run_python_file("calculator", "../main.py"))
print(run_python_file("calculator", "nonexistent.py"))