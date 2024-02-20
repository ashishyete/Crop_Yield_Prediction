import streamlit as st
from streamlit_supabase_auth import logout_button

session_state = st.session_state

if hasattr(st,'session_state'):

    if hasattr(st.session_state, 'id') and hasattr(st.session_state, 'email'):
        print("session_state is initialized with id and email - 10_Help")
    else:
        print("session_state is not fully initialized - 10_Help")
        st.warning("Please Login to Continue...")
        login_path = "/"
        st.markdown(f'<a href="{login_path}" target="_self"> Login </a>', unsafe_allow_html=True)
        st.stop()
else:
    st.warning('Session_state not initialized. - 10_Helps')

st.title("User Guidance")

tab1, tab2 = st.tabs(["Help", "Submit Feedback"])

with tab1:
    # Define the content for the help section
    help_content = """
    ### Crop Yield Prediction Help

    Welcome to the Crop Yield Prediction app! This application assists in estimating crop production and making informed decisions related to agriculture.

    Here's a quick guide on how to use the app:

    1. **Navigate Sections:**
       - Use the navigation buttons on the sidebar to explore different sections like 'About,' 'Dataset,' 'Descriptive', 'Exploration', 'Preprocessing,' 'Modeling,' and 'Report.'

    2. **Understanding Crop Yield Prediction:**
       - The app provides insights into the significance of accurate crop yield prediction, influencing factors, and the methods employed for precise forecasts.

    3. **Performing Crop Yield Prediction:**
       - Each section is designed to guide you through different aspects of the crop yield prediction process, from understanding the dataset to preprocessing, modeling, and generating reports.

    4. **Help Button:**
       - Click the 'Help' button anytime for assistance and tips on using specific features in each section.

    Feel free to explore and make use of the app for your agricultural insights!


    """

    # Custom CSS to style the Help button
    custom_css = """
    <style>
    #help_button {
        float: right;
        position: topRight;
        top: 1000px;
        right: 1000px;
        z-index: 1000;
        padding: 10px;
        background-color: #f44336;
        border: 1px solid #dcdcdc;
        border-radius: 5px;
        cursor: pointer;
        text-align: center;
    }
    </style>
    """

    # Apply custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)

    # Create a Help button with Markdown
    help_button_html = "<div id='help_button'>Help</div>"
    help_button_clicked = st.markdown(help_button_html, unsafe_allow_html=True)

    # Display help content when the button is clicked
    if help_button_clicked.button("Help"):
        with st.expander("Help Section"):
            st.markdown(help_content)


with tab2:
    st.header("Submit Your Feedback")

    feedback_form = """
    <form action="https://formsubmit.co/NYete@my.gcu.edu" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your feedback here"></textarea>
         <button type="submit">Send</button>
    </form>
    """

    st.markdown(feedback_form, unsafe_allow_html=True)


    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style/style.css")

with st.sidebar:
    st.write(f"Welcome  - {session_state.email}")
    logout_button()

col1, col2, col2, col4, col5 = st.columns(5)

with col1:

    st.page_link("pages/8_📜_Report.py", label="Previous", icon="⬅")

with col5:

    st.page_link("pages/2_🏠_HomePage.py", label="Next", icon="➡")




