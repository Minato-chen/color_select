import numpy as np


def generate_inducing_colors(radius_large=127, radius_small=63):
    inducing_colors = []

    # 大圆上的点 (C1到C10)
    for i in range(8):
        angle_deg = i * 45
        angle_rad = np.radians(angle_deg)
        a = radius_large * np.cos(angle_rad)
        b = radius_large * np.sin(angle_rad)
        inducing_colors.append((80, round(a), round(b)))

    # # 小圆上的点 (C11到C20)
    # for i in range(10):
    #     angle_deg = i * 36
    #     angle_rad = np.radians(angle_deg)
    #     a = radius_small * np.cos(angle_rad)
    #     b = radius_small * np.sin(angle_rad)
    #     inducing_colors.append((80, round(a), round(b)))

    return inducing_colors
