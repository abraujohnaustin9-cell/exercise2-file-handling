

# 1. write
note = input("Write short note/message: ")

with open("notes.txt", "w") as f:
    f.write(note + "\n")

# 4. read
print("\n Current content of notes.txt:")
try:
    with open("notes.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: notes.txt not found.")

# 3. append
second_note = input("Write another note to add: ")

with open("notes.txt", "a") as f:
    f.write(second_note + "\n")

print("\n Updated content of notes.txt:")
try:
    with open("notes.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: notes.txt not found.")