"""
Corrige el fenómeno de "doble salto de línea" en celdas Markdown de un .ipynb.

Cuando VS Code (o ciertas herramientas) importa un archivo .py con marcadores
# %% [markdown] como cuaderno de Jupyter, cada salto de línea (\n) en el
contenido Markdown se duplica, resultando en \n\n donde debería haber \n solo.

Este script:
  1. Une todas las líneas fuente de cada celda Markdown.
  2. Reemplaza \n\n → \n globalmente (la duplicación es uniforme).
  3. Reescribe la fuente como string único (estándar nbformat v4).

Los párrafos (separados originalmente por \n\n → duplicados a \n\n\n\n)
quedan correctamente con \n\n tras la corrección.

Uso:
    python fix_markdown_newlines.py lowpoly.ipynb
    python fix_markdown_newlines.py lowpoly.ipynb -o corregido.ipynb
"""

import json
import sys
import argparse
from pathlib import Path


def fix_markdown_cell_source(source) -> str:
    """Corrige fuente Markdown con saltos de línea duplicados."""
    # Unir si es lista; si es string, usar tal cual
    if isinstance(source, list):
        text = "".join(source)
    else:
        text = source

    # La duplicación es uniforme: cada \n original se volvió \n\n.
    # Un reemplazo global \n\n → \n restaura el contenido correcto.
    fixed = text.replace("\n\n", "\n")

    return fixed


def fix_notebook(input_path: Path, output_path: Path) -> None:
    """Lee un .ipynb, corrige sus celdas Markdown y guarda el resultado."""
    with open(input_path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    total_cells = len(nb.get("cells", []))
    fixed_count = 0

    for cell in nb["cells"]:
        if cell.get("cell_type") != "markdown":
            continue
        old_source = cell.get("source", "")
        new_source = fix_markdown_cell_source(old_source)

        if new_source != ("".join(old_source) if isinstance(old_source, list) else old_source):
            # Guardamos como string único (estándar nbformat v4)
            cell["source"] = new_source
            fixed_count += 1

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
        f.write("\n")  # nueva línea final

    print(f"✓ {input_path.name}  →  {output_path}")
    print(f"  {fixed_count} de {total_cells} celdas Markdown corregidas")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Corrige saltos de línea duplicados en celdas Markdown de un .ipynb"
    )
    parser.add_argument("notebook", type=Path, help="Archivo .ipynb a corregir")
    parser.add_argument(
        "-o", "--output", type=Path, default=None,
        help="Ruta de salida (por defecto: sobrescribe el original)"
    )
    args = parser.parse_args()

    src: Path = args.notebook.resolve()
    if not src.exists():
        sys.exit(f"No se encontró el archivo: {src}")
    if src.suffix.lower() != ".ipynb":
        sys.exit(f"Se esperaba un archivo .ipynb, recibido: {src}")

    dst: Path = args.output.resolve() if args.output else src
    fix_notebook(src, dst)


if __name__ == "__main__":
    main()
