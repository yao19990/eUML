# eUML
eUML is a project for galaxy morphotlogy classification with a voting clustering method based on coding from ConvNeXt large model.   

The method can be summarized into three key aspects as follows.  

(1) Convolutional autoencoder is used for image denoising and reconstruction, and the rotational invariance of the model is improved by polar coordinate extension.   

(2) We utilize a pre-trained convolutional neural network named ConvNeXt for encoding the image data, and the features were further compressed by Principal Component Analysis (PCA) dimensionality reduction.   
    
(3) Bagging-based multi-model voting classification algorithm is adopted to enhance robustness. 

## Data Preprocessing

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

---

## Clustering

### Environment Requirements
- `scikit-learn==1.2.2`
- `torch==1.7.1`

Model Weights Download Link:  
[Download ConvNeXt Model Weights](https://dl.fbaipublicfiles.com/convnext_in22k_224.pth)
如果无法进入，可以登录下载(https://github.com/facebookresearch/ConvNeXt?tab=readme-ov-file)
---

### Folder Descriptions
- **Data/**: Directory for storing datasets
- **cae_noise/**: Contains data preprocessing code
- **cluster/**: Contains clustering code

---

### Data Preparation
First, generate the data in the `Data/` folder, following the structure below:

```
Data/
  Datasets/
    train/
    test/
  raw/
```

1. Store all the raw image data in the `raw/` folder.
2. Randomly split the raw data into training and testing sets, and place them in `Datasets/train/` and `Datasets/test/`, respectively.  
   - **Note**: This step is intended for subsequent evaluation of the encoding results, not for training the network.

---

### Clustering Instructions

1. **Run `encoding.py` in the `cluster/` folder**  
   - This script generates the initial encoded files.

2. **Run `main.py`**  
   - Follow the prompts to input the number of clusters, clustering dimensions, and clustering type (choose between PCA-based clustering or raw encoding-based clustering).  
   - Select the appropriate output dimension from the list in the code.  
   - When prompted for input, interrupt the program and analyze the `s_ratio.jpg` output to choose a suitable dimension, specifically where a noticeable change occurs in the plot.  
   - The results of multi-model clustering will be saved in the `result` folder.

3. **Run `get_final_result.py`**  
   - This script generates the `result_final/` folder, containing the final mixed clustering results.  
   - Within `result_final/`, the `rest` folder holds the discarded data that the unsupervised model couldn't classify into any group.

---
