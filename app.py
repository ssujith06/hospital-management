import streamlit as st
from auth import login, register
from database import add_patient, get_patients

def main():
    st.sidebar.title("🏥 Hospital Management")
    menu = ["Home", "Login", "Register", "Add Patient", "View Patients"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.title("🏥 Hospital Patient Management System")
        st.write("Manage child patient records efficiently.")

    elif choice == "Login":
        user = login()
        if user:
            st.session_state["user"] = user

    elif choice == "Register":
        register()

    elif choice == "Add Patient":
        if "user" in st.session_state:
            st.title("Add Patient Record")
            name = st.text_input("Child's Name")
            age = st.number_input("Age", min_value=0, max_value=18, step=1)
            date_of_visit = st.date_input("Date of Visit")
            diagnosis = st.text_area("Diagnosis")
            treatment = st.text_area("Treatment")
            doctor = st.session_state["user"]

            if st.button("Save Record"):
                add_patient(name, age, str(date_of_visit), diagnosis, treatment, doctor)
                st.success("Patient record saved!")

        else:
            st.warning("You need to log in first.")

    elif choice == "View Patients":
        st.title("View Patient Records")
        patients = get_patients()
        if patients:
            for p in patients:
                st.write(f"**Name:** {p[1]}")
                st.write(f"**Age:** {p[2]}")
                st.write(f"**Date of Visit:** {p[3]}")
                st.write(f"**Diagnosis:** {p[4]}")
                st.write(f"**Treatment:** {p[5]}")
                st.write(f"**Doctor:** {p[6]}")
                st.markdown("---")
        else:
            st.warning("No records found.")

if __name__ == "__main__":
    main()
