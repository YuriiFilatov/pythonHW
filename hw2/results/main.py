import latex_generator as kek

def main():
    table = [[1, 2, 3], [3, 2, 1], [2, 3, 1], [2, 1, 3], [1, 3, 2], [3, 1, 2]]
    table_tex = kek.generate_latex_table(table)

    image_tex = kek.generate_latex_picture("../pictures/picture.png", 0.5, "Death for Kuban enemies!!!")

    latex_document = r"""\documentclass{article}
    \usepackage[T1]{fontenc}
    \usepackage[utf8]{inputenc}
    \usepackage{graphicx}
    \begin{document}
    """ + table_tex + r"""
    \bigskip
    """ + image_tex + r"""
    \end{document} 
    """

    with open("result.tex", "w+", encoding="utf-8") as f:
        f.write(latex_document)

if __name__ == "__main__":
    main()