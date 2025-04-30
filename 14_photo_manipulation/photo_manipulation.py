from PIL import Image 

if __name__ == "__main__":
    with Image.open('./images/image.jpg') as img:
        print(img.size)
        img.save('./saved/new_image.png')