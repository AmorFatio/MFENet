# MFENet
A lightweight and robust object detection network designed for severe foggy weather, achieving high precision with low complexity.

```markdown
# Multi-Scale Feature Enhancement Network for Object Detection in Severe Foggy Weather

📖 Introduction

This repository contains the official PyTorch implementation of the paper: **"Multi-Scale Feature Enhancement Network for Object Detection in Severe Foggy Weather"**.

**MFENet** is designed to address the challenges of low contrast and blurred structures in foggy traffic environments. 


🏗️ Architecture

![Architecture](./assets/architecture.png)
*Figure 1: The overall architecture of MFENet, integrating SFRM, DIM, and OADH modules.* 

🔨 Installation

Environment Requirements
* Windows
* Python 3.8+
* PyTorch 1.10+
* CUDA 11.0+

### Setup
```bash
# Clone this repository
git clone [https://github.com/YourUsername/MFENet.git](https://github.com/YourUsername/MFENet.git)
cd MFENet

# Create a virtual environment
conda create -n mfenet python=3.9
conda activate mfenet

# Install dependencies
pip install -r requirements.txt

```

## 📂 Data Preparation

We use **VOC-fog** (synthetic) and **RTTS** (real-world) datasets. Please organize your datasets as follows:

```text
├── data
│   ├── VOC_Fog
│   │   ├── images
│   │   │   ├── train
│   │   │   └── val
│   │   └── labels
│   ├── RTTS
│       ├── images
│       └── labels

```

* **RTTS Dataset:** Available at [RESIDE-Beta](https://www.google.com/search?q=https://sites.google.com/view/reside-dehaze-datasets/reside-beta).
* 
**VOC-fog:** Generated based on VOC2012.



## 🚀 Usage

### Training

To train MFENet on the RTTS dataset (Batch size 16, 300 epochs):

```bash
python train.py --data data/RTTS.yaml --cfg models/MFENet.yaml --batch-size 16 --epochs 300 --lr 0.01

```

### Testing / Evaluation

To evaluate the model on the test set:

```bash
python val.py --weights runs/train/exp/weights/best.pt --data data/RTTS.yaml --img 640

```

## 📊 Results

### Performance on RTTS (Real-world Fog)

Comparison with SOTA methods (Table 3 in the paper):

| Method | Type | Params (M) | FLOPs (G) | FPS | mAP50 (%) |
| --- | --- | --- | --- | --- | --- |
| IA-YOLO (AAAI'22) | Domain-Adaptive | 58.9 | 65.6 | 26 | 42.24 |
| GDIP-YOLO (ICRA'23) | Domain-Adaptive | 68.1 | 105.2 | 32 | 42.66 |
| YOLO11 (Baseline) | General | 2.6 | 6.5 | 126 | 74.45 |
| **MFENet (Ours)** | **Fog Detection** | **7.8** | **12.1** | **117** | **75.89** |

### Visualization

*Qualitative detection results on the RTTS dataset. MFENet demonstrates superior ability to detect occluded pedestrians and vehicles.*

## 🔗 Citation

If you find this work helpful, please consider citing:

```bibtex
@article{wang2026mfenet,
  title={Multi-Scale Feature Enhancement Network for Object Detection in Severe Foggy Weather},
  author={Wang, Yingjun and Yang, Xiaopeng and Wang, Yingjian and Zhuang, Peixian and Zhao, Wenyi and Lu, Haoxiang and Zhang, Weidong},
  journal={Engineering Applications of Artificial Intelligence},
  year={2026},
  note={Under Revision}
}

```

## 🤝 Acknowledgements

This work was supported by the National Natural Science Foundation of China (Grants 61971444, 62403066, etc.) and the Fundamental Research Funds for the Central Universities.

