import pandas as pd
from plot import plot_measure_use
import os

df = pd.read_csv('inducer_color_reference.csv')

rgb_data = df[['R_inducer', 'G_inducer', 'B_inducer']].values

for rgb in rgb_data:
    rgb_value = tuple([int(rgb[0]), int(rgb[1]), int(rgb[2])])
    print(rgb_value)
    plot_measure_use(rgb_value, 640, output_dir="./cs2000use_output")
