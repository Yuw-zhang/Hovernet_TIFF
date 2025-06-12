# HoVer-Net: Simultaneous Segmentation and Classification of Nuclei in Multi-Tissue Histology Images

A multiple branch network that performs nuclear instance segmentation and classification within a single network. The network leverages the horizontal and vertical distances of nuclear pixels to their centres of mass to separate clustered cells. A dedicated up-sampling branch is used to classify the nuclear type for each segmented instance. <br />

## Modification in this Fork
- Replaced OpenSlide with TiffSlide to support TIFF WSIs.
- Updated the environment dependencies to support TIFF.

[Link](https://www.sciencedirect.com/science/article/abs/pii/S1361841519301045?via%3Dihub) to Medical Image Analysis paper. <br />

This is the official PyTorch implementation of HoVer-Net. For the original TensorFlow version of this code, please refer to [this branch](https://github.com/vqdang/hover_net/tree/tensorflow-final). The repository can be used for training HoVer-Net and to process image tiles or whole-slide images. As part of this repository, we supply model weights trained on the following datasets:

- [CoNSeP](https://www.sciencedirect.com/science/article/pii/S1361841519301045)
- [PanNuke](https://arxiv.org/abs/2003.10778)
- [MoNuSAC](https://ieeexplore.ieee.org/abstract/document/8880654)
- [Kumar](https://ieeexplore.ieee.org/abstract/document/7872382)
- [CPM17](https://www.frontiersin.org/articles/10.3389/fbioe.2019.00053/full)

## Set Up Environment

```
conda env create -f environment.yml
conda activate hovernetTIFF
pip install torch==1.9.0 torchvision==0.10.0
```

Above, we install PyTorch version 1.9 with CUDA 10.2. 
