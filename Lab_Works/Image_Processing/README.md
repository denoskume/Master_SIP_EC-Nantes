# Image Processing

Academic laboratory work in image processing developed within the MSc. CORO DASSIP programme at École Centrale de Nantes.

## Laboratory Modules

1. **Image_Processing_Fundamental** — image formation, sampling, quantization, pixels, channels, statistics, histograms, noise, and image comparison.
2. **Image_Transformation** — intensity and geometric transformations, interpolation, and affine mapping.
3. **Filtering_in_Spatial_Domain** — convolution, smoothing, denoising, sharpening, and gradients.
4. **Filtering_in_Frequency_Domain** — Fourier analysis, classical frequency filters, periodic-noise removal, moiré suppression, and illumination correction.
5. **Image_Segmentation** — thresholding, morphology, connected components, color segmentation, watershed, and segmentation metrics.

The related **Background Subtraction** project is maintained separately under [`Projects/Background_Subtraction`](../../Projects/Background_Subtraction).

## Notebook Organization

Each module separates the work into complementary notebooks:

```text
Problem Statement
        ↓
Requirements Gathering & Approach
        ↓
Theory
        ↓
Implementation
```

The scope and number of numbered stages depend on the subject of each module.

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
- dedicated Python environment per module;
- explicit dependencies in `requirements.txt`;
- top-to-bottom notebook execution;
- generated figures stored under `outputs/figures/`;
- quantitative and visual validation where applicable;
- final numerical and output checks in the implementation notebook.
