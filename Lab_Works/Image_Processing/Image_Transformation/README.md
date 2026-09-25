<p>
  <img align="left" src="https://www.ec-nantes.fr/medias/photo/logocn-rvb_1648479844750-png?ID_FICHE=178994&amp;INLINE=FALSE" alt="Centrale Nantes" height="64">
</p>
<p align="right"><strong>MSc. CORO DASSIP</strong></p>
<br clear="both">

<table width="85%" align="center">
  <tr>
    <td align="center">
      <h1>Image Transformation</h1>
    </td>
  </tr>
</table>

image-transformation laboratory covering pointwise intensity mappings, homogeneous-coordinate geometry, inverse mapping, interpolation, transformation composition, and affine image warping.

The module is organized into four complementary notebooks:

- [Problem Statement](notebooks/image_transformation_problem_statement.ipynb) — problem definition, inputs, expected outputs, and the 25 required tasks.
- [Requirements Gathering & Approach](notebooks/image_transformation_requirements_gathering_and_approach.ipynb) — engineering requirements, selected methods, acceptance criteria, and implementation traceability.
- [Theory](notebooks/image_transformation_theory.ipynb) — mathematical formulation of intensity mappings, homogeneous coordinates, interpolation, affine geometry, and model limitations.
- [Implementation](notebooks/image_transformation.ipynb) — executable processing pipeline, quantitative results, figures, and validation checks.

## Outputs

Generated figures are stored in:

```text
outputs/figures/
```

Main outputs:

- `01_reference_images.png`
- `02_negative.png`
- `03_brightness_contrast.png`
- `04_contrast_stretching.png`
- `05_log_transform.png`
- `06_gamma_examples.png`
- `07_gamma_curves.png`
- `08_histogram_equalization.png`
- `09_equalization_mapping.png`
- `10_intensity_transform_comparison.png`
- `11_translation.png`
- `12_rotation_origin_center.png`
- `13_scaling.png`
- `14_interpolation_comparison.png`
- `15_reflection.png`
- `16_shear.png`
- `17_transformation_order.png`
- `18_affine_transform.png`

## Run

From the module directory:

```bash
cd ~/Master_SIP_EC-Nantes/Lab_Works/Image_Processing/Image_Transformation

source .venv/bin/activate
python -m pip install -r requirements.txt
code .
```

Open [image_transformation.ipynb](notebooks/image_transformation.ipynb), select the project `.venv` kernel, and run all cells from top to bottom.

A successful execution ends with:

```text
All image-transformation validation checks passed.
```

## Project Structure

```text
Image_Transformation/
├── data/
├── notebooks/
│   ├── image_transformation_problem_statement.ipynb
│   ├── image_transformation_requirements_gathering_and_approach.ipynb
│   ├── image_transformation_theory.ipynb
│   └── image_transformation.ipynb
├── outputs/
│   └── figures/
├── requirements.txt
└── README.md
```

## Scope

Implemented:

- identity, negative, brightness, contrast, stretching, logarithmic and gamma transformations;
- histogram equalization;
- homogeneous image coordinates;
- translation, rotation, scaling, reflection, and shear;
- centered transformations;
- forward and inverse mapping;
- nearest-neighbor, bilinear, and bicubic interpolation;
- transformation composition and order analysis;
- affine image transformation;
- resizing and aspect-ratio reasoning;
- numerical and visual validation.

Not included:

- spatial convolution and filtering;
- frequency-domain filtering;
- projective homography estimation;
- perspective rectification;
- image segmentation.

## Participants

- **Denos Kume**

**MSc. CORO DASSIP — École Centrale de Nantes**
