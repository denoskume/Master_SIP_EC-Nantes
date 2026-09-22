# Background Subtraction

End-to-end foreground extraction with registration, subtraction, enhancement, segmentation, morphology, and quantitative evaluation.

## Problem

Background subtraction must distinguish true temporal foreground changes from noise, illumination variation, and spatial misalignment. The project uses a deterministic controlled sequence to measure each pipeline stage.

## Objectives

1. Generate a sequence with known foreground ground truth.
2. Estimate/use a background reference.
3. Demonstrate raw subtraction and motion artifacts.
4. Register frames before subtraction.
5. Enhance and threshold subtraction results.
6. Clean masks morphologically.
7. Evaluate with IoU and Dice.
8. Analyze temporal foreground evolution.

## Method

A controlled fluoroscopy-like sequence is generated in code, shifted to create motion, registered with phase cross-correlation, subtracted from a reference, normalized, thresholded, cleaned, and compared with known ground truth.

## Configuration

| Parameter | Value |
| --- | ---: |
| Frame size | 256 × 320 |
| Frames | 7 |
| Registration | phase cross-correlation |
| Foreground | branching synthetic mask |
| Evaluation | IoU / Dice |

## Project Structure

```text
Background_Subtraction/
├── .venv/
├── data/
│   └── .gitkeep
├── notebooks/
│   └── Background_Subtraction.ipynb
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
Experimental Configuration
0. Setup
1. Data and Output Paths
2. Generate a Controlled Sequence
3. Background Reference and Raw Subtraction
4. Why Registration Matters
5. Signed vs Absolute Difference
6. Contrast Enhancement of the Subtraction Image
7. Thresholding and Morphological Cleanup
8. Ground-Truth Alignment and Quantitative Evaluation
9. Temporal Foreground Evolution
10. Failure Modes
11. Validation Checks
12. Practical Extensions
Discussion
Conclusion
```

## Environment

The laboratory is designed for:

```text
Python 3.12.3
```

Direct dependencies are defined in `requirements.txt`:

```text
numpy
matplotlib
scipy
scikit-image
ipykernel
```

## Installation

From the laboratory directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Register the environment as a Jupyter kernel:

```bash
python -m ipykernel install \
  --user \
  --name background-subtraction \
  --display-name "Background Subtraction (.venv)"
```

## Running the Notebook

Open the notebook under `notebooks/`, select:

```text
Background Subtraction (.venv)
```

Then run all cells from top to bottom.

The notebook is intentionally stored without executed outputs. During local execution, figures are displayed inline with `plt.show()` and saved to:

```text
outputs/figures/
```

## Outputs

### Sequence and Subtraction

Sequence visualization, raw subtraction, and registration effect.

`outputs/figures/01_sequence.png`
`outputs/figures/02_raw_subtraction.png`
`outputs/figures/03_registration_effect.png`

### Foreground Extraction

Difference representation, contrast enhancement, and foreground mask.

`outputs/figures/04_signed_absolute.png`
`outputs/figures/05_contrast_enhancement.png`
`outputs/figures/06_foreground_mask.png`

### Evaluation

Ground-truth comparison and temporal foreground response.

`outputs/figures/07_evaluation.png`
`outputs/figures/08_temporal_foreground.png`

## Evaluation

The laboratory uses the following validation criteria:

* registration-shift interpretation
* foreground-mask IoU and Dice
* shape validation
* temporal response consistency

## Limitations

* The sequence is controlled synthetic data, not patient data.
* The background is mostly static and motion is translational.
* Phase correlation does not model non-rigid deformation.

## Technologies

* Python
* NumPy
* Matplotlib
* SciPy
* scikit-image
* Phase cross-correlation
* Background subtraction
* Thresholding
* Morphology
* IoU
* Dice

## Participants

* **Denos Kume**

Master SIP  
École Centrale de Nantes
