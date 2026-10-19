# The Value of Stopping: Evidence Queues, Recoverability, and Priority Rights

**Dr. Jan-Hendrik Weinert** · Working paper · Editorial edition F1, 19 October 2026

[Read the paper](paper.pdf) · [LaTeX source](manuscript.tex) · [Editable Markdown](manuscript.md) · [Reproduction instructions](REPRODUCIBILITY.md)

## Abstract

Correlated evidence can make efficient research privately unattractive both initially and at continuation. In a two-case, two-slot model with expiration and optional terminal action, we derive the exact implementation and funding frontier for two nonnegative public-history credits. One rewards the initial experiment; the other rewards a specified contingent final experiment. Complete backward induction gives necessary and sufficient inequalities, separate expected and pathwise gross-funding limits, and attainment boundaries on a certified interval of binary priors. Credits are transfers rather than resource losses. The independent benchmark retains the recoverability-versus-priority comparison and common-charge classification. Complete proofs and exact synthetic enumeration support this restricted implementation result; no unrestricted mechanism optimum or empirical effect is claimed.

## Contents

- `paper.pdf`: complete paper, including proofs, bibliography and appendices.
- `manuscript.tex`: authoritative mathematical typesetting source; `manuscript.md`: editable alternative.
- Calculation scripts, recorded synthetic outputs, and the paper-specific source ledgers and prospective research protocols.
- `reproduce.py`, `requirements.txt`: one entry point and dependencies for the supplied analysis.
- `build_paper.sh`: rebuilds the current PDF from the LaTeX source without replacing the supplied PDF.
- `CITATION.cff`: citation metadata; `SHA256SUMS.txt`: published payload checksums.

## Reproduce the calculations

Use Python 3.12. From the repository root, create a virtual environment and run:

```sh
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 reproduce.py
```

The analysis uses synthetic inputs or exact model primitives supplied with the code. It requires no private organizational data, API credentials or data download. Installing dependencies may require access to a package index. Full analytical proofs remain in the paper; finite computations supplement those proofs.

## Rebuild the paper

With TeX Live and the packages declared in `manuscript.tex` installed:

```sh
bash build_paper.sh
```

The result is `build/manuscript.pdf`. Compile from the repository root so figure paths resolve. The supplied `paper.pdf` is the visually checked publication edition. PDF byte hashes can vary between rebuilds because of timestamps and toolchain metadata. Do not regenerate this edition's LaTeX through Pandoc when a matching layout is required.

## Research status

This is a theoretical working paper with synthetic computational illustrations. Any empirical or field protocol included here is prospective, and no reported synthetic output is an observed firm result. Publication of this repository does not imply journal acceptance or empirical validation. The paper states its model-specific assumptions and limitations.

## Citation

Weinert, Jan-Hendrik (2026). *The Value of Stopping: Evidence Queues, Recoverability, and Priority Rights*. Working paper, editorial edition F1.
Use the repository's citation metadata when citing or reusing the work.
