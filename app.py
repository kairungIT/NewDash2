import streamlit as st

# สร้างแหล่งข้อมูลเพื่อเก็บข้อมูลปุ่ม
button_colors = {
    'Red': 'red',
    'Green': 'green',
    'Blue': 'blue'
}

# สร้างแบบฟอร์มสำหรับเลือกสี
selected_color = st.selectbox('เลือกสี:', list(button_colors.keys()))

# สร้างปุ่มที่มีสีตามที่ผู้ใช้เลือก
if st.button('แสดงผล'):
    color = button_colors[selected_color]
    st.write(f'คุณเลือกสี: {selected_color}')
    st.write(f'สีที่คุณเลือกคือ {color}', unsafe_allow_html=True)

# แสดงสไลด์เดอร์เพื่อเปลี่ยนค่าอื่น ๆ
st.sidebar.header('ตัวเลือก')
text_input = st.sidebar.text_input('ใส่ข้อความ:')
number_input = st.sidebar.number_input('ใส่ตัวเลข:', min_value=0)

# แสดงผลข้อความและตัวเลข
st.sidebar.write(f'ข้อความที่คุณใส่: {text_input}')
st.sidebar.write(f'ตัวเลขที่คุณใส่: {number_input}')