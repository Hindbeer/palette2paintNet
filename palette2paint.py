from PIL import Image

palette_name = input(str('Название файла палитры( расширение .png указывать не надо ): '))

image = Image.open(palette_name + '.png')  # Открываем изображение
file = open(palette_name + '.txt', 'w') # Открываем txt файл для палитры

size = image.size # Узнаем размеры изображения
pixel = image.load() # Загружаем изображение 

for i in range(size[0]): # Запись палитры в файл, вывод в консоль hex формата

    color_rgb = pixel[i, 0] # Узнаем цвет одного пикселя в rgb
    color_hex = '{:02x}{:02x}{:02x}'.format(*color_rgb) # Конвертация rgb в hex

    file.write('FF' + color_hex + '\n') # Запись hex в файл и добавление альфа канала
    print('FF' + color_hex) # Вывод в консоль

file = open(palette_name + '.txt', 'a+')
file.write(';Палитра сделана через palette2paintNet\n;https://github.com/lukovi4ka/palette2paintNet')
input('Готово, нажмите на enter чтобы закрыть...')