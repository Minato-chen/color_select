import numpy as np
# import matplotlib.pyplot as plt
from skimage.color import lab2rgb


def new_lab_to_rgb(l, a, b):
    lab_color = np.array(
        [[[l, a, b]]], dtype=np.float32
    )  # Create a 3D array for the Lab color
    rgb_color = lab2rgb(lab_color)  # Convert to RGB
    rgb_color = np.clip((rgb_color * 255), 0, 255).astype(
        int
    )  # Scale to [0, 255] and convert to int
    return tuple(rgb_color[0][0])  # Return the RGB values

# # Example Lab values
# lab_values = [
#     (50, 20, 30),  # Example 1
#     (70, -50, 50),  # Example 2
#     (30, 60, -60),  # Example 3
# ]
#
# # Convert Lab to RGB
# rgb_values = [lab_to_rgb(L, a, b) for (L, a, b) in lab_values]
#
# # Print RGB values
# for i, rgb in enumerate(rgb_values):
#     print(f"Lab {lab_values[i]} -> RGB {rgb}")
#
# # Visualize the colors
# fig, ax = plt.subplots(1, len(rgb_values), figsize=(15, 2))
# for i, rgb in enumerate(rgb_values):
#     ax[i].imshow([[rgb / 255]])  # Divide by 255 to normalize for display
#     ax[i].set_title(f"Lab {lab_values[i]}")
#     ax[i].axis("off")
#
# plt.show()
