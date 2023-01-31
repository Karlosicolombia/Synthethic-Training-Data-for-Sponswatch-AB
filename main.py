"Authors for this project is Karl Rosengren and Theodor Ahrenius"
"Started 6/2-2023"

import tensorflow as tf
import numpy as np
import pytorch 



"Hello Theodor this is a test"
a = "Tensorflow yes"
print(a)
print(tf.__version__)
"Hello Hello"

#Importera folder av bilder


batch_size = 776
img_height = 256
img_width = 256



directory = 'C:\\Users\\kalle\\Documents\\Exjobb\\football'

train_images = tf.keras.utils.image_dataset_from_directory(
    directory,
    labels=None,
    label_mode='categorical',
    class_names=None,
    color_mode='rgb',
    batch_size=None,
    image_size=(256, 256),
    shuffle=True,
    seed=None,
    validation_split=None,
    subset=None,
    interpolation='bilinear',
    follow_links=False,
    crop_to_aspect_ratio=False,

).take(100)


x_train = None

for image in tfds.as_numpy(train_images):
  x_train = image
  




BUFFER_SIZE = 60000
BATCH_SIZE = 256


x_train = (x_train/255).astype('float32')
