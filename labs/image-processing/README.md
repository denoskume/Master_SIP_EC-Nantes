<p>
  <img align="left" src="https://www.ec-nantes.fr/medias/photo/logocn-rvb_1648479844750-png?ID_FICHE=178994&amp;INLINE=FALSE" alt="Centrale Nantes" height="64">
</p>
<p align="right"><strong>MSc. CORO DASSIP</strong></p>
<br clear="both">

<h1 align="center">Image Processing</h1>

Academic laboratory work in image processing developed within the MSc CORO DASSIP programme at École Centrale de Nantes.

## Laboratory Modules

| Module | Scope |
| --- | --- |
| [Image Processing Fundamentals](image-processing-fundamentals) | image formation, sampling, quantization, pixels, channels, statistics, histograms, noise, image comparison |
| [Image Transformation](image-transformation) | intensity and geometric transformations, interpolation, affine mapping |
| [Spatial-Domain Filtering](filtering-in-spatial-domain) | convolution, smoothing, denoising, sharpening, Sobel, Prewitt, Scharr |
| [Frequency-Domain Filtering](filtering-in-frequency-domain) | Fourier analysis, classical frequency filters, periodic-noise removal, moiré suppression, illumination correction |
| [Image Segmentation](segmentation) | thresholding, morphology, connected components, color segmentation, watershed, segmentation metrics |

The related larger project is maintained independently: [Background Subtraction — Fluoroscopy](https://github.com/denoskume/Background-Subtraction-Fluoroscopy).

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

The implementation notebook remains code-focused. Theory, method-selection criteria, assumptions, limitations, and interpretation belong in the supporting notebooks.

## Standard Module Structure

```text
module/
├── README.md
├── data/
├── notebooks/
│   ├── *_problem_statement.ipynb
│   ├── *_requirements_gathering_and_approach.ipynb
│   ├── *_theory.ipynb
│   └── *.ipynb
├── outputs/
│   └── figures/
└── requirements.txt
```

## Reproducibility

- repository-relative data and output paths;
- dedicated Python environment per module;
- explicit dependencies in `requirements.txt`;
- top-to-bottom notebook execution;
- generated evidence stored under `outputs/`;
- quantitative and visual validation where applicable.

[← Portfolio home](../../README.md)
