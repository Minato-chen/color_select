import numpy as np


def generate_inducing_colors(radius_large=127, radius_small=63):
    inducing_colors = []

    # 大圆上的点 (C1到C10)
    for i in range(10):
        angle_deg = i * 36
        angle_rad = np.radians(angle_deg)
        a = radius_large * np.cos(angle_rad)
        b = radius_large * np.sin(angle_rad)
        inducing_colors.append((80, round(a), round(b)))

    # 小圆上的点 (C11到C20)
    for i in range(10):
        angle_deg = i * 36
        angle_rad = np.radians(angle_deg)
        a = radius_small * np.cos(angle_rad)
        b = radius_small * np.sin(angle_rad)
        inducing_colors.append((80, round(a), round(b)))

    return inducing_colors


'''
结果是一个list，包含20个元组，每个元组是一个颜色的lab值，如下： [(80, 127, 0), (80, 0, 127), (80, -127, 0), (80, 0, -127), (80, 111, 64), 
(80,64, 111), (80, -64, 111), (80, -111, 64), (80, -111, -64), (80, -64, -111), (80, 64, -111), (80, 111, -64),
(80,63, 36), (80, 36, 63), (80, -36, 63), (80, -63, 36), (80, -63, -36), (80, -36, -63), (80, 36, -63), (80, 63, -36)]
'''
