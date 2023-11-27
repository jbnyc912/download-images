import streamlit as st
import requests
import os

def download_image(url):
    if url:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                # Extract image name from URL or generate a name
                image_name = url.split("/")[-1] or f"image_{len(url_list)}.jpg"
                
                # Save the image
                with open(image_name, 'wb') as file:
                    file.write(response.content)
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
    for url in url_list:
        if download_image(url):
            success_count += 1
    st.success(f'Download Complete: {success_count}/{len(url_list)} images downloaded successfully.')

# Remove the if __name__ == "__main__": main() part
