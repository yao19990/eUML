scikit-learn==1.2.2
torch == 1.7.1
pytorch_pretrained_vit

**Folder Descriptions**:  
Place this folder within the directory, at the same level as the following folders:

- **Data/**: Storage location for the dataset
- **Data_process/**: Contains data preprocessing code
- **cluster/**: Contains clustering code

**Steps to Run Clustering**:

1. Run `python encoding.py` within the `cluster/` folder to generate the initial encoded files.

2. Run `python main.py`. Follow the prompts to enter the number of clusters, clustering dimensions, and clustering type (choose either PCA-based clustering or raw encoding-based clustering). When prompted, select the desired output dimension from the dimension list in the code.  
   - Stop the program when prompted for input and check the output `s_ratio.jpg` file to identify an appropriate dimension (look for a noticeable breakpoint in the middle of the range). The clustering results for multiple models will be saved in the `result` folder.

3. Run `python get_final_result.py` to create the `result_final/` folder, which contains the final results for the combined clustering.

4. Within `result_final/`, the `rest` folder contains discarded data that the unsupervised model couldn’t classify into any group.

5. Run `python check_result.py`. Follow the prompts to enter the number of clusters and clustering type (PCA-based or raw encoding). This script will generate detailed Excel files in the `log/` folder, including summaries of classifications, correctly classified samples, misclassified samples, and overall classification results.
