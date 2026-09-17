# Feature Detection and Object Tracking

Feature-based object tracking in video using ORB keypoints, binary descriptor matching, RANSAC homography estimation, and perspective transformation.

The objective is to track an object from an initial bounding box defined in the first video frame and estimate its position in subsequent frames.

## Problem

The location of the object is known only in the first frame.

To recover its position throughout the video:

1. local visual features are extracted from the initial object region;
2. these features are matched against features detected in subsequent frames;
3. geometrically consistent matches are selected with RANSAC;
4. a homography is estimated;
5. the original bounding box is transformed into the current frame.

## Objectives

The laboratory implements the complete feature-based tracking pipeline:

1. Define the initial object bounding box.
2. Detect ORB keypoints inside the object region.
3. Compute binary ORB descriptors.
4. Detect ORB features in subsequent frames.
5. Match descriptors using Hamming distance.
6. Estimate a homography using RANSAC.
7. Transform the initial bounding box.
8. Visualize the tracked object.
9. Analyze feature matches and RANSAC inliers.

## Method

The first video frame is used as the fixed reference.

ORB features are detected only inside the initial bounding box to describe the object of interest.

For each subsequent frame:

1. ORB keypoints and descriptors are detected across the complete image.
2. Reference descriptors are matched to current-frame descriptors using a brute-force matcher.
3. Hamming distance is used because ORB produces binary descriptors.
4. Matched keypoint coordinates are used to estimate a homography.
5. RANSAC rejects geometrically inconsistent correspondences.
6. The estimated homography transforms the four corners of the original bounding box.
7. The transformed polygon indicates the estimated object location.

The tracking pipeline can be summarized as:

```text
Initial frame
    ↓
Object bounding box
    ↓
ORB reference features
    ↓
Current-frame ORB features
    ↓
Brute-force matching
    ↓
RANSAC
    ↓
Homography
    ↓
Perspective transformation
    ↓
Tracked bounding box
```

## Configuration

| Parameter           |       Value |
| ------------------- | ----------: |
| Initial row         |          24 |
| Initial column      |          46 |
| Bounding-box height |      170 px |
| Bounding-box width  |      160 px |
| Feature detector    |         ORB |
| Descriptor type     |      Binary |
| Descriptor matcher  | Brute Force |
| Distance metric     |     Hamming |
| Geometric model     |  Homography |
| Robust estimator    |      RANSAC |
| RANSAC threshold    |         5.0 |
| Minimum matches     |           4 |

## Project Structure

```text
Feature_Detection/
├── .venv/
├── data/
│   └── video1.mp4
├── notebooks/
│   └── Feature_Detection.ipynb
├── outputs/
│   └── figures/
│       ├── reference_orb_keypoints.png
│       ├── representative_tracking_frames.png
│       ├── ransac_inlier_matches.png
│       ├── matches_and_inliers_by_frame.png
│       └── inlier_ratio_by_frame.png
├── requirements.txt
└── README.md
```

The `.venv/` directory is local and is not tracked by Git.

## Notebook Structure

```text
0. Setup
1. Data Path
2. Output Directory
3. Tracking Parameters
4. Initialize ORB and Descriptor Matcher
5. Read the Reference Frame
6. Detect Reference Features Inside the Object Region
7. Visualize the Reference Object and ORB Keypoints
8. Define Frame Matching and Homography Estimation
9. Track the Object Through the Video
10. Tracking Summary
11. Visualize Representative Tracking Frames
12. Visualize Inlier Feature Matches
13. Matches and Inliers Across the Sequence
14. Inlier Ratio Across the Sequence

Discussion
Conclusion
```

## Environment

The laboratory was developed using:

```text
Python 3.12.3
OpenCV 5.0.0
NumPy 2.5.3
```

Direct dependencies are defined in `requirements.txt`.

```text
numpy
matplotlib
opencv-python
ipykernel
```

## Installation

From the `Feature_Detection/` directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Register the Jupyter kernel:

```bash
python -m ipykernel install \
  --user \
  --name feature-detection \
  --display-name "Feature Detection (.venv)"
```

## Running the Notebook

Open:

```text
notebooks/Feature_Detection.ipynb
```

Select:

```text
Feature Detection (.venv)
```

Then run all cells from top to bottom.

The input video must be located at:

```text
data/video1.mp4
```

Generated figures are stored in:

```text
outputs/figures/
```

## Outputs

### Reference ORB Features

ORB keypoints detected inside the initial object region are visualized together with the manually defined bounding box.

```text
outputs/figures/reference_orb_keypoints.png
```

### Representative Tracking Frames

Several frames from the sequence show the transformed bounding box obtained from the estimated homography.

```text
outputs/figures/representative_tracking_frames.png
```

### RANSAC Inlier Matches

Feature correspondences retained by RANSAC are displayed between the reference frame and a representative current frame.

```text
outputs/figures/ransac_inlier_matches.png
```

### Matches and Inliers

The number of descriptor matches and geometrically consistent RANSAC inliers is monitored throughout the sequence.

```text
outputs/figures/matches_and_inliers_by_frame.png
```

### Inlier Ratio

The ratio between RANSAC inliers and descriptor matches provides an indication of the geometric consistency of the correspondence set.

```text
outputs/figures/inlier_ratio_by_frame.png
```

## Evaluation

Tracking quality is examined using:

* number of descriptor matches;
* number of RANSAC inliers;
* inlier ratio;
* visual consistency of the transformed bounding box;
* stability of object localization across the video sequence.

Frames for which descriptors, matches, or a valid homography cannot be obtained are rejected rather than producing an invalid transformation.

## Limitations

The method depends on stable local visual features.

Tracking performance may decrease when the object undergoes:

* strong motion blur;
* severe occlusion;
* large illumination changes;
* strong non-planar deformation;
* significant appearance changes;
* insufficient visible texture.

The homography model is most appropriate when the tracked region can be approximated by a planar surface or when perspective changes remain moderate.

## Technologies

* Python
* NumPy
* OpenCV
* Matplotlib
* Jupyter
* ORB
* Hamming distance
* Brute-force feature matching
* RANSAC
* Homography estimation
* Perspective transformation
* Feature-based object tracking

## Participants

* **Denos Kume**
* **Oluwole SHOKUNBI**

Master SIP
École Centrale de Nantes
