# image_files = ["D:\image\c.jpg", "D:\image\h1.jpg", "D:\image\h2.jpg", "D:\image\h3.jpg", "D:\image\h4.jpg"]

import tkinter as tk
from PIL import Image, ImageTk
import math

def zoom_image(event):
    # Lấy thông tin về ảnh được nhấp chuột
    image_label = event.widget
    photo_image = image_label.photo

    # Tạo cửa sổ mới
    new_window = tk.Toplevel()
    new_window.title("Zoom")

    # Thay đổi kích thước ảnh gốc thành một nửa kích thước ban đầu
    original_image = Image.open(photo_image.filename)
    resized_image = original_image.resize((original_image.width // 2, original_image.height // 2))
    photo_resized = ImageTk.PhotoImage(resized_image)
    
    # Hiển thị ảnh đã thay đổi kích thước trong cửa sổ mới
    zoomed_label = tk.Label(new_window, image=photo_resized)
    zoomed_label.photo = photo_resized
    zoomed_label.pack()

# Tạo cửa sổ
window = tk.Tk()
window.title("Hiển thị và phóng to ảnh")

# Tạo khung chứa các ảnh
frame = tk.Frame(window)
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
window.mainloop()
