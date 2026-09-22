# Master SIP Repository Standard

This document defines the mandatory structure for notebook-based scientific laboratories and experiment-driven projects in this repository.

## 1. Single Canonical Reference

The **one and only structural reference** is:

```text
Lab_Works/Computer_Vision/Camera_Calibration/
```

Camera Calibration is the golden template.

Other modules may differ in scientific content, algorithms, data, number of tasks, figures, metrics, and dependencies. They must not introduce a competing structural convention.

**Non-negotiable rule:** when another module differs structurally from Camera Calibration, the other module is adapted to Camera Calibration, not the reverse.

## 2. Canonical Module Structure

```text
Module_Name/
├── data/
├── notebooks/
│   ├── module_problem_statement.ipynb
│   ├── module_requirements_gathering_and_approach.ipynb
│   ├── module_theory.ipynb
│   └── module.ipynb
├── outputs/
│   └── figures/
├── requirements.txt
└── README.md
```

A category-level `.gitignore` may protect local environments for multiple child modules. Redundant per-module structural files should not be added when the parent rule already covers them.

## 3. Four-Notebook Contract

The same numbered task sequence must be traceable through all four notebooks of a module:

```text
Problem Statement
        ↓
Requirements Gathering & Approach
        ↓
Theory
        ↓
Implementation
```

The **number of tasks is problem-dependent**. Camera Calibration's task count is not a target.

### Problem Statement

Mandatory structural order:

1. Camera-style branded header
2. `## Context`
3. `## Problem Statement`
4. `## Inputs and Fixed Parameters`
5. `## 1. ...` through `## N. ...`
6. `## Completion Criterion`

The Problem Statement is a **standalone laboratory specification**, not a project summary or checklist.

It must be sufficiently complete that another engineer can implement and evaluate the laboratory using this notebook alone.

Required content:

- **Context:** technical/scientific setting, data characteristics, modeling assumptions, and the engineering difficulty being addressed.
- **Problem Statement:** precise objective, expected deliverables, measurable outputs, and explicit scope boundaries.
- **Inputs and Fixed Parameters:** datasets, filenames/paths, dimensions, constants, ranges, algorithm settings, conventions, candidate parameter sets, and output requirements whenever these are fixed by the experiment.
- **Numbered tasks:** each task must specify the work to perform, relevant equations or mathematical model, fixed/controlled variables, required numerical or visual evidence, and any comparison/decision rule.
- **Experiments:** parameter sweeps and ablations must state the tested values and the rule used to retain/reject a configuration.
- **Evaluation:** required metrics, figures, tables, residual/diagnostic analyses, and numerical validity conditions must be explicit.
- **Completion Criterion:** objective conditions under which the laboratory is considered complete.

A numbered task must not be reduced to a one-line instruction such as “implement X” or “analyze Y”. Where appropriate it should contain sub-questions, equations, parameter values, expected figures/tables, validation conditions, and requested technical interpretation.

Implementation code does not belong here except very small interface/signature fragments when the required API itself is part of the laboratory specification.

### Requirements Gathering & Approach

Mandatory structural order:

1. Camera-style branded header
2. `## Requirements and Approach`
3. `## Global Requirements`
4. the same `## 1. ...` through `## N. ...` tasks, in the same order and with the same titles
5. `## Requirement-to-Code Traceability`

Purpose: translate each task into engineering requirements, method choices, acceptance criteria, and implementation responsibilities.

### Theory

Mandatory structural order:

1. Camera-style branded header
2. `## Theoretical Foundations`
3. `### Technical Context`
4. `### Core <Domain> Model`
5. `### Notation and Conventions`
6. `### Analytical Scope`
7. the same `## 1. ...` through `## N. ...` tasks
8. `## Technical Synthesis`
9. `## Scope and Limitations`
   - `### Included`
   - `### Not included`

Purpose: document the mathematical model, derivations, assumptions, numerical conditioning, method-specific failure modes, and the direct link between theory and implementation.

The Theory notebook is **not a teaching progression**. It must not contain "Concept Check", beginner/intermediate/advanced levels, learning-outcome ladders, interview questions, exam-preparation material, or tutorial exercises.

### Implementation

Mandatory structural order:

1. Camera-style branded header
2. concise technical execution summary
3. `## Setup — Environment and Configuration`
4. the same `## 1. ...` through `## N. ...` tasks
5. `## Final Result Summary`

Purpose: provide the executable experimental workflow and its measured evidence.

The Implementation notebook is **code-first**. It may contain only:

- concise task objectives tied to the actual execution;
- configuration and parameter values actually used;
- executable code;
- tables and figures produced by the execution;
- measured metrics and diagnostics;
- observations tied directly to generated outputs;
- experimental retention/rejection decisions;
- final numerical and output validation.

The Implementation notebook must **not** contain:

- general mathematical derivations;
- generic equations already documented in Theory;
- conceptual definitions;
- textbook explanations;
- "why" sections unrelated to a measured result;
- tutorial questions or checkpoints;
- general method-selection theory;
- historical development labels such as "Step 1", "Improvement 2", or similar internal working notes.

If an equation explains the method in general, it belongs in `*_theory.ipynb`. If a numerical value, table, curve, or conclusion is produced by running the experiment, it belongs in the Implementation notebook.

Subsections inside a task use `###` or deeper headings so they cannot be confused with top-level tasks.

## 4. Task Alignment Rule

Within one module:

- task numbers must match across all four notebooks;
- task titles must match across all four notebooks;
- task order must match across all four notebooks;
- each requirement must map to implementation;
- theory must support the corresponding implementation task;
- no unrelated top-level numbered sections may appear.

A module fails the completion gate if the four task lists differ.

## 5. README Standard

README files follow the Camera Calibration order:

1. `# Module Title`
2. concise technical summary
3. statement that the module is organized into four complementary notebooks
4. linked descriptions of:
   - Problem Statement
   - Requirements Gathering & Approach
   - Theory
   - Implementation
5. `## Outputs`
6. `## Run`
7. `## Project Structure`
8. `## Scope`
   - Implemented
   - Not included
9. `## Participants`

README files are navigation documents, not substitute theory notebooks.

## 6. Naming Rules

Module folders:

```text
Pascal_or_Title_Case_With_Underscores
```

Notebook stems use lowercase snake case:

```text
module_problem_statement.ipynb
module_requirements_gathering_and_approach.ipynb
module_theory.ipynb
module.ipynb
```

Generated figures use ordered descriptive names such as:

```text
01_input_data.png
02_preprocessing.png
03_method_result.png
04_evaluation.png
```

Legacy, duplicate, `final2`, `new`, `latest`, and ambiguous notebook names must not remain beside the canonical four-notebook set.

## 7. Reproducibility Rules

Every module must:

- use repository-relative paths;
- validate required inputs before processing;
- define and pin direct dependencies in `requirements.txt`;
- execute top to bottom without hidden manual steps;
- make randomness deterministic where applicable;
- save generated figures under `outputs/figures/`;
- preserve meaningful outputs when appropriate;
- report quantitative metrics appropriate to the problem;
- include numerical and/or logical validation checks;
- document limitations and rejected alternatives;
- avoid secrets, credentials, and machine-specific absolute paths.

## 8. Evaluation and Validation

Metrics are problem-specific, not mechanically copied from another module.

Examples:

- calibration → reprojection error / RMSE;
- tracking → matches / RANSAC inliers / inlier ratio;
- classification → loss / accuracy / precision / recall / confidence;
- segmentation → Dice / IoU / precision / recall;
- filtering → MAE / MSE / RMSE / PSNR plus visual inspection;
- background subtraction → SAD / MSE / PSNR plus mask/overlay validation.

Every executable notebook ends with explicit validation followed by a Final Result Summary.

## 9. Visual and Writing Identity

Mandatory principles:

- professional English;
- Camera-style branded notebook header;
- academic/engineering laboratory tone;
- concise technical prose;
- equations used to justify implemented methods;
- explicit assumptions, conditioning issues, failure modes, and limitations;
- results presented as evidence, not as teaching examples;
- discussion tied to observed figures and quantitative metrics;
- no decorative clutter;
- no unnecessary emojis;
- no "Beginner / Intermediate / Advanced" progression;
- no "Concept Check";
- no "Expected Competencies" or learning-outcome ladders;
- no interview/exam-preparation sections;
- no bootcamp, tutorial, mastery, or "from zero" language;
- no duplicated long explanations across notebooks;
- evidence-based conclusions.

The repository should read as a coherent **Master-level scientific and engineering portfolio**. A reviewer should immediately see experimental discipline, reproducibility, mathematical grounding, and technical judgment.

## 10. Notebook Responsibility Rule

Each artifact has one non-overlapping responsibility:

- laboratory specification, fixed parameters, requested experiments, required deliverables, and completion criteria → `*_problem_statement.ipynb`;
- engineering requirements, constraints, method choices, acceptance criteria, and traceability → `*_requirements_gathering_and_approach.ipynb`;
- mathematical models, derivations, assumptions, interpretation, conditioning, and theoretical failure modes → `*_theory.ipynb`;
- executable code, actual parameter configuration, measured results, generated figures, diagnostics, experiment-specific observations, and final validation → `*.ipynb`;
- concise navigation and module summary → `README.md`.

Long explanations must not be duplicated across roles. A mathematical formula that describes the general method belongs in Theory even when the corresponding computation is implemented in code.

## 11. Completion Gate

A scientific module is repository-ready only if:

- [ ] Camera Calibration structure is respected;
- [ ] exactly four canonical notebooks exist;
- [ ] all four notebook headers follow the Camera presentation;
- [ ] no bootcamp/tutorial/learning-progression language remains;
- [ ] task titles/order align across all four notebooks;
- [ ] Problem Statement ends with Completion Criterion;
- [ ] Requirements ends with Requirement-to-Code Traceability;
- [ ] Theory contains Technical Synthesis and Scope and Limitations;
- [ ] Implementation starts with Setup and ends with Final Result Summary;
- [ ] Implementation contains no general theory, generic derivations, or duplicated method equations;
- [ ] Problem Statement, Requirements, and Theory contain no executable code or stored outputs;
- [ ] README follows Camera Calibration order;
- [ ] dependencies are explicit and pinned;
- [ ] paths are portable;
- [ ] outputs are organized;
- [ ] validation is explicit;
- [ ] legacy/duplicate notebooks are removed.

This standard applies to current refactoring and all future notebook-based scientific additions to **Master_SIP_EC-Nantes**.
