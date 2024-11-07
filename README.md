# eUML
eUML is a project for galaxy morphotlogy classification with a voting clustering method based on coding from ConvNeXt large model.   

The method can be summarized into three key aspects as follows.  

(1) Convolutional autoencoder is used for image denoising and reconstruction, and the rotational invariance of the model is improved by polar coordinate extension.   

(2) We utilize a pre-trained convolutional neural network named ConvNeXt for encoding the image data, and the features were further compressed by Principal Component Analysis (PCA) dimensionality reduction.   
    
(3) Bagging-based multi-model voting classification algorithm is adopted to enhance robustness. 

## Data Preprocessing



