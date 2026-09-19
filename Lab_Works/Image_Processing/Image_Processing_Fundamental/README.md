# Image Processing Fundamental

Beginner-first laboratory for understanding digital images from first principles.

The notebook is designed for readers with no previous image-processing background. It develops the numerical and visual foundations required before studying image transformations, spatial filtering, frequency-domain processing, and segmentation.

## Learning objectives

By the end of the lab, you should be able to:

- explain how sampling and quantization produce a digital image;
- describe binary, grayscale, and RGB images as NumPy arrays;
- understand pixels, coordinates, image dimensions, aspect ratio, channels, data types, and bit depth;
- distinguish pixel dimensions from physical resolution;
- load, inspect, display, and save images reproducibly;
- understand `(row, column)` indexing versus `(x, y)` coordinates;
- convert RGB images to grayscale from first principles;
- access and modify pixels safely;
- extract regions of interest and understand pixel neighborhoods;
- separate and interpret RGB channels;
- compute image statistics and histograms;
- understand dynamic range and min-max normalization;
- work safely with `uint8` and floating-point arrays;
- identify common image-noise models;
- quantify image differences using MAE, MSE, RMSE, and PSNR;
- recognize common implementation mistakes before moving to advanced processing.

## Notebook philosophy

The notebook follows a consistent learning pattern:

```text
Concept
  ↓
Mathematical intuition
  ↓
Array representation
  ↓
Commented Python implementation
  ↓
Visualization
  ↓
Interpretation
  ↓
Common mistakes
  ↓
Exercise / self-check
```

The goal is not to memorize library calls. The goal is to understand what the numbers mean and why each operation changes the image.

## Structure

```text
Image_Processing/
├── data/
│   └── common/
│       ├── ballons.jpg
│       ├── einstein.png
│       ├── Elizabeth_Tower_London.jpg
│       ├── grass.jpg
│       └── peppers.png
└── Image_Processing_Fundamental/
    ├── notebooks/
    │   └── Image_Processing_Fundamental.ipynb
    ├── outputs/
    │   └── figures/
    ├── README.md
    ├── requirements.txt
    └── .gitignore
```

## Run locally

From `Lab_Works/Image_Processing/Image_Processing_Fundamental/`:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name image-processing-fundamental --display-name "Image Processing Fundamental (.venv)"
jupyter notebook notebooks/Image_Processing_Fundamental.ipynb
```

The notebook uses relative paths only. Generated figures are written to `outputs/figures/`.

## Next lab

After completing the fundamentals, continue with **Image_Transformation**, where these array concepts are used to modify image intensities and spatial coordinates.