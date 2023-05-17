import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import math

a = tk.Tk()
a.title('Loggin')

# Định nghĩa tài khoản và mật khẩu
ACCOUNT = "admin"
PASSWORD = "1"

def login():
    # Lấy giá trị nhập vào từ người dùng
    username = entry1.get()
    password = entry2.get()

    if username == ACCOUNT and password == PASSWORD:
        # Ẩn cửa sổ hiện tại
        a.withdraw()
        messagebox.showinfo("Thông báo", "Chào mừng bạn đến với ứng dụng!")
        # Kiểm tra nếu chưa có cửa sổ mới được tạo
        if not hasattr(a, 'new_window'):
            # Tạo cửa sổ mới
            a.new_window = tk.Toplevel()
            a.new_window.title("Kho tư liệu")
            # a.new_window.geometry("600x600")

            def zoom_image(event):
                # Lấy thông tin về ảnh được nhấp chuột
                image_label = event.widget
                photo_image = image_label.photo

                # Tạo cửa sổ mới
                new_window = tk.Toplevel()
                new_window.title("Zoom")

                # Thay đổi kích thước ảnh gốc thành một nửa kích thước ban đầu
                original_image = Image.open(photo_image.filename)
                resized_image = original_image.resize((original_image.width // 2, original_image.height // 2)) # chỉnh kích thước ảnh
                photo_resized = ImageTk.PhotoImage(resized_image)
                
                # Hiển thị ảnh đã thay đổi kích thước trong cửa sổ mới
                zoomed_label = tk.Label(new_window, image=photo_resized)
                zoomed_label.photo = photo_resized
                zoomed_label.pack()

            # Tạo cửa sổ
            

            # Tạo khung chứa các ảnh
            frame = tk.Frame(a.new_window)
            frame.pack()

            # Đường dẫn đến 20 file ảnh (đổi đường dẫn và tên file tương ứng)
            image_files = ["D:\image\Girl\h1.jpg", "D:\image\Girl\h2.jpg", "D:\image\Girl\h3.jpg", "D:\image\Girl\h4.jpg", "D:\image\Girl\h5.jpg", "D:\image\Girl\h6.jpg", "D:\image\Girl\h7.jpg", "D:\image\Girl\h8.jpg", "D:\image\Girl\h9.jpg", "D:\image\Girl\h10.jpg",
                           "D:\image\Girl\h11.jpg", "D:\image\Girl\h12.jpg", "D:\image\Girl\h13.jpg", "D:\image\Girl\h14.jpg", "D:\image\Girl\h15.jpg", "D:\image\Girl\h16.jpg", "D:\image\Girl\h17.jpg", "D:\image\Girl\h18.jpg", "D:\image\Girl\h19.jpg", "D:\image\Girl\h20.jpg",
                           "D:\image\Girl\h21.jpg", "D:\image\Girl\h22.jpg", "D:\image\Girl\h23.jpg", "D:\image\Girl\h24.jpg", "D:\image\Girl\h25.jpg"]


            # Số ảnh trên mỗi dòng và số dòng
            num_images_per_row = 5
            num_rows = math.ceil(len(image_files) / num_images_per_row)

            # Hiển thị ảnh trong khung theo từng dòng
            for i in range(num_rows):
                for j in range(num_images_per_row):
                    index = i * num_images_per_row + j
                    if index < len(image_files):
                        file = image_files[index]
                        image = Image.open(file)
                        resized_image = image.resize((100, 100))  # Điều chỉnh kích thước ảnh trong khung
                        photo_resized = ImageTk.PhotoImage(resized_image)
                        photo_resized.filename = file  # Lưu đường dẫn tới file ảnh
                        label = tk.Label(frame, image=photo_resized)
                        label.photo = photo_resized  # Lưu tham chiếu đến ảnh để tránh bị hủy bỏ bởi garbage collector
                        label.bind("<Button-1>", zoom_image)  # Gắn sự kiện nhấp chuột để phóng to ảnh
                        label.grid(row=i, column=j)
                    else:
                        # Thêm ô trống nếu số ảnh không đủ để điền vào dòng cuối cùng
                        empty_label = tk.Label(frame)
                        empty_label.grid(row=i, column=j)

            # Chạy vòng lặp chính của ứng dụng
            a.new_window.mainloop()

            # Khi đóng cửa sổ mới, hiển thị lại cửa sổ gốc và hủy biến new_window
            a.new_window.protocol("WM_DELETE_WINDOW", lambda: close_new_window(a.new_window))
            messagebox.showinfo("Thông báo", "Chào mừng bạn đến với ứng dụng!")
        
        # Hiển thị cửa sổ mới
        a.new_window.deiconify()
    else:
        # Nếu sai, hiển thị thông báo lỗi
        error_label.config(text="Tài khoản hoặc mật khẩu không chính xác")
        messagebox.showinfo("Cảnh báo!", "Tài khoản hoặc mật khẩu không chính xác")

# Hàm đóng cửa sổ mới và hiển thị lại cửa sổ gốc
def close_new_window(window):
    window.destroy()
    # a.deiconify()
    # delattr(a, 'new_window')


# Tạo hai canvas và đặt chúng vào vị trí khác nhau
can1 = tk.Canvas(a, width=500, height=500, bg='blue')
can1.grid(row=0, column=0)

can2 = tk.Canvas(a, width=500, height=500, bg='white')
can2.grid(row=0, column=1)

# Vẽ một đường thẳng trên canvas can1
can1.create_line(500, 0, 500, 500, fill='black', width=10)

# label 1
username_label = tk.Label(a, text='username:', font=('Times New Roman', 12))
username_label.place(x=130, y=200)

# label 2
password_label = tk.Label(a, text='password:', font=('Times New Roman', 12))
password_label.place(x=130, y=250)

# Entry1
entry1 = tk.Entry(a, width=10, font=('Arial', 12))
entry1.place(x=210, y=200)

# Entry 2
entry2 = tk.Entry(a, width=10, font=('Arial', 12))
entry2.place(x=210, y=250)

error_label = tk.Label(a, text="error")

entry1.focus()

but = tk.Button(a, text='Log in', width=10, height=1, font=('Arial', 10), command=login)
but.place(x=200, y=300)

quit_button = tk.Button(a, text='Quit', width=10, height=1, font=('Arial', 10), command=quit)
quit_button.place(x=407, y=476)

# Tạo đối tượng Image từ hình ảnh biểu tượng
image = Image.open("D:\image\he2.png")
photo = ImageTk.PhotoImage(image)
# Tạo một label để hiển thị hình ảnh
c = tk.Label(a, image=photo)
c.place(x=503, y=70)

intro = tk.Label(a, text='Cùng Khám Phá Tư liệu', width=30, height=3, font=('Arial', 15))
intro.place(x=600, y=40)

b = tk.Label(a, text="Đăng nhập vào thì biết nha!, hahaaa :))", font=("Arial", 16), foreground='black')
b.place(x=640, y=230)





a.mainloop()