import qrcode
import pandas as pd
import os

# Example: Student data
students = [
    {"Name": "Pranjal", "RollNo": "1", "Dept": "AIML", "Year": "TY"},
    {"Name": "Nikita", "RollNo": "2", "Dept": "AIML", "Year": "TY"},
    {"Name": "Pratiksha", "RollNo": "3", "Dept": "AIML", "Year": "TY"},
    {"Name": "Nikhil", "RollNo": "4", "Dept": "AIML", "Year": "TY"},
    {"Name": "Prathmesh", "RollNo": "5", "Dept": "AIML", "Year": "TY"}
]

# Create a folder to save QR images
qr_folder = "qr_images"
os.makedirs(qr_folder, exist_ok=True)  # Create the folder if it doesn't exist

# Prepare list to save in CSV
data_for_csv = []

for student in students:
    # Format the info into a single string
    info = f"{student['Name']}|{student['RollNo']}|{student['Dept']}|{student['Year']}"
    
    # Generate QR Code
    qr = qrcode.make(info)
    
    # Define the QR image filename
    qr_filename = f"{student['RollNo']}.png"  # Example: A101.png
    qr_path = os.path.join(qr_folder, qr_filename)
    
    # Save QR code image
    qr.save(qr_path)
    
    # Append info to CSV list
    data_for_csv.append({
        "Name": student['Name'],
        "RollNo": student['RollNo'],
        "Dept": student['Dept'],
        "Year": student['Year'],
        "QRCode_Path": qr_path
    })

# Convert to DataFrame
df = pd.DataFrame(data_for_csv)

# Save to CSV
df.to_csv("students_with_qr.csv", index=False)

print(" All QR codes generated and saved! CSV also created successfully.")