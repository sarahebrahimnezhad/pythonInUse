import re

# Read number of locks (k)
k = int(input())

# Read the safe password as a string
password = input()

# If the password length is not equal to k, input is invalid
if len(password) != k:
    print("invalid")
    exit()

# Total minimum rotations needed
total_rotations = 0

# Process each lock
for i in range(k):
    lock = input()  # Read the 9-digit arrangement of this lock (clockwise)

    # Validate that each lock input is exactly 9 digits
    pattern = r"^\d{9}$"
    if not re.match(pattern, lock):
        print("invalid lock")
        exit()

    # Target digit for this lock from the password
    target_digit = password[i]

    # Find the index of the target digit inside the lock string
    index = lock.find(target_digit)

    # Since it is a circular lock with 9 digits:
    # clockwise rotations = index
    # counterclockwise rotations = 9 - index
    # We take the minimum of these two values
    if index <= 4:
        total_rotations += index
    else:
        total_rotations += 9 - index

# Print the final answer
print(total_rotations)
