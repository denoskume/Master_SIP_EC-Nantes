# Filtering in Frequency Domain

Frequency-domain image processing laboratory covering Fourier analysis, spectral interpretation, filtering, periodic-noise removal, moiré suppression, and illumination correction.

## Problem

Images can be analyzed not only in the spatial domain, where operations act directly on pixels, but also in the frequency domain, where the image is represented as a combination of spatial frequencies.

This laboratory develops the complete path from spatial-frequency intuition to practical Fourier-domain filtering.

Typical interpretations include:

* smooth variations and illumination → low frequencies;
* edges and fine textures → high frequencies;
* blur → reduction of high-frequency content;
* periodic noise → localized spectral peaks;
* repeated image structures → characteristic frequency patterns.

## Objectives

The laboratory aims to develop both theoretical understanding and practical implementation skills.

By the end of the notebook, the reader should be able to:

1. Explain spatial frequency from first principles.
2. Understand the connection between sinusoids, complex numbers, and the Fourier transform.
3. Compute and visualize the 2-D Fourier transform of an image.
4. Use `fftshift` and `ifftshift` correctly.
5. Interpret magnitude and phase spectra.
6. Reconstruct images with the inverse FFT.
7. Explain the structural importance of Fourier phase.
8. Design Ideal, Gaussian, and Butterworth low-pass filters.
9. Construct corresponding high-pass filters.
10. Perform high-boost sharpening.
11. Explain ringing and the Gibbs phenomenon.
12. Understand the convolution theorem.
13. Design band-pass and band-reject filters.
14. Detect periodic interference in the frequency spectrum.
15. Build notch-reject filters.
16. Reduce moiré patterns.
17. Estimate and correct slowly varying illumination.
18. Validate frequency-domain processing numerically and visually.
19. Recognize common FFT implementation mistakes.

## Method

The notebook is designed for an **absolute beginner** and progresses from intuition to implementation.

Each major concept follows the same structure:

1. intuitive explanation;
2. mathematical formulation;
3. Python implementation;
4. visual experiment;
5. result interpretation;
6. common mistakes;
7. practical exercises;
8. interview and exam questions.

The goal is not simply to execute FFT functions, but to understand how spatial image structure is represented in the frequency domain.

## Fundamental Configuration

| Parameter | Value |
|---|---:|
| Main numeric library | NumPy |
| Visualization | Matplotlib |
| Image I/O | Pillow |
| Fourier transform | NumPy FFT |
| Frequency origin | centered with `fftshift` |
| Reconstruction | inverse FFT |
| Notebook environment | Jupyter |
| Python version | 3.12.x |
| Generated figures | PNG |

## Project Structure

```text
Filtering_in_Frequency_Domain/
├── .venv/
├── data/
│   ├── Fourier/
│   │   ├── house.png
│   │   ├── squares.png
│   │   ├── textures.jpg
│   │   ├── tiled.png
│   │   └── zebra-wall.png
│   │
│   ├── Frequency/
│   │   ├── astronaut-interference.tif
│   │   ├── car-moire-pattern.tif
│   │   ├── checkerboard.png
│   │   ├── face1.jpg
│   │   ├── face2.jpg
│   │   ├── frequences.png
│   │   ├── hand.png
│   │   ├── letter.png
│   │   ├── seaport.jpg
│   │   ├── snow.jpg
│   │   ├── squares.png
│   │   ├── sunset.jpg
│   │   ├── text-spotshade.tif
│   │   └── tower.jpg
│   │
│   └── PhaseMag/
│       ├── cat.jpg
│       └── wolf.jpg
│
├── notebooks/
│   └── Filtering_in_Frequency_Domain.ipynb
│
├── outputs/
│   └── figures/
│
├── requirements.txt
├── .gitignore
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
1. Spatial Frequency
2. Sinusoids, Complex Numbers, and the DFT
3. The 2-D Fourier Transform for Images
4. Reading a 2-D Spectrum
5. Inverse FFT and Reconstruction
6. Magnitude vs Phase
7. Frequency-Domain Filtering
8. Frequency Distance Grid
9. Ideal, Gaussian, and Butterworth Low-Pass Filters
10. Ringing and the Gibbs Phenomenon
11. High-Pass Filtering
12. High-Boost Sharpening
13. Convolution Theorem
14. Band-Pass and Band-Reject Filters
15. Periodic Noise
16. Spectral Peak Detection
17. Notch-Reject Filtering
18. Moiré Removal
19. Slowly Varying Illumination / Shading
20. Cutoff Sensitivity
21. Quantitative Checks
22. Validation Checks
23. Common Mistakes
24. Practical Exercises
25. Interview / Exam Questions
26. Final Concept Map

Discussion
Conclusion
```

## Core Concepts

### Spatial Frequency

Spatial frequency describes how rapidly image intensity changes across space.

Low frequencies correspond mainly to smooth structures and gradual variations.

High frequencies correspond mainly to rapid changes such as:

* edges;
* fine texture;
* small details;
* some forms of noise.

### Fourier Transform

For an image \(f(x,y)\), the two-dimensional discrete Fourier transform is

$$
F(u,v)
=
\sum_{x=0}^{M-1}
\sum_{y=0}^{N-1}
f(x,y)
e^{-j2\pi\left(\frac{ux}{M}+\frac{vy}{N}\right)}.
$$

The FFT is used to compute this transform efficiently.

### Magnitude and Phase

A Fourier coefficient can be represented as

$$
F(u,v)
=
|F(u,v)|e^{j\phi(u,v)}.
$$

The magnitude represents the strength of frequency components.

The phase contains important spatial and structural information.

The notebook demonstrates this experimentally using the supplied `cat.jpg` and `wolf.jpg` images.

### Frequency-Domain Filtering

Frequency-domain filtering follows

$$
G(u,v)
=
H(u,v)F(u,v),
$$

followed by inverse Fourier transformation.

The notebook compares:

* Ideal filtering;
* Gaussian filtering;
* Butterworth filtering.

## Low-Pass Filters

Low-pass filters preserve low frequencies and suppress high-frequency information.

They are primarily associated with:

* smoothing;
* removal of fine detail;
* estimation of slowly varying image components.

The laboratory compares three families.

### Ideal Low-Pass Filter

Abrupt frequency cutoff.

Main limitation:

* significant ringing near sharp spatial transitions.

### Gaussian Low-Pass Filter

Smooth frequency transition.

Advantages:

* very low ringing;
* smooth spatial response.

### Butterworth Low-Pass Filter

Provides a controllable transition using filter order.

The order controls how quickly the response changes from passband to stopband.

## High-Pass Filtering

High-pass filters suppress low frequencies and preserve high-frequency information.

They emphasize:

* edges;
* details;
* texture;
* noise.

High-frequency detail is also used for high-boost sharpening.

## Ringing

The notebook demonstrates the relationship between an abrupt frequency cutoff and oscillatory spatial artifacts.

This behavior is related to the Gibbs phenomenon.

A synthetic square image is used to compare Ideal, Gaussian, and Butterworth responses.

## Magnitude and Phase Experiment

The notebook exchanges Fourier magnitude and phase between two images.

This demonstrates that phase often carries much of the recognizable spatial organization of an image.

## Convolution Theorem

The laboratory connects spatial-domain filtering with frequency-domain processing through

$$
f*h
\quad\Longleftrightarrow\quad
F\cdot H.
$$

It also introduces the distinction between:

* circular convolution;
* linear convolution;
* the role of zero-padding.

## Periodic Noise

Periodic interference frequently produces localized spectral peaks.

The notebook includes:

* spectrum inspection;
* candidate peak detection;
* conjugate symmetry;
* notch-mask construction;
* selective frequency removal.

The supplied image

```text
astronaut-interference.tif
```

is used for this experiment.

## Moiré Removal

The laboratory applies frequency-domain notch filtering to

```text
car-moire-pattern.tif
```

to demonstrate how periodic moiré interference can be isolated and attenuated.

## Illumination Correction

The notebook uses

```text
text-spotshade.tif
```

to demonstrate how slowly varying illumination can be estimated from low-frequency information.

A multiplicative image model is introduced:

$$
I(x,y)
\approx
R(x,y)L(x,y).
$$

The illumination field is estimated with low-pass filtering and used for normalization.

## Quantitative Evaluation

The notebook includes:

### Mean Squared Error

$$
\mathrm{MSE}
=
\frac{1}{MN}
\sum_{x,y}
[f(x,y)-g(x,y)]^2
$$

### Peak Signal-to-Noise Ratio

$$
\mathrm{PSNR}
=
10\log_{10}
\left(
\frac{255^2}{\mathrm{MSE}}
\right).
$$

The notebook also explains why PSNR must be interpreted in context and should not automatically be treated as a perceptual-quality score.

## Evaluation

The notebook performs checks for:

* FFT/IFFT reconstruction accuracy;
* image-shape preservation;
* finite filter values;
* valid filter range;
* low-pass DC preservation;
* high-pass DC rejection;
* consistency of frequency masks.

## Outputs

During execution, figures are saved to:

```text
outputs/figures/
```

Representative outputs include:

```text
01_spatial_frequency.png
02_fft_1d.png
03_house_spectrum.png
04_orientation_spectra.png
05_dataset_spectra.png
06_reconstruction.png
07_phase_magnitude_swap.png
08_phase_only_magnitude_only.png
09_lpf_comparison.png
10_butterworth_orders.png
11_ringing.png
12_high_pass.png
13_high_boost.png
14_band_filters.png
15_periodic_noise_spectra.png
16_notch_filter.png
17_moire_removal.png
18_shading_correction.png
19_cutoff_sensitivity.png
```

## Environment

Designed for Python 3.12.

Dependencies are defined in:

```text
requirements.txt
```

The core environment uses:

```text
numpy
matplotlib
Pillow
ipykernel
```

Additional packages can remain in `requirements.txt` if they are shared with the broader image-processing lab environment.

## Installation

From the laboratory directory:

```bash
python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Register the dedicated Jupyter kernel:

```bash
python -m ipykernel install \
  --user \
  --name filtering-frequency-domain \
  --display-name "Filtering in Frequency Domain (.venv)"
```

## Running the Notebook

Open:

```text
notebooks/Filtering_in_Frequency_Domain.ipynb
```

in VS Code.

Select:

```text
Filtering in Frequency Domain (.venv)
```

as the notebook kernel.

Then execute:

```text
Run All
```

from the first cell to the last.

The final committed notebook should retain its executed outputs so that figures and results remain directly visible on GitHub.

## Common Mistakes Covered

The notebook explicitly addresses:

* confusing pixel brightness with spatial frequency;
* displaying raw FFT magnitude;
* forgetting `fftshift`;
* forgetting `ifftshift`;
* assuming all high frequencies are noise;
* treating every bright spectral peak as interference;
* ignoring conjugate symmetry;
* using aggressive Ideal filters without considering ringing;
* ignoring circular convolution;
* using PSNR without understanding the reference;
* applying filters without interpreting the resulting spectrum.

## Practical Exercises

Exercises are organized into:

* beginner;
* intermediate;
* advanced.

They include:

* synthetic frequency generation;
* spectrum prediction;
* phase/magnitude experiments;
* cutoff studies;
* Butterworth-order studies;
* ringing analysis;
* manual notch selection;
* periodic-noise removal;
* moiré suppression;
* illumination correction;
* circular-versus-linear convolution.

## Limitations

This laboratory focuses on classical Fourier-domain image processing. It does not cover wavelet transforms, learned frequency representations, or advanced restoration methods.

## Technologies

* Python
* NumPy
* Matplotlib
* Pillow
* Digital Image Processing
* Spatial Frequency
* Fourier Transform
* FFT / IFFT
* Magnitude Spectrum
* Phase Spectrum
* Ideal Filters
* Gaussian Filters
* Butterworth Filters
* Low-Pass Filtering
* High-Pass Filtering
* Band-Pass Filtering
* Band-Reject Filtering
* High-Boost Sharpening
* Ringing
* Gibbs Phenomenon
* Convolution Theorem
* Periodic Noise
* Notch Filtering
* Moiré Removal
* Illumination Correction
* MSE
* PSNR

## Learning Outcome

After completing this laboratory, the learner should be able to interpret a 2-D image spectrum, design and justify classical frequency-domain filters, diagnose periodic interference, and validate reconstruction and filtering results numerically and visually.

## Participants

**Denos Kume**

Master SIP
École Centrale de Nantes
