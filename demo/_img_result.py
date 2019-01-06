from skimage import data, exposure, img_as_float
import matplotlib.pyplot as plt
from skimage import io

image1 = img_as_float(io.imread('FB003_58_Mirror_140.jpg'))
image2 = img_as_float(io.imread('FB043_161.jpg'))
image3 = img_as_float(io.imread('FB069_41_Mirror_140.jpg'))
image4 = img_as_float(io.imread('output_FB003_58_Mirror_140.png'))
image5 = img_as_float(io.imread('output_FB043_161.png'))
image6 = img_as_float(io.imread('output_FB069_41_Mirror_140.png'))
image7 = img_as_float(io.imread('visualization_FB003_58_Mirror_140.jpg'))
image8 = img_as_float(io.imread('visualization_FB043_161.jpg'))
image9 = img_as_float(io.imread('visualization_FB069_41_Mirror_140.jpg'))

plt.figure('FCN_train_iter_12000',figsize=(8,8))

plt.subplot(331)
plt.title('origin image')
plt.imshow(image1)
plt.axis('off')

plt.subplot(334)
plt.title('origin image')
plt.imshow(image2)
plt.axis('off')

plt.subplot(337)
plt.title('origin image')
plt.imshow(image3)
plt.axis('off')

plt.subplot(332)
plt.title('FCN result')
plt.imshow(image4)
plt.axis('off')

plt.subplot(335)
plt.title('FCN result')
plt.imshow(image5)
plt.axis('off')

plt.subplot(338)
plt.title('FCN result')
plt.imshow(image6)
plt.axis('off')

plt.subplot(333)
plt.title('visualization')
plt.imshow(image7)
plt.axis('off')

plt.subplot(336)
plt.title('visualization')
plt.imshow(image8)
plt.axis('off')

plt.subplot(339)
plt.title('visualization')
plt.imshow(image9)
plt.axis('off')

plt.show()