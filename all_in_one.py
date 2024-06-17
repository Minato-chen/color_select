from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color

from color_generate import generate_inducing_colors
from plot import plot_type1, plot_type2, plot_type3


def lab_to_rgb(lab):
    rgb = convert_color(lab, sRGBColor)
    # Clamp the values to be between 0 and 1 before converting to 0-255 range
    rgb_values = (
        round(min(max(rgb.rgb_r, 0.0), 1.0) * 255),
        round(min(max(rgb.rgb_g, 0.0), 1.0) * 255),
        round(min(max(rgb.rgb_b, 0.0), 1.0) * 255),
    )
    return rgb_values


size = 640
dpi = 94
# 自己的笔记本141dpi，1920x1080分辨率15.6英寸屏幕
# 实验室94dpi，1920x1200分辨率24.1英寸屏幕
square_size_mm = 0

test_color_lab = (80, -90, 90)
# (80, -90, 90)
'''
LAB: (80, 60, 20) - Approximate RGB: (255, 195, 142)
理由: 这个颜色在a值（红/绿轴）上偏向正值，在b值（黄/蓝轴）上也偏向正值，因此这是一个暖色调的颜色（橙色系）。这有助于研究暖色调混合时的色彩变化。
LAB: (80, -60, -60) - Approximate RGB: (0, 196, 255)
理由: 这个颜色在a值和b值上都偏向负值，呈现出冷色调（蓝绿色系）。这有助于研究冷色调混合时的色彩变化。
LAB: (80, 50, -50) - Approximate RGB: (206, 201, 255)
理由: 这个颜色在a值上偏正值，在b值上偏负值，形成紫色调。紫色是一个混合了红色和蓝色的颜色，具有很强的对比性，适合观察混色效果。
LAB: (80, -50, 50) - Approximate RGB: (51, 233, 33)
理由: 这个颜色在a值上偏负值，在b值上偏正值，形成黄绿色调。黄色和绿色都是很鲜明的颜色，容易观察到混色效果。
LAB: (80, 0, -80) - Approximate RGB: (116, 209, 255)
理由: 这个颜色在a值上为0，在b值上偏负值，形成一种纯蓝色调。蓝色是基础颜色之一，与其他颜色混合时，效果明显且容易观察。

'''
print("Testing color lab(T):", test_color_lab)
test_color_rgb = lab_to_rgb(LabColor(*test_color_lab))
print("Testing color rgb(T):", test_color_rgb)

inducing_colors_lab = generate_inducing_colors()
print("Inducing Colors lab(C1 to C20):", inducing_colors_lab)
inducing_colors_rgb = [
    tuple(lab_to_rgb(LabColor(L, a, b))) for (L, a, b) in inducing_colors_lab
]
print("Inducing Colors rgb(C1 to C20):", inducing_colors_rgb)
rgb_fg = test_color_rgb

for i in range(7):  # i=0,1,2,3,4,5,6
    if i == 0:
        square_size_mm = 1.25
    else:
        square_size_mm = square_size_mm + 1
    for rgb_bg in inducing_colors_rgb:
        plot_type1(rgb_fg, rgb_bg, dpi, square_size_mm, output_dir="./output_type_1")
        plot_type2(rgb_fg, rgb_bg, dpi, square_size_mm, output_dir="./output_type_2")
        plot_type3(rgb_fg, rgb_bg, dpi, square_size_mm, output_dir="./output_type_3")
