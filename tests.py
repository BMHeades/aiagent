from functions.get_files_info import get_files_info

# 1
print(get_files_info("calculator", "."))

# 2
print(get_files_info("calculator", "pkg"))

# 3
print(get_files_info("calculator", "/bin"))

# 4
print(get_files_info("calculator", "../"))