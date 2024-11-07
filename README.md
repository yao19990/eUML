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

## Clustering
环境要求：
scikit-learn==1.2.2
torch == 1.7.1
模型权重下载地址: https://dl.fbaipublicfiles.com/convnext_in22k_224.pth

各文件夹介绍
Data/：数据集存放地址
cae_niose/：数据预处理代码
cluster/：聚类代码

先在Data中生成数据，请符合以下格式：
Data/
	Datasets/
		train/
		test/
	raw/
请将原始数据全部存入raw/中，将raw的数据随机划分成训练和测试集，分别存入Datasets下的train/和test/。


进入cluster中：
1.python encoding.py,生成原始编码文件。
2.python main.py 请按照提示，输入聚类数量，聚类维度和聚类类型（pca聚类或者raw原始编码聚类），请在代码种的维度列表中选择输出维度，
  运行到输入提示时，中断程序并根据输出的s_ratio.jpg选择合适的维度（中间发生突变的维度），在result文件夹中得到多模型聚类的结果。
3.python get_final_result.py  生成result_final/，其中为混合聚类的最终结果. result_final/中rest文件夹是丢弃的数据，即无监督无法分出来的类。
