# Camera Calibration

Planar camera calibration from multiple chessboard views using **normalized Direct Linear Transform (DLT)** and **Zhang's calibration method**. The project estimates the intrinsic camera matrix, recovers one pose per valid view, reprojects the known calibration points, and validates the complete geometry numerically and visually.

## Objective

Given several images of the same planar chessboard with known geometry, estimate:

- the intrinsic camera matrix $K$;
- one rotation matrix $R$ per valid view;
- one translation vector $t$ per valid view;
- the reprojection error associated with the recovered camera model.

The implemented model is a pinhole camera model. Radial/tangential lens distortion and nonlinear refinement are intentionally outside the project scope.

## Calibration Data

| Parameter | Value |
| --- | --- |
| Input directory | `data/calibration_images/` |
| Image type | JPEG |
| Internal corners | $8 \times 6$ |
| Points per valid view | 48 |
| Square size | $0.03\,\mathrm{m}$ |
| Minimum valid views | 3 |
| Calibration plane | $Z=0$ |
| Error unit | pixels |

## Required Tasks — 1 to 13

The four notebooks follow the same numbered structure from problem definition to executable implementation:

1. Load the Sorted JPEG Calibration Images
2. Detect and Refine Chessboard Corners
3. Build the Planar World Coordinates
4. Compute $T_{\mathrm{image}}$ and $T_{\mathrm{plane}}$
5. Build the DLT Matrix $Q$ and Solve $Q\mathbf{h}=0$ by SVD
6. Denormalize Each Homography
7. Build the Zhang Matrix $V$ and Solve $Vb=0$ by SVD
8. Recover $\alpha,\beta,\gamma,u_0,v_0$ and Construct $K$
9. Recover $R$ and $t$ for Every Retained View
10. Reproject the $Z=0$ Calibration Points
11. Compute Point-wise Errors, Mean Error and RMSE
12. Produce and Save the Six Required Diagnostic Figures
13. Run the Numerical and Output-file Validation Checks

## Pipeline

```text
Sorted calibration images
        ↓
Chessboard detection
        ↓
Sub-pixel corner refinement
        ↓
Known planar coordinates
        ↓
Image + plane point normalization
        ↓
Normalized DLT: Qh = 0
        ↓
Denormalized homography H
        ↓
Zhang constraints: Vb = 0
        ↓
Intrinsic matrix K
        ↓
Pose recovery R, t
        ↓
Reprojection
        ↓
Point-wise residuals
        ↓
Per-view + global mean / RMSE
        ↓
Visual diagnostics
        ↓
Final validation
```

## Mathematical Model

For a homogeneous world point

$$
\mathbf{X}_w=[X,Y,Z,1]^T
$$

and image point

$$
\mathbf{x}=[u,v,1]^T,
$$

the pinhole camera model is

$$
s\mathbf{x}
=
K
\begin{bmatrix}
R&t
\end{bmatrix}
\mathbf{X}_w.
$$

The intrinsic matrix is

$$
K=
\begin{bmatrix}
\alpha&\gamma&u_0\\
0&\beta&v_0\\
0&0&1
\end{bmatrix}.
$$

For the planar calibration target $Z=0$,

$$
H=
K
\begin{bmatrix}
\mathbf{r}_1&\mathbf{r}_2&t
\end{bmatrix}.
$$

The complete derivation of DLT, Zhang constraints, intrinsic recovery, pose recovery, reprojection and validation is developed in the Theory notebook.

## Notebooks

- [Problem Statement](notebooks/camera_calibration_problem_statement.ipynb) — defines the problem, inputs, expected outputs and the 13 required tasks.
- [Requirements Gathering & Approach](notebooks/camera_calibration_requirements_gathering_and_approach.ipynb) — maps each task to its engineering requirement, method, acceptance condition and implementation location.
- [Theory — Zero to Mastery](notebooks/camera_calibration_theory.ipynb) — explains the complete calibration pipeline from intuition to derivation, interpretation, failure modes and mastery checks.
- [Implementation](notebooks/camera_calibration.ipynb) — executable source of truth; each numbered task is followed immediately by its corresponding code.

## Implementation Design

The implementation uses explicit standalone functions so that each required task remains visible and traceable:

- `detect_and_refine_corners()`
- `build_planar_points()`
- `homogenize()`
- `normalize_trans()`
- `build_dlt_matrix()`
- `denormalize_homography()`
- `v_ij()`
- `zhang_constraints()`
- `recover_extrinsic()`

This one-task / one-code-block structure makes the notebook easier to learn from, debug, review and present.

## Key Methods

- OpenCV chessboard detection
- Sub-pixel corner refinement
- Homogeneous coordinates
- Hartley-style point normalization
- Normalized DLT
- Singular Value Decomposition (SVD)
- Planar homography estimation
- Zhang planar calibration
- Closed-form intrinsic recovery
- SVD projection to a proper rotation
- Reprojection analysis
- Numerical and filesystem validation

## Evaluation

For measured pixel point $\mathbf{x}_i$ and predicted point $\hat{\mathbf{x}}_i$,

$$
e_i=
\lVert
\hat{\mathbf{x}}_i-\mathbf{x}_i
\rVert_2.
$$

The implementation reports:

- point-wise reprojection errors;
- per-view mean reprojection error;
- per-view RMSE;
- overall mean reprojection error;
- overall RMSE;
- Zhang-system singular values;
- residual norm $\lVert Vb\rVert$.

## Diagnostic Outputs

Generated figures are saved under:

```text
outputs/figures/
```

The six required figures are:

1. `detected_chessboard_corners.png`
2. `homography_estimation_pipeline.png`
3. `estimated_camera_poses.png`
4. `reprojection_results.png`
5. `mean_reprojection_error_by_view.png`
6. `reprojection_error_distribution.png`

## Validation

The final implementation verifies:

- at least three valid calibration views;
- 48 detected and planar points per retained view;
- finite homographies;
- finite $3\times3$ intrinsic matrix $K$;
- rotation orthonormality $R^TR\approx I$;
- proper rotations with $\det(R)\approx1$;
- finite reprojection errors;
- existence of all six diagnostic figures.

A successful complete execution ends with:

```text
All Camera Calibration validation checks passed.
```

The notebook has been executed successfully from top to bottom in the project VS Code / WSL environment and reached this final validation message.

## Project Structure

```text
Camera_Calibration/
├── .venv/
├── data/
│   └── calibration_images/
├── notebooks/
│   ├── camera_calibration_problem_statement.ipynb
│   ├── camera_calibration_requirements_gathering_and_approach.ipynb
│   ├── camera_calibration_theory.ipynb
│   └── camera_calibration.ipynb
├── outputs/
│   └── figures/
├── requirements.txt
└── README.md
```

## Run Locally

From the Camera Calibration module:

```bash
cd ~/Master_SIP_EC-Nantes/Lab_Works/Computer_Vision/Camera_Calibration

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

code .
```

In VS Code:

1. open `notebooks/camera_calibration.ipynb`;
2. select the project `.venv` Python kernel;
3. run the notebook from top to bottom;
4. confirm that the final validation message is displayed;
5. inspect the generated figures in `outputs/figures/`.

## Scope and Limitations

Included:

- planar camera calibration;
- normalized DLT;
- Zhang closed-form calibration;
- intrinsic estimation;
- pose recovery;
- reprojection analysis;
- visual and numerical validation.

Not included:

- radial lens distortion;
- tangential lens distortion;
- nonlinear bundle adjustment;
- robust outlier rejection;
- uncertainty propagation.

Systematic residual patterns near image borders may therefore indicate unmodelled lens distortion rather than a failure of the implemented linear calibration pipeline.

## Participants

- **Denos Kume**
- **Oluwole SHOKUNBI**

**MSc. CORO DASSIP — École Centrale de Nantes**
