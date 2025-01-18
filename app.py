import hmac
import streamlit as st

from src.instructions import instruction_panel
import src.single_dose_single_segm as sdss
import src.single_dose_mult_segm as sdms
import src.mult_dose_single_segm as mdss
import src.mult_dose_mult_segm as mdms


# Initial code from here: https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app
# Run this from >> streamlit run app.py
def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] in st.secrets[
            "passwords"
        ] and hmac.compare_digest(
            st.session_state["password"],
            st.secrets.passwords[st.session_state["username"]],
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the username or password.
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False


def main_loop():
    if not check_password():
        st.stop()

    def single_dose_single_segmentation():
        st.markdown(f"# {list(page_names_to_funcs.keys())[1]}")
        sdss.panel()

    def single_dose_multiple_segmentation():
        st.markdown(f"# {list(page_names_to_funcs.keys())[2]}")
        sdms.panel()

    def multiple_dose_single_segmentation():
        st.markdown(f"# {list(page_names_to_funcs.keys())[3]}")
        mdss.panel()

    def multiple_dose_multiple_segmentation():
        st.markdown(f"# {list(page_names_to_funcs.keys())[4]}")
        mdms.panel()

    page_names_to_funcs = {
        "Instructions": instruction_panel,
        "Single Dose Plan, Single Segmentation": single_dose_single_segmentation,
        "Single Dose Plan, Multiple Segmentations": single_dose_multiple_segmentation,
        "Multiple Dose Plans, Single Segmentation": multiple_dose_single_segmentation,
        "Multiple Dose Plans, Multiple Segmentations": multiple_dose_multiple_segmentation,
    }

    task_selection = st.sidebar.selectbox("Choose a task:", page_names_to_funcs.keys())
    page_names_to_funcs[task_selection]()


if __name__ == "__main__":
    main_loop()