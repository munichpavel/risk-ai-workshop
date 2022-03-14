import os
from pathlib import Path
import subprocess
import shutil

import pytest

from risk_learning.tex import build_pdf_latex


def test_single_filebuild_pdf_latex(tmpdir):
    """Test if pdf file for inputted latex file gets built"""
    tex_dir = Path(tmpdir)

    text = r'''\documentclass{book}
\begin{document}
\title{\textbf{It's a story}}
\maketitle
\end{document}
'''
    tex_path = tex_dir / 'example.tex'

    with open(tex_path, 'w') as fp:
        fp.write(text)

    build_pdf_latex(filepath=tex_path, outdir=tex_dir)

    assert (tex_dir / (tex_path.stem + '.pdf')).exists()


# Test(s) with on-disk files
test_call_dir = Path(os.getcwd())


@pytest.mark.parametrize(
    'filepath',
    [
        test_call_dir / 'slides' / 'ai-for-risk' / 'ai_for_risk.tex',
    ]
)
def test_build_read_pdf_latex(tmpdir, filepath):

    # Test setup -- folder structure
    test_texdir = Path(tmpdir) / 'tex'
    lecture_dir = test_texdir / 'lecture'
    graphics_dir = lecture_dir / 'graphics'
    graphics_dir.mkdir(parents=True)

    # Copy needed contents of parent folder, else potential input directives
    # fail
    shutil.copy(filepath.parent.parent / 'ai_for_risk_header.tex', test_texdir)

    for match_file in filepath.parent.glob('*.tex'):
        print(match_file)
        shutil.copy(match_file, lecture_dir)

    for match_file in filepath.parent.glob('graphics/*'):
        shutil.copy(match_file, graphics_dir)

    copied_filepath = lecture_dir / filepath.name

    subprocess.run(
        [
            'python', 'risk_learning/tex.py',
            '--filepath', copied_filepath,
            '--outdir', lecture_dir
        ]
    )

    outpath = lecture_dir / (filepath.stem + '.pdf')

    # for p in test_texdir.glob('*'):
    #     print(p)
    for p in lecture_dir.glob('*'):
        print(p)

    assert outpath.exists()
