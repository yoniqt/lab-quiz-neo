
#!/usr/bin/env python3
import datetime

# Print personal info
full_name = "Neo Nicolas"
student_id = "231-0795"
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"Name: {full_name}")
print(f"Student ID: {student_id}")
print(f"Date & Time: {current_time}")

# Prompt user input
issue = input("Describe a networking issue you're facing: ")

# Save to file
with open("network_issue.txt", "w") as file:
    file.write(f"Networking Issue: {issue}\n")

    
