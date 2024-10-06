import os
import nibabel as nib
import numpy as np
import shutil

# 原始数据路径
data_dir = '/mnt/pan/courses/sxl1912_csds463/dxl952/AbdomenAtlas/uncompressed/'
output_dir = '/mnt/pan/courses/sxl1912_csds463/dxl952/AbdomenAtlas/P1/nnUNet_raw_data_base/nnUNet_raw_data/TaskXXX_PancreasSegmentation/'
pancreas_label = 6  # 胰腺的标签
# 创建必要的目录
images_tr_dir = os.path.join(output_dir, 'imagesTr')
labels_tr_dir = os.path.join(output_dir, 'labelsTr')
os.makedirs(images_tr_dir, exist_ok=True)
os.makedirs(labels_tr_dir, exist_ok=True)

# 假设文件结构是：
# data_dir/
# ├── subject_001/
# │   ├── image.nii.gz
# │   └── label.nii.gz
subject_dirs = [os.path.join(data_dir, d) for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))]
print("数据路径：", subject_dirs)
raise RuntimeError("请检查数据路径是否正确！")

# 设置胰腺的标签值
pancreas_label_value = 6

for subject_dir in subject_dirs:
    subject_id = os.path.basename(subject_dir)

    # 路径
    combined_label_path = os.path.join(subject_dir, 'combined_labels.nii.gz')
    pancreas_label_path = os.path.join(subject_dir, 'segmentations', 'pancreas.nii.gz')
    
    if not os.path.exists(combined_label_path) or not os.path.exists(pancreas_label_path):
        print(f"Warning: Missing image or pancreas label for subject {subject_id}. Skipping.")
        continue

    # 加载图像和标签
    image = nib.load(combined_label_path)
    
    # 加载 pancreas.nii.gz 文件中的二值化胰腺标签
    pancreas_label = nib.load(pancreas_label_path)
    binary_pancreas_label = pancreas_label.get_fdata()

    # 提取 combined_labels 中胰腺的标签 (标签值为 6)
    combined_label_data = image.get_fdata()
    pancreas_from_combined = np.where(combined_label_data == pancreas_label_value, 1, 0).astype(np.uint8)

    # 比较二者：使用 binary_pancreas_label 作为最终的二值标签
    # 保存图像到 imagesTr
    new_image_filename = f'{subject_id}_0000.nii.gz'  # 确保命名符合 nnU-Net 格式
    new_image_path = os.path.join(images_tr_dir, new_image_filename)
    nib.save(image, new_image_path)

    # 保存处理后的胰腺标签到 labelsTr
    new_label_filename = f'{subject_id}.nii.gz'  # 标签文件不用模态编号
    new_label_path = os.path.join(labels_tr_dir, new_label_filename)
    new_label_img = nib.Nifti1Image(binary_pancreas_label, pancreas_label.affine)
    nib.save(new_label_img, new_label_path)

    print(f"Processed subject {subject_id}")

print("数据处理完成，已保存到:", output_dir)