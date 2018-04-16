from PIL import Image,ImageFilter

nom_img = input()
n_pixel = int(input())
img_orig = Image.open(nom_img)
tamaño = (3,3)
cruz = n_pixel/2
esquina = n_pixel/4
coef = [esquina,cruz,esquina,cruz,n_pixel,cruz,esquina,cruz,esquina]
img_fin = img_orig.filter(ImageFilter.kernel(tamaño,coef))
img_fin.save('suave.pgn')

img_orig.close()
img_fin.close()
