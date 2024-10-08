# -*- coding: utf-8 -*-
"""Manipulate Image.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11kMT7dFoAlMM0_dGiMeVL5n56pOq8rko
"""

!pip install pillow

from google.colab import files
uploaded = files.upload()

from PIL import Image
import numpy as np
from google.colab import files

# Function to encrypt the image
def encrypt_image(image_path, key):
    # Open image
    img = Image.open(image_path)
    img_array = np.array(img)

    # Apply basic operation on pixel values (adding key to pixel values)
    encrypted_img_array = (img_array + key) % 256

    # Convert the array back to an image
    encrypted_img = Image.fromarray(np.uint8(encrypted_img_array))

    return encrypted_img

# Function to decrypt the image
def decrypt_image(encrypted_img, key):
    # Convert encrypted image to array
    encrypted_img_array = np.array(encrypted_img)

    # Subtract the key from pixel values to decrypt
    decrypted_img_array = (encrypted_img_array - key) % 256

    # Convert the array back to an image
    decrypted_img = Image.fromarray(np.uint8(decrypted_img_array))

    return decrypted_img

# Main code for running the encryption and decryption
def main():
    # Upload the image
    uploaded = files.upload()

    # Get the uploaded image's filename
    image_path = list(uploaded.keys())[0]  # Use the first uploaded file

    # Key for encryption (integer value to manipulate pixel values)
    key = 50

    # Encrypt the image
    encrypted_image = encrypt_image(image_path, key)
    encrypted_image.show()  # This will display the encrypted image in Colab

    # Save the encrypted image
    encrypted_image.save('encrypted_image.jpg')

    # Decrypt the image
    decrypted_image = decrypt_image(encrypted_image, key)
    decrypted_image.show()  # This will display the decrypted image in Colab

    # Save the decrypted image
    decrypted_image.save('decrypted_image.jpg')

# Call the main function
main()

files.download('encrypted_image.jpg')
files.download('decrypted_image.jpg')