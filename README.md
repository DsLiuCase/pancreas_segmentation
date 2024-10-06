# pancreas_segmentation
AI for medical imaging, project 1  
<font color=blue>segmentation in pancreas</font>

# Dataset:
[AbdomenAtlas--huggingface](https://huggingface.co/datasets/AbdomenAtlas/_AbdomenAtlas1.0Mini):
CT image dataset for multiple origins

**Dataset references**  
1. How Well Do Supervised 3D Models Transfer to Medical Imaging Tasks?
Wenxuan Li, Alan Yuille, and Zongwei Zhou*
Johns Hopkins University
International Conference on Learning Representations (ICLR) 2024 (oral; top 1.2%)  
[paper](https://www.cs.jhu.edu/~alanlab/Pubs23/li2023suprem.pdf) | [text](https://github.com/MrGiovanni/SuPreM)


2. AbdomenAtlas-8K: Annotating 8,000 CT Volumes for Multi-Organ Segmentation in Three Weeks
Chongyu Qu1, Tiezheng Zhang1, Hualin Qiao2, Jie Liu3, Yucheng Tang4, Alan L. Yuille1, and Zongwei Zhou1,*
1 Johns Hopkins University,
2 Rutgers University,
3 City University of Hong Kong,
4 NVIDIA
NeurIPS 2023  
[paper](https://www.cs.jhu.edu/~alanlab/Pubs23/qu2023abdomenatlas.pdf) | [code](https://github.com/MrGiovanni/AbdomenAtlas)| [dataset](https://huggingface.co/datasets/AbdomenAtlas/AbdomenAtlas1.0Mini) | [annotation](https://www.dropbox.com/scl/fi/28l5vpxrn212r2ejk32xv/AbdomenAtlas.tar.gz?rlkey=vgqmao4tgv51hv5ew24xx4xpm&dl=0) | [poster](https://huggingface.co/datasets/AbdomenAtlas/_AbdomenAtlas1.0Mini/blob/main/document/neurips_poster.pdf)


> dataset glance  
./BDMAP_00001895/
├── combined_labels.nii.gz
├── ct.nii.gz
└── segmentations
    ├── adrenal_gland_left.nii.gz
    ├── adrenal_gland_right.nii.gz
    ├── aorta.nii.gz
    ├── bladder.nii.gz
    ├── celiac_trunk.nii.gz
    ├── colon.nii.gz
    ├── duodenum.nii.gz
    ├── esophagus.nii.gz
    ├── femur_left.nii.gz
    ├── femur_right.nii.gz
    ├── gall_bladder.nii.gz
    ├── hepatic_vessel.nii.gz
    ├── intestine.nii.gz
    ├── kidney_left.nii.gz
    ├── kidney_right.nii.gz
    ├── liver.nii.gz
    ├── lung_left.nii.gz
    ├── lung_right.nii.gz
    ├── pancreas.nii.gz
    ├── portal_vein_and_splenic_vein.nii.gz
    ├── postcava.nii.gz
    ├── prostate.nii.gz
    ├── rectum.nii.gz
    ├── spleen.nii.gz
    └── stomach.nii.gz


ct_image = [-1000, 1000]
seg_image = [0, 1]
combine = [0, 25]
