# Background Subtraction

Neurointerventional background-subtraction project for automatic guidewire and microcatheter enhancement using controlled ablation across background modeling, histogram transformation, spatial and spectral filtering, morphology, segmentation, field-of-view restriction, and quantitative validation.

The module is organized into four complementary notebooks:

- [Problem Statement](notebooks/background_subtraction_problem_statement.ipynb) — problem definition, inputs, expected outputs, and the 13 required tasks.
- [Requirements Gathering & Approach](notebooks/background_subtraction_requirements_gathering_and_approach.ipynb) — engineering requirements, controlled-ablation rules, acceptance criteria, and implementation traceability.
- [Theory](notebooks/background_subtraction_theory.ipynb) — mathematical and statistical basis of background modeling, filtering, segmentation, EM/GMM comparison, metrics, and limitations.
- [Implementation](notebooks/Background_Subtraction.ipynb) — executable code and stored outputs only; project context, requirements, approach, and theory remain in their dedicated notebooks.

## Outputs

Generated figures are stored in:

```text
outputs/figures/
```

Main outputs:

- `01_representative_data.png`
- `02_background_models.png`
- `03_histogram_transformation.png`
- `04_background_residual.png`
- `05_spatial_filtering.png`
- `06_spatial_sigma_sensitivity.png`
- `07_spectral_filtering.png`
- `08_segmentation.png`
- `09_threshold_sensitivity.png`
- `10_morphological_refinement.png`
- `11_mask_vs_ground_truth.png`
- `12_guidance_overlay.png`
- `13_validation_overlay.png`
- `14_sad_vs_time.png`
- `15_mse_vs_time.png`
- `16_psnr_vs_time.png`
- `17_overlap_vs_time.png`

## Run

From the module directory:

```bash
cd ~/Master_SIP_EC-Nantes/Lab_Works/Image_Processing/Project/Background_Subtraction

source .venv/bin/activate
python -m pip install -r requirements.txt
code .
```

Open [Background_Subtraction.ipynb](notebooks/Background_Subtraction.ipynb), select the project `.venv` kernel, and run all cells from top to bottom.

A successful execution ends with:

```text
All Background Subtraction validation checks passed.
```

## Project Structure

```text
Background_Subtraction/
├── data/
│   └── catheter/
├── notebooks/
│   ├── background_subtraction_problem_statement.ipynb
│   ├── background_subtraction_requirements_gathering_and_approach.ipynb
│   ├── background_subtraction_theory.ipynb
│   └── Background_Subtraction.ipynb
├── outputs/
│   └── figures/
├── requirements.txt
└── README.md
```

## Scope

Implemented:

- reproduction of the original first-frame background baseline;
- temporal-median background estimation;
- fixed background-derived histogram transformation;
- spatial Gaussian-filter optimization;
- Gaussian spectral high-pass filtering;
- controlled morphological refinement;
- segmentation-threshold optimization;
- EM/GMM segmentation comparison;
- field-of-view masking with ground-truth coverage guardrail;
- final retained-pipeline assembly;
- SAD, MSE, and PSNR sequence-level evaluation;
- qualitative masks and guidance overlays;
- explicit numerical and output validation.

Not included:

- non-rigid registration;
- optical flow;
- learned segmentation networks;
- adaptive online background models;
- clinical validation or deployment.

## Participants

- **Denos Kume**

**MSc. CORO DASSIP — École Centrale de Nantes**
