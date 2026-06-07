import streamlit as st
import sqlite3

# -------------------------
# DB FUNCTIONS
# -------------------------

def create_user_table():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()


def register_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    try:
        c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()


def login_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    data = c.fetchone()

    conn.close()

    return data


# -------------------------
# AUTH UI
# -------------------------

def auth_screen():

    create_user_table()

    st.markdown(
        "<h2 style='text-align:center;'>🔐 AI TalentMatch Login</h2>",
        unsafe_allow_html=True
    )

    menu = ["Login", "Register"]
    choice = st.radio("", menu, horizontal=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        if choice == "Login":
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")

            if st.button("Login"):
                if login_user(username, password):
                    st.session_state["user"] = username
                    st.session_state["logged_in"] = True
                    st.success("Login Successful ✅")
                    st.rerun()
                else:
                    st.error("Invalid Credentials ❌")

        else:
            new_user = st.text_input("Create Username")
            new_pass = st.text_input("Create Password", type="password")

            if st.button("Register"):
                if register_user(new_user, new_pass):
                    st.success("Account Created ✅ Now login")
                else:
                    st.error("Username already exists ❌")


def check_login():
    return st.session_state.get("logged_in", False)