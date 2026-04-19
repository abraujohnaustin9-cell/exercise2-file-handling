# Exercise 2 (Finals): File Handling

# 1. Write
note = input("Enter a short note/message: ")

with open("notes.txt", "w") as f:
    f.write(note + "\n")

# 2. Read
print("\n📄 Current content of notes.txt:")
try:
    with open("notes.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: notes.txt not found.")

# 3. Append
second_note = input("Enter another note to add: ")

with open("notes.txt", "a") as f:
    f.write(second_note + "\n")

print("\n📄 Updated content of notes.txt:")
try:
    with open("notes.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: notes.txt not found.")