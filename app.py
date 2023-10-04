import streamlit as st

# ใช้ HTML สำหรับการเชื่อมโยงไฟล์ CSS
st.markdown("""<link rel="stylesheet" href="style.css">
<button class="button">Green</button>
<button class="button button2">Blue</button>
<button class="button button3">Red</button>
<button class="button button4">Gray</button>
<button class="button button5">Black</button>
""", unsafe_allow_html=True)

# สร้างข้อมูลหลักในแอพพลิเคชัน
st.title('แอพพลิเคชัน Streamlit ที่ได้รับการตกแต่ง')
