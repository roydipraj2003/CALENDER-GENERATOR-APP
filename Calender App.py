import streamlit as st
import calendar

# Title of the app
st.title("Calender Generator App")

st.subheader("Welcome to the **Calendar Generator App**! 🎉  ")
# Add a description for the app
st.write(
    """
    This app allows you to quickly view and download a yearly calendar.  
    Simply enter the desired year below and click **Show Calendar** to generate it.  
    You can also download the calendar in a text format for offline use.  
    """
)


# Input box to enter the year
year = st.number_input("Enter a year:", min_value=1, max_value=9999, value=2024, step=1)

# Button to display the calendar
if st.button("Show Calendar"):
    st.write(f"### Calendar for the year {year}")
    # Generate the calendar for the entered year
    year_calendar = calendar.TextCalendar().formatyear(year, 2, 1, 1, 3)
    # Display the calendar
    st.text(year_calendar)
    # Create a downloadable file
    file_name = f"calendar_{year}.txt"
    with open(file_name, "w") as file:
        file.write(year_calendar)

    # Provide a download button
    with open(file_name, "r") as file:
        st.download_button(
            label="Download Calendar",
            data=file,
            file_name=file_name,
            mime="text/plain"
        )
st.markdown(
    f"""</style>
        <div class="footer">
            &copy; {2024} Created by Darshanikanta
        </div>
        """,
        unsafe_allow_html=True)