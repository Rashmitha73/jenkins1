import os

# 1. Print Name and Roll Number
print("Name: Rashmitha")
print("Roll Number: ai_141")

# 2. Print Environment Variables
print("\n--- Environment Variables ---")
for key, value in os.environ.items():
    print(f"{key} = {value}")

# 3. Create a data file
with open("data.txt", "w") as file:
    file.write("This is a test file created by Rashmitha (ai_141)\n")
    file.write("Welcome to Jenkins JOB A!")

# 4. Display the contents of the file
print("\n--- Contents of data.txt ---")
with open("data.txt", "r") as file:
    print(file.read())
