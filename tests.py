from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

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
print(get_file_content("calculator", "lorem.txt"))

# print(get_file_content("calculator", "pkg/calculator.py"))
# print(get_file_content("calculator", "main.py"))
# print(get_file_content("calculator", "/bin/cat"))
# print(get_file_content("calculator", "pkg/does_not_exist.py") )