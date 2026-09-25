<p>
  <img align="left" src="https://www.ec-nantes.fr/medias/photo/logocn-rvb_1648479844750-png?ID_FICHE=178994&amp;INLINE=FALSE" alt="Centrale Nantes" height="64">
</p>
<p align="right"><strong>MSc. CORO DASSIP</strong></p>
<br clear="both">

<table width="85%" align="center">
  <tr>
    <td align="center">
      <h1>Image Segmentation</h1>
    </td>
  </tr>
</table>

Classical image-segmentation laboratory covering thresholding, morphology, connected components, contours, color segmentation, watershed, segmentation metrics, and end-to-end mask generation.

The module is organized into four complementary notebooks:

- [Problem Statement](notebooks/image_segmentation_problem_statement.ipynb) — problem definition, inputs, expected outputs, and the 28 required tasks.
- [Requirements Gathering & Approach](notebooks/image_segmentation_requirements_gathering_and_approach.ipynb) — engineering requirements, selected methods, acceptance criteria, and implementation traceability.
- [Theory](notebooks/image_segmentation_theory.ipynb) — mathematical formulation of thresholding, morphology, region analysis, watershed, evaluation metrics, and limitations.
- [Implementation](notebooks/image_segmentation.ipynb) — concise executable workflow with code, generated outputs, metrics, diagnostics, and validation only.

## Outputs

Generated figures are stored in:

```text
outputs/figures/
```

Main outputs:

- `01_input_images.png`
- `02_hand_histogram.png`
- `03_manual_threshold.png`
- `04_threshold_sensitivity.png`
- `05_otsu_threshold.png`
- `06_smoothing_before_otsu.png`
- `07_adaptive_thresholding.png`
- `08_structuring_elements.png`
- `09_erosion_dilation.png`
- `10_opening_closing.png`
- `11_morphological_gradient.png`
- `12_hole_filling.png`
- `13_connected_components.png`
- `14_component_area_filtering.png`
- `15_contours.png`
- `16_hsv_channels.png`
- `17_color_segmentation.png`
- `18_edge_based_segmentation.png`
- `19_distance_transform.png`
- `20_watershed.png`
- `21_complete_pipeline.png`

## Run

From the module directory:

```bash
cd ~/msc-coro-dassip-portfolio/labs/image-processing/segmentation

source .venv/bin/activate
python -m pip install -r requirements.txt
code .
```

Open [image_segmentation.ipynb](notebooks/image_segmentation.ipynb), select the project `.venv` kernel, and run all cells from top to bottom.

A successful execution ends with:

```text
All image-segmentation validation checks passed.
```

## Project Structure

```text
Image_Segmentation/
├── data/
├── notebooks/
│   ├── image_segmentation_problem_statement.ipynb
│   ├── image_segmentation_requirements_gathering_and_approach.ipynb
│   ├── image_segmentation_theory.ipynb
│   └── image_segmentation.ipynb
├── outputs/
│   └── figures/
├── requirements.txt
└── README.md
```

## Scope

Implemented:

- manual, Otsu, and adaptive thresholding;
- Gaussian preprocessing;
- erosion, dilation, opening, closing, and morphological gradient;
- structuring-element analysis and hole filling;
- connected components and area filtering;
- contours and region properties;
- HSV color segmentation;
- edge-based segmentation intuition;
- distance transform and watershed segmentation;
- pixel accuracy, precision, recall, IoU, and Dice;
- under-segmentation and over-segmentation analysis;
- end-to-end binary segmentation;
- numerical and visual validation.

Not included:

- deep semantic segmentation;
- learned feature extractors;
- instance-segmentation networks;
- production annotation pipelines.

## Participants

- **Denos Kume**

**MSc. CORO DASSIP — École Centrale de Nantes**
