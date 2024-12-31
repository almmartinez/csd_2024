import streamlit as st  # type: ignore
import folium  # type: ignore
from streamlit_folium import st_folium  # type: ignore # Asegúrate de instalar streamlit-folium

st.set_page_config(layout="wide")

markdown = """
Plantilla de Streamlit en
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("Conéctese")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Comparación Cartas Sinópticas")

with st.expander("See source code"):
    with st.echo():
        # Crear el mapa base
        m = folium.Map(location=[10, -80], zoom_start=3)

        # Añadir la imagen como capa
        folium.raster_layers.ImageOverlay(
            name='18Z Image',
            image='https://www.nhc.noaa.gov/tafb/USA_18Z.gif',
            bounds=[[-36.50, -169.0], [59.00, 4.7]],
            opacity=0.6
        ).add_to(m)

# Mostrar el mapa en Streamlit
st_folium(m, width=1400, height=700)

folium.LayerControl().add_to(m)

