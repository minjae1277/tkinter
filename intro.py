import tkinter as tk

#함수 정의: 버튼 클릭 시 호출
def on_button_click():
    if button["text"]=="클릭":
        button.config(text="닫기") # 버튼 텍스트를 "닫기"로 변경
        label.config(text="버튼이 클릭되었습니다!")
    else:
        window.destroy() #윈도우 종료


#기본 윈도우 생성
window=tk.Tk()
window.title("Tkinter 기본 예제") #윈도우 제목 설정

#레이블 생성
label = tk.Label(window, text="버튼을 클릭하세요!" , font=('Arial' , 14))
label.pack(pady=20) #레이블은 윈도우에 추가하고, 여백을 설정

#버튼 생성
button= tk.Button(window, text="클릭", command=on_button_click, font=('Arial', 14))
button.pack(pady=10) # 버튼을 윈도우에 추가하고, 여백을 설정

#메인 루프 시작
window.mainloop()
