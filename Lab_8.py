# Написать функцию, которая принимает путь к изобра- жению и создает
# отраженное изображение, сохраняя его по тому же пути.

from PIL import Image, ImageOps

im = Image.open('/Users/southrussian/PycharmProjects/Laboratories/floppa.png')
im_mirror = ImageOps.mirror(im)
im_mirror.save('/Users/southrussian/PycharmProjects/Laboratories/floppa.png', quality=95)



