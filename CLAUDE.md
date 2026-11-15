# Notes for Claude Code sessions

HASA is a flood frequency analysis tool in Python. The 2022 course version is tagged `v1.0.0`.
The plan is in [ROADMAP.md](ROADMAP.md); the workflow is in [CONTRIBUTING.md](CONTRIBUTING.md).

## Rules

- Work on one roadmap item per session. Each item has a GitHub issue.
- Create a branch before touching code (`<type>/<issue>-<description>`); never commit to `main`.
- Open a pull request with `Closes #<issue>` and a changelog entry. The maintainer merges.
- Keep the v1.0.0 reference results (in ROADMAP.md) reproducible. Once the regression test
  exists, run it before every commit and never change its expected values without saying why.
- Keep hydrology out of UI files. Calculations go in the core package with tests.
- Do not copy code from other repositories. Other tools may be studied as references only.
- Prefer established libraries (numpy, pandas, scipy, lmoments3) over hand-written statistics.

## Layout today (v1.0.0)

- `main.py` – Gumbel calculation and `main()`
- `discharge_data.py` – reads the LUBW CSV, annual maxima
- `gumbel_reduce.py`, `gumbel_reduced/gumbel.csv` – Yn/Sn table
- `plot_discharge.py`, `gui.py` – matplotlib plots and the Tkinter GUI
- `config.py`, `log.py` – imports, paths, logging
- `Discharge-data/river_discharge_data.csv` – Neckar at Oberndorf, LUBW gauge 409

Run the 2022 code from the repository root (paths are relative to the working directory).
It needs pandas < 3.0 until the Phase 1 fixes are merged (v1.0.0 results were confirmed on pandas 1.4.1).
