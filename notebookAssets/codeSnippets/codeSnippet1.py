#A series of operations that were selected to apply to images to create a greater amount of image variation
datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')
#root directory for data augmentation
rootdir = '{{ENTER YOUR DIRECTORY}}'