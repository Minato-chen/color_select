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
square_size_mm = 0  # 初始化

test_color_lab = (80, -90, 90)
# (80, -90, 90)

print("Testing color lab(T):", test_color_lab)
test_color_rgb = lab_to_rgb(LabColor(*test_color_lab))
print("Testing color rgb(T):", test_color_rgb)

inducing_colors_lab = generate_inducing_colors()
print("Inducing Colors lab(C1 to C8):", inducing_colors_lab)
inducing_colors_rgb = [
    tuple(lab_to_rgb(LabColor(L, a, b))) for (L, a, b) in inducing_colors_lab
]
print("Inducing Colors rgb(C1 to C20):", inducing_colors_rgb)
rgb_fg = test_color_rgb

# for i in range(7):  # i=0,1,2,3,4,5,6
#     if i == 0:
#         square_size_mm = 1.25
#     else:
#         square_size_mm = square_size_mm + 1
#     for rgb_bg in inducing_colors_rgb:
#         plot_type1(rgb_fg, rgb_bg, dpi, square_size_mm, output_dir="./output_type_1")
#         plot_type2(rgb_fg, rgb_bg, dpi, square_size_mm, output_dir="./output_type_2")
#         plot_type3(rgb_fg, rgb_bg, dpi, square_size_mm, output_dir="./output_type_3")


square_size_list = [2.5, 5, 10, 20, 40]

for square_size_mm in square_size_list:
    for rgb_bg in inducing_colors_rgb:
        plot_type1(rgb_fg, rgb_bg, dpi, square_size_mm, output_dir="./output_type_1")
        plot_type2(rgb_fg, rgb_bg, dpi, square_size_mm, output_dir="./output_type_2")
        plot_type3(rgb_fg, rgb_bg, dpi, square_size_mm, output_dir="./output_type_3")
