# Master SIP — Centrale Nantes

**Academic engineering portfolio in Data Science, Signal & Image Processing**  
Computer Vision • Image Processing • Deep Learning • Multimodal Machine Learning

This repository contains laboratory work and selected projects developed during the **Master CORO / DASSIP at École Centrale de Nantes**. The emphasis is on reproducible implementations, quantitative validation, technical interpretation, and clean engineering documentation.

---

## Selected Work

| Area | Module / Project | Main topics |
| --- | --- | --- |
| **Computer Vision** | [Camera Calibration](Lab_Works/Computer_Vision/Camera_Calibration) | Zhang calibration, DLT, SVD, intrinsic/extrinsic estimation, reprojection error |
| **Computer Vision** | [Feature Detection & Tracking](Lab_Works/Computer_Vision/Feature_Detection) | ORB, Hamming matching, RANSAC, homography, object tracking |
| **Deep Learning** | [MNIST Classification](Lab_Works/Computer_Vision/Deep_Learning) | PyTorch MLPs, training, evaluation, architecture comparison |
| **Image Processing** | [Fundamentals](Lab_Works/Image_Processing/Image_Processing_Fundamental) | intensity operations, histograms, image representation |
| **Image Processing** | [Image Transformation](Lab_Works/Image_Processing/Image_Transformation) | geometric and intensity transformations |
| **Image Processing** | [Spatial-Domain Filtering](Lab_Works/Image_Processing/Filtering_in_Spatial_Domain) | convolution, smoothing, sharpening, derivatives |
| **Image Processing** | [Frequency-Domain Filtering](Lab_Works/Image_Processing/Filtering_in_Frequency_Domain) | FFT, spectral analysis, Butterworth/Gaussian/Ideal filtering, notch filtering |
| **Image Processing** | [Image Segmentation](Lab_Works/Image_Processing/Image_Segmentation) | thresholding, morphology, connected components, watershed, metrics |
| **Medical Imaging** | [Background Subtraction](Projects/Background_Subtraction) | static background subtraction, spatial/spectral filtering, morphology, segmentation, sequence validation |
| **Multimodal ML** | [CLAP Audio Classification](Projects/Prompt_Engineering_Audio_Classification) | zero-shot audio classification, prompt engineering, audio-text embeddings |
| **Software Project** | [CardGame](Projects/CardGame) | Python application, game logic, interface, assets |

---

## Notebook Organization

The laboratory modules and structured projects use a consistent four-notebook organization where appropriate:

```text
Problem Statement
      ↓
Requirements Gathering & Approach
      ↓
Theory
      ↓
Implementation
```

- **Problem Statement** — engineering context, objectives, constraints, and deliverables.
- **Requirements & Approach** — implementation requirements, strategy, and acceptance criteria.
- **Theory** — mathematical foundations, assumptions, and limitations.
- **Implementation** — executable experiments, figures, metrics, diagnostics, and validation.

Generated results are stored in each module's `outputs/` directory.

---

## Repository Structure

```text
Master_SIP_EC-Nantes/
├── Lab_Works/
│   ├── Computer_Vision/
│   │   ├── Camera_Calibration/
│   │   ├── Feature_Detection/
│   │   └── Deep_Learning/
│   │
│   └── Image_Processing/
│       ├── Image_Processing_Fundamental/
│       ├── Image_Transformation/
│       ├── Filtering_in_Spatial_Domain/
│       ├── Filtering_in_Frequency_Domain/
│       └── Image_Segmentation/
│
└── Projects/
    ├── Background_Subtraction/
    ├── Prompt_Engineering_Audio_Classification/
    └── CardGame/
```

---

## Engineering Practices

- reproducible Python environments and explicit dependencies;
- clear separation of data, notebooks, and generated outputs;
- quantitative and visual validation;
- controlled experiments and parameter studies;
- project-specific README files;
- committed figures and notebook outputs where useful for review.

---

## Technical Stack

**Python • NumPy • SciPy • pandas • Matplotlib • OpenCV • Pillow • scikit-learn • PyTorch • Jupyter • VS Code • WSL Ubuntu**

---

## Academic Context

**Programme:** Master CORO — Data Science, Signal & Image Processing (DASSIP)  
**Institution:** École Centrale de Nantes  
**Repository scope:** academic laboratories, engineering exercises, and selected personal/project work

[GitHub profile →](https://github.com/denoskume)
