import streamlit as st
import requests
import os
import zipfile
from io import BytesIO

def download_image(url, zipf):
    if url:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                # Extract image name from URL or generate a name
                image_name = url.split("/")[-1] or f"image_{len(url_list)}.jpg"
                
                # Write the image to the zip file
                zipf.writestr(image_name, response.content)
                return True
        except Exception as e:
            st.error(f"Error downloading {url}: {e}")
            return False
    return False

st.title('Bulk Image Downloader')

# Text area for URLs input
urls = st.text_area("Enter the Image URLs (one per line)")

if st.button('Download Images'):
    url_list = urls.split('\n')
    success_count = 0

    # Create a bytes buffer for the zip file
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'a', zipfile.ZIP_DEFLATED, False) as zipf:
        for url in url_list:
            if download_image(url, zipf):
                success_count += 1

    # Set the pointer of the buffer to the beginning
    zip_buffer.seek(0)

    st.success(f'Download Complete: {success_count}/{len(url_list)} images downloaded successfully.')

    # Provide a link to download the zip file
    st.download_button(
        label="Download Images as Zip",
        data=zip_buffer,
        file_name="downloaded_images.zip",
        mime="application/zip"
    )
