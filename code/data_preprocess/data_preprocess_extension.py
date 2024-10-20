# import os
# import nibabel as nib
# import shutil
# import numpy as np
# from tqdm import tqdm

# """
# in this dataset, there are 26 unique values in the combined label files, 0 for background and 1-25 for organs
# the map of the organs is as follows:
# class_map = {1: 'aorta', 2: 'gall_bladder', 3: 'kidney_left', 4: 'kidney_right', 5: 'liver',
#              6: 'pancreas', 7: 'postcava', 8: 'spleen', 9: 'stomach', 10: 'adrenal_gland_left',
#              11: 'adrenal_gland_right', 12: 'bladder', 13: 'celiac_trunk', 14: 'colon', 15: 'duodenum',
#              16: 'esophagus', 17: 'femur_left', 18: 'femur_right', 19: 'hepatic_vessel', 20: 'intestine',
#              21: 'lung_left', 22: 'lung_right', 23: 'portal_vein_and_splenic_vein',
#              24: 'prostate', 25: 'rectum'}
# """


surrounding_organs = ["liver", "stomach", "duodenum", "spleen", "kidney", 'aorta']
class_map = {1: 'aorta', 2: 'gall_bladder', 3: 'kidney_left', 4: 'kidney_right', 5: 'liver',
             6: 'pancreas', 7: 'postcava', 8: 'spleen', 9: 'stomach', 10: 'adrenal_gland_left',
             11: 'adrenal_gland_right', 12: 'bladder', 13: 'celiac_trunk', 14: 'colon', 15: 'duodenum',
             16: 'esophagus', 17: 'femur_left', 18: 'femur_right', 19: 'hepatic_vessel', 20: 'intestine',
             21: 'lung_left', 22: 'lung_right', 23: 'portal_vein_and_splenic_vein',
             24: 'prostate', 25: 'rectum'}
# 反转 class_map 方便查找 key
reverse_class_map = {v: k for k, v in class_map.items()}
surronding_organ_dict = {}
for organ in surrounding_organs:
  for original_key, original_organ_label in reverse_class_map.items():
    if organ in original_key:
        print(f"Key for {organ}: {reverse_class_map[original_key]}")
        surronding_organ_dict[original_key] = original_organ_label


# # 原始数据路径
# labels_tr_dir = '/mnt/pan/courses/sxl1912_csds463/dxl952/AbdomenAtlas/P1/nnUNet_raw_data_base/nnUNet_raw_data/Dataset001_PancreasSegmentation//labelsTr'
# labels_ts_dir = '/mnt/pan/courses/sxl1912_csds463/dxl952/AbdomenAtlas/P1/nnUNet_raw_data_base/nnUNet_raw_data/Dataset001_PancreasSegmentation/labelsTs'

# # 目标扩展数据集路径
# training_label_extension = '/mnt/pan/courses/sxl1912_csds463/dxl952/AbdomenAtlas/P1/nnUNet_raw_data_base/nnUNet_raw_data/Dataset001_PancreasSegmentation//labelsTr_extension'
# testing_label_extension = '/mnt/pan/courses/sxl1912_csds463/dxl952/AbdomenAtlas/P1/nnUNet_raw_data_base/nnUNet_raw_data/Dataset001_PancreasSegmentation//labelsTs_extension'

# # 创建和清理目录的函数
# def create_clean_dir(directory):
#     if os.path.exists(directory):
#         print(f"Deleting existing directory: {directory}")
#         shutil.rmtree(directory)
#     os.makedirs(directory, exist_ok=True)

# # 创建扩展目录
# create_clean_dir(training_label_extension)
# create_clean_dir(testing_label_extension)

# # 定义修改标签的函数，基于原始标签的索引生成新的标签
# def modify_label_by_index(original_label, surronding_organ_dict = surronding_organ_dict):
#     """
#     基于原始标签索引生成新的标签数据.
#     假设这里的修改是：将标签为1的地方变为2 (可以自定义)
#     """
#     replaced_label_indices = [i for i in surronding_organ_dict.values()]

#     mask = np.isin(original_label, replaced_label_indices)
#     assert mask.any(), "at least one label should be modified"
#     # 示例：将原始标签为1的体素修改为2
#     modified_label = np.where(mask, 1, 0)
    
#     return modified_label

# # 处理函数：基于原始train/test标签，生成扩展标签
# def process_labels(src_dir, dest_dir):
#     uncompacted_files = "/mnt/pan/courses/sxl1912_csds463/dxl952/AbdomenAtlas/uncompressed/"
#     for filename in tqdm(os.listdir(src_dir), desc="Processing"):
#         sample_name = filename.split("/")[-1].split(".")[0]
#         original_sample_path = os.path.join(uncompacted_files, sample_name)
#         combined_label_path = os.path.join(original_sample_path, "combined_labels.nii.gz")
#         src_file = os.path.join(src_dir, filename)
#         dest_file = os.path.join(dest_dir, filename)
#         if os.path.isfile(combined_label_path):
#             label_img = nib.load(combined_label_path)
#             label_data = label_img.get_fdata()   # in the combined label files contained 26 unqiue value, 0 for background and 1-25 for organs
          
#             modified_label_data = modify_label_by_index(label_data)
            
#             modified_label_img = nib.Nifti1Image(modified_label_data.astype(np.int32), label_img.affine)
#             nib.save(modified_label_img, dest_file)
            

# # 处理训练集和测试集标签
# process_labels(labels_tr_dir, training_label_extension)
# process_labels(labels_ts_dir, testing_label_extension)

# print("训练标签扩展和测试标签扩展已完成并修改。")



import os
import nibabel as nib
import shutil
import numpy as np
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool

# # 假设 surrounding_organs 和 class_map 都已经定义好
# reverse_class_map = {v: k for k, v in class_map.items()}
# surronding_organ_dict = {reverse_class_map[organ]: reverse_class_map[organ] for organ in surrounding_organs if organ in reverse_class_map}

# 原始数据路径
labels_tr_dir = '/mnt/pan/courses/sxl1912_csds463/dxl952/AbdomenAtlas/P1/nnUNet_raw_data_base/nnUNet_raw_data/Dataset001_PancreasSegmentation//labelsTr_standard'
labels_ts_dir = '/mnt/pan/courses/sxl1912_csds463/dxl952/AbdomenAtlas/P1/nnUNet_raw_data_base/nnUNet_raw_data/Dataset001_PancreasSegmentation/labelsTs_standard'

# 目标扩展数据集路径
training_label_extension = '/mnt/pan/courses/sxl1912_csds463/dxl952/AbdomenAtlas/P1/nnUNet_raw_data_base/nnUNet_raw_data/Dataset001_PancreasSegmentation//labelsTr'
testing_label_extension = '/mnt/pan/courses/sxl1912_csds463/dxl952/AbdomenAtlas/P1/nnUNet_raw_data_base/nnUNet_raw_data/Dataset001_PancreasSegmentation//labelsTs'

# 创建和清理目录的函数
def create_clean_dir(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
        print(f"Deleting existing directory: {directory}")
    os.makedirs(directory, exist_ok=True)


# 创建扩展目录
create_clean_dir(training_label_extension)
create_clean_dir(testing_label_extension)

# 定义修改标签的函数
def modify_label_by_index(original_label, surronding_organ_dict=surronding_organ_dict):
    replaced_label_indices = [i for i in surronding_organ_dict.values()]
    mask = np.isin(original_label, replaced_label_indices)
    modified_label = np.where(mask, 1, 0)  # 示例：将指定器官标签设为1，其余为0
    good = True
    if not mask.any():
        print("No label is modified.")
        good = False
    return modified_label, good

# 处理单个文件的函数
def process_single_label(file_info):
    dest_file, combined_label_path = file_info
    if os.path.isfile(combined_label_path):
        label_img = nib.load(combined_label_path)
        label_data = label_img.get_fdata()
        modified_label_data, good = modify_label_by_index(label_data)
        modified_label_img = nib.Nifti1Image(modified_label_data.astype(np.int32), label_img.affine)
        if not good:
            print(f"Skipping {dest_file}")
        else:
          nib.save(modified_label_img, dest_file)

# 多进程处理标签的函数
def process_labels_in_parallel(src_dir, dest_dir, num_workers=4):
    uncompacted_files = "/mnt/pan/courses/sxl1912_csds463/dxl952/AbdomenAtlas/uncompressed/"
    files_to_process = []
    
    for filename in os.listdir(src_dir):
        sample_name = filename.split("/")[-1].split(".")[0]
        original_sample_path = os.path.join(uncompacted_files, sample_name)
        combined_label_path = os.path.join(original_sample_path, "combined_labels.nii.gz")
        dest_file = os.path.join(dest_dir, filename)
        if os.path.isfile(combined_label_path):
            files_to_process.append((dest_file, combined_label_path))
    
    # 使用 multiprocessing Pool 进行多进程处理
    with Pool(processes=num_workers) as pool:
        list(tqdm(pool.imap(process_single_label, files_to_process), total=len(files_to_process), desc="Processing"))

# 处理训练集和测试集标签
process_labels_in_parallel(labels_tr_dir, training_label_extension, num_workers=40)
process_labels_in_parallel(labels_ts_dir, testing_label_extension, num_workers=40)

print("训练标签扩展和测试标签扩展已完成并修改。")