import math
def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1 
    while baixo <= alto:
        meio = math.floor((baixo + alto) / 2)
        chute = lista[meio]
        if chute == item:
            return lista[meio]
        if chute > item:
            alto =  meio - 1
        else:
            baixo = meio + 1
    return None

lista_ordenada = list(range(1, 256))
minha_lista = [1, 3, 5, 7 , 9 ]
print( pesquisa_binaria(minha_lista, 3))
   
print(pesquisa_binaria(minha_lista, - 1))    # None

print(pesquisa_binaria(lista_ordenada, 17))

# from PIL import Image

# # Paths to the individual images
# image_paths = [
#     "/mnt/data/A_minimalist,_stylized_black_image_with_two_large,.png",
#     "/mnt/data/A_minimalist,_stylized_white_image_with_two_large,.png",
#     "/mnt/data/A_minimalist,_stylized_image_of_a_person_sitting_o.png",
#     "/mnt/data/A_minimalist,_stylized_image_of_a_person_sitting_a.png"
# ]

# # Open the images
# images = [Image.open(path) for path in image_paths]

# # Determine the size of the final image
# width, height = images[0].size
# final_image = Image.new("RGB", (width * 2, height * 2))

# # Paste images into the final image
# final_image.paste(images[0], (0, 0))
# final_image.paste(images[1], (width, 0))
# final_image.paste(images[2], (0, height))
# final_image.paste(images[3], (width, height))

# # Save the final image
# final_image_path = "/mnt/data/quadrinho_completo.png"
# final_image.save(final_image_path)

# final_image_path
     