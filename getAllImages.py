import os
path = "img/galerie"
all_images = os.listdir(path)

for image in all_images:
    print(f"<img src=\"{path}/{image}\" loading=\"lazy\">")
