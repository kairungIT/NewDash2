import streamlit as st

# ใช้ HTML สำหรับการเชื่อมโยงไฟล์ CSS
html_string = "<h3>this is an html string</h3>"
st.markdown(html_string, unsafe_allow_html=True)
st.markdown("<link rel='stylesheet' href='styles.css'>", unsafe_allow_html=True)
st.write("<p style='color: red;'>This text is red.</p>")

# สร้างข้อมูลหลักในแอพพลิเคชัน
st.title('แอพพลิเคชัน Streamlit ที่ได้รับการตกแต่ง')
