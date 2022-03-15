"""LaTex build and preview functionality"""

from pathlib import Path
import subprocess
import shutil


def build_pdf_latex(filepath: Path, outdir: Path):
    '''
    Perform combination of pdf latex and bibtex, using the recipe taught to me
    by https://www.sfu.ca/~nilten/ way back when
    '''

    n_reps_pdf_latex = 2

    for _ in range(n_reps_pdf_latex):
        subprocess.run(
            ['pdflatex', filepath],
            cwd=filepath.parent.as_posix()
        )

    # bibtex
    subprocess.run(
        ['bibtex', filepath],
        cwd=filepath.parent.as_posix()
    )

    # pdflatex again, this time use output directory
    for _ in range(n_reps_pdf_latex):
        subprocess.run(
            ['pdflatex', filepath],
            cwd=filepath.parent.as_posix()
        )

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
