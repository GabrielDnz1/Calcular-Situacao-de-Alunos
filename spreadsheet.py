def calculateRequiredGrade(average):
    required_grade = 10 - average
    return max(required_grade, 0)

def studentData():
    # Function Variables
    all_values = sheet.get_all_values()  # Get the total number of lines from the XLSX file
    totalLines = len(all_values) - 3  # Get the integer number of lines by subtracting the number of lines without content
    line = 4  # Value defined from the beginning of the required data
    i = 0  # Counter
    totalSemesterClasses = 60  # Fixed number of classes in the semester

    # Loop to go through all the necessary lines
    while i < totalLines:
        # Get the scores to generate an average that will later be used to determine the student's situation
        grade1 = int(sheet.cell(line, 4).value)
        grade2 = int(sheet.cell(line, 5).value)
        grade3 = int(sheet.cell(line, 6).value)
        studentAverage = (grade1 + grade2 + grade3) / 3

        # Calculate Minimum Attendance and percentage required for Non-Reproval
        minimumAttendancePercentage = (25 / 100) * totalSemesterClasses
        studentAbsences = int(sheet.cell(line, 3).value)

        # Final Grade Calculation
        calculatedRequiredGrade = calculateRequiredGrade(studentAverage)
        sheet.cell(line, 8).value = calculatedRequiredGrade

        # Conditionals aiming at updating the student's status and final approval grade by sheet.cell().value
        if studentAbsences < minimumAttendancePercentage:
            sheet.cell(line, 7).value = "Reprovado por Falta"
            sheet.cell(line, 8).value = "0"
        elif studentAverage < 50 and studentAbsences >= minimumAttendancePercentage:
            sheet.cell(line, 7).value = "Reprovado por Nota"
            sheet.cell(line, 8).value = "0"
        elif 50 <= studentAverage < 70 and studentAbsences >= minimumAttendancePercentage:
            sheet.cell(line, 7).value = "Exame Final"
            sheet.cell(line, 8).value = "0"
        elif studentAverage >= 70 and studentAbsences >= minimumAttendancePercentage:
            sheet.cell(line, 7).value = "Aprovado"
            sheet.cell(line, 8).value = "0"

        # Counters
        line += 1
        i += 1

import math
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Variables

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
spreadsheet_name = "Software Engineering - Challenge Gabriel Augusto Diniz Barbosa"

# Attempt to open the spreadsheet or catch possible exceptions
try:
    sheet = client.open(spreadsheet_name).sheet1
# if it does not detect an error, the function is called
    studentData()

except gspread.exceptions.SpreadsheetNotFound:
    print(f"Error: Spreadsheet '{spreadsheet_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
