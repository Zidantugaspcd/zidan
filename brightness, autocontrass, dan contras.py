#in [1]
#import Library yang di perlukan dan untuk imageio digunakan cv2
import numpy as np
import cv2
import matplotlib.pyplot as plt

#in [2]
#load gambar dari file mengunakan cv2 dan cari path 
img = cv2.imread("D:\SEMESTER 6\Pengolahan Citra Digital\image\Boo.jpg")

#in [3]
# mendapat define resolusi dan tipe gambar
img_height =img.shape[0]
img_width =img.shape[1]
img_channel =img.shape[2]
img_type =img.dtype

#Brightness Grayscale
#in [4]
# buat brigness untuk gambar grayscale membuat variabel img_brignest untuk menampung hasil dengan protokol np.zeros
img_brightness = np.zeros(img.shape, dtype = np.uint8)

#in [5]
# membuat fungsi penambahan brigntness dengan nilai yang menjadi parameter disini nilai gray didefinisikan dengan nilai max=225 dan min=0 dengan nested loop
def brighter(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            #untuk mengisi variabel dengan kode masing masing warna pada x dan y
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            # fungsi gray yang berisi nilai RGB/3
            gray = (int(red)+int(green)+int(blue))/3
            gray += nilai
            # inisialisasi nilai max dan min untuk mencegah overflow dan underlow pada fungsi gray
            if gray > 255:
                gray = 255
            if gray < 0:
                gray =0
            img_brightness[y][x]=(gray, gray, gray)

#Brightness RGB
#in [7] 
#Fungsi untuk brigntness RGB dengan nilai parameter
img_rgbbrightness = np.zeros(img.shape, dtype = np.uint8)

#in[8]
# ditambahkan brightness dengan nilai yg menjadi parameter
def rgbbright(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red =img[y][x][0]
            red += nilai
            if red > 255:
                red =255
            if red < 0:
                red = 0
            green =img[y][x][1]
            green += nilai
            if green > 255:
                green =255
            if green < 0:
                green = 0
            blue =img[y][x][2]
            blue += nilai
            if blue > 255:
                blue =255
            if blue < 0:
                blue = 0
            img_rgbbrightness[y][x]=(red, green, blue)

#Contrass
#in [10]
# membuat variabel img_contrass untuk menampung hasil 
img_contrass = np.zeros(img.shape, dtype = np.uint8)
# membuat fungsi penambahan brigntness dengan nilai yang menjadi parameter, disini nilai rgb dijadikan grayscale
def contrass(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue))/3
            gray += nilai
            if gray > 255:
                gray = 255
            img_contrass[y][x] = (gray, gray, gray)


#in[11]
# variabel untuk autocontrass 
img_autocontrass = np.zeros(img.shape, dtype=np.uint8)
# membuat definisi dari auto contrass dengan nilai max, min dan d
def autocontrass():
    xmax = 300
    xmin = 0
    d = 0
# Mendapatkan nilai d, dimana nilai d ini akan berpengaruh pada hitungan
# untuk mendapatkan tingkat kontras
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            if gray < xmax:
                xmax = gray
            if gray > xmin:
                xmin = gray
    d = xmin-xmax
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(float(255/d) * (gray-xmax))
            img_autocontrass[y][x] = (gray, gray, gray)

#buat figur yang berisi plot dengan 4 baris dan 2 kolom
fig, axs = plt.subplots(nrows=4, ncols=2, figsize=(15,8))

#in[6]
# untuk set brightness -100 
brighter(-100)
axs[0,0].imshow(img_brightness)
axs[0,0].set_title('brightness -100')
axs[0,0].axis('off')
# untuk set brightness +100 
brighter(100)
axs[0,1].imshow(img_brightness)
axs[0,1].set_title('brightness +100')
axs[0,1].axis('off')

#in [9]
# untuk set brightness -100 
rgbbright(-100)
axs[1,0].imshow(img_rgbbrightness)
axs[1,0].set_title('rgb brightness -100')
axs[1,0].axis('off')

# untuk set brightness -100 
rgbbright(100)
axs[1,1].imshow(img_rgbbrightness)
axs[1,1].set_title('rgb brightness +100')
axs[1,1].axis('off')

#in [12]
# menampilkan hasil set contrass  2
contrass(2)
axs[2,0].imshow(img_brightness)
axs[2,0].set_title('contrass 2')
axs[2,0].axis('off')
# menampilkan hasil set contrass  2
contrass(3)
axs[2,1].imshow(img_brightness)
axs[2,1].set_title('contras 3')
axs[2,1].axis('off')

# hasil autocontrass
autocontrass()
axs[3,0].imshow(img_autocontrass)
axs[3,0].set_title('auto contras')
axs[3,0].axis('off')

axs[3,1].axis('off')

plt.show()