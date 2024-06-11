dpi = 141
# for i in range(16, 64, 8):
#     pixel = 640 / i
#     width = 25.4 * pixel / dpi
#     print(i, width)

for width in range(1, 8):
    n = round(640 / (width * dpi / 25.4))
    # n = 640 / (width * dpi / 25.4)
    real_width = 640 / n * 25.4 / dpi
    print(width, n, real_width)
# 1 115 1.0025285229725562
# 2 58 1.987772071411103
# 3 38 3.033967898469578
# 4 29 3.975544142822206
# 5 23 5.012642614862781
# 6 19 6.067935796939156
# 7 16 7.205673758865248

# width = 7.2对应n=16
# width = 6对应n=19
# width = 5对应n=23
# width = 4对应n=29
# width = 3对应n=38
# width = 2对应n=58
# width = 1对应n=115
