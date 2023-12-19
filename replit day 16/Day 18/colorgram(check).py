import colorgram

colors = colorgram.extract('image.jpg', 21)
rgb_colors = []
for color in colours:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)