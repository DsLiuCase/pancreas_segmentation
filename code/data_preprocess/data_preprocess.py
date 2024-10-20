import os
import nibabel as nib
import shutil
import random
from concurrent.futures import ThreadPoolExecutor

# 数据保存结构：
#1.在uncompacted文件夹中，每个subject文件夹(eg: BDMAP_00003466)包含ct.nii.gz(部分), combined_labels.nii.gz 和 segmentations文件夹
#2. 在segmentations文件夹中，包含器官的标签文件(eg: pancreas.nii.gz)
#如下是segmentations文件夹的结构：
# -rwx------ 1 dxl952 sxl1912_csds463  81479 Jul  4 18:16 adrenal_gland_left.nii.gz
# -rwx------ 1 dxl952 sxl1912_csds463  80866 Jul  4 18:16 adrenal_gland_right.nii.gz
# -rwx------ 1 dxl952 sxl1912_csds463  88864 Jul  4 18:16 aorta.nii.gz
# -rwx------ 1 dxl952 sxl1912_csds463  95336 Jul  4 18:16 bladder.nii.gz
# -rwx------ 1 dxl952 sxl1912_csds463  80479 Jul  4 18:16 celiac_trunk.nii.gz
# -rwx------ 1 dxl952 sxl1912_csds463 134387 Jul  4 18:16 colon.nii.gz
# -rwx------ 1 dxl952 sxl1912_csds463  90883 Jul  4 18:16 duodenum.nii.gz
# -rwx------ 1 dxl952 sxl1912_csds463  81833 Jul  4 18:16 esophagus.nii.gz
# -rwx------ 1 dxl952 sxl1912_csds463  87215 Jul  4 18:16 femur_left.nii.gz
# -rwx------ 1 dxl952 sxl1912_csds463  86412 Jul  4 18:16 femur_right.nii.gz
# -rwx------ 1 dxl952 sxl1912_csds463  82333 Jul  4 18:16 gall_bladder.nii.gz
# -rwx------ 1 dxl952 sxl1912_csds463  82563 Jul  4 18:16 hepatic_vessel.nii.gz
# -rwx------ 1 dxl952 sxl1912_csds463 157203 Jul  4 18:16 intestine.nii.gz
# -rwx------ 1 dxl952 sxl1912_csds463  91372 Jul  4 18:16 kidney_left.nii.gz
# -rwx------ 1 dxl952 sxl1912_csds463  90727 Jul  4 18:16 kidney_right.nii.gz
# -rwx------ 1 dxl952 sxl1912_csds463 133198 Jul  4 18:16 liver.nii.gz
# -rwx------ 1 dxl952 sxl1912_csds463 104736 Jul  4 18:16 lung_left.nii.gz
# -rwx------ 1 dxl952 sxl1912_csds463 107586 Jul  4 18:16 lung_right.nii.gz
# -rwx------ 1 dxl952 sxl1912_csds463  87009 Jul  4 18:16 pancreas.nii.gz
# -rwx------ 1 dxl952 sxl1912_csds463  83102 Jul  4 18:16 portal_vein_and_splenic_vein.nii.gz
# -rwx------ 1 dxl952 sxl1912_csds463  85333 Jul  4 18:16 postcava.nii.gz
# -rwx------ 1 dxl952 sxl1912_csds463  82002 Jul  4 18:16 prostate.nii.gz
# -rwx------ 1 dxl952 sxl1912_csds463  84045 Jul  4 18:16 rectum.nii.gz
# -rwx------ 1 dxl952 sxl1912_csds463  89431 Jul  4 18:16 spleen.nii.gz
# -rwx------ 1 dxl952 sxl1912_csds463 102086 Jul  4 18:16 stomach.nii.gz


# 原始数据路径
data_dir = '/mnt/pan/courses/sxl1912_csds463/dxl952/AbdomenAtlas/uncompressed/'
output_dir = '/mnt/pan/courses/sxl1912_csds463/dxl952/AbdomenAtlas/P1/nnUNet_raw_data_base/nnUNet_raw_data/Task_PancreasSegmentation/'

# 创建和清理目录的函数
def create_clean_dir(directory):
    if os.path.exists(directory):
        print(f"Deleting existing directory: {directory}")
        shutil.rmtree(directory)
    os.makedirs(directory, exist_ok=True)

# 创建或清理必要的目录
images_tr_dir = os.path.join(output_dir, 'imagesTr')
labels_tr_dir = os.path.join(output_dir, 'labelsTr')
images_ts_dir = os.path.join(output_dir, 'imagesTs')  # 测试集图像文件夹
labels_ts_dir = os.path.join(output_dir, 'labelsTs')  # 测试集标签文件夹

create_clean_dir(images_tr_dir)
create_clean_dir(labels_tr_dir)
create_clean_dir(images_ts_dir)
create_clean_dir(labels_ts_dir)

# 获取所有 subject 文件夹
subject_dirs = [os.path.join(data_dir, d) for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))]

# 过滤出包含ct.nii.gz和胰腺标签的文件夹
usable_subjects = []
for subject_dir in subject_dirs:
    ct_image_path = os.path.join(subject_dir, 'ct.nii.gz')
    pancreas_label_path = os.path.join(subject_dir, 'segmentations', 'pancreas.nii.gz')
    
    # 检查ct.nii.gz和pancreas标签是否存在
    if os.path.exists(ct_image_path) and os.path.exists(pancreas_label_path):
        usable_subjects.append(subject_dir)
    else:
        print(f"Skipping {os.path.basename(subject_dir)}: missing ct.nii.gz or pancreas.nii.gz")

# 随机抽取 10% 的 subject 作为测试集，剩余 90% 作为训练集
test_size = int(0.1 * len(usable_subjects))
test_subjects = random.sample(usable_subjects, test_size)  # 10% 用作测试集
train_subjects = list(set(usable_subjects) - set(test_subjects))  # 其余 90% 用作训练集

# 定义处理训练集的函数
def process_train_subject(subject_dir):
    subject_id = os.path.basename(subject_dir)

    # 路径
    ct_image_path = os.path.join(subject_dir, 'ct.nii.gz')
    pancreas_label_path = os.path.join(subject_dir, 'segmentations', 'pancreas.nii.gz')

    # 加载CT图像和二值化的胰腺标签
    ct_image = nib.load(ct_image_path)
    pancreas_label = nib.load(pancreas_label_path)
    binary_pancreas_label = pancreas_label.get_fdata()

    # 保存CT图像到 imagesTr
    new_image_filename = f'{subject_id}_0000.nii.gz'  # 确保命名符合 nnU-Net 格式
    new_image_path = os.path.join(images_tr_dir, new_image_filename)
    nib.save(ct_image, new_image_path)

    # 保存二值化胰腺标签到 labelsTr
    new_label_filename = f'{subject_id}.nii.gz'  # 标签文件不用模态编号
    new_label_path = os.path.join(labels_tr_dir, new_label_filename)
    new_label_img = nib.Nifti1Image(binary_pancreas_label, pancreas_label.affine)
    nib.save(new_label_img, new_label_path)

    print(f"Processed training subject {subject_id}")

# 定义处理测试集的函数（保存图像和标签）
def process_test_subject(subject_dir):
    subject_id = os.path.basename(subject_dir)

    # 路径
    ct_image_path = os.path.join(subject_dir, 'ct.nii.gz')
    pancreas_label_path = os.path.join(subject_dir, 'segmentations', 'pancreas.nii.gz')

    # 加载CT图像
    ct_image = nib.load(ct_image_path)

    # 保存CT图像到 imagesTs
    new_image_filename = f'{subject_id}_0000.nii.gz'  # 确保命名符合 nnU-Net 格式
    new_image_path = os.path.join(images_ts_dir, new_image_filename)
    nib.save(ct_image, new_image_path)

    # 保存胰腺标签到 labelsTs
    pancreas_label = nib.load(pancreas_label_path)
    binary_pancreas_label = pancreas_label.get_fdata()
    new_label_filename = f'{subject_id}.nii.gz'  # 标签文件不用模态编号
    new_label_path = os.path.join(labels_ts_dir, new_label_filename)
    new_label_img = nib.Nifti1Image(binary_pancreas_label, pancreas_label.affine)
    nib.save(new_label_img, new_label_path)

    print(f"Processed testing subject {subject_id}")

# 使用 ThreadPoolExecutor 进行并行处理训练集
with ThreadPoolExecutor(max_workers=40) as executor:  # 使用40个线程
    executor.map(process_train_subject, train_subjects)

# 使用 ThreadPoolExecutor 进行并行处理测试集
with ThreadPoolExecutor(max_workers=40) as executor:  # 使用40个线程
    executor.map(process_test_subject, test_subjects)

print("数据处理完成，已保存到:", output_dir)
