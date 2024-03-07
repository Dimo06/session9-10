file_name = "x-file.txt"
fd = open(file_name, "w")
while True:
    line = input("enter a line (or just press Enter to quit): ")
    if line:
        fd.write(line +"\n")
    else:
        break

# fd.write("Hello, World!")
fd.close()
