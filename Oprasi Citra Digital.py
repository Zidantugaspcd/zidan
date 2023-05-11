# Oprasi Dasar Citra Digital
# import library yang diperlukan
import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage import data
from skimage.color import rgb2gray 

# 1. Cropping Image
# panggil direktori path gambar dari file
Totoro= cv2.imread("D:\SEMESTER 6\Pengolahan Citra Digital\image\Totoro.jpeg")
Spirit= cv2.imread("D:\SEMESTER 6\Pengolahan Citra Digital\image\Spirit away.jpeg")
# croping image sesuai ukuran yang di inginkan dengan mengukur posisi vektor[range tinggi,range lebar]
TotoroCropped = np.copy(Totoro[100:400,100:380])
SpiritCropped = np.copy(Spirit[750:1100,200:450])
# tampilkan pada terminal ukuran gambar asli dan hasil crop
print('Totoro ori: ',Totoro.shape)
print('Totoro Crop: ',TotoroCropped.shape)
print('Spirit ori: ',Spirit.shape)
print('Spirit Crop: ',SpiritCropped.shape)
#subplot gabar di tampilkan pada satu figur 2 kolom 2 baris sebagai perbandingan
fig, axes = plt.subplots(2,2, figsize=(12,12))
ax = axes.ravel()
# urutkan gambar sesuai axes
ax[0].imshow(Totoro)
ax[0].set_title("Image Totoro")
ax[1].imshow(Spirit)
ax[1].set_title('Image Spirit Away')
ax[2].imshow(TotoroCropped)
ax[2].set_title("Crop Totoro")
ax[3].imshow(SpiritCropped)
ax[3].set_title('Crop Spirit Away')

# 2. Citra Negative
invspirit = np.invert(Spirit)
print('Shape Input : ', Spirit.shape)
print('Shape Output : ',invspirit.shape)
# buta figur untuk plot nilai dari citra asli dan citra negative
fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()
ax[0].imshow(Spirit)
ax[0].set_title("Citra asli")
ax[1].hist(Spirit.ravel(), bins=256)
ax[1].set_title('Histogram citra asli')
ax[2].imshow(invspirit)
ax[2].set_title('Citra negative (Inverted Image)')
ax[3].hist(invspirit.ravel(), bins=256)
ax[3].set_title('Histogram citra negative')

# 3.brightness
# import data kamera dari library skimage

# mengubah mentuk variabel menjadi data float
copytotoro = TotoroCropped.copy().astype(float)
# menentukan dimensi dari gambar dengan memisahkan nilai tinggi dan lebar
brightness =100
totorobright = np.clip(copytotoro+ brightness,0,255).astype(dtype=np.uint8)
 # buat figur untuk menampilkan subplo ukuran 2 x 2        
fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()
ax[0].imshow(cv2.cvtColor(Totoro, cv2.COLOR_BGR2RGB))
ax[0].set_title("Citra Input")
ax[1].hist(TotoroCropped.ravel(), bins=256)
ax[1].set_title('Histogram Input')
ax[2].imshow(cv2.cvtColor(totorobright, cv2.COLOR_BGR2RGB))
ax[2].set_title('Citra Output (Brightnes)')
ax[3].hist(totorobright.ravel(), bins=256)
ax[3].set_title('Histogram Input')
# tampilkan gambar
plt.show()