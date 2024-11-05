#在原文件夹下的所有星系中抽取9800个fits测试
import os
import random
import shutil

def random_copy_files(src_folder, dest_folder, num_files):
    # 获取指定文件夹下所有fits文件路径
    fits_files = [f for f in os.listdir(src_folder) if f.endswith('.fits')]

    # 随机选择指定数量的文件
    selected_files = random.sample(fits_files, num_files)

    # 创建目标文件夹
    os.makedirs(dest_folder, exist_ok=True)

    # 复制选中的文件到目标文件夹
    for file_name in selected_files:
        src_file = os.path.join(src_folder, file_name)
        dest_file = os.path.join(dest_folder, file_name)
        shutil.copy2(src_file, dest_file)

#print(f"{num_files}")

# 示例用法
src_folder = '/share/songjie/COSMOS_Image/cutimage'  # 指定源文件夹路径
dest_folder = '/home/daiyao/cae_noise/fit_raw'  # 指定目标文件夹路径
num_files = 9980  # 指定要抽取的文件数量

random_copy_files(src_folder, dest_folder, num_files)