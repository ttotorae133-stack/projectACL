# 간단한 네트워크 패킷 스니퍼
# 차단하고 싶은 IP 설정(ACL 규칙)
# 터미널 글자  색상 지정

from  scapy.all import sniff,IP, TCP
from scapy.layers.inet import ICMPerror

import lib.mymodule
import lib.mymodule2
# 메인 실행 부분
# 현재 파일썬 파일은 직접 호출했을때만 실행되게 하고
# import 했을떄는 자동으로 실행되지 않게 하기 위한 코드
if __name__ =='__main__':
    print(">>> 패킷 감시를 시작합니다... (중지는 Ctrl + C)")

# 터미널 색상 지정 (ANSI Code)
# 이스케이프 시쿼스로 색상 지정 : ESC [코드 m]
RED  = "\033[91m" # 8진수 33 -> 10진수 27 -> ESC, 제어명령 시작을 알림
# 91: 빨강, 92: 녹색, 0: 검정
# m: 색상 sgr 형식 (색상,굵기,밑줄,반전)으로 표기
GREEN = "\033[92m"
RESET = "\033[0m"

# 차단하고 싶은 IP 지정(ACL)
#BLOCKED_IP ="8.8.8.8"
BLOCKED_IP ="104.18.23.5"


#패킷이 캡쳐될때마다 호출되는 함수
#여기서 패킷의 헤더 정보를 꺼내봄
#1. IP 레이어가 있는지 확인
#  네트워크에는 IP가 없는 패킷도 존재할 수있음 - 주의 요망!


    # TCP 헤더에서 출발지/도착지 포트번호 추출


def process_packet(packet):
    if packet.haslayer(IP):
        # IP 헤더에서 출발지/도착지 IP 주소 추출 (프로토콜 번호도 함계)
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst


       # 출발지 ip 가 우리가 지정한 차단 ip와 같다면
        if ip_src == BLOCKED_IP:
            print(f"{RED}" + "="*50)
            print(f"[!!!경고 !!!] 차단된 IP가 감지되었습니다!!")

            print(f"="*50 +f"{RESET}") # 색상초기화

            # TCP 계층도 있다면 포트정보도 출력
            if packet.haslayer(TCP):
                print(f"포토정보 :{packet[TCP].sport} -> {packet[TCP].dport}")
            print




        else:
            # 정상 패킷은 그대록 출력
            if packet.haslayer(TCP):
                print(f"{GREEN} [통과 패킷] {ip_src} -> {ip_dst} {RESET}")



#    sniff : 패킷을 낚아채는 함수
#   filter
#   prn
#   store: 잡은 패킷을 메모리에 저장하지 않음(메모리 부족 방지)
# sniff(filter="ip",prn=process_packet,store=False)
sniff(filter="ip",prn=process_packet,store=False)
