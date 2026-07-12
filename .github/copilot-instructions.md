# Instrucciones para agentes de IA — exploraciones

> Proyecto de aprendizaje autodidacta con Python funcional, type hints estrictos y cuadernos pedagógicos en español.
> Más contexto en [README.md](../README.md).

---

## 🎨 Idioma

**Todo en español.** Variables, funciones, comentarios, docstrings, mensajes de commit y documentación. Es el idioma del proyecto y de Cervantes.

## 🧠 Estilo funcional puro

- **Sin clases** (salvo para enseñar `unittest.TestCase` en tutoriales de testing).
- **Sin `for` explícitos.** Usar `map`, `filter`, `functools.reduce`, `itertools` (`pairwise`, `accumulate`, `tee`, `islice`, `starmap`, etc.), `collections` (`Counter`, `defaultdict`, `deque`, `ChainMap`) y expresiones generadoras.
- **Sin estado mutable global.** La aleatoriedad se gestiona con `random.Random` explícito como parámetro.
- **Funciones puras:** misma entrada → misma salida, sin efectos secundarios observables.
- **Composición declarativa** con `functools.reduce` para encadenar funciones (patrón `pipe`).
- **Preferir comprensiones** de listas, diccionarios y conjuntos sobre `map`/`filter` con `lambda` cuando mejore la legibilidad.

## 🏷️ Type hints obligatorios

- **`mypy --strict` no perdona.** Toda función lleva type hints completos en parámetros y retorno.
- Usar `from __future__ import annotations` para sintaxis moderna (`dict[str, Any]`, `Path | None`).
- Definir alias de tipo semánticos con `#:` cuando aporten claridad:
  ```python
  #: Un n-grama es una cadena de n caracteres consecutivos.
  NGram = str
  ```
- Preferir `Generator[Y, S, R]` de `typing` sobre types genéricos ambiguos.

## 📝 Docstrings

- **Una sola línea por función.** Describir qué hace, no cómo.
- En español.
- Sin `Args:`, `Returns:` ni `Raises:` — los type hints ya comunican esa información.

## 📏 Código minimalista

- Mantener el código **lo más pequeño posible** sin sacrificar claridad.
- Una función = una responsabilidad. Si pasa de ~20 líneas, considerar dividirla.
- Sin comentarios redundantes con el código. Solo explicar el *por qué*, no el *qué*.
- Preferir `itertools` y expresiones generadoras a bucles manuales.
- Prohibido importar archivos locales: cada archivo es un cuaderno independiente. Solo se permite importar módulos de la biblioteca estándar y paquetes de terceros.

## 📓 Pedagogía y cuadernos

- El proyecto es un **portafolio educativo**. Todo código debe ser legible y enseñar.
- Los cuadernos usan **formato percent**: `# %% [markdown]` y `# %%` como delimitadores de celda.
- Separar cómputo de presentación. Las visualizaciones van en funciones `graficar_*` separadas.
- Incluir badges de "Open in Colab" en notebooks nuevos.

## 📊 Gráficas estilo Tufte

Los principios de Edward Tufte guían todo gráfico del proyecto:

- **Proporción datos/tinta** (data-ink ratio): maximizar la tinta que representa datos. Eliminar toda decoración superflua (chartjunk): fondos, bordes gruesos, grid densa, sombras, 3D.
- **No distorsionar**: evitar escalas rotas, efectos 3D, proporciones engañosas.
- **Etiquetado directo**: anotar valores sobre los datos (`.text()` o `bar_label()`) en lugar de remitir a leyendas distantes.
- **Micro/macro**: cuando sea posible, mostrar detalle fino y panorama general simultáneamente.
- **Color sobrio y funcional**: preferir una paleta de dos tonos apagados (azul `#4A6FA5`, rojo óxido `#C44E52`). Usar color solo para diferenciar categorías, nunca por decoración.
- **Spines mínimos**: eliminar bordes superior y derecho (`ax.spines[["top", "right"]].set_visible(False)`). Grid casi invisible (`alpha=0.3, lw=0.5`), solo en el eje donde aporte referencia.
- **Escalas legibles**: dividir valores grandes (población → millones) para que las etiquetas de eje no requieran notación científica.
- **Funciones `graficar_*`**: cada gráfico se encapsula en una función que recibe un DataFrame ya agregado y devuelve `None` (dibuja directamente). Esto separa cómputo de presentación y mantiene las celdas limpias.
- **Pirámide poblacional**: usar `barh` enfrentadas (hombres valores negativos a la izquierda, mujeres positivos a la derecha), nunca histogramas dodge. Agrupar edades en quinquenios.
- **Distribuciones**: preferir KDE con relleno suave (`kdeplot(..., fill=True, alpha=0.25)`) sobre histogramas con muchas barras.

## 🧰 Herramientas y configuración

- **mypy** en modo `--strict` (configurado en `.vscode/settings.json`).
- **black** como formateador (formato al guardar).
- **isort** para ordenar imports.
- **pylint** para linting.
- Las pruebas se ejecutan con `unittest` y `doctest` dentro de notebooks o con `python -m unittest`.
- No hay gestor de dependencias formal. Las dependencias nuevas se documentan en [README.md](../README.md).

## 📂 Convenciones de archivos

- Nombres en `snake_case`: `enoe_schema.py`, `cargar_diccionario()`.
- `_prefijo_guion_bajo` para funciones y constantes privadas.
- `UPPER_CASE` para constantes de módulo.
- Comentarios breves, de preferencia en línea, con `#` y espacio después. Evitar comentarios multilínea.
- Cada celda debe tener una longitud máxima de 40 líneas de código. Si se excede, es necesario refactorizar en funciones auxiliares o reescribir en secciones más pequeñas.
- Uso de memoria mínimo: es prefeible cargar y procesar datos en streaming, en lugar de cargar todo en memoria.
- Evitar saturar de variables el espacio de nombres global. Usar funciones auxiliares para encapsular variables temporales.

## 🔗 Importaciones

- Importaciones absolutas para funciones.
- Sólo se pueden importar directamente clases y módulos, pero no funciones individuales.
- Prohibido importar módulos locales.
- Agrupar: estándar → terceros → locales, separados por una línea en blanco.
