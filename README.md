#  우분투에 미니콘다 설치하기
+ 우분투\
# 콘다 버전 확인 -25.11.1
conda -- version

# 콘다 자동 base 환경 비활성하고 확인 -> Faclse 
conda config --set auto_activate_base false
conda config --show auto_activate



### conda로 가상환경 생성
'''bash
# 가상환경 생선전  다음 명령 먼저 실행 (최초 한번!)
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r

# 그런 다음 아래 명령응로 가상환경 생성
conda create -y -n py311 python=3.11
source activate py311
'''


'''bash
pip install --upgrade pip
pip install scapy

mkdir ~/projectACL
cd ~/projectACL
vi main.py
sudo ~/miniconda3/envs/py311/bin/python main.py


'''
# py311 가상 환경에서 나감
conda deactivate


