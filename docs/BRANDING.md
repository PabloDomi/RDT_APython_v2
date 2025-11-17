# Vyte Branding Guide

Este documento describe cómo usar los logos y recursos de marca de Vyte.

## 📁 Archivos de Logo

Todos los logos están disponibles en la carpeta `images/`:

### Logo Principal - Transparente

- **Archivo**: `Logo_V_Transparente.png`
- **Uso**: README, documentación, presentaciones
- **Fondo**: Transparente (ideal para cualquier fondo)

### Logo Blanco y Negro

- **Archivo**: `Logo_V_ByN.png`
- **Uso**: Documentos impresos, casos donde se necesita contraste alto
- **Fondo**: Transparente

### Logo Cuadrado

- **Archivo**: `Logo_V_cuadrado.png`
- **Uso**: Perfiles de redes sociales, avatares
- **Tamaño**: Relación 1:1

### Favicon

- **Archivo**: `Logo_V_Favicon.png`
- **Uso**: Favicon para sitios web, documentación
- **Tamaño**: 16x16, 32x32, 64x64 píxeles

### Isotipo

- **Archivo**: `Logo_V_isotipo.png`
- **Uso**: Icono de aplicación, watermarks pequeños
- **Tamaño**: Versión simplificada del logo

## 🎨 Uso en Diferentes Plataformas

### GitHub

1. **Repositorio Social Preview**:

   - Settings → Social preview → Upload image
   - Usa: `Logo_V_cuadrado.png`
   - Tamaño recomendado: 1280x640px

1. **Avatar del Proyecto**:

   - Usa: `Logo_V_cuadrado.png` o `Logo_V_isotopo.png`

1. **README.md**:

   ```markdown
   <p align="center">
     <img src="images/Logo_V_Transparente.png" alt="Vyte Logo" width="400"/>
   </p>
   ```

### PyPI

- El README.md se muestra automáticamente en PyPI
- El logo aparecerá en: https://pypi.org/project/vyte/

### Documentación (MkDocs/Sphinx)

```yaml
# mkdocs.yml
theme:
  logo: images/Logo_V_isotipo.png
  favicon: images/Logo_V_Favicon.png
```

### CLI

Para mostrar el logo en la terminal:

```python
from rich.console import Console
from rich.panel import Panel

console = Console()
console.print(
    Panel("[cyan]VYTE[/cyan]", title="🚀 Rapid Development Tool", border_style="cyan")
)
```

### Redes Sociales

#### Twitter/X Card

```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Vyte - Rapid Development Tool">
<meta name="twitter:description" content="Professional API project generator for Python">
<meta name="twitter:image" content="https://raw.githubusercontent.com/PabloDomi/Vyte/main/images/Logo_V_cuadrado.png">
```

#### Open Graph (Facebook, LinkedIn)

```html
<meta property="og:title" content="Vyte - Rapid Development Tool">
<meta property="og:description" content="Professional API project generator for Python">
<meta property="og:image" content="https://raw.githubusercontent.com/PabloDomi/Vyte/main/images/Logo_V_cuadrado.png">
<meta property="og:url" content="https://github.com/PabloDomi/Vyte">
```

## 🎯 Recomendaciones de Uso

### ✅ Hacer

- Mantener proporciones originales del logo
- Usar suficiente espacio en blanco alrededor
- Usar versión transparente en fondos de colores
- Usar versión B&N para impresiones monocromáticas

### ❌ No Hacer

- No distorsionar o estirar el logo
- No cambiar los colores originales
- No añadir efectos (sombras, bordes, gradientes)
- No rotar el logo
- No colocar texto muy cerca del logo

## 📐 Tamaños Recomendados

| Plataforma            | Archivo          | Tamaño Recomendado    |
| --------------------- | ---------------- | --------------------- |
| GitHub Social Preview | Cuadrado         | 1280x640px            |
| GitHub Avatar         | Cuadrado/Isotipo | 460x460px             |
| PyPI                  | Transparente     | ~400px ancho          |
| Twitter Card          | Cuadrado         | 1200x675px            |
| Favicon               | Favicon          | 16x16, 32x32, 64x64px |
| Documentación         | Isotipo          | 128x128px             |

## 🔗 URLs de Recursos

- **GitHub**: https://github.com/PabloDomi/Vyte
- **PyPI**: https://pypi.org/project/vyte/
- **Documentación**: (próximamente)
- **Logo Raw**: https://raw.githubusercontent.com/PabloDomi/Vyte/main/images/

## 📄 Licencia

Los logos de Vyte son propiedad de PabloDomi y están protegidos bajo la misma licencia MIT del proyecto.
