<p>
  <img align="left" src="https://www.ec-nantes.fr/medias/photo/logocn-rvb_1648479844750-png?ID_FICHE=178994&amp;INLINE=FALSE" alt="Centrale Nantes" height="64">
</p>
<p align="right"><strong>MSc. CORO DASSIP</strong></p>
<br clear="both">

<table width="85%" align="center">
  <tr>
    <td align="center">
      <h1>Image Processing</h1>
    </td>
  </tr>
</table>

Academic laboratory work in image processing developed within the MSc. CORO DASSIP programme at École Centrale de Nantes.

## Laboratory Modules

1. **Image_Processing_Fundamental** — image formation, sampling, quantization, pixels, channels, statistics, histograms, noise, and image comparison.
2. **Image_Transformation** — intensity and geometric transformations, interpolation, and affine mapping.
3. **Filtering_in_Spatial_Domain** — convolution, smoothing, denoising, sharpening, and gradients.
4. **Filtering_in_Frequency_Domain** — Fourier analysis, classical frequency filters, periodic-noise removal, moiré suppression, and illumination correction.
5. **Image_Segmentation** — thresholding, morphology, connected components, color segmentation, watershed, and segmentation metrics.

The related **Background Subtraction** project is maintained as a standalone repository: [Background-Subtraction-Fluoroscopy](https://github.com/denoskume/Background-Subtraction-Fluoroscopy).

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

The implementation notebook is intentionally code-focused: concise execution headings, executable cells, outputs, metrics, and validation only. Mathematical explanations, interpretation guidance, method-selection criteria, assumptions, and limitations belong in the dedicated Theory and Requirements & Approach notebooks.

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
