<p>
  <img align="left" src="https://www.ec-nantes.fr/medias/photo/logocn-rvb_1648479844750-png?ID_FICHE=178994&amp;INLINE=FALSE" alt="Centrale Nantes" height="64">
</p>
<p align="right"><strong>MSc. CORO DASSIP</strong></p>
<br clear="both">

<h1 align="center">Computer Vision, Image Processing & Deep Learning</h1>

Hello and welcome to my MSc CORO DASSIP portfolio!

This repository brings together eight laboratory modules in **Computer Vision, Image Processing, and Deep Learning**. Each lab starts from a defined experimental objective, establishes the relevant theory and assumptions, implements the required methods, and evaluates the observations through quantitative measures, visual diagnostics, and validation checks.

The repository follows the same structure across all labs: a **Problem Statement** defines the experiment, **Theory** develops the required concepts and models, **Requirements** specifies the environment and data, and **Implementation** contains the executable workflow, results, analysis, and validation. Source data and generated figures remain separated in dedicated `data/` and `outputs/` directories.

Beyond the code, the notebooks document the experimental reasoning: how methods and parameters are selected, how results are interpreted, which assumptions hold, and where limitations appear. The modules below provide a direct path from laboratory specification to analyzed and validated results.

---

## Laboratory Work

### Computer Vision

| Module | Main topics |
| --- | --- |
| [Camera Calibration](labs/computer-vision/camera-calibration) | normalized DLT, Zhang calibration, SVD, intrinsic/extrinsic estimation, reprojection error |
| [Feature Detection & Tracking](labs/computer-vision/feature-tracking) | ORB, Hamming matching, BFMatcher, RANSAC, homography, object tracking |
| [Deep Learning](labs/computer-vision/deep-learning) | PyTorch MLP, MNIST classification, BatchNorm, ReLU, Cross-Entropy, Adam, model evaluation |

[Computer Vision →](labs/computer-vision)

### Image Processing

| Module | Main topics |
| --- | --- |
| [Image Processing Fundamentals](labs/image-processing/image-processing-fundamentals) | image representation, intensity operations, statistics, histograms, noise |
| [Image Transformation](labs/image-processing/image-transformation) | intensity and geometric transformations, interpolation, affine mapping |
| [Spatial-Domain Filtering](labs/image-processing/filtering-in-spatial-domain) | convolution, smoothing, denoising, sharpening, Sobel, Prewitt, Scharr |
| [Frequency-Domain Filtering](labs/image-processing/filtering-in-frequency-domain) | FFT, spectral analysis, Ideal/Gaussian/Butterworth filters, notch filtering |
| [Image Segmentation](labs/image-processing/segmentation) | thresholding, morphology, connected components, HSV segmentation, watershed, IoU, Dice |

[Image Processing →](labs/image-processing)

---

## Notebook Structure

Each laboratory module contains:

```text
notebooks/
├── theory.ipynb
├── problem_statement.ipynb
├── requirements.ipynb
└── main.ipynb
```

- **Theory** — concepts, formulas, assumptions, limitations, and references.
- **Problem Statement** — context, objectives, tasks, input data, and deliverables.
- **Requirements** — Python version, dependencies, required data, and installation instructions.
- **Implementation** — executable code, outputs, metrics, diagnostics, validation, and final interpretation.

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
├── .github/
│   └── workflows/
│       └── notebook-qa.yml
├── scripts/
│   └── validate_notebooks.py
├── .gitignore
└── README.md
```

---

## Standalone Projects

- [Background Subtraction — Fluoroscopy](https://github.com/denoskume/Background-Subtraction-Fluoroscopy)
- [CLAP Zero-Shot Audio Classification](https://github.com/denoskume/CLAP-Zero-Shot-Audio-Classification)
- [Python CardGame](https://github.com/denoskume/Python-CardGame)

---

## Repository Standard

- one `requirements.txt` per laboratory module;
- repository-relative data and output paths;
- four notebooks per laboratory module;
- generated figures under `outputs/figures/`;
- explicit numerical and output validation in implementation notebooks;
- final technical interpretation in each `main.ipynb`.

---

## Automated QA

The `Notebook QA` workflow runs on pushes to `main` and on pull requests.

It checks:

- 8 laboratory modules;
- 32 notebooks;
- notebook JSON validity;
- Python syntax in every code cell;
- absence of machine-specific absolute paths;
- absence of the deprecated `Zero to Mastery` wording;
- presence of `Final Analysis & Interpretation` in every implementation notebook.

---

## Technical Stack

**Python • NumPy • SciPy • Matplotlib • OpenCV • Pillow • PyTorch • python-mnist • tqdm • Jupyter • VS Code • WSL Ubuntu**

---

[GitHub profile →](https://github.com/denoskume)
