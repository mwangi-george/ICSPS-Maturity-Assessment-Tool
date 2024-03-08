import streamlit as st

# Function to collect user details


def collect_user_details():
    name = st.text_input("Name:")
    organization = st.text_input("Organization:")
    return name, organization

# Main function


def main():
    users = []

    st.title("User Information")

    # Add users dynamically
    button_counter = 0  # Counter to generate unique keys
    while st.button(f"Add User {button_counter}"):
        user_details = collect_user_details()
        users.append(user_details)
        button_counter += 1

    # Display user details
    st.title("User Details")
    for i, (name, organization) in enumerate(users, start=1):
        st.write(f"User {i}:")
        st.write(f"Name: {name}")
        st.write(f"Organization: {organization}")
        st.write("")


if __name__ == "__main__":
    main()
