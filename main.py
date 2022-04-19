# READ FILE DEMO by MR. V

# Read Entire Contents of File as a Single String
# open(path_to_file, mode)
# mode: "r" - read, "w" - write
file = open("data.txt", "r")
contents = file.read()
file.close()

print(contents)

# Read Entire Contents of File into a List
# Each list element is a line from the file
file = open("data.txt", "r")
lines = file.readlines()
file.close()

print(lines)

# Read Entire Contents of File Line by Line
# Remove extra characters from each line with strip()
file = open("data.txt", "r")
lines = []
for line in file:
    line = line.strip()
    lines.append(line)
file.close()

print(lines)
