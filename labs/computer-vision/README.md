<p>
  <img align="left" src="https://www.ec-nantes.fr/medias/photo/logocn-rvb_1648479844750-png?ID_FICHE=178994&amp;INLINE=FALSE" alt="Centrale Nantes" height="64">
</p>
<p align="right"><strong>MSc. CORO DASSIP</strong></p>
<br clear="both">

<h1 align="center">Computer Vision</h1>

Laboratory modules in **computer vision and deep learning**.

**Topics:** planar camera calibration, feature-based object tracking, and MNIST classification.

## Modules

| Module | Technical scope |
| --- | --- |
| [Camera Calibration](camera-calibration) | normalized DLT, Zhang calibration, SVD, intrinsic/extrinsic estimation, camera poses, reprojection error |
| [Feature Detection & Tracking](feature-tracking) | ORB, binary descriptors, Hamming matching, BFMatcher, RANSAC, homography, fixed-reference object tracking |
| [Deep Learning](deep-learning) | PyTorch MLP on MNIST, BatchNorm, ReLU, Cross-Entropy, Adam, hidden-size comparison, confidence analysis |

## Notebook Structure

Each module contains:

```text
notebooks/
├── theory.ipynb
├── problem_statement.ipynb
├── requirements.ipynb
└── main.ipynb
```

- **Theory** — mathematical foundations, assumptions, limitations, and references.
- **Problem Statement** — context, tasks, inputs, objectives, and deliverables.
- **Requirements** — environment, dependencies, required data, and installation.
- **Implementation** — code, outputs, metrics, diagnostics, validation, and final interpretation.

## Module Standard

- repository-relative paths;
- module-specific `requirements.txt`;
- top-to-bottom implementation workflow;
- generated figures under `outputs/figures/`;
- numerical and visual diagnostics;
- explicit validation and final technical interpretation.

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

---

[← Portfolio home](../../README.md)
