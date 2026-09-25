# MSc CORO DASSIP Portfolio — Centrale Nantes

**Academic engineering portfolio in Data Science, Signal & Image Processing**  
Computer Vision • Image Processing • Deep Learning

This repository contains laboratory work developed within the **MSc CORO DASSIP programme at École Centrale de Nantes**. The portfolio emphasizes reproducible implementations, quantitative validation, technical interpretation, and structured engineering documentation.

---

## Laboratory Work

### Computer Vision

| Module | Main topics |
| --- | --- |
| [Camera Calibration](labs/computer-vision/camera-calibration) | normalized DLT, Zhang calibration, SVD, intrinsic/extrinsic estimation, reprojection error |
| [Feature Detection & Tracking](labs/computer-vision/feature-tracking) | ORB, Hamming matching, BFMatcher, RANSAC, homography, object tracking |
| [Deep Learning](labs/computer-vision/deep-learning) | PyTorch MLP, MNIST classification, BatchNorm, ReLU, Cross-Entropy, Adam, model evaluation |

[Computer Vision lab overview →](labs/computer-vision)

### Image Processing

| Module | Main topics |
| --- | --- |
| [Image Processing Fundamentals](labs/image-processing/image-processing-fundamentals) | image representation, intensity operations, statistics, histograms, noise |
| [Image Transformation](labs/image-processing/image-transformation) | intensity and geometric transformations, interpolation, affine mapping |
| [Spatial-Domain Filtering](labs/image-processing/filtering-in-spatial-domain) | convolution, smoothing, denoising, sharpening, Sobel, Prewitt, Scharr |
| [Frequency-Domain Filtering](labs/image-processing/filtering-in-frequency-domain) | FFT, spectral analysis, Ideal/Gaussian/Butterworth filters, notch filtering |
| [Image Segmentation](labs/image-processing/segmentation) | thresholding, morphology, connected components, HSV segmentation, watershed, IoU, Dice |

[Image Processing lab overview →](labs/image-processing)

---

## Notebook Standard

Laboratory modules use a consistent four-part organization where appropriate:

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
- **Implementation** — executable code, outputs, metrics, diagnostics, and validation.

Generated results are stored inside each module's `outputs/` directory when applicable.

---

## Repository Structure

```text
msc-coro-dassip-portfolio/
├── labs/
│   ├── computer-vision/
│   │   ├── README.md
│   │   ├── camera-calibration/
│   │   ├── deep-learning/
│   │   └── feature-tracking/
│   │
│   └── image-processing/
│       ├── README.md
│       ├── filtering-in-frequency-domain/
│       ├── filtering-in-spatial-domain/
│       ├── image-processing-fundamentals/
│       ├── image-transformation/
│       └── segmentation/
├── .gitignore
└── README.md
```

---

## Standalone Projects

Larger projects are maintained independently so each can be reviewed as a complete engineering project:

- [Background Subtraction — Fluoroscopy](https://github.com/denoskume/Background-Subtraction-Fluoroscopy)
- [CLAP Zero-Shot Audio Classification](https://github.com/denoskume/CLAP-Zero-Shot-Audio-Classification)
- [Python CardGame](https://github.com/denoskume/Python-CardGame)

---

## Engineering Practices

- reproducible Python environments and explicit dependencies;
- clear separation of problem definition, requirements, theory, implementation, data, and outputs;
- quantitative and visual validation;
- controlled experiments and parameter studies;
- concise technical documentation and reproducible results.

---

## Technical Stack

**Python • NumPy • SciPy • pandas • Matplotlib • OpenCV • Pillow • scikit-learn • PyTorch • Jupyter • VS Code • WSL Ubuntu**

---

## Academic Context

**Programme:** MSc CORO — Data Science, Signal & Image Processing (DASSIP)  
**Institution:** École Centrale de Nantes  
**Repository scope:** laboratory work in computer vision, image processing, and deep learning

[GitHub profile →](https://github.com/denoskume)
