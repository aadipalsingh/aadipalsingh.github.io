'''Smart Student Result Analyzer

A school stores student data in a file:

id,name,marks1,marks2,marks3

Build a system that:

Reads file
Calculates total, percentage
Assigns grade using selection statements
Handles missing/invalid data using exception handling
Outputs toppers per class'''
#importing csv module to read the student data from a file
import csv
#function to calculate grade based on percentage
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"

#function to process the student data file and calculate results
def process_file(filename):
    topper = None
    max_percentage = -1
#handling file reading and data processing with exception handling to manage errors gracefully
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)

            print("\n--- Student Results ---")

            for row in reader:
                try:
                    name = row['name']

                    # Convert marks safely
                    m1 = int(row['marks1'])
                    m2 = int(row['marks2'])
                    m3 = int(row['marks3'])
# Calculate total and percentage
                    total = m1 + m2 + m3
                    percentage = total / 3

                    grade = calculate_grade(percentage)

                    print(f"{name}: Total={total}, %={percentage:.2f}, Grade={grade}")

                    # Track topper
                    if percentage > max_percentage:
                        max_percentage = percentage
                        topper = name

                except ValueError:
                    print(f"Invalid data for student {row['name']} → Skipped")
                except KeyError:
                    print("Missing column in file")

        print("\n--- Topper ---")
        if topper:
            print(f"{topper} with {max_percentage:.2f}%")
        else:
            print("No valid data found")

    except FileNotFoundError:
        print("File not found. Please check filename.")


# Run program
process_file("students.csv")