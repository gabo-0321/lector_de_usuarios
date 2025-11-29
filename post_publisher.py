import streamlit as st
from beem import Hive
import json, os
from dotenv import load_dotenv

load_dotenv()

posting_key = os.getenv("POSTING_KEY")

h = Hive(node=["https://api.hive.blog"], keys=[posting_key])

st.markdown('# Publicador de Posts')

with st.form("my_form"):

    post_author = st.text_input("Ingrese el nombre de la cuenta:")

    post_title = st.text_input("Ingrese el titulo del post:")

    post_content = st.text_area("Ingrese el contenido del post:")

    post_image = st.file_uploader("Ingrese una imagen (solo vista previa)")

    post_image_url = st.text_input("URL de la imagen (opcional):")

    post_tags = st.text_input("Ingrese los tags del post (separados por comas):")

    sumbit_button = st.form_submit_button(label="Publicar", use_container_width=True)

if sumbit_button:
    if post_image is not None:
        st.image(post_image, caption="Vista previa:", use_container_width=False)

    tags_list = []
    if post_tags:
        parts = [t.strip() for t in post_tags.split(',')]
        for t in parts:
            if not t:
                continue
            t = t.lower().lstrip('#').replace('', '')
            if t and t not in tags_list:
                tags_list.append(t)

    images_meta = [post_image_url] if post_image_url else []

    post = h.post(
        title=post_title,
        body=post_content,
        author=post_author,
        json_metadata=json.dumps({"tags": tags_list, "image": images_meta}),
        blockchain_instance=h
    )

    st.success("Post publicado correctamente")

    st.write(f"https://peakd.com/@{post_author}")
