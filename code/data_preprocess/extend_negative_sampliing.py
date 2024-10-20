import os
import shutil
from tqdm import tqdm

def process_and_copy_files(folderA, folderB):
    # 创建目标文件夹，如果不存在则创建
    if not os.path.exists(folderB):
        os.makedirs(folderB)
    
    # 遍历folderA中的所有文件
    for filename in tqdm(os.listdir(folderA), desc="Processing Files"):
        # 如果文件名包含 'seg'
        if 'seg' in filename:
            # 分离文件名和后缀
            file_base, file_extension = os.path.splitext(filename)
            
            # 构造新的文件名，文件名后添加 'negative'
            new_filename = f"{file_base}_negative{file_extension}"
            
            # 构造原始文件和新文件的完整路径
            original_file_path = os.path.join(folderA, filename)
            new_file_path = os.path.join(folderB, new_filename)
            
            # 将文件复制到folderB，并重命名
            shutil.copy(original_file_path, new_file_path)
            # print(f"Processed and copied: {filename} -> {new_filename}")

# 使用示例
folderA = '/mnt/pan/courses/sxl1912_csds463/dxl952/AbdomenAtlas/P1/nnUNet_preprocessed/Dataset001_PancreasSegmentation/nnUNetPlans_3d_fullres/'
folderB = '/mnt/pan/courses/sxl1912_csds463/dxl952/AbdomenAtlas/P1/nnUNet_preprocessed_standard/Dataset001_PancreasSegmentation/nnUNetPlans_3d_fullres/'
process_and_copy_files(folderA, folderB)