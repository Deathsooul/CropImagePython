import os
from PIL import Image

print(os.getcwd())

savedir = os.getcwd() + str('/Image')
filename = os.getcwd() + str('/assets/teste.jpeg')


img = Image.open(filename)
print(img.size)

box = (200, 1950, 1700, 3000)#left, upper, right, lower
cropped_image = img.crop(box)
cropped_image.save('cropped_image.jpg')

# Print size of cropped image
print(cropped_image.size) # Output: (500, 300)



# width, height = img.size

# start_pos = start_x, start_y = (0, 0)
# cropped_image_size = w, h = (64,64)

# frame_num = 1
# for col_i in range(0, width, w):
#     for row_i in range(0, height, h):
#         crop = img.crop((col_i, row_i, col_i + w, row_i + h))
#         save_to= os.path.join(savedir, "counter_{:03}.jpg")
#         crop.save(save_to.format(frame_num))
#         frame_num += 1