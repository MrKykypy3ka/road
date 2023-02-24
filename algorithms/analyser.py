from PIL import Image


def analyser():
    im = Image.open('data/map.png')
    result = Image.new('RGB', im.size)
    center = im.getpixel((325, 225))
    print(center)
    #result.putpixel((i, j), (s, s, s))
    return result.save("out.png")


if __name__ == "__main__":
    analyser()
