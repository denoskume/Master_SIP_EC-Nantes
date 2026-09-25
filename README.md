# Master SIP — Centrale Nantes

**Academic engineering portfolio in Data Science, Signal & Image Processing**  
Computer Vision • Image Processing • Deep Learning

This repository contains laboratory work developed during the **Master CORO / DASSIP at École Centrale de Nantes**. The focus is on reproducible implementations, quantitative validation, technical interpretation, and structured engineering documentation.

---

## Lab Work

### Computer Vision

| Module | Main topics |
| --- | --- |
| [Camera Calibration](Lab_Works/Computer_Vision/Camera_Calibration) | Zhang calibration, normalized DLT, SVD, intrinsic/extrinsic estimation, reprojection error |
| [Feature Detection & Tracking](Lab_Works/Computer_Vision/Feature_Detection) | ORB, Hamming matching, BFMatcher, RANSAC, homography, object tracking |
| [Deep Learning](Lab_Works/Computer_Vision/Deep_Learning) | PyTorch MLP, MNIST classification, BatchNorm, ReLU, Cross-Entropy, Adam, model evaluation |

### Image Processing

| Module | Main topics |
| --- | --- |
| [Image Processing Fundamentals](Lab_Works/Image_Processing/Image_Processing_Fundamental) | image representation, intensity operations, histograms |
| [Image Transformation](Lab_Works/Image_Processing/Image_Transformation) | geometric and intensity transformations |
| [Spatial-Domain Filtering](Lab_Works/Image_Processing/Filtering_in_Spatial_Domain) | convolution, smoothing, denoising, sharpening, Sobel, Prewitt, Scharr |
| [Frequency-Domain Filtering](Lab_Works/Image_Processing/Filtering_in_Frequency_Domain) | FFT, spectral analysis, Ideal/Gaussian/Butterworth filters, notch filtering |
| [Image Segmentation](Lab_Works/Image_Processing/Image_Segmentation) | thresholding, morphology, connected components, HSV segmentation, watershed, IoU, Dice |

---

## Notebook Organization

Laboratory modules use a consistent four-notebook organization where appropriate:

```text
Problem Statement
      ↓
Requirements Gathering & Approach
      ↓
Theory
      ↓
Implementation
```

- **Problem Statement** — context, objectives, constraints, and expected deliverables.
- **Requirements Gathering & Approach** — implementation requirements, workflow, and acceptance criteria.
- **Theory** — mathematical foundations, assumptions, and limitations.
- **Implementation** — concise execution headings, executable code, generated outputs, metrics, diagnostics, and validation only. Theory, interpretive guidance, and method-selection discussion remain in the supporting notebooks.

Generated results are stored inside each module's `outputs/` directory when applicable.

### Standalone Projects

The larger project work has been moved out of this academic lab repository and is maintained independently:

- [Background Subtraction — Fluoroscopy](https://github.com/denoskume/Background-Subtraction-Fluoroscopy)
- [CLAP Zero-Shot Audio Classification](https://github.com/denoskume/CLAP-Zero-Shot-Audio-Classification)
- [Python CardGame](https://github.com/denoskume/Python-CardGame)

---

## Repository Structure

```text
Master_SIP_EC-Nantes/
├── Lab_Works/
│   ├── Computer_Vision/
│   │   ├── Camera_Calibration/
│   │   ├── Deep_Learning/
│   │   └── Feature_Detection/
│   │
│   └── Image_Processing/
│       ├── Filtering_in_Frequency_Domain/
│       ├── Filtering_in_Spatial_Domain/
│       ├── Image_Processing_Fundamental/
│       ├── Image_Segmentation/
│       └── Image_Transformation/
│
├── .gitignore
└── README.md
```

---

## Engineering Practices

- reproducible Python environments and explicit dependencies;
- clear separation of problem definition, requirements, theory, implementation, data, and generated outputs;
- implementation notebooks kept code-focused, with explanatory theory and discussion isolated in the supporting notebooks;
- quantitative and visual validation;
- controlled experiments and parameter studies;
- structured problem statements, theory, and implementation workflows;
- concise technical documentation and reproducible results.

---

## Technical Stack

**Python • NumPy • SciPy • pandas • Matplotlib • OpenCV • Pillow • scikit-learn • PyTorch • Jupyter • VS Code • WSL Ubuntu**

---

## Academic Context

**Programme:** Master CORO — Data Science, Signal & Image Processing (DASSIP)  
**Institution:** École Centrale de Nantes  
**Repository scope:** laboratory work in computer vision, image processing, and deep learning

[GitHub profile →](https://github.com/denoskume)
