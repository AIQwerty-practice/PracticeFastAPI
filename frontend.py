import streamlit as st
import requests

st.set_page_config(page_title="Task Manager UI", page_icon="📝")
st.title("📝 Task Manager")

# Address of your Backend
API_URL = "https://practicefastapi.onrender.com"

# --- SIDEBAR: ADD NEW TASK ---
with st.sidebar:
    st.header("Create Task")
    with st.form("add_form", clear_on_submit=True):
        new_title = st.text_input("Title")
        new_desc = st.text_area("Description")
        new_priority = st.selectbox("Priority", ["low", "medium", "high"], index=1)
        submit = st.form_submit_button("Add Task")

        if submit and new_title:
            payload = {"title": new_title, "description": new_desc, "priority": new_priority}
            requests.post(API_URL, json=payload)
            st.rerun()

# --- MAIN AREA: VIEW TASKS ---
try:
    # 1. Get tasks from Backend
    response = requests.get(API_URL)
    tasks = response.json()

    # 2. Display them in a nice list
    for task in tasks:
        with st.container(border=True):
            col1, col2 = st.columns([4, 1])
            
            # Left side: Task Info
            status = "✅" if task["completed"] else "⏳"
            col1.subheader(f"{status} {task['title']}")
            col1.caption(f"Priority: {task['priority'].upper()} | Created: {task['created_at']}")
            col1.write(task["description"])

            # Right side: Actions
            if not task["completed"]:
                if col2.button("Done", key=f"done_{task['id']}"):
                    requests.patch(f"{API_URL}/{task['id']}", json={"completed": True})
                    st.rerun()
            
            if col2.button("🗑️", key=f"del_{task['id']}"):
                requests.delete(f"{API_URL}/{task['id']}")
                st.rerun()

except Exception:
    st.error("Cannot connect to Backend. Is 'uvicorn main:app' running?")
