from keras.applications import VGG16, VGG19, ResNet50
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from keras.models import Model
from keras.layers import Input, Flatten, Dense
from keras import optimizers
import numpy as np

vgg16 = VGG16(weights='imagenet', include_top=False, pooling='max')

img_path = './post-images-01/05088502_145487.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

features = vgg16.predict(x) # Features for regression

print type(features)
print features.shape # Shape = (1, 512), could be too large
# print features

# print vgg16.summary()

regressionLayer = Dense(128, activation='tanh', name='PCALayer')(vgg16.output)
regressionLayer = Dense(1, activation='relu', name='RegressionLayer')(regressionLayer)
model = Model(input = vgg16.input, output = regressionLayer)

# No need PCA or sklearn: use Keras for both PCA and linear regression 

for layer in model.layers[:20]:
	layer.trainable = False
	print layer.name

# print 'Model summary'
# print model.summary()
# print len(model.layers)

print "Compiling..."
model.compile(loss='binary_crossentropy', optimizer=optimizers.SGD(lr=1e-4, momentum=0.9))

print "Compile done."
