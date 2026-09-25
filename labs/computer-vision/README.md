<p>
  <img align="left" src="https://www.ec-nantes.fr/medias/photo/logocn-rvb_1648479844750-png?ID_FICHE=178994&amp;INLINE=FALSE" alt="Centrale Nantes" height="64">
</p>
<p align="right"><strong>MSc. CORO DASSIP</strong></p>
<br clear="both">

<h1 align="center">Computer Vision</h1>

Academic laboratory work in computer vision and deep learning developed within the MSc CORO DASSIP programme at École Centrale de Nantes.

## Laboratory Modules

| Module | Scope |
| --- | --- |
| [Camera Calibration](camera-calibration) | normalized DLT, Zhang calibration, intrinsic/extrinsic estimation, reprojection analysis |
| [Feature Detection & Tracking](feature-tracking) | ORB, Hamming matching, BFMatcher, RANSAC homography, fixed-reference object tracking |
| [Deep Learning](deep-learning) | PyTorch MLP classification on MNIST, model-capacity comparison, confidence analysis |

## Notebook Organization

Each module follows the same separation where appropriate:

```text
Problem Statement
        ↓
Requirements Gathering & Approach
        ↓
Theory
        ↓
Implementation
```

The implementation notebook remains code-focused: concise execution headings, executable cells, outputs, metrics, diagnostics, and validation. Mathematical explanations, assumptions, limitations, and interpretation remain in the supporting notebooks.

## Standard Module Structure

```text
module/
├── README.md
├── data/
├── notebooks/
│   ├── problem_statement.ipynb
│   ├── requirements.ipynb
│   ├── theory.ipynb
│   └── main.ipynb
├── outputs/
│   └── figures/
└── requirements.txt
```

## Reproducibility

- repository-relative data and output paths;
- explicit dependencies in `requirements.txt`;
- top-to-bottom notebook execution;
- generated evidence stored under `outputs/`;
- quantitative and visual validation;
- final numerical and output checks in implementation notebooks.

[← Portfolio home](../../README.md)
