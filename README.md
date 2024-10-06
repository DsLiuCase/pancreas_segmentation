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

