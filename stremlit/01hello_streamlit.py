import streamlit as st
from PIL import Image
import datetime
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# 기본 텍스트 위젯
st.title("Streamlit Basics")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is a simple text")
st.write("This is a write dimension") # 만능 출력함수

# 마크다운을 이용한 출력 지원 (추천!)
st.markdown("## 마크다운을 이용한 제목 ")
st.markdown("[Streamlit](https://www.streamlit.io)")
st.markdown("https://www.streamlit.io")


# 사용자 작성 HTML 코드도 삽입 가능
html_page = """
<div style="background-color:orange; padding:50px">
<p style="color:white; font-size:50px">Enjoy Streamlit!</p>
</div>
"""
st.markdown(html_page, unsafe_allow_html=True)

# 구분선 위젯
# st.divider()
st.markdown("---")

# 간단한 알림상자 위젯
st.success("Success!")
st.info("Information")
st.warning("This is a warning!")
st.error("This is an error!")

# 이미지 불러오기
from pathlib import Path

# streamlit 파일이 실행중인 경로를 기준으로 이미지 경로 설정

BASE_DIR = Path(__file__).parent
img_path = BASE_DIR /"imgs" / "img.png"

img = Image.open(img_path)
st.image(img, width=300, caption="Hello Logo")


# 유투브 url 도 포함 가능
ㅏ
st.video("https://youtu.be/YFDiuj0Pu8Q?si=fEP3vVKNDvJUCix7")




st.button("Play1")

if st.button("Play2"):
    st.text("Hello world!")

if st.checkbox("Checkbox"): # 체크박스 버튼을 클릭하면
    st.text("Checkbox selected")

radio_but = st.radio("Your Selection", ["A", "B"])
if radio_but == "A":
    st.info("You selected A")
else:
    st.info("You selected B")

city = st.selectbox("Your City", ["Napoli", "Palermo", "Catania"])

occupation = st.multiselect("Your Occupation",
                            ["Programmer", "Data Scientist", "IT Consultant", "DBA"])

st.divider()

# 입력 폼 위젯
Name = st.text_input("Your Name", "Write something…")
st.text(Name)

Age = st.number_input("Input a number")

message = st.text_area("Your Message", "Write something...")


select_val = st.slider("Select a Value", 1, 10)



st.divider()

# 신기한 기능!
if st.button("Balloons"):
    st.balloons()

st.divider()
# 날짜/시간 위젯
today = st.date_input("Today is",datetime.datetime.now())
hour = st.time_input("The time is",datetime.time(12,30))

st.divider()

# json 데이터를 다루는 위젯
data = {"name":"John","surname":"Wick"}
st.json(data)
st.code("import pandas as pd")



st.divider()

# 진행 상태 위젯
my_bar = st.progress(0)

for value in range(10):
    time.sleep(0.01)
    my_bar.progress(value+2)

# 스피너 위젯
with st.spinner("Please wait..."):
    time.sleep(3)

st.success("Done!")


st.divider()

csv_path = BASE_DIR / "Auto.csv"
st.header("Dataframes and Tables")
df = pd.read_csv(csv_path)

# 데이터집합을 가변적으로 출력
st.dataframe(df.head(10))

# 데이터 집합을 정적을 출력
st.table(df.head(10))

# 차트 위젯
st.area_chart(df[["mpg","cylinders"]])

st.bar_chart(df[["mpg","cylinders"]].head(20))

st.line_chart(df[["mpg","cylinders"]].head(20))


# matplotlib, seaborn 위젯


fig, ax = plt.subplots()
corr_plot = sns.heatmap(df[["mpg","cylinders", "displacement"]].corr(), annot= True)
st.pyplot(fig)

