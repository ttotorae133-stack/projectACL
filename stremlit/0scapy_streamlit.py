import streamlit as st
import  pandas as pd
from scapy.all import sniff,IP,TCP,ICMP,send
from datetime import datetime

st.title("Hello.Scapy!!")

# 패킷 5개 캡쳐후 출력
# 캡쳐한 패킷은 streamlit 콘솔에 출력
# sniff (count = 5, prnlambda x: print(x))

packets =sniff(count =5)
for p in packets:
    # st.tect(p)
    st.write(p)

# 특정 프로코롤의 패킷 5개 캡쳐후 캡쳐
st.markdown("### tcp 패킷 5개 캡쳐후 출력")
packete =sniff(filter="tcp", count = 5)
for p in packete:
    st.write(p)

# ICMP 패킷 하나 생성하고 전송
st.markdown("### ICMP 패킷 하나 생성하고 전송")
packet = IP(dst='8.8.8.8') / ICMP()
for _ in range(1):
    send(packet)
    st.success("Sent 1 packets")

# 패킷 구조 확인
st.markdown("### 패킷 구조 확인")
st.text(packet.show(dump=True))

# 패킷 캡쳡 후 데이터 프레임으로 출력
st. markdown("### 패킷 캡쳐 후 데이터프레임으로 출력")
packet = sniff (filter = "tcp", count = 5)
# for p in packet:
   # st.text(p.time.p[0])  # 타임스탬프 형식
   # st.text(p[0].src)
   # st.text(p[0].dsst)
    #st.text(p[0].summary())
data =[]
for p in packets:
    #data.append({
        #"Time":p.time,
        #"Source":p[0].src if hasattr(p[0], 'src') else "",
        #"Destination":p[0].dst if hasattr(p[0], 'dst') else""
    #})

df = pd.DataFrame(data)
st.dataframe(df)


# 버튼 클릭시 패킷 캡쳐시작

st.markdown("### 버튼 클릭시 패킷 캡쳐시작")

if st.button("캡쳐시작"):
    packet = sniff(count = 5)
    for p in packets:
        st.write(p)