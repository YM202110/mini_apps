import os
import sys
from PIL import Image


def convert_heic_to_jpeg(heic_folder_path, jpeg_folder_path):
    for filename in os.listdir(heic_folder_path):
        if filename.endswith('.heic'):
            heic_file_path = os.path.join(heic_folder_path, filename)
            with Image.open(heic_file_path) as im:
                jpeg_file_path = os.path.join(jpeg_folder_path, os.path.splitext(filename)[0] + '.jpeg')
                im.convert('RGB').save(jpeg_file_path, 'JPEG')


if __name__ == '__main__':
    heic_folder_path = sys.argv[1]
    jpeg_folder_path = sys.argv[2]
    convert_heic_to_jpeg(heic_folder_path, jpeg_folder_path)