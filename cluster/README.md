环境要求,请看环境文件：
scikit-learn==1.2.2
torch == 1.7.1
pytorch_pretrained_vit
提示缺那些库就conda install +库名
不行就pip install +库名

各文件夹介绍：
这个文件夹放到之前发的那个编码+机器学习目录下，即和这些目录平级：
Data/：数据集存放地址
Data_process/：数据预处理代码
cluster/：聚类代码

运行顺序：
先在Data中生成数据，请符合以下格式：
Data/
	Datasets/
		train/
		test/
	raw/
请将全部数据存入raw/中，每个图片可以按以下格式随意附上标签+'_'+图片名（如果原始数据无标签的话），例：1_cosmos.jpg
同时，请将raw的数据随机划分成训练和测试集，分别存入Datasets下的train/和test/，两文件夹的文件个数随便定。



随后进入cluster中：
1.python encoding.py,生成原始编码文件。
2.python main.py   请按照提示，输入聚类数量，聚类维度和聚类类型（pca聚类或者raw原始编码聚类），请在代码种的维度列表中选择输出维度，第一次可以随便设置，
运行到输入提示时，中断程序并根据输出的s_ratio.jpg选择合适的维度（中间发生突变的维度），在result文件夹中得到多模型聚类的结果。
3.python get_final_result.py  生成result_final/，其中为混合聚类的最终结果
4.result_final/中rest文件夹是丢弃的数据，即无监督无法分出来的类。
5.python check_result.py, 请按照提示，输入聚类数量和聚类类型（pca聚类或者raw原始编码聚类），在log文件夹中生成excel文件，分类详细，分对结果详细，分错结果详细和总的分类结果