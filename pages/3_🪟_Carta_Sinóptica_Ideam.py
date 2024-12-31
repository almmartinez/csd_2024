import streamlit as st  # type: ignore
import folium  # type: ignore
from streamlit_folium import st_folium  # type: ignore # Asegúrate de instalar streamlit-folium
from folium.plugins import Draw  # type: ignore

st.set_page_config(layout="wide")

markdown = """
Plantilla de Streamlit en
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("Conéctese")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Carta sinóptica Ideam")

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

        # Añadir la imagen al mapa con los límites iniciales
        image_path = "Carta_sinoptica_20241014_1425HLC.jpg"
        bounds=[[-22.30, -103.0], [48.10, 5.25]]
        image_overlay = folium.raster_layers.ImageOverlay(
            name="Carta Sinóptica",
            image=image_path,
            bounds=bounds,
            opacity=0.3
        )
        image_overlay.add_to(m)

        # Añadir control de capas
        folium.LayerControl().add_to(m)

        # Añadir Draw Control
        draw = Draw(
            draw_options={
                'polyline': True,
                'polygon': True,
                'circle': True,
                'rectangle': True,
                'marker': True,
                'circlemarker': True,
            },
            edit_options={
                'edit': True,
                'remove': True,
            }
        )
        draw.add_to(m)

# Mostrar el mapa en Streamlit
st_folium(m, width=1400, height=700)
