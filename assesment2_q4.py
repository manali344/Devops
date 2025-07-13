'''4. Read from a File
We used open in read mode and file.read to read and print to display.
'''

with open("Devops_notes.txt","r") as file:
    data = file.read()
    print("FILE1: ",data)

print("\n\nFile-2")
with open("My_file.txt","r") as f:
    for line in f:
        print(line.strip())