# SmartDectector
PIR센서와 pi camera를 이용한 차량내 동작 감지 카메라

#카메라를 사용하기 위한 motion설치
sudo apt-get install motion 입력해서 설치

#motion 세팅 방법
명령 프롬폼트 창에서 sudo nano/etc/motion/motion.conf 명령을 통해 파일을 수정할 예정
(Ps. nano에서 검색방법 Ctrl + w 저장방법 Ctrl + x -> y -> Enter)
1. framerate 검색후 60으로 수정
2. ffmpeg 검색 ffmpeg_output_movies off (해당 기능은 동영상을 계속 저장하는 기능이라 스트리밍을 할 예정이면 필요 x) 
3. stream_maxrate 검색 60으로 수정 (초당 프레임, 카메라 성능에 맞춰서 수정하세요)
4. stream_localhost off로 수정 (외부에서 접속할 수 있게 함)
5. webcontrol_localhost off(off를 할 경우 밖에서도 언제든지 바꿀수 있다.)
#motion 서비스 등록
sudo nano /etc/default/motion
start_motion_daemon=yes로 변경
#motion 자동실행 설정
sudo nano /etc/rc.local
맨아래줄에 있는 exit 0 바로 윗줄에 sudo motion 추가

#해당 motion 폴더 권한설정
sudo chmod 777 /var/lib/motion
이후 외부접속을 하기위한 포트포워딩
(상세한건 구글에 검색하세요 공유기마다 방법이 약간씩 다릅니다)

#카메라를 스트리밍 하기위한 UV4L 설치
1. Stretch 저장소 설정
curl http://www.linux-projects.org/listing/uv4l_repo/lpkey.asc | sudo apt-key add -
sudo nano /etc/apt/source.list
맨 아래 부분에 추가
deb http://www.linux-projects.org/listing/uv4l_repo/raspbian/stretch stretch main
2. 변경된 저장소를 업데이트 합니다
sudo apt-get update
3. UV4L 모듈을 설치합니다.
sudo apt-get install uv4l uv4l-raspicam
4. 부팅시 자동으로 UVL 드라이버 로드하기위한 문장
sudo apt-get install uv4l-raspicam-extras
5. 펌웨어 업데이트
sudo rpi-update
6. UV4L 서비스 재시작
sudo service uv4l_raspicam restart
7. uvrl-server 설치
sudo apt-get install uv4l-server uv4l-uvc uv4l-xscreen uv4l-mjpegstream uv4l-dummy uv4l-raspidisp
8. WebRTC Streaming server 설치(양방향 스트리밍)
sudo apt-get install uv4l-webrtc
9. ssl 구성(보안상 이유 입력해야함)
openssl genrsa -out selfsign.key 2048&& openssl req -new-x509 -key selfsign.key -out selfsign.crt -sha256
Country 설정 부분은 KO 입력후나머지는 .을 치고 엔터를 눌러 default값을 주게한다
10. xmpp-bridge 설치
sudo apt-get install uv4l-xmpp-bridge
11. 설치완료
reboot 후 netstat -nlpt를 이용하여 8080포트활성화 확인

#라즈베리파이에서 메세지를 보내기위한 ssmtp설치
해당 방법은 참조를 남긴다
참조:https://blog.naver.com/simjk98/221970838993

#핸드폰 어플을 이용하여 카메라 확인하는법 참고바람
참고주소:https://blog.naver.com/durian0328/221757910190
