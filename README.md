# MFENet
A lightweight and robust object detection network designed for severe foggy weather, achieving high precision with low complexity.
基于您提供的论文 **EAAI-25-12673**，我为您撰写了一份完整的、高度定制的 `README.md`。

这份文档包含了您的**模型架构图**、**环境配置**、**数据集准备**、**训练/测试命令**以及最重要的**引用格式**。您可以直接复制以下内容到您的 GitHub 仓库的 `README.md` 文件中。

---

### **README.md 模板 (直接复制)**

```markdown
# Multi-Scale Feature Enhancement Network for Object Detection in Severe Foggy Weather

<div align="center">

**[EAAI Under Revision]**
**MFENet: A lightweight and robust object detection network designed for severe foggy weather, achieving high precision with low complexity.**

[![Paper](https://img.shields.io/badge/Journal-EAAI-blue)](https://www.sciencedirect.com/journal/engineering-applications-of-artificial-intelligence)
[![Framework](https://img.shields.io/badge/Framework-PyTorch-orange)](https://pytorch.org/)
[![License](https://img.shields.io/badge/License-MIT-green)]()

</div>

## 📖 Introduction

This repository contains the official PyTorch implementation of the paper: **"Multi-Scale Feature Enhancement Network for Object Detection in Severe Foggy Weather"**.

**MFENet** is designed to address the challenges of low contrast and blurred structures in foggy traffic environments. It integrates three novel modules into a lightweight architecture:
* [cite_start]**SFRM (Spatial-Frequency Feature Recovery Module):** Recovers degraded features using both local spatial details and global frequency context[cite: 16].
* [cite_start]**DIM (Dual-Dimensional Interaction Module):** Enhances feature representation through spatial and channel-wise semantic interaction[cite: 18].
* [cite_start]**OADH (Occlusion-Aware Detection Head):** Improves detection of occluded objects in dense fog[cite: 19].

### Key Performance
* [cite_start]**High Accuracy:** Achieves **78.85% mAP50** on VOC-fog and **75.89% mAP50** on RTTS datasets[cite: 47].
* [cite_start]**Real-time Speed:** Inference speed of **117 FPS** on an RTX 4060 Ti[cite: 49].
* [cite_start]**Lightweight:** Only **7.8M parameters**, balancing complexity and performance[cite: 48].

## 🏗️ Architecture

![Architecture](./assets/architecture.png)
*Figure 1: The overall architecture of MFENet, integrating SFRM, DIM, and OADH modules.* 

## 🔨 Installation

### Environment Requirements
* Linux (Tested on Ubuntu 20.04)
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

```

---

### **💡 上传前的必做事项**

1.  **创建文件夹**：在您的 GitHub 仓库里创建一个名为 `assets` 的文件夹。
2.  **上传图片**：
    * 将论文中的 **Fig. 1 (架构图)** 截图，命名为 `architecture.png`，放入 `assets` 文件夹。
    * 将论文中的 **Fig. 6 (RTTS 结果图)** 截图，命名为 `results.png`，放入 `assets` 文件夹。
3.  **替换链接**：
    * 将 `https://github.com/YourUsername/MFENet.git` 中的 `YourUsername` 替换为您真实的 GitHub 用户名。
4.  **准备依赖文件**：
    * 确保根目录下有一个 `requirements.txt` 文件（包含 `torch`, `opencv-python` 等依赖）。
    * 确保有一个 `models/MFENet.yaml` 配置文件。

这样写出来的 README 非常专业，审稿人看到会认为您的工作非常扎实且易于复现，极大地增加录用概率！

```
