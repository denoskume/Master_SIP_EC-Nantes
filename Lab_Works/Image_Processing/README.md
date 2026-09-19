# Image Processing Labs

M1 image-processing laboratory series organized as a progressive learning path from digital-image fundamentals to segmentation and a complete background-subtraction project.

## Laboratory sequence

1. **Image_Processing_Fundamental** — digital-image representation, pixels, coordinates, sampling, quantization, grayscale/RGB, data types, histograms, statistics, dynamic range, noise, and image comparison.
2. **Image_Transformation** — intensity and geometric transformations.
3. **Filtering_in_Spatial_Domain** — convolution, smoothing, denoising, sharpening, and gradient-based operators.
4. **Filtering_in_Frequency_Domain** — 2-D Fourier transform, spectra, low/high-pass filters, and frequency-domain interpretation.
5. **Image_Segmentation** — thresholding, morphology, connected regions, contours, and segmentation evaluation.

## Project

- **Background_Subtraction** — complete foreground/background separation pipeline.

## Shared data

Input images are stored in `data/` and reused across laboratories when appropriate. Keeping shared inputs in one location avoids duplication and makes notebook paths consistent.

## Learning philosophy

Each notebook is designed to be readable from top to bottom and combines:

- conceptual explanation;
- mathematical intuition;
- explicit Python/NumPy implementation;
- visual interpretation;
- common mistakes;
- practical exercises;
- reproducibility checks.

The sequence is cumulative: later laboratories assume the concepts established in the earlier ones.