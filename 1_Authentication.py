import streamlit as st
import os
import requests
from dotenv import load_dotenv
from streamlit_supabase_auth import login_form, logout_button

hide_sidebar = """
<style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            display: none;
        }
</style>
"""

def main():
    session_state = st.session_state
    st.title("Login")
    st.header("Auth using Supabase")
    load_dotenv()
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_api_key = os.getenv("SUPABASE_KEY")
    session = login_form(
        url=supabase_url,
        apiKey=supabase_api_key,
        providers=["apple", "facebook", "github", "google"],
    )

    #st.write(session)
    if not session:
        print('USER NOT IN SESSION, LOGIN TO CONTINUE')
        st.markdown(hide_sidebar, unsafe_allow_html=True)
        #st.switch_page('1_Authentication.py')
        return
    else:
        print('USER SESSION EXIST - redirecting to HOMEPAGE')
        if 'id' not in session_state:
            session_state.id = session['user']['id']
            session_state.email = session['user']['email']
            st.switch_page('pages/2_🏠_HomePage.py')
        with st.sidebar:
            st.write(f"Welcome  - {session_state.email}")
            logout_button()


def clearSessionState():
    prev_session_state = st.session_state
    if hasattr(st, 'prev_session_state'):
        print('Old Session state Exist -- Clearing')
        prev_session_state.id = None
        prev_session_state.email = None
        print('Old Session state Cleared.')

if __name__ == "__main__":
    clearSessionState()
    main()
