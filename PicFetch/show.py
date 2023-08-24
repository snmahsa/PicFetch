from .dependencies import *
from .path import *


def imshow(image):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    

def show_multi_images_plt(images, rows, columns,img_titles, vmin=0, vmax=255):

    fig = plt.figure(figsize=(15, 17), dpi=100)

    for i in range(len(images)):
        fig.add_subplot(rows, columns, i+1)
        plt.imshow(images[i], cmap='gray', vmin=vmin, vmax=vmax)
        plt.axis('off')
        plt.title(img_titles[i])        
     
