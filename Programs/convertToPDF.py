from docx2pdf import convert
import os

try:
    os.chdir('C:/Users/Faraz/OneDrive/Desktop/Harvard/CSCIE-90/Week1/submit')
    # Get the filename from the user
    input_file = input("Enter the file name with complete path: ")

    # Convert the Word document to PDF
    convert(input_file)

    print(f"Conversion of '{input_file}' to PDF completed.")
except Exception as e:
    print(f"An error occurred: {str(e)}")