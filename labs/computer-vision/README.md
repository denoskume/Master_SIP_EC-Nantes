<p>
  <img align="left" src="https://www.ec-nantes.fr/medias/photo/logocn-rvb_1648479844750-png?ID_FICHE=178994&amp;INLINE=FALSE" alt="Centrale Nantes" height="64">
</p>
<p align="right"><strong>MSc. CORO DASSIP</strong></p>
<br clear="both">

<h1 align="center">Computer Vision</h1>

Laboratory work in **computer vision and deep learning** developed within the MSc CORO DASSIP programme at École Centrale de Nantes.

The modules focus on reproducible implementation, quantitative validation, and technical interpretation rather than isolated code exercises.

## Current Modules

| Module | Technical scope |
| --- | --- |
| [Camera Calibration](camera-calibration) | normalized DLT, Zhang calibration, SVD, intrinsic/extrinsic estimation, camera poses, reprojection error |
| [Feature Detection & Tracking](feature-tracking) | ORB, binary descriptors, Hamming matching, BFMatcher, RANSAC, homography, fixed-reference object tracking |
| [Deep Learning](deep-learning) | PyTorch MLP on MNIST, BatchNorm, ReLU, Cross-Entropy, Adam, hidden-size comparison, confidence analysis |

## Common Notebook Structure

Each lab follows the same notebook-first organization:

```text
notebooks/
├── theory.ipynb
├── problem_statement.ipynb
├── requirements.ipynb
└── main.ipynb
```

- **Theory** — concepts, mathematical foundations, assumptions, and limitations.
- **Problem Statement** — context, tasks, inputs, learning objectives, and deliverables.
- **Requirements** — environment, dependencies, required data, and execution checks.
- **Implementation** — executable workflow, figures, metrics, discussion, and validation.

## Lab Standard

Across the modules:

- paths are repository-relative;
- dependencies are declared in each module's `requirements.txt`;
- `main.ipynb` is structured for top-to-bottom execution;
- generated evidence is stored under `outputs/`;
- numerical results are paired with visual diagnostics;
- implementation notebooks close with explicit validation, consistency checks, and final technical interpretation where relevant.

## Directory Structure

```text
computer-vision/
├── README.md
├── camera-calibration/
│   ├── README.md
│   ├── data/
│   ├── notebooks/
│   ├── outputs/
│   └── requirements.txt
├── deep-learning/
│   ├── README.md
│   ├── data/
│   ├── notebooks/
│   ├── outputs/
│   └── requirements.txt
└── feature-tracking/
    ├── README.md
    ├── data/
    ├── notebooks/
    ├── outputs/
    └── requirements.txt
```

## Related Standalone Project

The larger fluoroscopy project is maintained separately so it can be reviewed as a complete computer-vision and image-processing workflow:

[**Background Subtraction — Fluoroscopy →**](https://github.com/denoskume/Background-Subtraction-Fluoroscopy)

---

[← Portfolio home](../../README.md)
