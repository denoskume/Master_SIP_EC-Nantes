<p>
  <img align="left" src="https://www.ec-nantes.fr/medias/photo/logocn-rvb_1648479844750-png?ID_FICHE=178994&amp;INLINE=FALSE" alt="Centrale Nantes" height="64">
</p>
<p align="right"><strong>MSc. CORO DASSIP</strong></p>
<br clear="both">

<table width="85%" align="center">
  <tr>
    <td align="center">
      <h1>Feature Detection and Object Tracking</h1>
    </td>
  </tr>
</table>

Feature-based object tracking in video using ORB keypoints/descriptors, Hamming-distance matching, RANSAC homography estimation, and perspective transformation of an initial object bounding box.

The module is organized into four complementary notebooks:

- [Problem Statement](notebooks/feature_detection_problem_statement.ipynb) — problem definition, fixed tracking configuration, expected outputs, and the 13 required tasks.
- [Requirements Gathering & Approach](notebooks/feature_detection_requirements_gathering_and_approach.ipynb) — engineering requirements, method choices, acceptance criteria, and task-to-code traceability.
- [Theory](notebooks/feature_detection_theory.ipynb) — theoretical foundations of ORB, binary descriptors, Hamming matching, homographies, RANSAC, and tracking diagnostics.
- [Implementation](notebooks/feature_detection.ipynb) — concise executable workflow with code, generated outputs, metrics, diagnostics, and validation only.

## Outputs

Generated figures are stored in:

```text
outputs/figures/
```

Main outputs:

- `reference_orb_keypoints.png`
- `representative_tracking_frames.png`
- `ransac_inlier_matches.png`
- `matches_and_inliers_by_frame.png`
- `inlier_ratio_by_frame.png`

## Run

From the module directory:

```bash
cd ~/Master_SIP_EC-Nantes/Lab_Works/Computer_Vision/Feature_Detection

source .venv/bin/activate
python -m pip install -r requirements.txt
code .
```

Open [feature_detection.ipynb](notebooks/feature_detection.ipynb), select the project `.venv` kernel, and run all cells from top to bottom.

A successful execution ends with:

```text
All Feature Detection validation checks passed.
```

## Project Structure

```text
Feature_Detection/
├── data/
│   └── video1.mp4
├── notebooks/
│   ├── feature_detection_problem_statement.ipynb
│   ├── feature_detection_requirements_gathering_and_approach.ipynb
│   ├── feature_detection_theory.ipynb
│   └── feature_detection.ipynb
├── outputs/
│   └── figures/
├── requirements.txt
└── README.md
```

## Scope

Implemented:

- fixed-reference ORB feature extraction;
- Hamming-distance descriptor matching;
- BFMatcher cross-check;
- RANSAC homography estimation;
- perspective-transformed object tracking;
- sequence-level match/inlier analysis;
- numerical and visual validation.

Not included:

- optical flow;
- learned feature descriptors;
- temporal motion models;
- non-rigid tracking;
- multi-object tracking;
- ground-truth localization-error evaluation.

## Participants

- **Denos Kume**
- **Oluwole SHOKUNBI**

**MSc. CORO DASSIP — École Centrale de Nantes**
