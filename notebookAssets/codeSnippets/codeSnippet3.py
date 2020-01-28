#The number of class labels == total number of categories which == length of the folders in .dir
data=load_files(dataDir, load_content= False)
total_categories=len(data.category_names)
# input image dimensions
img_rows, img_cols = 64, 64
dataDir= '{{INPUT YOUR TOP LEVEL IMAGE DIR}}'
#The function responsible for connecting the image data with the categories created
def build_data(data):
    X = []
    y = []
    #Operations to assign the categories to data structures
    encoder = LabelBinarizer()
    encoded_dict=dict()
    hotcoded_label = encoder.fit_transform(data.category_names)
    #Matching the category target names to the labels
    for i in range(len(data.category_names)):
        encoded_dict[data.category_names[i]]=hotcoded_label[i]
    for country in os.listdir(dataDir):
        label=encoded_dict[country]
        #labeling the images
        for each_flag in os.listdir(dataDir+'/'+country): 
            actual_path = os.path.join(dataDir,country,each_flag)
            img_data = cv2.imread(actual_path)
            img_data = cv2.resize(img_data, (img_rows, img_cols))
            X.append(np.array(img_data))
            y.append(label)
    #Creating a test and training set split with space for declaed variables
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=36)
    X_train = np.asarray(X_train)
    X_test = np.asarray(X_test)
    y_train = np.asarray(y_train)
    y_test = np.asarray(y_test)
#returns the training and testing set
    return [X_train, X_test, y_train, y_test]