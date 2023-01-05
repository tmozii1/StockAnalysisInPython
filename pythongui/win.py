from tkinter import *            # tkinter 라이브러리에 모든 함수를 사용하겠다.

def getWindow():
  root = Tk()                      # 창을 생성
  root.geometry("600x400")       # 창 크기설정
  root.title("창열기")    # 창 제목설정
  # root.option_add("*Font"."NanumGothic")  # 폰트설정
  root.resizable(False, False)  # x, y 창 크기 변경 불가
  return root

if __name__ == '__main__':
  root = getWindow()
  root.mainloop()                  # 창 실행
