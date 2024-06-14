import csv
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color
from color_generate import generate_inducing_colors


# 元组LabColor函数转化为字典,字典入,元组出
def lab_to_rgb(lab):
    rgb = convert_color(lab, sRGBColor)
    # Clamp the values to be between 0 and 1 before converting to 0-255 range
    rgb_values = (
        round(min(max(rgb.rgb_r, 0.0), 1.0) * 255),
        round(min(max(rgb.rgb_g, 0.0), 1.0) * 255),
        round(min(max(rgb.rgb_b, 0.0), 1.0) * 255),
    )
    return rgb_values


def write_lab_to_csv(lab_tuples, csv_filename):
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write header
        writer.writerow(['L', 'a', 'b', 'R', 'G', 'B'])

        for lab in lab_tuples:
            L, a, b = lab
            R, G, B = lab_to_rgb(LabColor(L, a, b))
            writer.writerow([L, a, b, R, G, B])


def main():
    # 输出CSV文件名
    csv_filename = 'output.csv'
    # 假设lab_tuples是一个包含(L, a, b)三维元组的列表
    lab_tuples = generate_inducing_colors()

    # 将LAB值和转换后的RGB值写入CSV
    write_lab_to_csv(lab_tuples, csv_filename)
    print(f"CSV file '{csv_filename}' created successfully.")


if __name__ == "__main__":
    main()
