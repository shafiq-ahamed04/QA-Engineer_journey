# Script 5: Test Report Generator
# Concepts Covered
# File Handling
# Error Handling
#
# Write a test report into: results.txt
# Then read the file and print it.

try:
    
    with open("results.txt", "w") as f:
        f.write("Login : PASSED\n")
        f.write("Search : FAILED\n")
        f.write("Checkout : PASSED\n")

    
    with open("results.txt", "r") as f:
        content = f.read()

    print(content)

except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")


