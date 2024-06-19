import os
from PIL import Image, ImageDraw


def plot_type1(rgb_fg, rgb_bg, dpi, square_size_mm, output_dir="./output_type_1"):
    square_size_pixels = round((square_size_mm / 25.4) * dpi)
    #  1 英寸等于 25.4 毫米，所以每 25.4 毫米有 dpi 个像素
    n = 640 // square_size_pixels
    adjusted_size = square_size_pixels * n
    image = Image.new("RGB", (adjusted_size, adjusted_size), rgb_bg)
    draw = ImageDraw.Draw(image)

    for i in range(n):
        for j in range(n):
            color = rgb_fg if (i + j) % 2 == 0 else rgb_bg
            draw.rectangle(
                [
                    i * square_size_pixels,
                    j * square_size_pixels,
                    (i + 1) * square_size_pixels,
                    (j + 1) * square_size_pixels,
                ],
                fill=color,
            )

    filename = (
        f"{square_size_mm}_{rgb_fg[0]}_{rgb_fg[1]}_{rgb_fg[2]}_{rgb_bg[0]}_{rgb_bg[1]}_{rgb_bg[2]}.png"
    )
    output_dir = os.path.join(
        output_dir, "{}_{}_{}".format(square_size_mm, dpi, adjusted_size)
    )
    os.makedirs(output_dir, exist_ok=True)
    image.save(os.path.join(output_dir, filename))
    print(f"Saved image as {filename}")


def plot_type2(rgb_fg, rgb_bg, dpi, square_size_mm, output_dir="./output_type_2"):
    square_size_pixels = round((square_size_mm / 25.4) * dpi)
    #  1 英寸等于 25.4 毫米，所以每 25.4 毫米有 dpi 个像素
    n = 640 // square_size_pixels
    adjusted_size = square_size_pixels * n

    image = Image.new("RGB", (adjusted_size, adjusted_size), rgb_bg)
    draw = ImageDraw.Draw(image)

    for i in range(n):
        color = rgb_fg if i % 2 == 0 else rgb_bg
        draw.rectangle(
            [
                i * adjusted_size // n,  # Left
                0,  # Top
                (i + 1) * adjusted_size // n,  # Right
                adjusted_size,  # Bottom
            ],
            fill=color,
        )

    filename = (
        f"{square_size_mm}_{rgb_fg[0]}_{rgb_fg[1]}_{rgb_fg[2]}_{rgb_bg[0]}_{rgb_bg[1]}_{rgb_bg[2]}.png"
    )
    output_dir = os.path.join(
        output_dir,
        "{}_{}_{}".format(square_size_mm, dpi, adjusted_size),
    )
    os.makedirs(output_dir, exist_ok=True)
    image.save(os.path.join(output_dir, filename))
    print(f"Saved image as {filename}")


def plot_type3(rgb_fg, rgb_bg, dpi, square_size_mm, output_dir="./output_type_3"):
    size = 640
    square_size_pixels = round((square_size_mm / 25.4) * dpi)

    # 计算尽量接近 640 的 n 值
    n = 640 // square_size_pixels

    # 动态计算网格线的宽度，使其与方块大小保持合理比例
    stripe_width = max(1, round(square_size_pixels / 5))

    # 创建一个填充前景色的图像
    image = Image.new("RGB", (size, size), rgb_fg)
    draw = ImageDraw.Draw(image)

    # 画垂直网格线
    for i in range(n + 1):
        left = i * size // n - stripe_width // 2
        right = i * size // n + stripe_width // 2
        draw.rectangle([left, 0, right, size], fill=rgb_bg)

    # 画水平网格线
    for i in range(n + 1):
        top = i * size // n - stripe_width // 2
        bottom = i * size // n + stripe_width // 2
        draw.rectangle([0, top, size, bottom], fill=rgb_bg)

    # 保存图像
    filename = (
        f"{square_size_mm}_{rgb_fg[0]}_{rgb_fg[1]}_{rgb_fg[2]}_{rgb_bg[0]}_{rgb_bg[1]}_{rgb_bg[2]}.png"
    )
    output_dir = os.path.join(
        output_dir,
        "{}_{}_{}".format(square_size_mm, dpi, size),
    )
    os.makedirs(output_dir, exist_ok=True)
    image.save(os.path.join(output_dir, filename))
    print(f"Image saved as {filename}")


def plot_measure_use(rgb, size=640, output_dir="./cs2000use_output"):
    image = Image.new("RGB", (size, size), rgb)
    image.save("cs2000use.png")
    # 保存图像
    filename = (
        f"{size}_{rgb[0]}_{rgb[1]}_{rgb[2]}.png"
    )

    os.makedirs(output_dir, exist_ok=True)
    image.save(os.path.join(output_dir, filename))
    print(f"Image saved as {filename}")
