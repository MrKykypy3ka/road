from PIL import Image
import os


def color_load():
    name = 'data/map.png'
    im = Image.open(name).convert('RGB')
    result = Image.new('RGB', im.size)
    center = im.getpixel((325, 225))
    print(center)
    result.save('data/map.png')


def trafficlight():
    im_analyser = Image.open('data/traficlight1.png').convert('RGB')
    im_trafficlight = Image.open('data/traficlight.png').convert('RGB')
    w1, h1 = im_analyser.size
    w2, h2 = im_trafficlight.size
    maximus = 0
    count = 0
    for i in range(w2):
        for j in range(h2):
            if im_analyser.getpixel((i, j)) == im_trafficlight.getpixel((i, j)):
                count += 1
    print(count / (w2 * h2) * 100)
    # for i in range(w1 - w2):
    #     for j in range(h1 - h2):
    #         count = 0
    #         for i2 in range(w2):
    #             for j2 in range(h2):
    #                 if im_analyser.getpixel((i, j)) == im_trafficlight.getpixel((i2, j2)):
    #                     count += 1
    #         maximus = max(maximus, count)
    # print(maximus)



if __name__ == "__main__":
    os.chdir(r'C:\Users\olegm\Documents\GitHub\road')
    trafficlight()
