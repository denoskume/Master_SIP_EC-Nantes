<p>
  <img align="left" src="https://www.ec-nantes.fr/medias/photo/logocn-rvb_1648479844750-png?ID_FICHE=178994&amp;INLINE=FALSE" alt="Centrale Nantes" height="64">
</p>
<p align="right"><strong>MSc. CORO DASSIP</strong></p>
<br clear="both">

# Computer Vision

Academic laboratory work in computer vision and deep learning developed within the MSc. CORO DASSIP programme at École Centrale de Nantes.

## Laboratory Modules

1. **Camera_Calibration** — normalized DLT, Zhang calibration, intrinsic/extrinsic estimation, reprojection analysis.
2. **Feature_Detection** — ORB, Hamming matching, RANSAC homography, fixed-reference object tracking.
3. **Deep_Learning** — PyTorch MLP classification on MNIST, model-capacity comparison, confidence analysis.

## Notebook Organization

Each module follows the same four-notebook separation:

```text
Problem Statement
        ↓
Requirements Gathering & Approach
        ↓
Theory
        ↓
Implementation
```

The implementation notebook is intentionally code-focused: concise execution headings, executable cells, outputs, metrics, diagnostics, and validation only. Mathematical explanations, interpretation guidance, assumptions, and limitations remain in the supporting notebooks.

## Module Structure

```text
Module_Name/
├── data/
├── notebooks/
│   ├── module_problem_statement.ipynb
│   ├── module_requirements_gathering_and_approach.ipynb
│   ├── module_theory.ipynb
│   └── module.ipynb
├── outputs/
│   └── figures/
├── requirements.txt
└── README.md
```

## Reproducibility

- repository-relative data and output paths;
- explicit dependencies in `requirements.txt`;
- top-to-bottom notebook execution;
- generated evidence stored under `outputs/figures/`;
- quantitative and visual validation;
- final numerical and output checks in the implementation notebook.
