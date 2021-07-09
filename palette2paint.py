from PIL import Image

image = Image.open('palette.png')  # Открываем изображение
file = open('palette.txt', 'w') # Открываем txt файл для палитры

size = image.size # Узнаем размеры изображения
pixel = image.load() # Загружаем изображение 

for i in range(size[0]): # Запись палитры в файл, вывод в консоль hex формата

    color_rgb = pixel[i, 0] # Узнаем цвет одного пикселя в rgb
    color_hex = '{:02x}{:02x}{:02x}'.format(*color_rgb) # Конвертация rgb в hex
    print(color_rgb)

    file.write('FF' + color_hex + '\n') # Запись hex в файл и добавление альфа канала
    print(color_hex) # Вывод в консоль