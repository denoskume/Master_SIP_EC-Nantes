# Image Processing Fundamental

Foundational image-processing laboratory reconstructed from the recovered course image data. The notebook is designed to be runnable from top to bottom and to explain how a digital image is represented and manipulated before introducing more advanced transformations and filters.

## Learning objectives

By the end of the lab, you should be able to:

- explain grayscale and RGB images as numerical arrays;
- inspect image dimensions, channels, data types, and intensity ranges;
- convert an RGB image to grayscale from first principles;
- access and modify individual pixels safely;
- extract a region of interest (ROI);
- separate and visualize RGB channels;
- compute basic image statistics and intensity histograms;
- normalize image intensity values;
- add controlled synthetic noise and quantify its effect;
- save processed images and figures reproducibly.

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

## Notes

The original lab handout was not recovered. This notebook therefore reconstructs the fundamental learning sequence from the recovered course images and standard digital-image-processing concepts. It does not claim to reproduce the original exercise sheet verbatim.
