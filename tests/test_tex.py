from pathlib import Path

from risk_learning.tex import build_pdf_latex


def test_build_pdf_latex(tmpdir):
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