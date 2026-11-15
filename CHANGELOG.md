# Changelog

All notable changes to this project are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project
uses [Semantic Versioning](https://semver.org/).

Every pull request adds a line under **Unreleased**. When a version is tagged, the
Unreleased section becomes that version.

## [Unreleased]

### Added

- `ROADMAP.md` with the plan for reviving the project and the v1.0.0 reference results.
- `CHANGELOG.md`, `CONTRIBUTING.md` and `CLAUDE.md`.
- Pull request and issue templates under `.github/`.
- Project status note in the README.

### Changed

- Corrected UML diagram and updated presentation PDF (28 Feb 2022, after the v1.0.0 release; no code changes).

## [1.0.0] - 2022-02-28

The original course project (University of Stuttgart, WS 2021/22), by Akash Handique and
Aswatha Narayana Sanagavarapu.

### Added

- Reading LUBW daily discharge CSV files and computing calendar-year annual maxima.
- Gumbel frequency-factor method with tabulated reduced mean and standard deviation (Yn, Sn).
- Flood discharges for return periods of 50, 100, 150, 200, 500 and 1000 years.
- Tkinter GUI with hydrograph and extrapolation plots.
- Example data: Neckar at Oberndorf (LUBW gauge 409), 1929–2021.

[Unreleased]: https://github.com/aswathCodeX/HASA-Python-Project/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/aswathCodeX/HASA-Python-Project/releases/tag/v1.0.0
