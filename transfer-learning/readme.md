# Techniques used in Transfer learning.

#### In general, there are two types of transfer learning when applied to deep learning for computer vision:
..* Treating networks as arbitrary feature extractors.
..* Removing the fully-connected layers of an existing network, by placing a new FC layer set on top of the CNN, and fine-tuning these weights (and optionally previous layers)  to recognize object classes.

#### For detailed usage and understanding of the process please visit the following [medium post](https://medium.com/@hd150295).

#### In case if you want to skip reading the blog you can follow these steps:
1. First clone or download this repo into you local directory.
2. Unzip the dataset which is the animals dataset or create your own dataset but please do not change the directory structure.
3. First run the feature_extractor.py script for extracting the features from the target dataset.
..* Usage: "python feature_extractor.py -d "path to the target dataset" -o "path for storing the creating the extracted feature file in hdf5 format"". 
4. After extracting the features now run the training.py script for training the image classifier.
..* Usage: "python training.py -d path for acessing the features.hdf5 file -m "path for storing the model pickle file""
