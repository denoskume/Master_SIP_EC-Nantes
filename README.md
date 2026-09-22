# Master SIP — Centrale Nantes

**Academic engineering portfolio in Data Science, Signal & Image Processing**  
Computer Vision • Image Processing • Deep Learning • Multimodal Machine Learning

This repository collects selected laboratory work and projects developed during the Master SIP / DASSIP curriculum at **École Centrale de Nantes**.

The focus is on reproducible implementations, quantitative evaluation, technical interpretation, and clear documentation rather than isolated notebook experiments.

---

## Selected Work

| Area | Project | Core methods | Evidence |
| --- | --- | --- | --- |
| **Multimodal ML** | [CLAP Zero-Shot Audio Classification](Projects/Prompt_Engineering_Audio_Classification) | LAION-CLAP, audio-text embeddings, cosine similarity, prompt engineering, Top-k evaluation | **91.15% Top-1**, **97.45% Top-3**, **99.00% Top-5** on ESC-50 |
| **Computer Vision** | [Camera Calibration](Lab_Works/Computer_Vision/Camera_Calibration) | Zhang planar calibration, normalized DLT, SVD, intrinsic matrix estimation, pose recovery, reprojection analysis | Per-view and global reprojection-error evaluation |
| **Computer Vision** | [Feature Detection & Object Tracking](Lab_Works/Computer_Vision/Feature_Detection) | ORB, Hamming matching, RANSAC, homography, perspective transformation | Match/inlier analysis and tracked-object visualization |
| **Deep Learning** | [MNIST Classification](Lab_Works/Computer_Vision/Deep_Learning) | PyTorch MLP, BatchNorm, ReLU, Adam, confidence analysis | Comparison of 128 / 256 / 512 hidden-unit architectures |
| **Image Processing** | [Image Processing Labs](Lab_Works/Image_Processing) | Spatial filtering, Fourier analysis, transformations, morphology, segmentation | Executed notebooks, generated figures, numerical checks |

---

## Multimodal Machine Learning

### [Prompt Engineering for Unsupervised Audio Classification Using CLAP](Projects/Prompt_Engineering_Audio_Classification)

Zero-shot environmental sound classification on **ESC-50** using **LAION-CLAP**.

The project evaluates ten text-prompt strategies without ESC-50-specific training or fine-tuning.

**Key results**

- Best prompt: `an audio recording of {}`
- **91.15% Top-1 accuracy**
- **95.80% Top-2**
- **97.45% Top-3**
- **99.00% Top-5**
- **99.55% Top-10**
- **+8.10 percentage points** over the class-only prompt

The analysis also includes class-wise performance, AudioSet metadata correlations, and contextual comparison with published ESC-50 classifiers.

[Open project →](Projects/Prompt_Engineering_Audio_Classification)

---

## Computer Vision

### [Camera Calibration](Lab_Works/Computer_Vision/Camera_Calibration)

Planar camera calibration from multiple chessboard images using **Zhang's method**.

Pipeline:

```text
chessboard images
      ↓
corner detection + sub-pixel refinement
      ↓
normalized DLT homographies
      ↓
SVD calibration constraints
      ↓
intrinsic matrix K
      ↓
camera pose R, t
      ↓
reprojection-error analysis
```

The project includes intrinsic calibration, pose recovery, camera-centre visualization, and per-view/global reprojection-error analysis.

[Open project →](Lab_Works/Computer_Vision/Camera_Calibration)

### [Feature Detection & Object Tracking](Lab_Works/Computer_Vision/Feature_Detection)

Feature-based object tracking from an initial bounding box using:

```text
ORB keypoints
    ↓
binary descriptors
    ↓
Hamming matching
    ↓
RANSAC
    ↓
homography
    ↓
perspective transform
    ↓
tracked object region
```

Evaluation includes descriptor-match counts, RANSAC inliers, inlier ratios, and representative tracking frames.

[Open project →](Lab_Works/Computer_Vision/Feature_Detection)

### [Deep Learning — MNIST Classification](Lab_Works/Computer_Vision/Deep_Learning)

PyTorch implementation of one-hidden-layer multilayer perceptrons for handwritten-digit classification.

Three architectures are compared:

```text
784 → 128 → 10
784 → 256 → 10
784 → 512 → 10
```

The experiment covers model training, Batch Normalization, Adam optimization, prediction confidence, precision, recall, and architecture comparison.

[Open project →](Lab_Works/Computer_Vision/Deep_Learning)

---

## Image Processing

The image-processing work is organized as a set of focused laboratories:

- [Image Processing Fundamentals](Lab_Works/Image_Processing/Image_Processing_Fundamental)
- [Image Transformations](Lab_Works/Image_Processing/Image_Transformation)
- [Spatial-Domain Filtering](Lab_Works/Image_Processing/Filtering_in_Spatial_Domain)
- [Frequency-Domain Filtering](Lab_Works/Image_Processing/Filtering_in_Frequency_Domain)
- [Image Segmentation](Lab_Works/Image_Processing/Image_Segmentation)

### Main technical coverage

**Spatial domain**
- convolution and correlation
- mean, Gaussian, median, and bilateral filtering
- Laplacian sharpening
- unsharp masking and high-boost filtering
- Sobel, Prewitt, and Scharr derivatives
- MAE, MSE, RMSE, and PSNR

**Frequency domain**
- 2-D FFT / inverse FFT
- magnitude and phase analysis
- Ideal, Gaussian, and Butterworth filters
- high-pass and high-boost filtering
- notch-reject filtering
- periodic-noise and moiré suppression
- illumination correction

**Segmentation**
- global, Otsu, and adaptive thresholding
- morphology
- connected components
- contours and region properties
- HSV segmentation
- distance transforms and watershed
- Dice, IoU, precision, recall, and pixel accuracy

[Open Image Processing workspace →](Lab_Works/Image_Processing)

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
    ├── Prompt_Engineering_Audio_Classification/
    └── CardGame/
```

---

## Engineering Practices

Across the repository, projects are organized around:

- dedicated Python environments and explicit dependencies;
- reproducible notebook execution;
- separated data, notebooks, and generated outputs;
- quantitative evaluation where appropriate;
- visual result inspection;
- documented assumptions and limitations;
- project-specific README files;
- committed figures and notebook outputs when useful for review.

Some academic work was completed collaboratively. Individual project README files identify the participants for each laboratory or project.

---

## Technical Stack

| Area | Technologies |
| --- | --- |
| **Programming** | Python |
| **Computer Vision** | OpenCV, ORB, RANSAC, homography, camera calibration |
| **Deep Learning** | PyTorch |
| **Multimodal ML** | LAION-CLAP, audio-text embeddings |
| **Image Processing** | NumPy, SciPy, Pillow, OpenCV, FFT, morphology |
| **Data & Evaluation** | pandas, scikit-learn, NumPy |
| **Visualization** | Matplotlib |
| **Environment** | Jupyter, VS Code, WSL Ubuntu |

---

## Academic Context

**Programme:** Data Science, Signal & Image Processing — Master SIP / DASSIP  
**Institution:** École Centrale de Nantes  
**Academic period represented:** 2025–2026 and ongoing repository work

For my broader engineering portfolio and current projects, see my [GitHub profile](https://github.com/denoskume).
