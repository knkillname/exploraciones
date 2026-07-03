# 🧭 exploraciones

> *Por el puro gusto de aprender.*
>
> Un portafolios personal de cuadernos de Jupyter donde exploro temas de computación
> de forma autodidacta: sin prisas, sin notas, sin más objetivo que la curiosidad.

---

## 📓 ¿Qué hay aquí?

| Cuaderno | Tema | Descripción |
|---|---|---|
| [**Jerigonza**](cuadernos/Jerigonza.ipynb) | Cadenas de Markov | Generación de texto en español usando programación funcional pura. Entrenado sobre *Don Quijote*, produce jerigonza que casi parece castellano. |
| [**Pruebas unitarias**](cuadernos/Pruebas%20unitarias.ipynb) | Testing en Python | Tutorial progresivo de `unittest`, `doctest` y TDD, ilustrado con una caja registradora (Kata09). |

## 🚀 Para empezar

El proyecto usa un [devcontainer](.devcontainer/devcontainer.json) con la imagen de Google Colab,
así que basta con abrirlo en VS Code y ejecutar las celdas. También funciona en cualquier entorno
con Python 3.10+ y las dependencias de siempre:

```bash
pip install numpy matplotlib networkx
```

## 🎨 Estilo y filosofía

- **Español**. Todo el código, comentarios y documentación van en español. Es mi idioma y el de Cervantes.
- **Funcional puro**. Sin clases, sin `for`, sin estado mutable. `itertools`, `functools.reduce`, `map`, `filter`… por el placer de pensarlo así.
- **Type hints a rajatabla**. `mypy --strict` no perdona.
- **Separación de concerns**. Cómputo por un lado, presentación por otro. Las visualizaciones tienen su propio espacio.

## 🛠️ Tecnologías

Python 3.10+ · Jupyter · NumPy · Matplotlib · NetworkX · mypy

## 📄 Licencia

MIT © 2026 Mario Abarca — ver [LICENSE](LICENSE).
