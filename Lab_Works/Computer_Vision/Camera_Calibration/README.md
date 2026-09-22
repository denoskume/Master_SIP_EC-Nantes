# Camera Calibration

Planar camera calibration from multiple chessboard views using normalized DLT and Zhang's method. The laboratory estimates camera intrinsics, recovers one pose per valid view, and evaluates geometric consistency through reprojection analysis.

## Problem

Estimate the intrinsic matrix \(K\), rotation \(R\), and translation \(t\) from several images of a known planar chessboard, then validate the estimated model in image space.

## Pipeline

```text
Calibration images
        ↓
Chessboard corners + sub-pixel refinement
        ↓
Planar correspondences
        ↓
Normalized DLT homographies
        ↓
Zhang constraints
        ↓
Intrinsic matrix K
        ↓
Pose recovery R, t
        ↓
Reprojection
        ↓
Quantitative + visual evaluation
```

## Notebooks

- [Problem Statement](notebooks/camera_calibration_problem_statement.ipynb)
- [Theory](notebooks/camera_calibration_theory.ipynb)
- [Requirements Gathering & Approach](notebooks/camera_calibration_requirements_gathering_and_approach.ipynb)
- [Implementation](notebooks/camera_calibration.ipynb)

## Key Methods

Normalized DLT · SVD · Zhang planar calibration · camera intrinsics · pose recovery · reprojection analysis

## Evaluation

The implementation reports per-view mean reprojection error and RMSE, global mean error and RMSE, reprojection overlays, camera-pose geometry, and the point-wise residual distribution.

## Outputs

Generated figures are stored in:

```text
outputs/figures/
```

Main outputs:

- `detected_chessboard_corners.png`
- `homography_estimation_pipeline.png`
- `estimated_camera_poses.png`
- `reprojection_results.png`
- `mean_reprojection_error_by_view.png`
- `reprojection_error_distribution.png`

## Project Structure

```text
Camera_Calibration/
├── data/
│   └── calibration_images/
├── notebooks/
│   ├── camera_calibration_problem_statement.ipynb
│   ├── camera_calibration_theory.ipynb
│   ├── camera_calibration_requirements_gathering_and_approach.ipynb
│   └── camera_calibration.ipynb
├── outputs/
│   └── figures/
├── requirements.txt
└── README.md
```

## Run

From `Camera_Calibration/`:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Open `notebooks/camera_calibration.ipynb`, select the project environment, and run it from top to bottom. Inputs are read from `data/calibration_images/` and generated figures are written to `outputs/figures/`.

## Participants

- **Denos Kume**
- **Oluwole SHOKUNBI**

Master SIP — École Centrale de Nantes
