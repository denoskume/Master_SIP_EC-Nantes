# Image Transformation

Beginner-first laboratory covering the two fundamental families of digital-image transformations: **intensity transformations** and **geometric transformations**.

The laboratory builds directly on `Image_Processing_Fundamental`. It explains how to modify pixel values safely, how to transform image coordinates using homogeneous matrices, and why digital geometric transformation requires inverse mapping and interpolation.

## Problem

Image transformation creates a new image by changing either:

- pixel **intensities** while keeping their spatial positions fixed; or
- pixel **positions** while preserving or resampling image information.

A correct implementation requires more than calling a transformation function. The learner must understand:

- the mathematical mapping being applied;
- intensity range and clipping;
- image coordinate conventions;
- transformation matrices;
- transformation origin and center;
- matrix composition and operation order;
- inverse coordinate mapping;
- interpolation;
- output canvas and border behavior;
- aspect-ratio preservation.

## Objectives

The laboratory develops the complete fundamental transformation workflow:

1. Distinguish intensity and geometric transformations.
2. Express pointwise processing as $s=T(r)$.
3. Apply identity and negative transformations.
4. Modify brightness and contrast using linear mappings.
5. Perform contrast stretching.
6. Apply logarithmic intensity transformation.
7. Apply gamma / power-law transformation.
8. Implement global histogram equalization from first principles.
9. Represent 2-D points with homogeneous coordinates.
10. Construct translation matrices.
11. Construct scaling matrices.
12. Construct rotation matrices.
13. Construct reflection matrices.
14. Construct shear matrices.
15. Transform around the image center.
16. Explain forward and inverse mapping.
17. Apply nearest-neighbor, bilinear, and bicubic interpolation.
18. Understand fixed-canvas cropping and fill values.
19. Preserve or deliberately change aspect ratio.
20. Compose transformations using matrix multiplication.
21. Explain why transformation order matters.
22. Apply a general affine transformation.
23. Validate transformations numerically and visually.

## Method

The laboratory follows the same learning structure as the Computer Vision notebooks:

```text
Concept
    ↓
Mathematical model
    ↓
Array / coordinate interpretation
    ↓
Commented Python implementation
    ↓
Visualization
    ↓
Interpretation
    ↓
Common pitfalls
    ↓
Validation
```

The complete transformation model is:

```text
Image Transformation
│
├── Intensity transformation
│   ├── Identity
│   ├── Negative
│   ├── Brightness
│   ├── Contrast
│   ├── Contrast stretching
│   ├── Log transform
│   ├── Gamma transform
│   └── Histogram equalization
│
└── Geometric transformation
    ├── Translation
    ├── Scaling
    ├── Rotation
    ├── Reflection
    ├── Shear
    ├── Composition
    ├── Interpolation
    └── Affine transformation
```

## Experimental Configuration

| Parameter | Value |
|---|---:|
| Main numeric library | NumPy |
| Visualization | Matplotlib |
| Image I/O | Pillow |
| Geometric resampling | SciPy |
| Primary stored dtype | `uint8` |
| Intensity range | 0–255 |
| Coordinate convention | `x = column`, `y = row` |
| Homogeneous coordinate | `[x, y, 1]ᵀ` |
| Outside-image fill value | 0 |
| Interpolation | nearest / bilinear / bicubic |
| Python version | 3.12.3 |

## Project Structure

```text
Image_Transformation/
├── .venv/
├── data/
│   ├── ascentB.png
│   ├── ballons.jpg
│   ├── einstein.png
│   ├── Elizabeth_Tower_London.jpg
│   └── peppers.png
├── notebooks/
│   └── Image_Transformation.ipynb
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
Transformation Map
Experimental Configuration

0. Setup
1. Data and Output Paths
2. Load and Inspect the Reference Images
3. What Is an Intensity Transformation?
4. Image Negative
5. Brightness and Contrast
6. Contrast Stretching
7. Logarithmic Transformation
8. Gamma / Power-Law Transformation
9. Histogram Equalization
10. Compare the Fundamental Intensity Transformations
11. What Is a Geometric Transformation?
12. Homogeneous Coordinates
13. Fundamental Geometric Transformation Matrices
14. The Origin and the Image Center
15. Forward Mapping vs Inverse Mapping
16. Translation
17. Rotation
18. Scaling and Resizing
19. Why Interpolation Is Necessary
20. Reflection / Flipping
21. Shear
22. Composition of Transformations
23. General Affine Transformation
24. Resizing to a New Array Shape
25. Validation Checks
26. Common Mistakes
27. Practical Exercises

Discussion
Conclusion
Glossary
```

## Intensity Transformations

A pointwise grayscale transformation is written as:

$$
s=T(r)
$$

where $r$ is an input intensity and $s$ is the corresponding output intensity.

The spatial coordinate is unchanged.

### Identity

$$
s=r
$$

The original image is preserved exactly.

### Negative

For 8-bit images:

$$
s=255-r
$$

Bright and dark intensities are reversed.

### Brightness and Contrast

A simple linear transformation is:

$$
s=ar+b
$$

where:

- $a$ controls gain / contrast;
- $b$ controls brightness offset.

Safe processing requires floating-point arithmetic followed by clipping to `[0,255]`.

### Contrast Stretching

Contrast stretching maps the observed image range to the full 8-bit range:

$$
s=
\frac{r-r_{\min}}
{r_{\max}-r_{\min}}
\times255
$$

### Log Transform

$$
s=c\log(1+r)
$$

The logarithm expands low intensities and compresses high intensities.

### Gamma Transform

For normalized intensity:

$$
s=r^\gamma
$$

Typical behavior:

```text
γ < 1  → brighter mid/dark values
γ = 1  → identity
γ > 1  → darker mid values
```

### Histogram Equalization

Histogram equalization constructs a global mapping from the cumulative histogram:

$$
s=(L-1)\operatorname{CDF}(r)
$$

with $L=256$ for an 8-bit image.

## Geometric Transformations

A spatial transformation changes coordinates:

$$
(x,y)\rightarrow(x',y')
$$

Using homogeneous coordinates:

$$
\mathbf{p}
=
\begin{bmatrix}
x\\
y\\
1
\end{bmatrix}
$$

and:

$$
\mathbf{p}'=\mathbf{H}\mathbf{p}
$$

## Fundamental Matrices

### Translation

$$
\mathbf{T}
=
\begin{bmatrix}
1&0&t_x\\
0&1&t_y\\
0&0&1
\end{bmatrix}
$$

### Scaling

$$
\mathbf{S}
=
\begin{bmatrix}
s_x&0&0\\
0&s_y&0\\
0&0&1
\end{bmatrix}
$$

### Rotation

$$
\mathbf{R}
=
\begin{bmatrix}
\cos\theta&-\sin\theta&0\\
\sin\theta&\cos\theta&0\\
0&0&1
\end{bmatrix}
$$

### Shear

$$
\mathbf{H}
=
\begin{bmatrix}
1&k_x&0\\
k_y&1&0\\
0&0&1
\end{bmatrix}
$$

## Centered Transformations

A matrix naturally acts around the origin.

To rotate or scale around an image center:

```text
translate center to origin
    ↓
apply transformation
    ↓
translate center back
```

Matrix form:

$$
H_{centered}
=
T(center)\,H\,T(-center)
$$

## Forward and Inverse Mapping

Forward mapping applies:

$$
p_{out}=Hp_{in}
$$

but can leave holes on a discrete output grid.

The notebook therefore implements inverse mapping:

$$
p_{in}=H^{-1}p_{out}
$$

For each output pixel, the source coordinate is calculated and sampled from the input.

## Interpolation

Geometric transformations often generate non-integer source coordinates.

The notebook compares:

- nearest neighbor;
- bilinear;
- bicubic interpolation.

Nearest-neighbor interpolation is especially important for discrete label images and segmentation masks because smooth interpolation may create invalid class values.

## Transformation Composition

If:

$$
p'=H_2H_1p
$$

then $H_1$ acts first and $H_2$ acts second.

Matrix multiplication is not commutative:

$$
H_2H_1\neq H_1H_2
$$

Therefore transformation order must always be considered explicitly.

## Affine Transformation

A general 2-D affine transformation is:

$$
\begin{bmatrix}
x'\\
y'\\
1
\end{bmatrix}
=
\begin{bmatrix}
a&b&t_x\\
c&d&t_y\\
0&0&1
\end{bmatrix}
\begin{bmatrix}
x\\
y\\
1
\end{bmatrix}
$$

It can represent translation, rotation, scaling, reflection, shear, and combinations of these operations.

Parallel lines remain parallel under affine transformation.

Projective perspective transformation is outside the scope of this laboratory.

## Environment

The laboratory is designed for:

```text
Python 3.12.3
```

Direct dependencies are defined in `requirements.txt`:

```text
numpy
matplotlib
Pillow
scipy
ipykernel
```

## Installation

From the `Image_Transformation/` directory:

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
  --name image-transformation \
  --display-name "Image Transformation (.venv)"
```

## Running the Notebook

Open:

```text
notebooks/Image_Transformation.ipynb
```

Select:

```text
Image Transformation (.venv)
```

Then run all cells from top to bottom.

The notebook is delivered without pre-executed outputs.

During local execution, figures appear inline using `plt.show()` and are saved under:

```text
outputs/figures/
```

## Outputs

### Input and Intensity Transformations

```text
01_reference_images.png
02_negative.png
03_brightness_contrast.png
04_contrast_stretching.png
05_log_transform.png
06_gamma_examples.png
07_gamma_curves.png
08_histogram_equalization.png
09_equalization_mapping.png
10_intensity_transform_comparison.png
```

### Geometric Transformations

```text
11_translation.png
12_rotation_origin_center.png
13_scaling.png
14_interpolation_comparison.png
15_reflection.png
16_shear.png
17_transformation_order.png
18_affine_transform.png
```

## Evaluation

Validation includes:

- identity transformation consistency;
- valid intensity range;
- `uint8` output checks;
- gamma identity behavior;
- monotonic equalization mapping;
- transformed image shape checks;
- exact transformation of known points;
- reflection consistency;
- transformation-matrix invertibility;
- visual interpretation of all generated figures.

Successful execution reports:

```text
All image-transformation validation checks passed.
```

## Limitations

This laboratory intentionally does not cover:

- spatial convolution and filtering;
- anti-alias filter design;
- Fourier-domain transformation/filtering;
- image segmentation;
- projective homography estimation;
- perspective rectification.

These topics are treated separately in the Image Processing and Computer Vision laboratories.

## Technologies

- Python
- NumPy
- Matplotlib
- Pillow
- SciPy
- Jupyter
- Point transformations
- Contrast stretching
- Log transform
- Gamma correction
- Histogram equalization
- Homogeneous coordinates
- Translation
- Rotation
- Scaling
- Reflection
- Shear
- Inverse mapping
- Interpolation
- Affine transformation

## Learning Outcome

After this laboratory, a learner should be able to look at an image transformation and identify:

```text
What changes?
Pixel value or spatial coordinate?
```

and then determine:

```text
Which mathematical mapping is required?
Which coordinate system is being used?
Which interpolation method is appropriate?
Will the output be clipped or cropped?
Does transformation order matter?
How can the result be validated?
```

The next laboratory is:

```text
Filtering_in_Spatial_Domain
```

## Participants

- **Denos Kume**

Master SIP  
École Centrale de Nantes
