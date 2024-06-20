from PIL import Image
import os

# 创建一个 720x720 的图像
width, height = 720, 720

# 生成从(15,15,15)到(255,255,255)，每隔8递增的颜色列表，（还有一个(0,0,0)和(7,7,7)是每隔7）
colors = [(r, r, r) for r in range(15, 256, 8)]

# 创建保存图片的文件夹
output_folder = "wb"
os.makedirs(output_folder, exist_ok=True)

# 填充图片并保存
for color in colors:
    image = Image.new("RGB", (width, height), color)
    file_name = f"wb{color[0]}_{color[1]}_{color[2]}.png"
    file_path = os.path.join(output_folder, file_name)
    image.save(file_path)
    print(f"Saved {file_path}")

# 打印完成信息
print("All images saved.")
