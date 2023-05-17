from tkinter import *
import tkinter as tk
def print_coordinates(event):
    x = event.x
    y = event.y
    print("Tọa độ của điểm là: ({}, {})".format(x, y))


a = Tk()
a.title('Loggin')
# a.geometry('800x800')


# Định nghĩa tài khoản và mật khẩu
ACCOUNT = "a"
PASSWORD = "1"

def login():
    # Lấy giá trị nhập vào từ người dùng
    username = username_label.get()
    password = password_label.get()

    # Kiểm tra xem thông tin đăng nhập có đúng hay không
    if username == ACCOUNT and password == PASSWORD:
        # Nếu đúng, đóng cửa sổ hiện tại và mở cửa sổ mới
        a.destroy()
        new_window = tk.Tk()
        new_window.title("New Window")
        new_window.geometry("600x600")
        new_window.mainloop()
    else:
        # Nếu sai, hiển thị thông báo lỗi
        error_label.config(text="Tài khoản hoặc mật khẩu không chính xác")



# Tạo hai canvas và đặt chúng vào vị trí khác nhau
can1 = Canvas(a, width=500, height=500, bg='blue')
can1.grid(row=0, column=0)

can2 = Canvas(a, width=500, height=500, bg='white')
can2.grid(row=0, column=1)



# Vẽ một đường thẳng trên canvas can1
can1.create_line(500, 0, 500, 500, fill='black', width=10)
# can1.create_line(4, 400, 4, 400,  fill = 'black', width=10)


# Tạo một widget Canvas để bắt sự kiện click chuột
# canvas = tk.Canvas(a, width=200, height=200)
# canvas.pack()




# label 1
username_label = Label(a, text='username:', font=('Times New Roman', 12)) # có thể thay đổi tủ tự
username_label.place(x = 130, y = 200) # tọa độ của text

# label 2
password_label = Label(a, text='password:', font=('Times New Roman', 12)) # có thể thay đổi tủ tự
password_label.place(x = 130, y = 250) # tọa độ của text



# Entry1
entry1 = Entry(a, width=10, font=('Arial', 12)) # kích thước hộp thay đổi theo width
entry1.place(x = 210, y = 200)

# Entry 2
entry2 = Entry(a, width=10, font=('Arial', 12))
entry2.place(x = 210, y = 250)

error_label = Label(a, text="error")

entry1.focus()
    

but = Button(a, text='Log in', width=10, height=1, font=('Arial', 10), command= login)
but.place(x =200, y = 300)




# Bắt sự kiện click chuột và hiển thị tọa độ của điểm
can1.bind("<Button-1>", print_coordinates)

a.mainloop()



