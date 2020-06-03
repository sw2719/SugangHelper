# SugangHelper
exe 파일 다운로드는 [여기](https://github.com/sw2719/SugangHelper/releases)

![ex](https://user-images.githubusercontent.com/22590718/83693710-90baf000-a631-11ea-8d90-a52d5f28bd2e.gif)

 수동으로 텍스트를 복사할 필요 없이 Ctrl+V 를 감지할 때마다 자동으로 텍스트를 클립보드로 복사해주는 프로그램입니다.
 프로그램 최초 실행후 생성되는 sugang.txt에 복사할 텍스트를 한 줄씩 입력해주시면 됩니다. 예를들어:
 
 텍스트1  
 텍스트2  
 텍스트3  
 이런식입니다.
 
 그러고나서 프로그램을 실행하면 첫번째 줄 텍스트가 로드되고 Ctrl+V를 누를때마다 다음 텍스트가 클립보드로 불러와지게 됩니다.
 한가지 중요한 점은, Ctrl+V 가 아닌 Ctrl키를 누른후 V를 누르면 그것도 Ctrl+V를 누른 것으로 인식하므로 주의하셔야 합니다.

# 파이썬으로 실행하려면
pywin32, pyWinhook 패키지가 필요합니다.
