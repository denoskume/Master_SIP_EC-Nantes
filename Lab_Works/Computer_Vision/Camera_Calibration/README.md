<p>
  <img align="left" src="https://www.ec-nantes.fr/medias/photo/logocn-rvb_1648479844750-png?ID_FICHE=178994&amp;INLINE=FALSE" alt="Centrale Nantes" height="64">
</p>
<p align="right"><strong>MSc. CORO DASSIP</strong></p>
<br clear="both">

<table width="85%" align="center">
  <tr>
    <td align="center">
      <h1>Camera Calibration</h1>
    </td>
  </tr>
</table>

Planar camera calibration from multiple chessboard views using normalized DLT and Zhang's method.

The module is organized into four complementary notebooks:

- [Problem Statement](notebooks/camera_calibration_problem_statement.ipynb) — problem definition, inputs, expected outputs, and the 13 required tasks.
- [Requirements Gathering & Approach](notebooks/camera_calibration_requirements_gathering_and_approach.ipynb) — engineering requirements, method selection, acceptance criteria, and implementation traceability.
- [Theory](notebooks/camera_calibration_theory.ipynb) — mathematical formulation, derivations, modeling assumptions, failure modes, and limitations.
- [Implementation](notebooks/camera_calibration.ipynb) — executable calibration pipeline, generated results, diagnostics, and numerical validation.

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

## Run

From the module directory:

```bash
cd ~/Master_SIP_EC-Nantes/Lab_Works/Computer_Vision/Camera_Calibration

source .venv/bin/activate
python -m pip install -r requirements.txt
code .
```

Open [camera_calibration.ipynb](notebooks/camera_calibration.ipynb), select the project `.venv` kernel, and run all cells from top to bottom.

A successful execution ends with:

```text
All Camera Calibration validation checks passed.
```

## Project Structure

```text
Camera_Calibration/
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

## Scope

Implemented:

- planar camera calibration;
- normalized DLT;
- Zhang calibration;
- intrinsic and pose recovery;
- reprojection analysis;
- numerical and visual validation.

Not included:

- lens-distortion estimation;
- nonlinear bundle adjustment;
- robust outlier rejection;
- uncertainty propagation.

## Participants

- **Denos Kume**
- **Oluwole SHOKUNBI**

**MSc. CORO DASSIP — École Centrale de Nantes**
