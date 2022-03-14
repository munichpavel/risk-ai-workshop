"""LaTex build and preview functionality"""

from pathlib import Path
import subprocess


def build_pdf_latex(filepath: Path, outdir: Path):
    subprocess.run(
        ['pdflatex', f'-output-directory={outdir}', filepath],
        cwd=filepath.parent.as_posix()
    )


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Build pdf latex files')
    parser.add_argument('--filepath', help='Path to source tex file')
    parser.add_argument('--outdir', help='Path to output directory')

    args = parser.parse_args()

    build_pdf_latex(Path(args.filepath), Path(args.outdir))
