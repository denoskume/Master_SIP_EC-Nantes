# Camera Calibration

Planar camera calibration from multiple chessboard images using Zhang's method.

This laboratory estimates the camera intrinsic matrix from several views of a known planar calibration pattern, recovers the camera pose associated with each view, and evaluates calibration quality through reprojection error analysis.

## Problem

Camera calibration determines the relationship between 3D world coordinates and 2D image coordinates.

For a planar chessboard target, the calibration estimates:

* the intrinsic camera matrix \(K\);
* focal scale parameters;
* principal point coordinates;
* skew coefficient;
* rotation matrix \(R\) for each calibration view;
* translation vector \(t\) for each calibration view.

Multiple images of the same planar chessboard are used to provide the geometric constraints required for calibration.

## Objectives

The laboratory implements the complete calibration pipeline:

1. Detect chessboard corners in each image.
2. Refine corner locations to sub-pixel accuracy.
3. Define the corresponding planar world coordinates.
4. Normalize image and world points.
5. Estimate a homography for each calibration view.
6. Construct Zhang's intrinsic calibration constraints.
7. Estimate the intrinsic camera matrix.
8. Recover camera pose for each image.
9. Reproject the calibration points.
10. Evaluate the calibration using reprojection errors.

## Method

The calibration follows Zhang's planar calibration method.

For each calibration image:

1. Chessboard corners are detected with OpenCV.
2. Pixel coordinates are refined using sub-pixel optimization.
3. Corresponding planar coordinates are generated using the known chessboard square size.
4. Image and planar points are normalized.
5. A normalized Direct Linear Transform (DLT) system is constructed.
6. Singular Value Decomposition (SVD) is used to estimate the homography.
7. The homography is denormalized.

The homographies from all valid views are then combined to estimate the intrinsic camera parameters.

Once the intrinsic matrix is available, the rotation and translation associated with each calibration view are recovered.

Calibration quality is assessed by projecting the known chessboard points back into each image and measuring the difference between detected and predicted image coordinates.

## Calibration Configuration

| Parameter                   |              Value |
| --------------------------- | -----------------: |
| Chessboard internal corners |              8 × 6 |
| Square size                 |             0.03 m |
| Calibration target          |  Planar chessboard |
| Point refinement            |          Sub-pixel |
| Homography estimation       |     Normalized DLT |
| Linear solver               |                SVD |
| Calibration method          |     Zhang's method |
| Evaluation                  | Reprojection error |

Lens distortion coefficients are not estimated in this implementation.

## Project Structure

```text
Camera_Calibration/
├── .venv/
├── data/
│   └── calibration_images/
│       ├── img0.jpg
│       ├── img1.jpg
│       ├── ...
│       └── img8.jpg
├── notebooks/
│   └── Camera_Calibration.ipynb
├── outputs/
│   └── figures/
│       ├── detected_chessboard_corners.png
│       ├── homography_estimation_pipeline.png
│       ├── estimated_camera_poses.png
│       ├── reprojection_results.png
│       ├── mean_reprojection_error_by_view.png
│       └── reprojection_error_distribution.png
├── requirements.txt
└── README.md
```

The `.venv/` directory is local and is not tracked by Git.

## Notebook Structure

```text
0. Setup
1. Data Path
2. Output Directory
3. Utility Functions
4. Calibration Image Model
5. Load Calibration Views
6. Verify Detected Corners
7. Homography Estimation
8. Construct the Intrinsic Calibration System
9. Estimate the Intrinsic Matrix
10. Estimate Camera Pose and Reprojection Error
11. Camera Pose Visualization
12. Visualize Reprojection
13. Overall Calibration Error
14. Mean Reprojection Error by Calibration View
15. Reprojection Error Distribution

Discussion
Conclusion
```

## Environment

The laboratory was developed using:

```text
Python 3.12.3
```

Direct Python dependencies are defined in `requirements.txt`:

```text
numpy==2.5.3
matplotlib==3.11.2
opencv-python==5.0.0.93
ipykernel==7.3.0
```

## Installation

From the `Camera_Calibration/` directory:

```bash
python3 -m venv .venv
```

Activate the environment:

```bash
source .venv/bin/activate
```

Install the required dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Register the environment as a Jupyter kernel:

```bash
python -m ipykernel install \
  --user \
  --name camera-calibration \
  --display-name "Camera Calibration (.venv)"
```

## Running the Notebook

Open:

```text
notebooks/Camera_Calibration.ipynb
```

Select the kernel:

```text
Camera Calibration (.venv)
```

Then run all cells from top to bottom.

The notebook expects calibration images in:

```text
data/calibration_images/
```

Generated figures are saved automatically in:

```text
outputs/figures/
```

## Outputs

### Chessboard Corner Detection

Detected internal chessboard corners are displayed for every valid calibration view.

Output:

```text
outputs/figures/detected_chessboard_corners.png
```

### Homography Estimation

The homography pipeline summarizes the normalized DLT procedure:

```text
World points
    ↓
Image points
    ↓
Point normalization
    ↓
DLT system
    ↓
SVD
    ↓
Homography denormalization
```

Output:

```text
outputs/figures/homography_estimation_pipeline.png
```

### Camera Pose Estimation

The recovered camera centres are visualized relative to the planar chessboard coordinate system.

Output:

```text
outputs/figures/estimated_camera_poses.png
```

### Reprojection

Detected chessboard corners are compared with the points predicted by the estimated camera model.

Output:

```text
outputs/figures/reprojection_results.png
```

### Reprojection Error by View

The mean reprojection error is compared across calibration images.

Output:

```text
outputs/figures/mean_reprojection_error_by_view.png
```

### Reprojection Error Distribution

Point-wise reprojection errors from all valid calibration views are combined to examine their overall distribution.

Output:

```text
outputs/figures/reprojection_error_distribution.png
```

## Evaluation

For each calibration point, the reprojection error is calculated as the Euclidean pixel distance between the detected image coordinate and the coordinate predicted by the estimated camera model.

The notebook reports:

* mean reprojection error for each image;
* RMSE for each image;
* overall mean reprojection error;
* overall reprojection RMSE;
* point-wise reprojection error distribution.

These measurements provide both per-view and global assessments of calibration consistency.

## Limitations

This implementation assumes a planar calibration target and does not estimate radial or tangential lens distortion.

The estimated model therefore focuses on the projective camera geometry required by the laboratory.

## Technologies

* Python
* NumPy
* OpenCV
* Matplotlib
* Jupyter
* Normalized DLT
* Singular Value Decomposition
* Homography estimation
* Camera intrinsic calibration
* Camera pose estimation
* Reprojection analysis

## Participants

* **Denos Kume**
* **Oluwole SHOKUNBI**

Master SIP
École Centrale de Nantes
