# ex 1
import os

root = r'C:\Users\Алихан\Desktop\labs'

for path, dirs, files in os.walk(root):
    for name in files:
            print(os.path.join(path, name))

# ex 2
import os

def check_path_access(path):
    print(f"Path: {path}")
    print(f"Existence: {os.access(path, os.F_OK)}")
    print(f"Readable: {os.access(path, os.R_OK)}")
    print(f"Writable: {os.access(path, os.W_OK)}")
    print(f"Executable: {os.access(path, os.X_OK)}")

path = r'C:\Users\Алихан\Desktop\labs'
check_path_access(path)

# ex 3
import os

def check_path_exist(path):
    print(f"Path: {path}")
    if os.path.exists(path):
        print("Path exists.")
        print(f"File name: {os.path.basename(path)}")
        print(f"Directory name: {os.path.dirname(path)}")
    else:
        print("Path does not exist.")
specified_path = r'C:\Users\Алихан\Desktop\labs'
check_path_exist(specified_path)

# ex 4
# import os

# def count_lines(file_path):
#      with open(file_path, 'r') as file:
#             line_count = sum(1 for _ in file)
#             return line_count
#    
# specified_path = r'C:\Users\Алихан\Desktop\labs'
# line_count = count_lines(specified_path)
# print(f"Number of lines : {line_count}")

# ex 5
my_list = [1, 2, 3, 4]

filename = 'output.txt'

with open(filename, 'w') as outfile:
    outfile.writelines([str(item) + '\n' for item in my_list])

# ex 6
for letter in range(ord('A'), ord('Z') + 1):
    filename = f"lab 6/{chr(letter)}.txt"
    with open(filename, "w") as f:
        f.write(chr(letter))
        
# ex 7

with open('input.txt', 'r') as file:
    content = file.read()

with open('output.txt', 'a') as dfile:
    dfile.write(content)
    
# ex 8
import os

def delete_file(path):
    if os.path.isfile(path):
        os.remove(path)
        print(f"Файл '{path}' удален")
    else:
        print(f"Файл '{path}' не существует")

file_to_delete = r"C:\Users\Алихан\Desktop\labs\deleted.txt" 
delete_file(file_to_delete)

        





