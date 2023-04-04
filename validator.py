import os

def userValidator(carpeta):
    if os.path.exists(carpeta) and os.path.isdir(carpeta):
        # contar la cantidad de imágenes en la carpeta
        num_images = len([name for name in os.listdir(carpeta) if os.path.isfile(os.path.join(carpeta, name)) and name.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))])
        return num_images
    else:
        print(f"La carpeta '{carpeta}' no existe en el directorio actual o no es una carpeta válida.")
        return 0