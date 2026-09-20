# Image Processing Fundamental

Beginner-first digital-image laboratory covering the numerical representation, inspection, manipulation, visualization, noise modeling, and quantitative comparison of images.

This laboratory is designed as a first contact with image processing. No previous background in digital images is assumed.

The objective is to establish the fundamental concepts required before studying image transformations, spatial filtering, frequency-domain processing, segmentation, and computer vision.

## Problem

A person looking at an image immediately interprets objects, colors, textures, shapes, and structures.

A computer does not see an image in this way.

Image-processing algorithms operate on numerical arrays containing discrete pixel values. Before applying advanced processing methods, it is therefore necessary to understand how visual information becomes numerical data and how those values are represented, manipulated, displayed, and compared.

This laboratory introduces the foundations required to answer questions such as:

* What is a digital image?
* What is a pixel?
* How does a real scene become an image array?
* What are sampling and quantization?
* What do image dimensions represent?
* How are coordinates defined?
* What is the difference between binary, grayscale, and RGB images?
* What do image channels contain?
* What are bit depth and dynamic range?
* Why does the image data type matter?
* How should pixel arithmetic be performed safely?
* What information does an image histogram provide?
* What information does a histogram lose?
* What types of noise can affect an image?
* How can two images be compared numerically?
* What is the difference between lossless and lossy image storage?

The laboratory builds these concepts progressively using NumPy arrays, mathematical interpretation, and direct visualization.

## Objectives

The laboratory develops the complete fundamental image-processing workflow.

By the end of the notebook, the learner should be able to:

1. Explain how a real scene becomes a digital image.
2. Explain spatial sampling and intensity quantization.
3. Represent binary, grayscale, and RGB images as arrays.
4. Interpret image pixels and coordinate conventions.
5. Distinguish mathematical coordinates `(x, y)` from NumPy indexing `[row, column]`.
6. Interpret image height, width, channels, aspect ratio, and pixel count.
7. Understand image data types and bit depth.
8. Interpret available and used dynamic range.
9. Estimate image memory usage.
10. Load images reproducibly.
11. Inspect image shape, dtype, range, and dimensions.
12. Display grayscale and RGB images correctly.
13. Access and modify individual pixels safely.
14. Extract regions of interest.
15. Inspect local pixel neighborhoods.
16. Decompose RGB images into their individual channels.
17. Understand RGB and BGR channel conventions.
18. Convert RGB images to grayscale from first principles.
19. Compute global image statistics.
20. Compute and interpret intensity histograms.
21. Understand the spatial limitations of histograms.
22. Normalize image intensity values.
23. Avoid unsigned-integer overflow during arithmetic.
24. Understand clipping and floating-point processing.
25. Model Gaussian, salt-and-pepper, Poisson, and speckle noise.
26. Compare images using MAE, MSE, RMSE, and PSNR.
27. Understand practical differences between PNG and JPEG.
28. Apply a standard inspection workflow to an unfamiliar image.
29. Validate image-processing results numerically and visually.

## Method

The laboratory follows a beginner-first learning sequence.

Each important topic is developed using the following reasoning process:

```text
Concept
    ↓
Mathematical meaning
    ↓
Array representation
    ↓
Python implementation
    ↓
Visualization
    ↓
Interpretation
    ↓
Common pitfalls
    ↓
Validation
```

The objective is not to memorize image-processing functions.

Instead, the notebook develops the numerical intuition required to understand what image-processing libraries actually manipulate.

The overall learning pipeline is:

```text
Real scene
    ↓
Image acquisition
    ↓
Spatial sampling
    ↓
Intensity quantization
    ↓
Digital image
    ↓
NumPy array
    ↓
Shape / dtype / range inspection
    ↓
Pixel and channel analysis
    ↓
Statistics and histograms
    ↓
Intensity processing
    ↓
Noise modeling
    ↓
Image comparison
    ↓
Validation
```

## Fundamental Configuration

| Parameter                  |                    Value |
| -------------------------- | -----------------------: |
| Main numeric library       |                    NumPy |
| Visualization              |               Matplotlib |
| Image I/O                  |                   Pillow |
| Primary stored image dtype |                  `uint8` |
| Standard `uint8` range     |                    0–255 |
| Color convention           |                      RGB |
| Grayscale representation   |                2-D array |
| RGB representation         |                3-D array |
| Random seed                |                       42 |
| Notebook environment       |                  Jupyter |
| Python version             |                   3.12.3 |
| Generated figures          |                      PNG |
| Notebook display           | Inline with `plt.show()` |

## Project Structure

```text
Image_Processing_Fundamental/
├── .venv/
├── data/
│   ├── ballons.jpg
│   ├── einstein.png
│   ├── Elizabeth_Tower_London.jpg
│   ├── grass.jpg
│   └── peppers.png
├── notebooks/
│   └── Image_Processing_Fundamental.ipynb
├── outputs/
│   └── figures/
├── requirements.txt
└── README.md
```

The `.venv/` directory is local and is not tracked by Git.

Input images are stored under:

```text
data/
```

Generated figures are stored under:

```text
outputs/figures/
```

## Notebook Structure

```text
Problem Statement
Objectives
Approach
Fundamental Configuration

0. Setup
1. Data and Output Paths
2. From a Real Scene to a Digital Image
   2.1 Sampling
   2.2 Quantization
3. Pixels, Coordinates, and Image Matrices
4. Binary, Grayscale, and RGB Images
5. Load and Inspect Real Images
6. Dimensions, Resolution, Aspect Ratio, and Channels
7. Data Types, Bit Depth, Dynamic Range, and Memory
8. Display Images Correctly
9. Pixel Access and Safe Modification
10. Regions of Interest (ROI)
11. Pixel Neighborhoods
12. RGB Channel Decomposition
13. RGB and BGR Conventions
14. RGB-to-Grayscale Conversion from First Principles
15. Image Statistics
16. Intensity Histograms
17. Dynamic Range and Min-Max Normalization
18. uint8 Arithmetic, Overflow, Clipping, and Floating Point
19. Image Noise Fundamentals
20. Image Comparison Metrics
21. PNG vs JPEG and Image Saving
22. Standard Image Inspection Workflow
23. Validation Checks
24. Practical Exercises

Discussion
Conclusion
Glossary
```

## Fundamental Concepts

### Digital Image

A digital image is a discrete numerical representation of visual information.

For a grayscale image, each spatial location contains one intensity value.

For a color image, each spatial location usually contains several channel values.

A grayscale image may be written mathematically as:

$$
I(x,y)
$$

In NumPy, the corresponding indexing convention is:

```python
image[y, x]
```

because arrays are indexed by:

```text
[row, column]
```

### Sampling

Sampling discretizes spatial position.

A continuous scene can conceptually be represented as:

$$
f(x,y)
$$

A digital image records measurements only at discrete positions:

$$
f[m,n]
$$

Increasing the number of spatial samples generally allows finer spatial detail to be represented.

Sampling therefore determines the spatial discretization of the image.

### Quantization

Quantization discretizes intensity.

If a pixel is represented using \(b\) bits, the number of possible intensity levels is:

$$
L = 2^b
$$

Examples:

| Bit depth | Intensity levels |
| --------: | ---------------: |
|     1 bit |                2 |
|    2 bits |                4 |
|    4 bits |               16 |
|    8 bits |              256 |
|   16 bits |           65,536 |

Sampling and quantization describe two different aspects of image digitization:

```text
Sampling     → spatial resolution
Quantization → intensity resolution
```

### Pixel Coordinates

For a conventional digital image, the coordinate origin is located at the top-left corner.

```text
(0,0) ─────────────→ x / columns
  │
  │
  ↓
 y / rows
```

Therefore:

```python
image[y, x]
```

is the appropriate NumPy indexing model.

### Image Types

The notebook introduces three basic representations.

#### Binary

A binary image represents two logical states.

Typical values are:

```text
0 and 1
```

or:

```text
0 and 255
```

#### Grayscale

A grayscale image stores one intensity value per pixel.

Typical shape:

```text
(H, W)
```

#### RGB

An RGB image stores three channel values per pixel:

```text
Red
Green
Blue
```

Typical shape:

```text
(H, W, 3)
```

## Data

The laboratory uses several natural reference images in order to observe different visual properties such as:

* brightness;
* color;
* texture;
* local structure;
* dynamic range;
* spatial detail.

The reference images are:

```text
ballons.jpg
einstein.png
Elizabeth_Tower_London.jpg
grass.jpg
peppers.png
```

All paths are resolved relative to the laboratory directory.

The notebook also validates that the required input files exist before processing begins.

## Image Inspection

The standard initial inspection includes:

```python
image.shape
image.ndim
image.dtype
image.min()
image.max()
image.mean()
image.nbytes
```

These values help determine:

* spatial dimensions;
* number of channels;
* numerical representation;
* available intensity range;
* observed intensity range;
* approximate memory consumption.

The notebook establishes the following inspection sequence:

```text
Locate
    ↓
Load
    ↓
Inspect shape
    ↓
Inspect dtype
    ↓
Inspect min / max
    ↓
Determine channel convention
    ↓
Display correctly
    ↓
Compute statistics
    ↓
Process safely
    ↓
Validate
    ↓
Save
```

## Data Types and Bit Depth

The primary stored image representation used in the laboratory is:

```text
uint8
```

An unsigned 8-bit integer has the legal range:

$$
0 \le I \le 255
$$

because:

$$
2^8 = 256
$$

possible values can be represented.

The notebook also discusses common image-processing representations:

| dtype     | Typical purpose                       |
| --------- | ------------------------------------- |
| `bool`    | Binary logic                          |
| `uint8`   | Standard images                       |
| `uint16`  | Higher bit-depth imaging              |
| `float32` | Image processing and machine learning |
| `float64` | Numerical analysis                    |

## Dynamic Range

The available range of a `uint8` image is:

```text
0–255
```

However, a particular image may use only part of that interval.

Its observed dynamic range is:

$$
I_{\max} - I_{\min}
$$

An image using only a narrow range of values may appear low contrast even though it is stored in an 8-bit format.

## Image Display

Image display must be separated conceptually from image data.

For grayscale images, Matplotlib may automatically choose display limits.

Therefore, when comparing images scientifically, explicit limits may be required:

```python
plt.imshow(
    image,
    cmap="gray",
    vmin=0,
    vmax=255,
)
```

This prevents automatic display scaling from making different numerical ranges appear artificially similar.

## Pixel Access

Individual pixels can be accessed using:

```python
pixel = image[y, x]
```

For an RGB image, the result is typically:

```text
[R, G, B]
```

Before modifying an image, the notebook uses:

```python
modified = image.copy()
```

to preserve the original input.

## Regions of Interest

A region of interest is extracted using NumPy slicing:

```python
roi = image[
    y_start:y_end,
    x_start:x_end,
]
```

ROIs are useful for:

* local analysis;
* object-focused processing;
* reduced computational cost;
* local statistics;
* visualization.

## Pixel Neighborhoods

A local \(3 \times 3\) neighborhood around a pixel is represented conceptually as:

$$
\begin{bmatrix}
I(y-1,x-1) & I(y-1,x) & I(y-1,x+1) \\
I(y,x-1) & I(y,x) & I(y,x+1) \\
I(y+1,x-1) & I(y+1,x) & I(y+1,x+1)
\end{bmatrix}
$$

Neighborhoods form the basis of later spatial filtering operations.

The notebook also introduces the border problem, where a neighborhood can extend outside the valid image array.

Common border strategies include:

* zero padding;
* reflection;
* replication;
* wrap-around.

## RGB Channel Decomposition

An RGB image can be decomposed into three individual channel planes:

$$
I_R(y,x)
$$

$$
I_G(y,x)
$$

$$
I_B(y,x)
$$

Using NumPy:

```python
red = image[..., 0]
green = image[..., 1]
blue = image[..., 2]
```

Channel analysis is important for later tasks involving:

* segmentation;
* color analysis;
* feature extraction;
* image enhancement.

## RGB and BGR

Channel order depends on the library.

The conventions used in this laboratory are:

```text
Pillow      → RGB
Matplotlib  → RGB
OpenCV      → commonly BGR when loading color images
```

Displaying BGR data directly as RGB exchanges the red and blue channels and produces incorrect colors.

## RGB-to-Grayscale Conversion

The notebook implements grayscale conversion explicitly.

A simple arithmetic average would be:

$$
Y = \frac{R+G+B}{3}
$$

A weighted luminance approximation is used instead:

$$
Y = 0.299R + 0.587G + 0.114B
$$

The unequal weights reflect the different sensitivity of human vision to the three color components.

The conversion is implemented from first principles rather than hidden behind a high-level grayscale conversion function.

## Image Statistics

The notebook computes global statistics including:

```text
minimum
maximum
mean
median
standard deviation
5th percentile
95th percentile
```

These quantities summarize image intensity characteristics.

However, global statistics do not encode spatial organization.

Two visually different images can have similar or even identical global statistics.

## Intensity Histograms

A grayscale histogram counts the number of pixels associated with each intensity interval.

For a standard 8-bit image, the notebook uses:

```text
256 bins
```

covering:

```text
0–255
```

Histograms can help identify:

* globally dark images;
* globally bright images;
* low-contrast images;
* broad intensity distributions;
* narrow intensity distributions.

### Histogram Limitation

A histogram contains no spatial information.

The notebook demonstrates this explicitly by shuffling all image pixels.

The shuffled image has the same histogram as the original while its visual structure is destroyed.

Therefore:

```text
same histogram ≠ same image
```

## Intensity Normalization

Min-max normalization stretches an observed intensity interval to a target interval.

For an 8-bit target:

$$
I_{\mathrm{norm}}
=
\frac{I-I_{\min}}
{I_{\max}-I_{\min}}
\times 255
$$

The mapping produces:

$$
I_{\min} \rightarrow 0
$$

and:

$$
I_{\max} \rightarrow 255
$$

The notebook includes protection against division by zero for constant images.

Min-max normalization is also distinguished from histogram equalization.

## Arithmetic Safety

Direct arithmetic on `uint8` images can produce unexpected numerical behavior because values outside 0–255 cannot be represented directly.

The notebook therefore follows the safe processing workflow:

```text
uint8 input
    ↓
Convert to float
    ↓
Perform arithmetic
    ↓
Clip valid range
    ↓
Convert back to uint8 if required
```

Example:

```python
image_float = image.astype(np.float32)

processed = image_float + offset

processed = np.clip(
    processed,
    0,
    255,
).astype(np.uint8)
```

## Noise Models

The notebook introduces four common noise models.

### Gaussian Noise

Gaussian noise is modeled as additive random variation.

A simplified model is:

$$
I_{\text{noisy}}
=
I + n
$$

where \(n\) follows a Gaussian distribution.

### Salt-and-Pepper Noise

Salt-and-pepper noise creates isolated extreme-valued pixels.

Typical corrupted values are:

```text
0
255
```

### Poisson Noise

Poisson noise is associated with counting statistics and is signal-dependent.

It is particularly important in photon-limited imaging systems.

### Speckle Noise

Speckle noise is modeled as multiplicative variation.

A simplified form is:

$$
I_{\text{noisy}}
=
I(1+n)
$$

Different noise models motivate different filtering strategies in later laboratories.

## Image Comparison Metrics

Several numerical metrics are introduced for comparing a reference image \(R\) and a test image \(T\).

### Mean Absolute Error

$$
\mathrm{MAE}
=
\frac{1}{N}
\sum |R-T|
$$

### Mean Squared Error

$$
\mathrm{MSE}
=
\frac{1}{N}
\sum (R-T)^2
$$

### Root Mean Squared Error

$$
\mathrm{RMSE}
=
\sqrt{\mathrm{MSE}}
$$

### Peak Signal-to-Noise Ratio

For an 8-bit image:

$$
\mathrm{PSNR}
=
10
\log_{10}
\left(
\frac{255^2}{\mathrm{MSE}}
\right)
$$

For identical images:

```text
MAE  = 0
MSE  = 0
RMSE = 0
PSNR = infinity
```

These metrics quantify pixel-level differences but do not fully model human visual perception.

They should therefore be interpreted together with visual inspection.

## PNG and JPEG

The laboratory compares two common file formats.

### PNG

PNG uses lossless compression.

It is appropriate for:

* binary masks;
* labels;
* diagrams;
* quantitative intermediate images;
* results where exact pixel preservation matters.

### JPEG

JPEG uses lossy compression.

It is useful for natural photographs where storage efficiency is important.

Decoded JPEG pixel values may differ from the original image.

Therefore, JPEG should generally not be used when exact numerical reproducibility of pixel values is required.

## Environment

The laboratory is designed for:

```text
Python 3.12.3
```

Direct Python dependencies are defined in:

```text
requirements.txt
```

Required packages are:

```text
numpy
matplotlib
Pillow
ipykernel
```

## Installation

From the `Image_Processing_Fundamental/` directory:

```bash
python3 -m venv .venv
```

Activate the environment:

```bash
source .venv/bin/activate
```

Upgrade `pip`:

```bash
python -m pip install --upgrade pip
```

Install the laboratory dependencies:

```bash
python -m pip install -r requirements.txt
```

Register the virtual environment as a Jupyter kernel:

```bash
python -m ipykernel install \
  --user \
  --name image-processing-fundamental \
  --display-name "Image Processing Fundamental (.venv)"
```

## Running the Notebook

Open:

```text
notebooks/Image_Processing_Fundamental.ipynb
```

Select the kernel:

```text
Image Processing Fundamental (.venv)
```

Then run all cells from top to bottom.

The notebook is intentionally stored without pre-executed outputs.

During execution:

* visualizations appear directly below the corresponding code cells using `plt.show()`;
* generated figures are saved automatically under:

```text
outputs/figures/
```

## Outputs

### Spatial Sampling

Demonstrates the effect of progressively reducing the number of spatial samples.

```text
outputs/figures/01_sampling.png
```

### Intensity Quantization

Demonstrates the effect of 1-bit, 2-bit, 4-bit, and 8-bit quantization.

```text
outputs/figures/02_quantization.png
```

### Grayscale Matrix Representation

Visualizes a small image together with its numerical pixel values.

```text
outputs/figures/03_grayscale_matrix.png
```

### Binary, Grayscale, and RGB Representation

Compares the three basic digital-image representations.

```text
outputs/figures/04_image_types.png
```

### Reference Images

Displays the image dataset used throughout the laboratory.

```text
outputs/figures/05_reference_images.png
```

### Display Scaling

Demonstrates the difference between automatic visualization scaling and a fixed 0–255 display range.

```text
outputs/figures/06_display_scaling.png
```

### Pixel Access and Modification

Visualizes a selected pixel and a controlled modification performed on a copy of the image.

```text
outputs/figures/07_pixel_edit.png
```

### Region of Interest

Displays an image together with a selected ROI and the extracted region.

```text
outputs/figures/08_region_of_interest.png
```

### RGB Channel Decomposition

Displays the original RGB image and its red, green, and blue components.

```text
outputs/figures/09_rgb_channels.png
```

### RGB and BGR Comparison

Demonstrates the visual effect of reversing RGB channel order.

```text
outputs/figures/10_rgb_bgr.png
```

### RGB-to-Grayscale Conversion

Compares the original RGB image with its grayscale representation.

```text
outputs/figures/11_rgb_to_grayscale.png
```

### Intensity Histogram

Displays a grayscale image together with its 256-bin intensity histogram.

```text
outputs/figures/12_intensity_histogram.png
```

### Dynamic-Range Normalization

Compares a low-contrast image and histogram before and after min-max normalization.

```text
outputs/figures/13_dynamic_range_normalization.png
```

### Noise Models

Compares the original image with Gaussian, salt-and-pepper, Poisson, and speckle noise.

```text
outputs/figures/14_noise_models.png
```

### Image Saving and Compression

The notebook saves an example using both lossless PNG and lossy JPEG representations.

```text
outputs/figures/15_saved_example.png
outputs/figures/15_saved_example.jpg
```

## Evaluation

The laboratory uses both numerical and visual validation.

Validation includes:

* complete top-to-bottom notebook execution;
* input-file existence checks;
* image dimensionality checks;
* channel-count checks;
* dtype checks;
* intensity-range inspection;
* histogram count consistency;
* normalization range verification;
* ROI dimension verification;
* metric self-consistency;
* PNG/JPEG comparison;
* visual inspection of generated figures.

The notebook contains explicit assertions for several fundamental assumptions.

Successful execution reports:

```text
All fundamental validation checks passed.
```

## Practical Exercises

The notebook contains exercises covering:

1. coordinate reasoning;
2. bit-depth calculations;
3. ROI extraction;
4. manual grayscale conversion;
5. histogram interpretation;
6. safe arithmetic;
7. Gaussian-noise experiments;
8. JPEG-quality experiments.

These exercises are intended to verify that the learner can reproduce the concepts rather than only read the demonstrations.

## Limitations

This laboratory intentionally focuses on foundational concepts.

It does not yet cover:

* geometric image transformations;
* convolution;
* smoothing filters;
* sharpening;
* edge detection;
* frequency-domain filtering;
* Fourier transforms;
* segmentation algorithms.

These topics are treated in subsequent laboratories.

Other important limitations include:

* array dimensions alone do not determine physical spatial resolution;
* histograms discard spatial information;
* pixel-wise numerical metrics do not perfectly model human visual perception;
* grayscale conversion discards color information;
* synthetic noise models are simplified approximations of real acquisition systems.

## Technologies

* Python
* NumPy
* Matplotlib
* Pillow
* Jupyter
* Digital image representation
* Sampling
* Quantization
* Binary images
* Grayscale images
* RGB images
* Pixel coordinates
* Regions of interest
* Pixel neighborhoods
* RGB channel decomposition
* RGB/BGR conventions
* Grayscale conversion
* Image statistics
* Intensity histograms
* Dynamic-range normalization
* Numeric data types
* `uint8` arithmetic
* Gaussian noise
* Salt-and-pepper noise
* Poisson noise
* Speckle noise
* MAE
* MSE
* RMSE
* PSNR
* PNG
* JPEG

## Learning Outcome

After completing this laboratory, a learner with no previous image-processing background should be able to interpret a digital image as both:

```text
visual information
```

and:

```text
structured numerical data
```

The learner should be able to inspect an unfamiliar image, understand its representation, manipulate its values safely, analyze its intensity distribution, simulate common degradations, compare it numerically with another image, and validate the result.

These foundations prepare the learner for the next laboratory:

```text
Image Transformation
```

## Participants

* **Denos Kume**

Master SIP
École Centrale de Nantes
