from PIL import Image
import os
import argparse

def rescale_images(directory, size, new_name):
    i = 200
    for img in os.listdir(directory):
        if os.path.isfile(directory+img):
            im = Image.open(directory+img)
            im_res = im.resize(size, Image.ANTIALIAS)
            ##os.remove(directory+img)
            im_res.save(directory+new_name+str(i)+'.JPG')       
            i+=1
    

if __name__ == '__main__' :
    parser = argparse.ArgumentParser(description='rescale images')
    parser.add_argument('-d', '--directory', type=str, required=True, help='directory path')
    parser.add_argument('-s', '--size', type=int, nargs=2, required=True)
    args = parser.parse_args()
    rescale_images(args.directory, args.size, 'BraBel')