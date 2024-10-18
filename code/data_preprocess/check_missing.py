import os

# 数据路径
data_dir = '/mnt/pan/courses/sxl1912_csds463/dxl952/AbdomenAtlas/uncompressed/'

# 获取所有 subject 文件夹
subject_dirs = [os.path.join(data_dir, d) for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))]

# 总文件夹数
total_folders = len(subject_dirs)

# 遍历每个 subject 文件夹并检查是否存在 ct.nii.gz 文件
missing_ct_folders = []  # 用于记录缺少 ct.nii.gz 文件的文件夹

for subject_dir in subject_dirs:
    subject_id = os.path.basename(subject_dir)
    ct_image_path = os.path.join(subject_dir, 'ct.nii.gz')
    
    if not os.path.exists(ct_image_path):
        print(f"Warning: {subject_id} is missing ct.nii.gz file.")
        missing_ct_folders.append(subject_dir)

# 缺少文件的文件夹数
missing_folders_count = len(missing_ct_folders)

# 输出结果
if missing_ct_folders:
    print("\n以下文件夹中缺少 ct.nii.gz 文件：")
    for folder in missing_ct_folders:
        print(folder)
    
    # 计算缺少文件的文件夹占总文件夹的百分比
    missing_percentage = (missing_folders_count / total_folders) * 100
    print(f"\n总共有 {missing_folders_count} 个文件夹中缺少 ct.nii.gz 文件，占总文件夹的 {missing_percentage:.2f}%。")
else:
    print("\n所有文件夹中都存在 ct.nii.gz 文件。")