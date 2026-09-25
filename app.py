import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
import os
import urllib.request

# Configure sleek commercial layout configurations
st.set_page_config(page_title="NGC 7212 Explorer", page_icon="🌌", layout="centered")

st.title("🌌 NGC 7212 Galactic Core Explorer")
st.write("An interactive Python data tool manipulating and visualizing raw multi-dimensional astronomical telemetry matrix arrays.")

# 1. Fallback Self-Healing Downloader: Pulls from a permanent astronomical mirror path
filename = 'ngc7212.fits'
url = 'https://githubusercontent.com'

if not os.path.exists(filename):
    with st.spinner("Downloading raw astronomical data array from telemetry node..."):
        try:
            # Set a standard browser header so the repository drops the file cleanly
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(url, filename)
            st.toast("Telemetry data synchronized!", icon="✅")
        except Exception as e:
            # Fallback Route 2: Try alternate archive branch if main mirror fluctuates
            try:
                fallback_url = 'https://githubusercontent.com'
                urllib.request.urlretrieve(fallback_url, filename)
                st.toast("Telemetry data synchronized via fallback mirror!", icon="✅")
            except Exception as fallback_error:
                st.error(f"Data pipeline download failed: {fallback_error}")

# 2. THE PYTHON SLIDER: Create the user interface slider widget
zoom_radius = st.slider(
    label="Adjust Galactic Core Slicing Radius (Matrix Pixels)",
    min_value=5,
    max_value=25,
    value=15,
    help="Slide to dynamically expand or contract the coordinate matrix slicing parameters around the center node."
)

# 3. CORE PROCESSING LOGIC: Trigger matrix slicing and plotting
if os.path.exists(filename):
    try:
        with fits.open(filename) as hdul:
            data = hdul.data
        
        # Dynamically calculate boundaries using your python slider variable
        center_x, center_y = 20, 20
        cropped_data = data[
            center_y - zoom_radius : center_y + zoom_radius,
            center_x - zoom_radius : center_x + zoom_radius
        ]
        
        # Construct the professional visualization asset
        fig, ax = plt.subplots(figsize=(6, 5))
        im = ax.imshow(cropped_data, cmap='plasma')
        fig.colorbar(im, ax=ax, label='Pixel Intensity Scale (Telemetry Counts)')
        ax.set_title(f'NGC 7212 Core - Active Matrix View ({cropped_data.shape}x{cropped_data.shape})')
        ax.axis('off') # Cleans up the outer border labels for a sleek UI
        
        # Pin the live painting onto the web application screen layout view
        st.pyplot(fig)
        
        # Display structural data insights directly to recruiters
        st.info(f"Active Grid Slicing Matrix Coordinates: [{center_y - zoom_radius}:{center_y + zoom_radius}, {center_x - zoom_radius}:{center_x + zoom_radius}]")

    except Exception as e:
        st.error(f"Data pipeline processing error: {e}")
else:
    st.warning("Waiting for telemetry file to register in system storage...")
