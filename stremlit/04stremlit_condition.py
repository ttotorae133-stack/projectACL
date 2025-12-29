import streamlit as st

# 이름을 표시하는 함수
def display_name(name):
    st.info(f'**Name:** {name}')

# 이름 입력
name = st.text_input('Please enter your name')

# 유효성 검사: 이름이 입력되면 정보 표시, 아니면 오류 메시지 표시
# 일반적으로 많이 사용하는 방식
if name:
    display_name(name)
else:
    st.error('No name entered')
    import streamlit as st

# 이름을 표시하는 함수
def display_name2(name):
    st.info(f'**Name:** {name}')

# 이름 입력
name = st.text_input('Please enter your name2')

# 이름이 입력되었는지 확인
# 예외처리를 염두에두고
if not name:
    st.error('No name entered')
else:
    display_name2(name)