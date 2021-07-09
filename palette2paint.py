from PIL import Image

image = Image.open('palette.png')  # Открываем изображение
file = open('palette.txt', 'w') # Открываем txt файл для палитры

size = image.size # Узнаем размеры изображения
pixel = image.load() # Загружаем изображение 

for i in range(size[0]): # Запись палитры в файл, вывод в консоль hex формата

    color_rgba = pixel[i, 0] # Узнаем цвет одного пикселя в rgba
    color_hex = '{:02x}{:02x}{:02x}'.format(*color_rgba) # Конвертация rgba в hex

    file.write(color_hex + '\n') # Запись hex в файл
    print(color_hex) # Вывод в консоль