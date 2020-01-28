def train_model(x_train, x_test, y_train, y_test):
    input_shape=(img_rows,img_cols,3)
    model=create_model(input_shape,total_countries)
    adams=optimizers.Adam(lr=1e-4)
    model.compile(loss='categorical_crossentropy',
                optimizer= adams,
                metrics=['accuracy'])
    model.fit(x = x_train, y = y_train, epochs=epochs)
    score = model.evaluate(x_test, y_test, verbose=1)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])
    model.save('flagFinder.model')   
    return model