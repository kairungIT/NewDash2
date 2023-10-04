import streamlit as st
import cv2
import numpy as np

# สร้างหน้าต่างแสดงภาพจากกล้อง
st.title('แอพพลิเคชันกล้อง')

# เปิดกล้อง
cap = cv2.VideoCapture(0)

# ตัวแปรสำหรับเก็บภาพจากกล้อง
frame = None

# สร้างส่วนของ UI เพื่อแสดงภาพจากกล้อง
image_placeholder = st.empty()

# รับข้อมูลจากกล้องและแสดงใน Streamlit
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # แสดงภาพใน Streamlit
    image_placeholder.image(frame, channels="BGR")

    # ใช้คำสั่งตรวจสอบการหยุดที่กำหนดเอง (ยกเลิกการแสดงภาพจากกล้อง)
    if st.button('หยุดการแสดงภาพ'):
        break

# ปิดกล้องเมื่อเสร็จสิ้น
cap.release()