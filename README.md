# eUML
eUML is a project for galaxy morphotlogy classification with a voting clustering method based on coding from ConvNeXt large model.   

The method can be summarized into three key aspects as follows.  

(1) Convolutional autoencoder is used for image denoising and reconstruction, and the rotational invariance of the model is improved by polar coordinate extension.   

(2) We utilize a pre-trained convolutional neural network named ConvNeXt for encoding the image data, and the features were further compressed by Principal Component Analysis (PCA) dimensionality reduction.   
    
(3) Bagging-based multi-model voting classification algorithm is adopted to enhance robustness. 

 ##Data Preprocessing

0. **`python readimg_fits.py`**  
   Reads raw `.fits` files, converts them to `.png` format, and saves the images in the `fit_img/` folder.

1. **Configure `config.py`**  
   Configure model parameters such as image size and kernel size (if performance is not satisfactory, consider increasing the size, e.g., change `[3, 3, 1, 16]` to `[5, 5, 1, 16]`). If the `the_dim` parameter is too large to run, consider reducing its size (e.g., by half).

2. **`python MAIN.py --train True`**  
   Trains the model for autoencoding, with support for checkpoint continuation.

3. **`python MAIN.py --test True`**  
   Outputs the denoised images in the `cae_img/` folder.

4. **`python polar.py`**  
   Converts images in `cae_img/` to polar coordinate images and saves them in the `polar_img/` folder.

##clustering
