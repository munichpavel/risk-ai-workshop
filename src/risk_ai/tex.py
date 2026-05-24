"""LaTex build and preview functionality"""

import os
from pathlib import Path
import subprocess
import shutil


def build_pdf_latex(filepath: Path, outdir: Path):
    '''
    Perform pdflatex. bibtex unfortunately out of scope (I tried and failed).
    '''

    # Change to parent dir of tex file. I tried and failed to use
    # subprocess.run's cwd argument. It seemed ok locally, but not in ci / cd
    # See https://github.com/munichpavel/risk-ai-workshop/issues/12
    original_wd = os.getcwd()
    os.chdir(filepath.parent)

    n_reps_pdflatex = 2

    for _ in range(n_reps_pdflatex):
        subprocess.run(['pdflatex', filepath.stem])

    subprocess.run(['bibtex', filepath.stem])

    for _ in range(n_reps_pdflatex):
        subprocess.run(['pdflatex', filepath.stem])

    os.chdir(original_wd)

    # copy pdf to output directory
    pdf_out_filename = filepath.stem + '.pdf'
    shutil.copy(
        src=filepath.parent / pdf_out_filename,
        dst=outdir / pdf_out_filename
    )


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Build pdf latex files')
    parser.add_argument('--filepath', help='Path to source tex file')
    parser.add_argument('--outdir', help='Path to output directory')

    args = parser.parse_args()

    build_pdf_latex(Path(args.filepath), Path(args.outdir))
