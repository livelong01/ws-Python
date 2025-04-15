# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python 😂

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
ORIGINAL_IMAGE_PATH = ROOT_FOLDER / 'original.jpg'
NEW_IMAGE_PATH = ROOT_FOLDER / 'redimensionada.jpg'

# Abrindo a imagem original
pil_image = Image.open(ORIGINAL_IMAGE_PATH)

# capturar a largura e altura da imagem
width, height = pil_image.size
exif = pil_image.info['exif']

# new width // new height

# Redimensionando a imagem para 50% do tamanho original CHATGPT
# new_width = int(width * 0.5)
# new_height = int(height * 0.5)

# Redimensionando a imagem para 640pixs do tamanho original professor
new_width = 640
new_height = int((new_width / width) * height)
print(f'width: {width}, height: {height}')
print(f'new_width: {new_width}, new_height: {new_height}')

# Redimensionando a imagem
resized_image = pil_image.resize(size=(new_width, new_height))
# salvando a imagem redimensionada
resized_image.save(
    NEW_IMAGE_PATH,
    exif=exif,
    optimize=True,
    quality=70,
)
