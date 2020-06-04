import pythoncom
import sys
import pyWinhook
import win32.win32clipboard as cb


class SugangHelper:
    def __init__(self):
        self.ctrl_var = False
        self.line_selector = 0

        try:  # sugang.txt 를 열어 한줄 씩 리스트에 저장
            with open('sugang.txt', 'r', encoding='utf-8') as txt:
                self.data = txt.read().splitlines()
        except FileNotFoundError:  # sugang.txt 가 존재하지 않을 경우 생성후 종료
            open('sugang.txt', 'w').close()
            print('생성된 sugang.txt에 복사할 내용을 한 줄씩 입력하세요.\n')
            input('Enter 를 눌러서 종료...')
            sys.exit(0)

        # Ctrl+V 감지를 위한 키보드 훅 생성
        self.hm = pyWinhook.HookManager()
        self.hm.KeyDown = self.keypress_event
        self.hm.HookKeyboard()  # 키 입력 감지 시작
        print('Ctrl+V 감지 시작. 실수로 누르지 않도록 주의하세요.')
        self.loadclipboard(init=True)

    def keypress_event(self, event):
        try:
            if event.KeyID == 86 and self.ctrl_var is True:  # Ctrl 키가 이전에 입력되었고 V가 입력된 경우
                self.loadclipboard()

                if self.line_selector + 1 == len(self.data):
                    self.hm.UnhookKeyboard()
                    print('-------------------------------')
                    print('마지막 줄이 복사되었습니다.\n')
                    print('창 상단의 닫기 버튼을 눌러 종료하세요.')
                    pythoncom.PostQuitMessage(0)
                else:
                    self.line_selector = self.line_selector + 1
            elif event.KeyID == 162:  # Ctrl 키가 입력된 경우
                self.ctrl_var = True
            else:  # Ctrl, V 이외의 키가 입력된 경우
                self.ctrl_var = False
        finally:
            return True

    def loadclipboard(self, init=False):
        text_target = self.data[self.line_selector]

        if init:
            print(f'다음 복사할 텍스트: {text_target}')
        else:
            cb.OpenClipboard()
            cb.EmptyClipboard()
            cb.SetClipboardText(text_target)
            cb.CloseClipboard()
            print(f'{text_target}을/를 복사했습니다. | {self.line_selector + 1}/{len(self.data)}')

            if self.line_selector + 1 < len(self.data):
                print(f'다음 복사할 텍스트: {self.data[self.line_selector + 1]}')


SugangHelper()
pythoncom.PumpMessages()
