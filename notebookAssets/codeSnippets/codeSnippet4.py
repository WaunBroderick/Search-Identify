#epochs = number of passes through entire training set
epochs = 100
def create_model(input_shape,classes):
    #Takes the specifications of the image inputted
    img_input = Input(shape=input_shape)
    #The following is an architecture structuring
    x = Conv2D(64, (3, 3), activation='relu', padding='same', name='block1_conv1')(img_input)
x = MaxPooling2D((2, 2), strides=(2, 2), name='block1_pool')(x)
    x = Conv2D(128, (3, 3), activation='relu', padding='same', name='block2_conv1')(x)
    
    x = MaxPooling2D((2, 2), strides=(2, 2), name='block2_pool')(x)
    x = Conv2D(256, (3, 3), activation='relu', padding='same', name='block3_conv1')(x)
    
    x = MaxPooling2D((2, 2), strides=(2, 2), name='block3_pool')(x)
    x = Conv2D(64, (3, 3), activation='relu', padding='same', name='block4_conv1')(x)
    
    x = MaxPooling2D((2, 2), strides=(2, 2), name='block4_pool')(x)
    x = Conv2D(128, (3, 3), activation='relu', padding='same', name='block5_conv1')(x)
    
    x = MaxPooling2D((2, 2), strides=(2, 2), name='block5_pool')(x)
    
    x = Flatten(name='flatten')(x)
    x = Dense(512, activation='relu', name='fc1')(x)
    x = Dropout(0.2)(x)
    x = Dense(256, activation='relu', name='fc2')(x)
    x = Dropout(0.2)(x)
    x = Dense(classes, activation='softmax', name='final_output')(x)
model = Model(img_input, x, name='flag')
    return model