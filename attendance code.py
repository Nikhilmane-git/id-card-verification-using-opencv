import cv2
import pandas as pd
from datetime import datetime

# Load dataset
df = pd.read_csv("students_with_qr.csv")
marked_attendance = set()

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

print("Scanning for QR Codes. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    data, bbox, _ = detector.detectAndDecode(frame)
    if data:
        name, roll, dept, year = data.split('|')

        if roll not in marked_attendance:
            print(f"[+] Marked: {name} ({roll})")
            marked_attendance.add(roll)

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("attendance_log.csv", "a") as f:
                f.write(f"{name},{roll},{dept},{year},{now}\n")

        if bbox is not None:
            pts = bbox.astype(int).reshape(-1, 2)
            for i in range(len(pts)):
                pt1 = tuple(pts[i])
                pt2 = tuple(pts[(i + 1) % len(pts)])
                cv2.line(frame, pt1, pt2, (0, 255, 0), 2)

            cv2.putText(frame, f"{name} | {roll}", (pts[0][0], pts[0][1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    cv2.imshow("QR Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()