try:
    from PIL import Image, ImageCms
    from pyswizzle import nsw_deswizzle, nsw_swizzle
    #import numpy as np
except ImportError as e:
    print(f"An import error occurred: {e}")


def gammaedit(img:Image, gamma = 0.4545):
    return img.point(lambda x: ((x / 255) ** gamma) * 255)

print('''

    Tomodachi Life: Living the Dream
    Facepaint Tool
    By Timimimi
    Thanks to RealDarkCraft for helping me with the format
    I kinda just made this script to help some friends with this
    Uses Aclios' pyswizzle library and Pillow, the friendly PIL fork (python-pillow.org).
''')
while True:
    print('''
    -------
    Functions
    -------
    1. Canvas to PNG
    2. PNG to Canvas
    3. Exit
''')
    try:
        select = int(input("Select an option: "))
        if select == 1:
            imagePath = input("Enter canvas filepath: ")

            with open(imagePath, 'rb') as file:
                rawdata = file.read()

            gob_w, gob_h = 1, 1
            bytes_per_block = 4
            swizzle_mode = 4
            height, width = 256,256

            swizzled = nsw_deswizzle(rawdata,(width, height),(gob_w, gob_h),bytes_per_block,swizzle_mode)

            img = Image.frombytes('RGBA',(256,256), swizzled, 'raw', 'RGBA')
            img = img.convert()
            img = gammaedit(img)
            img.show()
            savepath = imagePath.split('.')[0]+'OUTPUT'+'.png'
            img.save(savepath,'png')
        elif select ==2:
            imagePath = input("Enter png filepath: ")
            useSrgb = False
            while True:
                try:
                    miitopi = input("Is your image ripped from Miitopia? This means it is in sRGB. (Y/N)")
                    if miitopi.upper() == 'Y':
                        useSrgb = True
                        break
                    elif miitopi.upper() == 'N':
                        break
                    else:
                        print('Invalid input...Try that again.')
                except:
                    print("Invalid input...Okay man let's try that again...")
            with open(imagePath, 'rb') as file:
                rawdata = file.read()

            img = Image.open(imagePath)
            if not useSrgb:
                img = gammaedit(img,2.2)
            img = img.convert('RGBA')
            convertImg = img.tobytes('raw')
            savepath = imagePath.split('.')[0]+'OUTPUT'+'.canvas'
            gob_w, gob_h = 1, 1
            bytes_per_block = 4
            swizzle_mode = 4
            height, width = img.size

            linear = nsw_swizzle(convertImg,(width, height),(gob_w, gob_h),bytes_per_block,swizzle_mode)
            with open(savepath, 'wb') as f:
                f.write(bytes(linear))
        elif select == 3:
            print('Alright, see ya~')
            break
        else:
            print('Invalid input. Please try again.')
    except ValueError:
        print('woah man can you input a number please?')