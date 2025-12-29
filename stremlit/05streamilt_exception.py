import streamlit as st

# 입력을 위한 컬럼 생성
col1, col2 = st.columns(2)

with col1:
    number_1 = st.number_input('Please enter the first number', value=0, step=1)
with col2:
    number_2 = st.number_input('Please enter the second number', value=0, step=1)

# 앱을 실행하면 기본값으로 설정된 0을 0으로 나눌려고시도 -> 오류발생!!
# 스트림밋이 웹페이지 런타임 예외를 표시 - 해커에게 중요한 정보 제공
# st.info(f'**{number_1}/{number_2}=** {number_1/number_2}')

try:
    st.info(f'**{number_1}/{number_2}=** {number_1/number_2}')
except ZeroDivisionError:
    st.error(f'Error: {e}')