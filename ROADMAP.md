# HASA Roadmap

**Goal:** an open-source, browser-based flood frequency tool for European gauge data that follows
DWA-M 552 and shows the uncertainty of every estimate, kept in Python.

Every item below is tracked as a GitHub issue and lands through a pull request
(see [CONTRIBUTING.md](CONTRIBUTING.md)).

## Baseline: v1.0.0 (February 2022)

`v1.0.0` (released 28 Feb 2022) is the code as submitted for the course *Python Programming for Water Resources
Engineering and Research* (University of Stuttgart, WS 2021/22) by Akash Handique and
Aswatha Narayana Sanagavarapu. It is kept unchanged under that tag. Two later commits on `main` only updated the UML diagram and a presentation PDF; the code is identical.

Results of `v1.0.0` for the Neckar at Oberndorf (LUBW gauge 409, daily means 1929–2021,
93 calendar years), confirmed in November 2026 by running the untouched code on pandas 1.4.1:

| Return period T (years) | 50 | 100 | 150 | 200 | 500 | 1000 |
| --- | --- | --- | --- | --- | --- | --- |
| Q (m³/s) | 187.77 | 210.29 | 223.42 | 232.73 | 262.33 | 284.71 |

These numbers are the reference for the regression test in Phase 1. Any change that moves them
must be intentional and recorded in the changelog.

**Version plan:** Phase 1 fixes ship as `v1.1.0`; the restructured package in Phase 2 becomes
`v2.0.0`, because how the code is imported and run will change.

## Phase 1: Revive and protect

Gate: the 2022 app runs on current Python and the regression test passes in CI.

- [x] 2022 state preserved as release `v1.0.0` (published 28 Feb 2022)
- [ ] Project docs and workflow: roadmap, changelog, contributing guide, templates
- [ ] Fix the pandas 3 crash in `resample()`, explicit date format, header detection
- [ ] Regression test against the v1.0.0 results above
- [ ] Packaging: `pyproject.toml`, remove `.idea/`, move PDFs out of the repo
- [ ] Linting and CI: ruff, pre-commit, GitHub Actions running pytest

## Phase 2: Core package

Gate: `hasa analyse file.csv` prints a results table for any return period, with no GUI installed.

- [ ] `src/hasa` package; calculations separated from the GUI
- [ ] Hydrological year (Nov–Oct) with a completeness rule
- [ ] Yn/Sn computed directly instead of the lookup table (removes the 200-year limit)
- [ ] Gumbel (moments, L-moments, MLE) and GEV (L-moments, MLE), building on scipy / lmoments3
- [ ] Bootstrap confidence bands; Gringorten plotting positions
- [ ] Tkinter app moved to `legacy/` and calling the new core

## Phase 3: Web app

Gate: a public GitHub Pages link where a user uploads a CSV and gets a frequency plot with bands.

- [ ] Streamlit app: upload, data-quality panel, annual maximum plot, frequency plot, results table
- [ ] CSV and PDF report export
- [ ] Static build with stlite, deployed to GitHub Pages by GitHub Actions
- [ ] Documentation site and an updated README with screenshots

## Phase 4: Toward DWA-M 552

Gate: results for Oberndorf checked against official LUBW values.

- [ ] Pearson III, log-Pearson III, log-normal; goodness-of-fit tests
- [ ] Peaks-over-threshold series
- [ ] Trend and break-point tests (Mann–Kendall)
- [ ] Peak-flow (Scheitelwert) input, labelled separately from daily means
- [ ] Validation against Bulletin 17C worked examples and LUBW values for gauge 409

## Reaching users

- [ ] Zenodo DOI for each release
- [ ] Short paper (e.g. JOSS) once Phase 3 is done
- [ ] German and English interface and reports
