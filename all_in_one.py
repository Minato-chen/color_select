import numpy as np
from skimage.color import lab2rgb
from color_generate import generate_inducing_colors
from plot import plot_type1, plot_type2, plot_type3


def lab_to_rgb(l, a, b):
    lab_color = np.array([[[l, a, b]]], dtype=np.float32)
    rgb_color = lab2rgb(lab_color)  # Convert to RGB
    rgb_color = np.clip((rgb_color * 255), 0, 255).astype(int)
    return tuple(rgb_color[0][0])  # Return the RGB values


size = 640
dpi = 141
square_size_mm = 0

test_color_lab = (80, -90, 90)
print("Testing color lab(T):", test_color_lab)
test_color_rgb = lab_to_rgb(*test_color_lab)
print("Testing color rgb(T):", test_color_rgb)

inducing_colors_lab = generate_inducing_colors()
print("Inducing Colors lab(C1 to C20):", inducing_colors_lab)
inducing_colors_rgb = [
    tuple(lab_to_rgb(L, a, b)) for (L, a, b) in inducing_colors_lab
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
