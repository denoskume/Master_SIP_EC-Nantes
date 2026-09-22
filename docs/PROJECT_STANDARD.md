# Master SIP Repository Standard

This document defines the mandatory structure and presentation standard for every laboratory and project in this repository.

**Consistency is a repository requirement.** New work must follow this standard before it is considered complete.

---

## 1. Canonical Structure

Every notebook-based laboratory or scientific project must use:

```text
Lab_or_Project_Name/
├── data/
├── notebooks/
│   ├── <lab_name>_problem_statement.ipynb
│   ├── <lab_name>_theory.ipynb
│   ├── <lab_name>_requirements_gathering_and_approach.ipynb
│   └── <lab_name>.ipynb
├── outputs/
│   └── figures/
├── requirements.txt
└── README.md
```

Additional folders such as `src/`, `models/`, `reports/`, or `tests/` may be added only when the work genuinely requires them. The canonical backbone above must remain recognizable.

---

## 2. Notebook Responsibilities

### <lab_name>_problem_statement.ipynb

Purpose: define the problem before solving it.

Mandatory order:

1. Title
2. Context
3. Problem Statement
4. Inputs / Provided Data
5. Objectives
6. Constraints and Assumptions
7. Required Tasks
8. Expected Outputs
9. Success Criteria
10. Lab / Project Instructions

No implementation code belongs here except tiny illustrative snippets when strictly necessary.

### <lab_name>_theory.ipynb

Purpose: provide only the theory required to understand the solution.

Mandatory order:

1. Title
2. Theoretical Foundations
3. Mathematical Model
4. Core Equations
5. Algorithmic Principles
6. Assumptions
7. Interpretation
8. Limitations of the Theory
9. Key Takeaways

Rules:

- formulas must use consistent LaTeX notation;
- symbols must be defined before use;
- derivations must be readable and correctly aligned;
- theory must support the lab directly;
- unrelated textbook material must not be added.

### <lab_name>_requirements_gathering_and_approach.ipynb

Purpose: translate the problem into an engineering solution design.

Mandatory order:

1. Title
2. Requirements Gathering
3. Functional Requirements
4. Data Requirements
5. Input / Output Contract
6. Assumptions and Constraints
7. Proposed Approach
8. Pipeline Skeleton
9. Method Selection and Rationale
10. Evaluation Metrics
11. Validation Strategy
12. Failure Modes / Risks
13. Implementation Plan
14. Expected Deliverables

This notebook answers: **What exactly are we building and why this approach?**

### <lab_name>.ipynb

Purpose: provide the complete reproducible implementation.

Mandatory order:

1. Title
2. Environment and Imports
3. Configuration
4. Paths
5. Core Functions / Classes
6. Data Loading
7. Data Validation
8. Pipeline Implementation
9. Execution
10. Results
11. Quantitative Evaluation
12. Visual Evaluation
13. Save Outputs
14. Validation Checks
15. Final Result Summary

Rules:

- code must be reproducible;
- code cells must be commented where the reasoning is not obvious;
- repeated logic must become reusable functions or classes;
- paths must be relative to the project;
- outputs must be saved under `outputs/`;
- no long theory blocks belong here;
- no hidden manual steps;
- notebook execution must follow top-to-bottom order.

---

## 3. README Standard

Every lab or project README must be concise and use the same section order:

```markdown
# Project / Lab Name

One-paragraph technical summary.

## Problem

Short description of the engineering problem.

## Pipeline

Compact pipeline diagram.

## Notebooks

1. Problem Statement
2. Theory
3. Requirements Gathering & Approach
4. Implementation

## Key Methods

Concise method list.

## Evaluation

Metrics and validation strategy.

## Outputs

Where generated results are stored.

## Project Structure

Compact directory tree.

## Run

Minimal reproducibility instructions.

## Participants

Names and academic context.
```

README files are navigation and project-summary documents. They must not duplicate extensive theory, implementation explanations, or long tutorial content from the notebooks.

---

## 4. Naming Rules

Folder names:

```text
Pascal_or_Title_Case_With_Underscores
```

Notebook names:

```text
<lab_name>_problem_statement.ipynb
<lab_name>_theory.ipynb
<lab_name>_requirements_gathering_and_approach.ipynb
<lab_or_project_name>.ipynb
```

Generated figures should use ordered, descriptive names:

```text
01_input_data.png
02_preprocessing.png
03_method_result.png
04_evaluation.png
```

Avoid ambiguous names such as:

```text
test.png
final2.png
new_notebook.ipynb
result_latest.png
```

---

## 5. Visual and Writing Identity

All notebooks and README files must share the same visual and writing style.

Mandatory principles:

- professional English;
- concise technical prose;
- consistent heading hierarchy;
- consistent mathematical notation;
- consistent table formatting;
- consistent pipeline diagrams;
- consistent code-section ordering;
- no decorative clutter;
- no tutorial or bootcamp branding;
- no unnecessary emojis;
- no duplicated explanations across files;
- explicit assumptions and limitations;
- evidence-based conclusions.

The repository should read as one coherent engineering portfolio, not as unrelated coursework.

---

## 6. Reproducibility Rules

Each unit must:

- use relative paths;
- define dependencies in `requirements.txt`;
- run from top to bottom;
- preserve meaningful notebook outputs when appropriate;
- save generated figures under `outputs/figures/`;
- validate required input files before execution;
- report quantitative metrics when applicable;
- document limitations and failure cases;
- avoid machine-specific absolute paths;
- avoid secrets, private credentials, or private identifiers.

---

## 7. Evaluation Pattern

When applicable, every implementation notebook must include:

```text
Input validation
      ↓
Pipeline execution
      ↓
Quantitative evaluation
      ↓
Visual evaluation
      ↓
Validation checks
      ↓
Saved outputs
      ↓
Final result summary
```

Metrics must be chosen according to the task rather than reused mechanically.

Examples:

- calibration → reprojection error / RMSE;
- tracking → matches, RANSAC inliers, inlier ratio;
- classification → accuracy, precision, recall, confidence;
- segmentation → Dice, IoU, precision, recall;
- filtering → MSE, RMSE, PSNR plus visual inspection.

---

## 8. Source-of-Truth Rule

Information must live in one primary location:

- problem definition → `<lab_name>_problem_statement.ipynb`;
- theory and formulas → `<lab_name>_theory.ipynb`;
- engineering design → `<lab_name>_requirements_gathering_and_approach.ipynb`;
- executable implementation and results → `<lab_name>.ipynb`;
- navigation and concise summary → `README.md`.

Do not duplicate long content between these files.

---

## 9. Project Exceptions

Software-heavy projects may add `src/`, `tests/`, `docs/`, or application assets.

However, the repository identity must remain consistent:

- same README section order;
- same naming quality;
- same reproducibility expectations;
- same evaluation/validation discipline;
- same professional writing style.

Scientific or experiment-driven projects must use the four-notebook structure.

---

## 10. Completion Gate

A lab or project is considered repository-ready only if:

- [ ] canonical structure is respected;
- [ ] all required notebooks exist;
- [ ] notebook roles are not mixed;
- [ ] README follows the standard;
- [ ] dependencies are explicit;
- [ ] paths are portable;
- [ ] implementation is reproducible;
- [ ] outputs are organized;
- [ ] metrics and validation are present where applicable;
- [ ] limitations are documented;
- [ ] naming and visual identity are consistent;
- [ ] no private or machine-specific information is committed.

This standard is mandatory for current refactoring and all future additions to **Master_SIP_EC-Nantes**.
