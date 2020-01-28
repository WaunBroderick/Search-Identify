#Move through the designated root directory and traverse through the individual files inside
for subdir, dirs, files in os.walk(rootdir):
    print("working in " +subdir)
#Add all extensions necessary in the 'or file.endswith(".xx")' format
    for file in files:
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
            count += 1
            #Loading the image
            img = load_img(subdir + "/" + file)
            #The Numpy array responsible for shapes adherence
            x = img_to_array(img) 
            x = x.reshape((1,) + x.shape)
            # the .flow() command below generates batches of randomly transformed images
            # and saves the results to the `preview/` directory
            i = 0
            for batch in datagen.flow(x, batch_size=1,
                                      save_to_dir= subdir + "/", save_prefix='DA', save_format='jpg'):
                i += 1
                #Set to desired iterations
                if i > 3:
                    #Setting bound to break loop so to avoid indefinite run
                    break