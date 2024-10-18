#!/bin/bash
#!/bin/bash
# Source the environment's activation script directly
source ~/miniconda3/etc/profile.d/conda.sh
conda activate sxl1912_csds463
echo "dataset_dir = /mnt/pan/courses/sxl1912_csds463/dxl952/AbdomenAtlas/"
echo "conda activate sxl1912_csds463"
if [[ $? -ne 0 ]]; then
  echo "Failed to activate conda environment."
  exit 1
fi

# Your commands go here
echo "Conda environment activated successfully.

"echo "Environment activated, running commands in 'sxl1912_csds463'..."
newgrp sxl1912_csds463
export dataset_dir="/mnt/pan/courses/sxl1912_csds463/dxl952/AbdomenAtlas/"

echo "dataset_dir=/mnt/pan/courses/sxl1912_csds463/dxl952/AbdomenAtlas/"
source "/home/dxl952/Cource/AI_for_Medical_Imaging/nnUNet/setting.sh"