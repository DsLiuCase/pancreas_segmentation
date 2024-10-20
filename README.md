# pancreas_segmentation
AI for medical imaging, project 1  
<font color=blue>segmentation in pancreas</font>

## workflow:

1. baseline:
   1. nnUnet -- segmentation of pancreas
2. improvement:
   1. alternative loss function 
   2. image augmentation 
   3. different pre- or post-processing methods
3. evaluation:
   1. Dice similarity coefficient
4. interpretation:

## Goals:

1. understand a clinical application of image segmentation; 
2. execute and evaluate a baseline deep learning image segmentation model;
3. experiment with and evaluate techniques that extend beyond the baseline model. 
4. The presentation and report should demonstrate the completion of these goals, emphasizing the in-class presentation.



## Dataset:

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
> ./BDMAP_00001895/
> ├── combined_labels.nii.gz
> ├── ct.nii.gz
> └── segmentations
> ├── adrenal_gland_left.nii.gz
> ├── adrenal_gland_right.nii.gz
> ├── aorta.nii.gz
> ├── bladder.nii.gz
> ├── celiac_trunk.nii.gz
> ├── colon.nii.gz
> ├── duodenum.nii.gz
> ├── esophagus.nii.gz
> ├── femur_left.nii.gz
> ├── femur_right.nii.gz
> ├── gall_bladder.nii.gz
> ├── hepatic_vessel.nii.gz
> ├── intestine.nii.gz
> ├── kidney_left.nii.gz
> ├── kidney_right.nii.gz
> ├── liver.nii.gz
> ├── lung_left.nii.gz
> ├── lung_right.nii.gz
> ├── pancreas.nii.gz
> ├── portal_vein_and_splenic_vein.nii.gz
> ├── postcava.nii.gz
> ├── prostate.nii.gz
> ├── rectum.nii.gz
> ├── spleen.nii.gz
> └── stomach.nii.gz

ct_image = [-1000, 1000]
seg_image = [0, 1]
combine = [0, 25]



## Working ...

- [ ] Data splitting

- [ ] nn-Unet training 

- [ ] Hold-out testing evaluation

  - [ ] Dice similarity coefficient
  - [ ] Visualization

- [ ] Improvement 

  - [ ] implement 
  - [ ] hold-out evaluation 
    - [ ] Dice similarity coefficient 
    - [ ] Visualization

- [ ] Paper

  - [ ] cover page, 

    -----

  - [ ] abstract, 

  - [ ] introduction

  - [ ]  materials and methods, 

  - [ ] results, 

  - [ ] discussion, 

  - [ ] conclusion

    ---

  - [ ] references

  - [ ] appendices.

    

- [ ] Presentation (10/15)

  - [ ] 6 mins



## Rubric: Presentation

Total: 80 points

1. Motivation (10 points)

2. Methods (20 points)

3. Results (20 points)
4. . Questions and Discussion (10 points)

5. Overall clarity (20 points)




# 数据保存结构：
1. 在uncompacted文件夹中，每个subject文件夹(eg: BDMAP_00003466)包含ct.nii.gz(部分), combined_labels.nii.gz 和 segmentations文件夹
2. 在segmentations文件夹中，包含器官的标签文件(eg: pancreas.nii.gz)
如下是segmentations文件夹的结构：
<!-- # -rwx------ 1 dxl952 sxl1912_csds463  81479 Jul  4 18:16 adrenal_gland_left.nii.gz
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
# -rwx------ 1 dxl952 sxl1912_csds463 102086 Jul  4 18:16 stomach.nii.gz -->

---

To facilitate the segmentation of the pancreas, the following organs that surround it might be useful as they provide spatial context and anatomical boundaries:

1. Liver: The pancreas is positioned close to the liver on its right side.
2.	Stomach: The pancreas lies just behind the stomach, making it a useful reference organ.
3.	Duodenum: Part of the small intestine, the duodenum forms a C-shape around the pancreas and provides useful context.
4.	Spleen: Located to the left of the pancreas and helpful for identifying the left boundary.
5.	Kidneys (Left and Right): These are in close proximity to the posterior side of the pancreas.
6.	Aorta: The pancreas is near the abdominal aorta, which can help in identifying its position.
