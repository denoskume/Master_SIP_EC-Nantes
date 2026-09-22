# Filtering in Spatial Domain

Beginner-first laboratory covering neighborhood-based image filtering, denoising, sharpening, derivative operators, border handling, parameter selection, and quantitative validation.

The laboratory builds directly on `Image_Processing_Fundamental` and `Image_Transformation`. It is designed so that a learner with no previous filtering background can move from a hand-computed 3×3 neighborhood operation to robust SciPy/OpenCV implementations.

## Problem

Spatial filtering computes each output pixel from a local neighborhood.

A correct implementation requires more than calling a filtering function. The learner must understand:

- point processing vs neighborhood processing;
- kernels, anchors, weights, and kernel sums;
- correlation vs convolution;
- manual neighborhood computation;
- border handling;
- mean and Gaussian smoothing;
- Gaussian sigma and separability;
- median filtering and impulse noise;
- bilateral filtering and edge preservation;
- MAE, MSE, RMSE, and PSNR;
- Laplacian sharpening;
- unsharp masking and high-boost filtering;
- Sobel, Prewitt, and Scharr derivatives;
- gradient magnitude and orientation;
- RGB spatial filtering;
- dtype, clipping, and signed derivative safety;
- filter-selection trade-offs.

## Objectives

By the end of the notebook, the learner should be able to:

1. Explain neighborhood-based image processing.
2. Distinguish correlation and convolution.
3. Compute a small convolution manually.
4. Interpret kernel size, symmetry, weights, and normalization.
5. Explain and compare common padding modes.
6. Apply and tune mean filtering.
7. Build a Gaussian kernel from first principles.
8. Explain Gaussian sigma and separability.
9. Apply Gaussian smoothing.
10. Explain why noise type matters.
11. Apply median filtering to impulse noise.
12. Explain bilateral filtering and its parameters.
13. Compare denoising methods quantitatively.
14. Explain PSNR limitations.
15. Apply Laplacian sharpening.
16. Apply unsharp masking and high-boost filtering.
17. Compute Sobel gradients and orientation.
18. Compare Sobel, Prewitt, and Scharr.
19. Filter RGB images without mixing channels.
20. Avoid common numerical and implementation mistakes.
21. Choose a filter based on the degradation and objective.
22. Validate results numerically and visually.

## Method

```text
Visual idea
    ↓
Mathematical model
    ↓
Neighborhood / kernel interpretation
    ↓
Small manual example
    ↓
Python implementation
    ↓
Visualization
    ↓
Parameter experiment
    ↓
Interpretation
    ↓
Common pitfall
    ↓
Validation
```

## Fundamental Configuration

| Parameter | Value |
|---|---:|
| Main numeric library | NumPy |
| Visualization | Matplotlib |
| Image I/O | Pillow |
| Scientific filtering | SciPy |
| Computer vision operations | OpenCV |
| Primary stored dtype | `uint8` |
| Processing dtype | floating point / signed where required |
| Notebook environment | Jupyter |
| Python version | 3.12.3 |
| Generated figures | PNG |

## Project Structure

```text
Filtering_in_Spatial_Domain/
├── .venv/
├── data/
│   ├── ascentB.png
│   ├── moon-blurred.tif
│   └── bilateral/
│       ├── einstein/
│       ├── monarch/
│       ├── tajMahal/
│       └── zebra/
├── notebooks/
│   └── Filtering_in_Spatial_Domain.ipynb
├── outputs/
│   └── figures/
├── requirements.txt
└── README.md
```

The `.venv/` directory is local and is not tracked by Git.

## Notebook Structure

```text
Problem Statement
Objectives
Approach
Fundamental Configuration

0. Setup
1. Data and Output Paths
2. What Is Spatial Filtering?
3. Kernel Anatomy
4. Correlation vs Convolution
5. Convolution from First Principles
6. Border Handling
7. Mean / Box Filtering
8. Gaussian Filtering
9. Why Noise Type Matters
10. Median Filtering
11. Bilateral Filtering
12. Quantitative Denoising Metrics
13. Edge Preservation as a Secondary Check
14. Sharpening with the Laplacian
15. Unsharp Masking and High-Boost Filtering
16. First Derivatives and Image Gradients
17. Sobel vs Prewitt vs Scharr
18. Border Effects on a Real Image
19. Filtering RGB Images
20. Numerical Safety
21. Choosing a Filter
22. Standard Spatial-Filtering Workflow
23. Common Mistakes
24. Validation Checks
25. Practical Exercises
26. Interview-Style Questions

Discussion
Conclusion
Glossary
```

## Environment

Designed for Python 3.12.3 with:

```text
numpy
matplotlib
Pillow
scipy
opencv-python
ipykernel
```

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Register the kernel:

```bash
python -m ipykernel install \
  --user \
  --name filtering-spatial-domain \
  --display-name "Filtering in Spatial Domain (.venv)"
```

## Running the Notebook

Open:

```text
notebooks/Filtering_in_Spatial_Domain.ipynb
```

Select:

```text
Filtering in Spatial Domain (.venv)
```

Then run all cells from top to bottom.

The committed notebook should retain its executed outputs so that the results remain visible directly on GitHub.

## Outputs

The notebook generates and saves:

```text
01_border_modes.png
02_mean_filter.png
03_mean_kernel_sizes.png
04_gaussian_filter.png
05_gaussian_sigma_sweep.png
06_mean_vs_gaussian.png
07_noise_types.png
08_median_filter.png
09_median_sizes.png
10_bilateral_filter.png
11_bilateral_parameter_sweep.png
12_laplacian_sharpening.png
13_unsharp_highboost.png
14_sobel_gradients.png
15_gradient_orientation.png
16_derivative_operators.png
17_padding_real_image.png
18_color_filtering.png
```

## Evaluation

Validation includes:

- shape preservation;
- kernel normalization;
- derivative-kernel zero-sum checks;
- agreement between manual and SciPy convolution;
- non-negative gradient magnitude;
- RGB channel-shape preservation;
- output-range checks;
- visual comparison;
- MAE, MSE, RMSE, and PSNR comparison;
- edge/detail inspection.

Successful execution prints:

```text
All spatial-filtering validation checks passed.
```

## Practical Exercises

Exercises cover manual convolution, border handling, smoothing, denoising, sharpening, derivative operators, RGB filtering, parameter selection, and numerical validation.

## Limitations

This laboratory focuses on spatial-domain filtering. Fourier-domain filtering, segmentation, learned filters, and task-specific computer-vision pipelines are treated in later modules.

## Technologies

- Python
- NumPy
- Matplotlib
- Pillow
- SciPy
- OpenCV
- Jupyter
- Convolution
- Gaussian filtering
- Median filtering
- Bilateral filtering
- Laplacian sharpening
- Sobel / Prewitt / Scharr

## Learning Outcome

After this laboratory, the learner should be able to answer:

```text
What local structure am I trying to suppress, preserve, or emphasize?
Which filter family matches that objective?
Which parameters control the strength of the effect?
Which numerical pitfalls can corrupt the result?
How can I validate that the chosen filter actually helped?
```

The next laboratory is:

```text
Filtering_in_Frequency_Domain
```

## Participants

- **Denos Kume**

Master SIP  
École Centrale de Nantes
