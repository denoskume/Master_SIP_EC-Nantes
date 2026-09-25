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

Each laboratory module follows the same notebook-first structure:

```text
notebooks/
├── theory.ipynb
├── problem_statement.ipynb
├── requirements.ipynb
└── main.ipynb
```

- **Theory** — concepts, formulas, assumptions, method behavior, and references.
- **Problem Statement** — context, learning objectives, tasks, input data, and expected deliverables.
- **Requirements** — Python environment, required packages, input-data checks, and execution prerequisites.
- **Implementation** — executable workflow, generated figures, quantitative results, discussion, and validation.

Each lab keeps its own `data/`, `notebooks/`, `outputs/`, `README.md`, and `requirements.txt`.

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

## Lab Standard

- notebook-based implementation rather than a software-package layout;
- explicit dependencies in each lab's `requirements.txt`;
- repository-relative paths and reproducible execution;
- separate theory, problem statement, requirements, and implementation notebooks;
- generated figures and results stored under `outputs/`;
- quantitative and visual validation where relevant.

---

## Technical Stack

**Python • NumPy • SciPy • pandas • Matplotlib • OpenCV • Pillow • scikit-learn • PyTorch • Jupyter • VS Code • WSL Ubuntu**

---

## Academic Context

**Programme:** MSc CORO — Data Science, Signal & Image Processing (DASSIP)  
**Institution:** École Centrale de Nantes  
**Repository scope:** laboratory work in computer vision, image processing, and deep learning

[GitHub profile →](https://github.com/denoskume)
