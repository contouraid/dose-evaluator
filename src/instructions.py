import streamlit as st

def instruction_panel():
    st.write("# Dose Evaluator:")
    st.sidebar.success("Select an option above.")

    st.markdown(
        """
        This web-app evaluates the dosimetric impact in the following scenarios:

        1. Single Dose plan, single segmentation - displaying DVH and allied metrics.
        2. Single Dose plan, multiple alternative segmentations.
        3. Multiple dose plans based on multiple alternative segmentations.
        4. Multiple dose plans based on a single segmentation.

        This lives here: [dose-evaluator.streamlit.app](https://dose-evaluator.streamlit.app).

        ### Want to learn more?

        - Check out [www.contouraid.com](https://www.contouraid.com) for more info
        - Reach out back to us at [www.contouraid.com/contact](https://www.contouraid.com/contact)
    """
    )