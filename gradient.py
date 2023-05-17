import tkinter as tk

# Tạo cửa sổ
window = tk.Tk()
window.title("Hình nền gradient")

# Tạo một canvas để vẽ hình nền
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Tạo gradient màu
gradient_start_color = "#2980B9"  
gradient_end_color = "#6DD5FA"    

# Vẽ gradient trên canvas
for i in range(400):
    # Tính toán màu sắc tại mỗi điểm trên gradient
    r = int((1 - i/400) * int(gradient_start_color[1:3], 16) + (i/400) * int(gradient_end_color[1:3], 16))
    g = int((1 - i/400) * int(gradient_start_color[3:5], 16) + (i/400) * int(gradient_end_color[3:5], 16))
    b = int((1 - i/400) * int(gradient_start_color[5:7], 16) + (i/400) * int(gradient_end_color[5:7], 16))
    color = f"#{r:02x}{g:02x}{b:02x}"

    # Vẽ một đường ngang với màu gradient tại mỗi điểm trên canvas
    canvas.create_line(0, i, 400, i, fill=color)

# Chạy vòng lặp chính của ứng dụng
window.mainloop()
