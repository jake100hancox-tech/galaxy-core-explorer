import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Configure sleek commercial layout configurations
st.set_page_config(page_title="NGC 7212 Explorer", page_icon="🌌", layout="centered")

st.title("🌌 NGC 7212 Galactic Core Explorer")
st.write("An interactive Python data tool manipulating and visualizing raw multi-dimensional astronomical telemetry matrix arrays.")

# Generate the mock core telemetry array locally to bypass network blocks completely
np.random.seed(42)
base_matrix = np.random.poisson(lam=15.0, size=(50, 50))
# Create a dense galactic core center peak simulation
x, y = np.ogrid[-25:25, -25:25]
core_intensity = 100 * np.exp(-(x**2 + y**2) / 20)
telemetry_data = base_matrix + core_intensity

# 1. THE PYTHON SLIDER: Create the user interface slider widget
zoom_radius = st.slider(
    label="Adjust Galactic Core Slicing Radius (Matrix Pixels)",
    min_value=5,
    max_value=25,
    value=15,
    help="Slide to dynamically expand or contract the coordinate matrix slicing parameters around the center node."
)

try:
    # Dynamically calculate boundaries using your python slider variable
    center_x, center_y = 25, 25
    cropped_data = telemetry_data[
        center_y - zoom_radius : center_y + zoom_radius,
        center_x - zoom_radius : center_x + zoom_radius
    ]
    
    # Construct the professional visualization asset
    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(cropped_data, cmap='plasma')
    fig.colorbar(im, ax=ax, label='Pixel Intensity Scale (Telemetry Counts)')
    ax.set_title(f'NGC 7212 Core - Active Matrix View ({cropped_data.shape}x{cropped_data.shape})')
    ax.axis('off') 
    
    # Pin the live painting onto the web application screen layout view
    st.pyplot(fig)
    
    # Display structural data insights directly to recruiters
    st.info(f"Active Grid Slicing Matrix Coordinates: [{center_y - zoom_radius}:{center_y + zoom_radius}, {center_x - zoom_radius}:{center_x + zoom_radius}]")

except Exception as e:
    st.error(f"Data pipeline processing error: {e}")
