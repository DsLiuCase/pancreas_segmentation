import os
import nibabel as nib
import shutil
import random
from concurrent.futures import ProcessPoolExecutor

# 原始数据路径
data_dir = '/mnt/pan/courses/sxl1912_csds463/dxl952/AbdomenAtlas/uncompressed/'
output_dir = '/mnt/pan/courses/sxl1912_csds463/dxl952/AbdomenAtlas/P1/nnUNet_raw_data_base/nnUNet_raw_data/Task_PancreasSegmentation/'
# 创建必要的目录
images_tr_dir = os.path.join(output_dir, 'imagesTr')
labels_tr_dir = os.path.join(output_dir, 'labelsTr')
images_ts_dir = os.path.join(output_dir, 'imagesTs')  # 新增测试集文件夹
os.makedirs(images_tr_dir, exist_ok=True)
os.makedirs(labels_tr_dir, exist_ok=True)
os.makedirs(images_ts_dir, exist_ok=True)

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

# 定义处理测试集的函数（只需保存图像，不需要标签）
def process_test_subject(subject_dir):
    subject_id = os.path.basename(subject_dir)

    # 路径
    ct_image_path = os.path.join(subject_dir, 'ct.nii.gz')

    # 加载CT图像
    ct_image = nib.load(ct_image_path)

    # 保存CT图像到 imagesTs
    new_image_filename = f'{subject_id}_0000.nii.gz'  # 确保命名符合 nnU-Net 格式
    new_image_path = os.path.join(images_ts_dir, new_image_filename)
    nib.save(ct_image, new_image_path)

    print(f"Processed testing subject {subject_id}")

# 使用 ProcessPoolExecutor 进行并行处理训练集
with ProcessPoolExecutor(max_workers=8) as executor:  # 你可以调整 max_workers 的值来控制并行任务数
    executor.map(process_train_subject, train_subjects)

# 使用 ProcessPoolExecutor 进行并行处理测试集
with ProcessPoolExecutor(max_workers=8) as executor:
    executor.map(process_test_subject, test_subjects)

print("数据处理完成，已保存到:", output_dir)