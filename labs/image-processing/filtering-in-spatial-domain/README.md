<p>
  <img align="left" src="https://www.ec-nantes.fr/medias/photo/logocn-rvb_1648479844750-png?ID_FICHE=178994&amp;INLINE=FALSE" alt="Centrale Nantes" height="64">
</p>
<p align="right"><strong>MSc. CORO DASSIP</strong></p>
<br clear="both">

<table width="85%" align="center">
  <tr>
    <td align="center">
      <h1>Filtering in Spatial Domain</h1>
    </td>
  </tr>
</table>

Neighborhood-based image-filtering laboratory covering convolution, border handling, smoothing, denoising, sharpening, derivative operators, RGB filtering, quantitative comparison, and validation.

The module is organized into four complementary notebooks:

- [Problem Statement](notebooks/filtering_in_spatial_domain_problem_statement.ipynb) — problem definition, inputs, expected outputs, and the 23 required tasks.
- [Requirements Gathering & Approach](notebooks/filtering_in_spatial_domain_requirements_gathering_and_approach.ipynb) — engineering requirements, selected methods, acceptance criteria, and implementation traceability.
- [Theory](notebooks/filtering_in_spatial_domain_theory.ipynb) — mathematical formulation of spatial filtering, convolution, filter families, derivative operators, and limitations.
- [Implementation](notebooks/filtering_in_spatial_domain.ipynb) — concise executable workflow with code, generated outputs, metrics, diagnostics, and validation only.

## Outputs

Generated figures are stored in:

```text
outputs/figures/
```

Main outputs include:

- `01_border_modes.png`
- `02_mean_filter.png`
- `03_mean_kernel_sizes.png`
- `04_gaussian_filter.png`
- `05_gaussian_sigma_sweep.png`
- `06_mean_vs_gaussian.png`
- `07_noise_types.png`
- `08_median_filter.png`
- `09_median_sizes.png`
- `10_bilateral_filter.png`
- `11_bilateral_parameter_sweep.png`
- `12_laplacian_sharpening.png`
- `13_unsharp_highboost.png`
- `14_sobel_gradients.png`
- `15_gradient_orientation.png`
- `16_derivative_operators.png`
- `17_padding_real_image.png`
- `18_color_filtering.png`

## Run

From the module directory:

```bash
cd ~/msc-coro-dassip-portfolio/labs/image-processing/filtering-in-spatial-domain

source .venv/bin/activate
python -m pip install -r requirements.txt
code .
```

Open [filtering_in_spatial_domain.ipynb](notebooks/filtering_in_spatial_domain.ipynb), select the project `.venv` kernel, and run all cells from top to bottom.

A successful execution ends with:

```text
All spatial-filtering validation checks passed.
```

## Project Structure

```text
filtering-in-spatial-domain/
├── data/
├── notebooks/
│   ├── filtering_in_spatial_domain_problem_statement.ipynb
│   ├── filtering_in_spatial_domain_requirements_gathering_and_approach.ipynb
│   ├── filtering_in_spatial_domain_theory.ipynb
│   └── filtering_in_spatial_domain.ipynb
├── outputs/
│   └── figures/
├── requirements.txt
└── README.md
```

## Scope

Implemented:

- correlation and convolution;
- manual and library-based neighborhood filtering;
- border handling;
- mean and Gaussian smoothing;
- noise-model-aware denoising;
- median and bilateral filtering;
- MAE, MSE, RMSE, and PSNR comparison;
- Laplacian sharpening;
- unsharp masking and high-boost filtering;
- Sobel, Prewitt, and Scharr derivatives;
- gradient magnitude and orientation;
- RGB filtering and numerical-safety checks;
- numerical and visual validation.

Not included:

- frequency-domain filtering;
- segmentation;
- learned convolutional filters;
- task-specific computer-vision pipelines.

## Participants

- **Denos Kume**

**MSc. CORO DASSIP — École Centrale de Nantes**
