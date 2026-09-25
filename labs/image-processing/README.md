<p>
  <img align="left" src="https://www.ec-nantes.fr/medias/photo/logocn-rvb_1648479844750-png?ID_FICHE=178994&amp;INLINE=FALSE" alt="Centrale Nantes" height="64">
</p>
<p align="right"><strong>MSc. CORO DASSIP</strong></p>
<br clear="both">

<h1 align="center">Image Processing</h1>

Laboratory work in **digital image processing** developed within the MSc CORO DASSIP programme at École Centrale de Nantes.

The modules progress from image representation and transformations to spatial/frequency filtering and segmentation, with reproducible code, controlled experiments, and quantitative validation.

## Current Modules

| Module | Technical scope |
| --- | --- |
| [Image Processing Fundamentals](image-processing-fundamentals) | image representation, sampling, quantization, pixels, channels, statistics, histograms, noise, image comparison |
| [Image Transformation](image-transformation) | pointwise intensity mappings, homogeneous coordinates, interpolation, affine geometry, inverse mapping, transformation composition |
| [Spatial-Domain Filtering](filtering-in-spatial-domain) | convolution, border handling, smoothing, denoising, sharpening, Sobel, Prewitt, Scharr, RGB filtering |
| [Frequency-Domain Filtering](filtering-in-frequency-domain) | 2-D FFT, magnitude/phase analysis, Ideal/Gaussian/Butterworth filters, notch filtering, moiré suppression, illumination correction |
| [Image Segmentation](segmentation) | thresholding, morphology, connected components, contours, HSV segmentation, watershed, pixel accuracy, precision, recall, IoU, Dice |

## Common Notebook Structure

Each lab follows the same notebook-first organization:

```text
notebooks/
├── theory.ipynb
├── problem_statement.ipynb
├── requirements.ipynb
└── main.ipynb
```

- **Theory** — concepts, mathematical foundations, assumptions, and limitations.
- **Problem Statement** — context, tasks, inputs, learning objectives, and deliverables.
- **Requirements** — environment, dependencies, required data, and execution checks.
- **Implementation** — executable workflow, figures, metrics, discussion, and validation.

## Lab Standard

Across the modules:

- paths are repository-relative;
- dependencies are explicit in `requirements.txt`;
- notebooks execute top-to-bottom in a dedicated environment;
- parameter studies are used where method behavior depends on tuning;
- generated figures are stored under `outputs/figures/`;
- quantitative metrics and visual evidence are used together;
- final outputs are checked explicitly for reproducibility where relevant.

## Directory Structure

```text
image-processing/
├── README.md
├── image-processing-fundamentals/
├── image-transformation/
├── filtering-in-spatial-domain/
├── filtering-in-frequency-domain/
└── segmentation/
```

Each module contains its own documentation, data, notebooks, outputs, and dependency specification where applicable.

## Related Standalone Project

The larger fluoroscopy workflow is maintained separately so this repository remains focused on laboratory modules:

[**Background Subtraction — Fluoroscopy →**](https://github.com/denoskume/Background-Subtraction-Fluoroscopy)

---

[← Portfolio home](../../README.md)
