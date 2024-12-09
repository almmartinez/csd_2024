import streamlit as st # type: ignore
import leafmap.foliumap as leafmap # type: ignore

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("Conéctese")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

# Customize page title
st.title("Carta Sinóptica Dinámica - 2024")

st.markdown(
    """
    Esta plantilla de aplicación de varias páginas muestra varias aplicaciones web interactivas creadas usando [streamlit](https://streamlit.io) and [leafmap](https://leafmap.org). Es un proyecto de código abierto y eres bienvenido a contribuir en [GitHub repository](https://github.com/opengeos/streamlit-map-template).
    """
)

st.header("Instrucciones")

markdown = """
1. Para el [GitHub repository](https://github.com/opengeos/streamlit-map-template) o [úsalo como plantilla](https://github.com/opengeos/streamlit-map-template/generate) para tu propio proyecto.
2. Personalice la barra lateral cambiando el texto y el logotipo de la barra lateral en cada archivo de Python.
3. Encuentra tu emoji favorito desde https://emojipedia.org.
4. Agregar una nueva aplicación desde `pages/` directorio con un emoji en el nombre del archivo, e.g., `1_🚀_Chart.py`.

"""

st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)
