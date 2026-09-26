<p>
  <img align="left" src="https://www.ec-nantes.fr/medias/photo/logocn-rvb_1648479844750-png?ID_FICHE=178994&amp;INLINE=FALSE" alt="Centrale Nantes" height="64">
</p>
<p align="right"><strong>MSc. CORO DASSIP</strong></p>
<br clear="both">

<h1 align="center">MSc CORO DASSIP — Portfolio</h1>

This repository brings together laboratory modules in **Computer Vision, Image Processing, and Deep Learning**.

Each lab begins with a defined experimental objective, develops the relevant theory and assumptions, implements the required methods, and evaluates the results through quantitative measures, visual diagnostics, and validation checks.

All labs follow the same structure:

- **Problem Statement** — defines the experiment
- **Theory** — develops the required concepts and models
- **Requirements** — specifies the environment and data
- **Implementation** — contains the executable workflow, results, and analysis

Source data and generated figures are kept separate in `data/` and `outputs/`.

Beyond the code, the notebooks document the experimental reasoning: how methods and parameters are selected, how results are interpreted, which assumptions hold, and where limitations appear.

---

## Laboratory Work

### Computer Vision

| Module | Main topics |
| --- | --- |
| [Camera Calibration](labs/computer-vision/camera-calibration) | normalized DLT, Zhang calibration, SVD, intrinsic/extrinsic estimation, reprojection error |
| [Feature Detection & Tracking](labs/computer-vision/feature-tracking) | ORB, Hamming matching, BFMatcher, RANSAC, homography, object tracking |
| [Deep Learning](labs/computer-vision/deep-learning) | PyTorch MLP, MNIST classification, BatchNorm, ReLU, Cross-Entropy, Adam, model evaluation |

<p align="center">
  <a href="labs/computer-vision">
    <img src="https://img.shields.io/badge/Computer_Vision-Open_Module-181717?style=for-the-badge" alt="Computer Vision" />
  </a>
</p>

### Image Processing

| Module | Main topics |
| --- | --- |
| [Image Processing Fundamentals](labs/image-processing/image-processing-fundamentals) | image representation, intensity operations, statistics, histograms, noise |
| [Image Transformation](labs/image-processing/image-transformation) | intensity and geometric transformations, interpolation, affine mapping |
| [Spatial-Domain Filtering](labs/image-processing/filtering-in-spatial-domain) | convolution, smoothing, denoising, sharpening, Sobel, Prewitt, Scharr |
| [Frequency-Domain Filtering](labs/image-processing/filtering-in-frequency-domain) | FFT, spectral analysis, Ideal/Gaussian/Butterworth filters, notch filtering |
| [Image Segmentation](labs/image-processing/segmentation) | thresholding, morphology, connected components, HSV segmentation, watershed, IoU, Dice |

<p align="center">
  <a href="labs/image-processing">
    <img src="https://img.shields.io/badge/Image_Processing-Open_Module-181717?style=for-the-badge" alt="Image Processing" />
  </a>
</p>

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

## Projects

<p align="center">
  <a href="https://github.com/denoskume/Background-Subtraction-Fluoroscopy">
    <img src="assets/project-background-subtraction-light.svg" width="49%" alt="Background Subtraction" />
  </a>
  <a href="https://github.com/denoskume/CLAP-Zero-Shot-Audio-Classification">
    <img src="assets/project-clap-light.svg" width="49%" alt="CLAP Audio Classification" />
  </a>
</p>

<p align="center">
  <a href="https://github.com/denoskume/Python-CardGame">
    <img src="assets/project-cardgame-light.svg" width="49%" alt="Python CardGame" />
  </a>
</p>

---

## Tools and Libraries

<table align="center">
  <tr>
    <td align="center" width="100">
      <img src="assets/tools/python.svg" height="44" alt="Python" /><br>
      <sub><b>Python</b></sub>
    </td>
    <td align="center" width="100">
      <img src="assets/tools/numpy.svg" height="44" alt="NumPy" /><br>
      <sub><b>NumPy</b></sub>
    </td>
    <td align="center" width="100">
      <img src="assets/tools/scipy.svg" height="44" alt="SciPy" /><br>
      <sub><b>SciPy</b></sub>
    </td>
    <td align="center" width="100">
      <img src="assets/tools/matplotlib.svg" height="44" alt="Matplotlib" /><br>
      <sub><b>Matplotlib</b></sub>
    </td>
    <td align="center" width="100">
      <img src="assets/tools/opencv.svg" height="44" alt="OpenCV" /><br>
      <sub><b>OpenCV</b></sub>
    </td>
  </tr>
  <tr>
    <td align="center" width="100">
      <img src="assets/tools/pytorch.svg" height="44" alt="PyTorch" /><br>
      <sub><b>PyTorch</b></sub>
    </td>
    <td align="center" width="100">
      <img src="assets/tools/jupyter.svg" height="44" alt="Jupyter" /><br>
      <sub><b>Jupyter</b></sub>
    </td>
    <td align="center" width="100">
      <img src="assets/tools/vscode.svg" height="44" alt="VS Code" /><br>
      <sub><b>VS Code</b></sub>
    </td>
    <td align="center" width="100">
      <img src="assets/tools/linux.svg" height="44" alt="Linux" /><br>
      <sub><b>Linux</b></sub>
    </td>
    <td align="center" width="100">
      <img src="assets/tools/git.svg" height="44" alt="Git" /><br>
      <sub><b>Git</b></sub>
    </td>
  </tr>
</table>

---

<p align="center">
  <a href="https://github.com/denoskume">
    <img src="https://img.shields.io/badge/GitHub-Profile-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Profile" />
  </a>
</p>
