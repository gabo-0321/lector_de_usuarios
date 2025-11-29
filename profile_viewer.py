import streamlit as st
from beem import Hive
from beem.account import Account
import json

h = Hive(node=["https://api.hive.blog"])

st.write("# Prueba de Streamlit")

def get_account_info(username):
    
      account = Account(username, blockchain_instance=h)

      st.write(account)

      account_profile = json.loads(account["posting_json_metadata"])

      account_photo = account_profile["profile"]["profile_image"]

      st.write(account_photo)

      return account, account_profile, account_photo

col1, col2 = st.columns([3,1])
col3, col4 = st.columns([1,3])

with col1:
    
      username = st.text_input("Ingrese el nombre de la cuenta")

with col2:

      st.markdown("<br>", unsafe_allow_html=True)
      search_button = st.button(label="Buscar", type="primary", use_container_width=True)

if search_button and username:

      account, account_profile, account_photo = get_account_info(username)

      st.image(account_photo, width=250)

      st.write(account)

      with col3:
            st.write(f"Nombre: {account['name']}")

      with col4:
            st.write(f"Memo key: {account['memo_key']}")

get_account_info("gabo-0321")