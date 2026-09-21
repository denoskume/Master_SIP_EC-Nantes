# Image Segmentation

Classical image-segmentation laboratory covering thresholding, morphology, connected components, contours, color segmentation, watershed, segmentation metrics, and complete end-to-end mask generation.

## Problem

Image segmentation assigns a label to each pixel in an image.

Unlike classification, which predicts one label for an entire image, segmentation determines **which pixels belong to which region or object**.

For binary segmentation:

$$
M(x,y)=
\begin{cases}
1,&\text{foreground}\\
0,&\text{background}
\end{cases}
$$

The resulting binary mask can then be used for:

* foreground/background separation;
* object measurement;
* shape analysis;
* connected-region extraction;
* contour analysis;
* object counting;
* later computer-vision processing.

## Objectives

This laboratory develops image segmentation progressively from first principles.

By the end of the notebook, the reader should be able to:

1. Explain what image segmentation is.
2. Distinguish classification, detection, semantic segmentation, and instance segmentation.
3. Create binary masks from grayscale images.
4. Apply global thresholding.
5. Understand threshold sensitivity.
6. Apply Otsu thresholding.
7. Use adaptive thresholding under non-uniform illumination.
8. Understand erosion and dilation.
9. Apply opening and closing.
10. Select structuring-element shapes and sizes.
11. Fill holes in binary masks.
12. Label connected components.
13. Remove small components based on area.
14. Extract object contours.
15. Measure region properties.
16. Perform color-based segmentation in HSV.
17. Understand edge-based segmentation.
18. Compute distance transforms.
19. Apply marker-based watershed segmentation.
20. Identify over-segmentation and under-segmentation.
21. Compute segmentation metrics including Dice and IoU.
22. Build a complete reusable segmentation pipeline.
23. Recognize common segmentation mistakes.
24. Explain classical segmentation concepts in interviews and exams.

## Learning Philosophy

The notebook is designed for an **absolute beginner**.

Each topic follows a progressive pattern:

1. intuitive explanation;
2. mathematical formulation;
3. Python/OpenCV implementation;
4. visual result;
5. interpretation;
6. common mistakes;
7. practical exercises;
8. interview/exam questions.

The objective is not simply to generate a binary mask, but to understand why each processing step is required.

## Project Structure

```text
Image_Segmentation/
├── .venv/
│
├── data/
│   ├── hand.png
│   ├── peppers.png
│   └── tower.jpg
│
├── notebooks/
│   └── Image_Segmentation.ipynb
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
Learning Objectives

0. Setup
1. What Is Image Segmentation?
2. Load the Lab Images
3. Histograms and Why Thresholding Can Work
4. Manual Global Thresholding
5. Threshold Sensitivity
6. Otsu Thresholding
7. Gaussian Smoothing Before Thresholding
8. Adaptive Thresholding
9. Morphological Processing
10. Structuring Elements
11. Erosion and Dilation
12. Opening and Closing
13. Morphological Gradient
14. Hole Filling
15. Connected Components
16. Remove Small Components
17. Contours
18. Region Properties
19. Color Segmentation
20. Edge-Based Segmentation Intuition
21. Distance Transform
22. Watershed Segmentation
23. Ground Truth and Segmentation Metrics
24. Dice vs IoU Relationship
25. Under-Segmentation vs Over-Segmentation
26. End-to-End Binary Segmentation Pipeline
27. How to Choose a Segmentation Strategy
28. Common Mistakes
29. Practical Exercises
30. Interview / Exam Questions
31. Final Concept Map

Discussion
Conclusion
```

## Core Concepts

### Binary Segmentation

For a binary segmentation problem, every pixel is assigned to one of two classes:

* foreground;
* background.

A binary mask can therefore be represented with Boolean values, `0/1`, or `0/255`.

## Classification vs Detection vs Segmentation

| Task                  | Typical Output                         |
| --------------------- | -------------------------------------- |
| Classification        | one label for the entire image         |
| Object detection      | bounding boxes and labels              |
| Semantic segmentation | class label for every pixel            |
| Instance segmentation | separate mask for each object instance |

This laboratory focuses mainly on **classical binary and region-based segmentation**.

## Histogram-Based Segmentation

A grayscale histogram represents the distribution of image intensities.

If object and background occupy sufficiently different intensity ranges, a threshold can separate them.

For threshold \(T\):

$$
M(x,y)=
\begin{cases}
1,&I(x,y)>T\\
0,&I(x,y)\le T
\end{cases}
$$

The direction may be reversed depending on whether the object is brighter or darker than the background.

## Global Thresholding

Global thresholding uses one threshold for the entire image.

Advantages:

* simple;
* fast;
* easy to interpret.

Limitations:

* sensitive to illumination;
* sensitive to contrast;
* may fail when foreground and background distributions overlap.

The notebook demonstrates threshold sensitivity on `hand.png`.

## Otsu Thresholding

Otsu automatically chooses a global threshold.

Its goal is to separate two intensity classes by minimizing within-class variance or equivalently maximizing between-class separation.

Otsu works especially well when the grayscale histogram is approximately bimodal.

## Adaptive Thresholding

Adaptive thresholding computes a local threshold for different image neighborhoods.

It is useful when illumination varies spatially.

The notebook compares:

* adaptive mean thresholding;
* adaptive Gaussian thresholding.

Important parameters include:

* local block size;
* threshold offset \(C\).

## Smoothing Before Segmentation

Noise can produce unstable threshold results.

A common processing chain is:

```text
input
  ↓
Gaussian smoothing
  ↓
thresholding
```

Smoothing reduces isolated intensity fluctuations before segmentation.

## Mathematical Morphology

Morphology modifies shapes in binary masks using a structuring element.

The notebook introduces:

* erosion;
* dilation;
* opening;
* closing;
* morphological gradient.

## Structuring Elements

The structuring element defines which neighboring pixels participate in a morphological operation.

Common shapes include:

* rectangle;
* ellipse;
* cross.

Its size must be selected relative to the size of the structures being processed.

## Erosion

Erosion shrinks foreground regions.

Typical uses:

* removing small foreground noise;
* separating thin connections;
* reducing object size.

## Dilation

Dilation expands foreground regions.

Typical uses:

* connecting nearby components;
* filling small gaps;
* expanding object boundaries.

## Opening

Opening is erosion followed by dilation:

$$
A\circ B
=
(A\ominus B)\oplus B
$$

Typical purpose:

* remove small foreground structures while approximately preserving larger regions.

## Closing

Closing is dilation followed by erosion:

$$
A\bullet B
=
(A\oplus B)\ominus B
$$

Typical purpose:

* close small gaps;
* fill small holes;
* reconnect nearby foreground regions.

## Morphological Gradient

The morphological gradient approximates boundaries:

$$
G
=
\mathrm{dilation}
-
\mathrm{erosion}
$$

It highlights transitions between foreground and background.

## Hole Filling

Binary masks can contain unwanted holes inside segmented objects.

The notebook uses binary hole filling to recover continuous foreground regions before later measurements.

## Connected Components

Connected-component labeling assigns a unique integer label to each connected foreground region.

Typical outputs include:

* component ID;
* area;
* centroid;
* bounding box.

This makes it possible to count and analyze separate objects.

## Component Area Filtering

Small connected regions are often caused by noise.

The notebook demonstrates filtering components according to their area.

For example:

```text
keep region if area >= minimum_area
```

This is frequently more controlled than using aggressive morphology.

## Contours

Contours represent object boundaries as ordered boundary points.

They can be used for:

* drawing boundaries;
* measuring perimeter;
* computing area;
* finding bounding boxes;
* shape analysis;
* polygon approximation.

## Region Properties

The notebook computes properties such as:

* area;
* perimeter;
* centroid;
* bounding-box width and height;
* aspect ratio;
* circularity.

Circularity is defined as:

$$
C=
\frac{4\pi A}{P^2}
$$

where:

* \(A\) = area;
* \(P\) = perimeter.

A perfect circle has circularity close to 1.

## Color Segmentation

Grayscale processing discards color information.

For color segmentation, the notebook introduces HSV:

* Hue;
* Saturation;
* Value.

HSV is often useful because color and brightness are represented more independently than in RGB.

The notebook demonstrates red-region segmentation using `peppers.png`.

Because red wraps around the HSV hue axis, two hue intervals are combined.

## Edge-Based Segmentation

Segmentation can also begin from object boundaries.

Typical pipeline:

```text
image
  ↓
smoothing
  ↓
edge detection
  ↓
boundary linking / closing
  ↓
region construction
```

The notebook uses Canny edge detection on `tower.jpg`.

## Distance Transform

For every foreground pixel, the distance transform computes the distance to the nearest background pixel.

Boundary pixels have small values.

Pixels near the center of objects have larger values.

This representation is useful for separating touching objects.

## Watershed Segmentation

Watershed interprets the image as a topographic surface.

Marker-based watershed typically uses:

```text
binary mask
    ↓
noise cleanup
    ↓
sure background
    ↓
distance transform
    ↓
sure foreground
    ↓
unknown region
    ↓
connected-component markers
    ↓
watershed
```

The notebook demonstrates watershed on `peppers.png`.

## Watershed Failure Modes

### Over-Segmentation

One true object is split into too many regions.

Typical causes:

* noise;
* too many markers;
* insufficient smoothing.

### Under-Segmentation

Multiple real objects remain merged.

Typical causes:

* poor markers;
* insufficient object separation;
* weak foreground extraction.

## Segmentation Evaluation

A predicted mask should ideally be compared with a ground-truth mask.

Important pixel categories are:

* True Positive;
* True Negative;
* False Positive;
* False Negative.

## Pixel Accuracy

$$
\mathrm{Accuracy}
=
\frac{TP+TN}
{TP+TN+FP+FN}
$$

Accuracy can be misleading when background pixels dominate the image.

## Precision

$$
\mathrm{Precision}
=
\frac{TP}
{TP+FP}
$$

Precision measures how many predicted foreground pixels are actually correct.

## Recall

$$
\mathrm{Recall}
=
\frac{TP}
{TP+FN}
$$

Recall measures how much of the true foreground was recovered.

## Intersection over Union

$$
\mathrm{IoU}
=
\frac{|A\cap B|}
{|A\cup B|}
$$

IoU is also called the Jaccard index.

## Dice Score

$$
\mathrm{Dice}
=
\frac{2|A\cap B|}
{|A|+|B|}
$$

Dice is widely used in segmentation tasks, particularly in medical imaging and other pixel-level applications.

## Dice and IoU Relationship

$$
\mathrm{Dice}
=
\frac{2\mathrm{IoU}}
{1+\mathrm{IoU}}
$$

and:

$$
\mathrm{IoU}
=
\frac{\mathrm{Dice}}
{2-\mathrm{Dice}}
$$

For the same non-perfect prediction, Dice is numerically larger than IoU.

## End-to-End Segmentation Pipeline

The notebook implements a reusable pipeline:

```text
input image
    ↓
grayscale
    ↓
Gaussian smoothing
    ↓
Otsu thresholding
    ↓
opening
    ↓
closing
    ↓
hole filling
    ↓
connected components
    ↓
area filtering
    ↓
final mask
    ↓
overlay / measurements
```

This demonstrates how classical segmentation is usually constructed from multiple complementary steps rather than one isolated algorithm.

## Choosing a Segmentation Strategy

### Strong intensity difference

Use:

* global thresholding;
* Otsu.

### Uneven illumination

Use:

* adaptive thresholding;
* illumination correction before thresholding.

### Strong color difference

Use:

* HSV;
* Lab;
* color-range segmentation.

### Touching objects

Use:

* distance transform;
* markers;
* watershed.

### Noisy binary mask

Use:

* opening;
* component-area filtering.

### Small holes and gaps

Use:

* closing;
* hole filling.

### Boundary-driven problem

Use:

* edge detection;
* contours;
* boundary linking.

## Generated Figures

During execution, figures are saved under:

```text
outputs/figures/
```

Representative generated outputs include:

```text
01_input_images.png
02_hand_histogram.png
03_manual_threshold.png
04_threshold_sensitivity.png
05_otsu_threshold.png
06_smoothing_before_otsu.png
07_adaptive_thresholding.png
08_structuring_elements.png
09_erosion_dilation.png
10_opening_closing.png
11_morphological_gradient.png
12_hole_filling.png
13_connected_components.png
14_component_area_filtering.png
15_contours.png
16_hsv_channels.png
17_color_segmentation.png
18_edge_based_segmentation.png
19_distance_transform.png
20_watershed.png
21_complete_pipeline.png
```

## Environment

The laboratory is designed for Python 3.12.

Core dependencies include:

```text
numpy
matplotlib
Pillow
scipy
opencv-python
ipykernel
```

They are defined in:

```text
requirements.txt
```

## Installation

From the laboratory directory:

```bash
python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Jupyter Kernel

Register a dedicated kernel:

```bash
python -m ipykernel install \
  --user \
  --name image-segmentation \
  --display-name "Image Segmentation (.venv)"
```

## Running the Notebook

Open:

```text
notebooks/Image_Segmentation.ipynb
```

in VS Code.

Select:

```text
Image Segmentation (.venv)
```

as the notebook kernel.

Then execute:

```text
Run All
```

from top to bottom.

The committed notebook should retain its executed outputs so that results and visualizations remain directly visible on GitHub.

## Validation

The notebook includes checks and reasoning around:

* valid binary masks;
* connected components;
* shape preservation;
* mask cleanup;
* morphological behavior;
* segmentation metrics;
* ground-truth requirements;
* reproducibility of the segmentation pipeline.


## Technologies and Concepts

* Python
* NumPy
* Matplotlib
* Pillow
* SciPy
* OpenCV
* Image Segmentation
* Binary Masks
* Histograms
* Global Thresholding
* Otsu Thresholding
* Adaptive Thresholding
* Gaussian Smoothing
* Mathematical Morphology
* Erosion
* Dilation
* Opening
* Closing
* Morphological Gradient
* Hole Filling
* Connected Components
* Contours
* Region Properties
* HSV Segmentation
* Canny Edge Detection
* Distance Transform
* Watershed
* Dice Score
* Intersection over Union
* Precision
* Recall
* Pixel Accuracy

## Participants

**Denos Kume**

Master SIP
École Centrale de Nantes
