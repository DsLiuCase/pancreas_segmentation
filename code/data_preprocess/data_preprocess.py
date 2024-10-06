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

# 假设胰腺的标签是2，遍历所有subject并处理数据
for subject_dir in subject_dirs:
    subject_id = os.path.basename(subject_dir)
    
    # 加载图像和标签
    image_path = os.path.join(subject_dir, 'image.nii.gz')
    label_path = os.path.join(subject_dir, 'label.nii.gz')
    
    # 读取图像和标签
    image = nib.load(image_path)
    label = nib.load(label_path)
    
    # 提取胰腺的标签（假设胰腺标签为2）
    label_data = label.get_fdata()
    pancreas_label = np.where(label_data == 2, 1, 0)  # 将标签2的胰腺提取出来并二值化

    # 保存图像到imagesTr
    new_image_filename = f'{subject_id}_0000.nii.gz'  # 确保命名符合 nnU-Net 格式
    new_image_path = os.path.join(images_tr_dir, new_image_filename)
    nib.save(image, new_image_path)

    # 保存处理后的胰腺标签到labelsTr
    new_label_filename = f'{subject_id}.nii.gz'  # 标签文件不用模态编号
    new_label_path = os.path.join(labels_tr_dir, new_label_filename)
    new_label_img = nib.Nifti1Image(pancreas_label.astype(np.uint8), label.affine)
    nib.save(new_label_img, new_label_path)

print("数据处理完成，已保存到:", output_dir)