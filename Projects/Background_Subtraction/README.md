# Background Subtraction

Neurointerventional background-subtraction project for automatic guidewire and microcatheter enhancement using controlled ablation across background modeling, histogram transformation, spatial and spectral filtering, morphology, segmentation, field-of-view restriction, and quantitative validation.

The module is organized into four complementary notebooks:

- [Problem Statement](notebooks/background_subtraction_problem_statement.ipynb) — problem definition, inputs, expected outputs, and the numbered implementation tasks.
- [Requirements Gathering & Approach](notebooks/background_subtraction_requirements_gathering_and_approach.ipynb) — engineering requirements, controlled-ablation rules, acceptance criteria, and implementation traceability.
- [Theory](notebooks/background_subtraction_theory.ipynb) — mathematical and statistical basis of background modeling, filtering, segmentation, EM/GMM comparison, metrics, and limitations.
- [Implementation](notebooks/Background_Subtraction.ipynb) — executable code and stored outputs only; project context, requirements, approach, and theory remain in their dedicated notebooks.

## Outputs

Generated figures are stored in:

```text
outputs/figures/
```

Current generated figures:

- `01_background_reference.png`
- `02_intermediate_pipeline.png`
- `03_strategy_comparison_representative.png`
- `04_temporal_metric_curves.png`
- `05_strategy_summary.png`
- `06_final_guidance_gallery.png`
- `07_final_validation.png`

## Run

From the module directory:

```bash
cd ~/Master_SIP_EC-Nantes/Projects/Background_Subtraction

source .venv/bin/activate
python -m pip install -r requirements.txt
code .
```

Open [Background_Subtraction.ipynb](notebooks/Background_Subtraction.ipynb), select the project `.venv` kernel, and run all cells from top to bottom.

A successful execution runs all 15 code cells without errors and regenerates the two CSV result files plus the seven figures listed above.

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
