# Image Processing

Progressive M1 image-processing laboratory series organized with the same structure and documentation conventions as the Computer Vision laboratories in this repository.

## Laboratory Sequence

1. **Image_Processing_Fundamental** — digital-image representation, sampling, quantization, pixels, channels, statistics, histograms, noise, and image comparison.
2. **Image_Transformation** — intensity and geometric transformations.
3. **Filtering_in_Spatial_Domain** — convolution, smoothing, denoising, sharpening, and gradients.
4. **Filtering_in_Frequency_Domain** — Fourier transform, spectra, low/high-pass filters, magnitude/phase, and notch filtering.
5. **Image_Segmentation** — thresholding, morphology, connected components, contours, color segmentation, IoU, and Dice.

## Project

- **Background_Subtraction** — complete foreground-extraction pipeline with registration, subtraction, enhancement, segmentation, morphology, and quantitative evaluation.

## Common Structure

Every laboratory follows the same organization:

```text
Lab_Name/
├── .venv/                  # local only, not tracked
├── data/                   # inputs used by this lab
├── notebooks/
│   └── Lab_Name.ipynb
├── outputs/
│   └── figures/
├── requirements.txt
└── README.md
```

Every notebook follows the same academic flow:

```text
Problem Statement
Objectives
Approach
Configuration
0. Setup
1...N. Complete processing pipeline
Validation Checks
Practical Exercises
Discussion
Conclusion
```

## Execution Policy

Notebooks are distributed without pre-executed outputs. Each laboratory uses its own local virtual environment and dedicated Jupyter kernel.

During local execution:

- figures are displayed inline with `plt.show()`;
- figures are also saved to `outputs/figures/`;
- outputs can be reviewed before committing the executed notebook and figures to GitHub.

This keeps source notebooks clean while preserving the same final workflow used by the Computer Vision labs.
