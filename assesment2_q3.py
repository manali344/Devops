"""3.Write to a File
Write a program to create a text file and write some content to it.

Using file functions like write and open.
"""

with open("Devops_notes.txt", "w") as file:
    file.write("This is for writing Devops notes")

with open("My_file.txt","w") as f:
    f.write("This is multi line file \n")
    f.write("Trying to read multiple lines")