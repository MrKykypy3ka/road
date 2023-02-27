from PIL import Image
import os
from time import sleep


def color_load():
    name = 'data/map.png'
    im = Image.open(name).convert('RGB')
    result = Image.new('RGB', im.size)
    center = im.getpixel((325, 225))
    print(center)
    result.save('data/map.png')


def trafficlight():
    im_analyser = Image.open('data/traficlight.png').convert('RGB')
    im_trafficlight = Image.open('data/traficlight1.png').convert('RGB')

    w1, h1 = im_analyser.size
    w2, h2 = im_trafficlight.size
    new = im_analyser.crop((310, 189, 310+w2, 189+h2))
    new.save('cut.jpg', quality=100)

    maximus = 0
    count = 0
    for i in range(w2):
        for j in range(h2):
            if im_analyser.getpixel((i, j)) == im_trafficlight.getpixel((i, j)):
                count += 1
    print(f'{round(count / (w2 * h2) * 100, 2)} %')
    # flag = False
    # for i in range(310, 311):
    #     # if flag is True:
    #     #     break
    #     for j in range(189, 190):
    #         count = 0
    #         for i2 in range(w2):
    #             for j2 in range(h2):
    #                 if im_analyser.getpixel((i, j)) == im_trafficlight.getpixel((j2, j2)):
    #                     count += 1
    #                 print(i2, j2)
    #         maximus = max(maximus, count)
    #         print(f'{round(maximus / (w2 * h2) * 100, 2)} %')
    #         print(maximus)
    #         # if maximus == 2069:
    #         new = im_analyser.crop((i, j, i + w2, j + h2))
    #         new.save('cut2.jpg', quality=100)
            # flag = True
            # break

    print(maximus)

if __name__ == "__main__":
    # os.chdir(r'C:\Users\olegm\Documents\GitHub\road')
    os.chdir(r'C:\Users\Олег\PycharmProjects\road')
    trafficlight()
