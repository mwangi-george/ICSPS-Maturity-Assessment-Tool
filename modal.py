import streamlit as st
from streamlit_modal import Modal
modal = Modal(key="Demo Key", title="Validation", max_width=500, padding=10)

open_modal = st.button(label='button', key="btkfjsdfh")
if open_modal:
    with modal.container():
        st.write(
            "Data for country x for review period x already exists! Would you like to replace it with this data?")
        st.button(label="Yes", key="resubmit", type="primary")
        st.button(label="No", key="dont_submit", type="primary")
