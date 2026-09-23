# Image Processing

Image-processing laboratory portfolio organized under the repository-wide **Camera Calibration reference standard**.

```text
Canonical reference:
Lab_Works/Computer_Vision/Camera_Calibration/
```

The subject matter and number of tasks vary by module. The structural roles, notebook traceability, README order, reproducibility rules, and validation discipline do not.

## Laboratory Modules

1. **Image_Processing_Fundamental** — image formation, sampling, quantization, pixels, channels, statistics, histograms, noise, and image comparison.
2. **Image_Transformation** — intensity and geometric transformations, interpolation, and affine mapping.
3. **Filtering_in_Spatial_Domain** — convolution, smoothing, denoising, sharpening, and gradients.
4. **Filtering_in_Frequency_Domain** — Fourier analysis, classical frequency filters, periodic-noise removal, moiré suppression, and illumination correction.
5. **Image_Segmentation** — thresholding, morphology, connected components, color segmentation, watershed, and segmentation metrics.

The related **Background Subtraction** project is maintained separately under [`Projects/Background_Subtraction`](../../Projects/Background_Subtraction).

## Mandatory Module Structure

Every scientific module follows the Camera Calibration backbone:

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

The four notebooks use the same numbered task sequence inside a module:

```text
Problem Statement
        ↓
Requirements Gathering & Approach
        ↓
Theory
        ↓
Implementation
```

The number of tasks is determined by the problem itself. It is **not** required to match Camera Calibration's task count.

## Execution Policy

- repository-relative paths only;
- dedicated local `.venv` per module;
- dependencies explicitly pinned in `requirements.txt`;
- top-to-bottom notebook execution;
- generated figures stored under `outputs/figures/`;
- quantitative and visual validation where applicable;
- explicit final validation checks;
- no module is considered complete unless its four notebooks remain task-aligned.

## Reference Rule

When a structural question is ambiguous, **Camera Calibration wins**. Other modules are not templates for one another.
