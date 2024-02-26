import streamlit as st
import random

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Main function to run the application
def main():
    # Set page title and page layout
    st.set_page_config(page_title="Dice Rolling Simulator", page_icon="🎲", layout="wide")

    # Add title and description with styling
    st.title("🎲 Dice Rolling Simulator")
    st.markdown(
        """
        <style>
        .big-font {
            font-size: 36px !important;
        }
        .highlight {
            background-color: #f0f0f0;
            padding: 10px;
            border-radius: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<p class='big-font'>Welcome to the Dice Rolling Simulator!</p>", unsafe_allow_html=True)
    st.markdown(
        "<p class='highlight'>Select 'Roll Dice' from the sidebar to roll the dice.</p>",
        unsafe_allow_html=True,
    )

    # Add sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Roll Dice"])

    # Display selected page content
    if page == "Home":
        st.write("### About")
        st.markdown("""
        This is a simple web application built with Streamlit to simulate rolling a six-sided dice.
        Click on 'Roll Dice' from the sidebar to roll the dice and see the result.

        **How to Use:**
        - Select 'Roll Dice' from the sidebar.
        - Click on the 'Roll the Dice' button to roll the dice.
        - The result will be displayed on the screen.

        Enjoy rolling the dice!
        """)

    elif page == "Roll Dice":
        st.header("🎲 Roll the Dice")
        roll_button = st.button("Roll the Dice")

        if roll_button:
            dice_roll = roll_dice()
            st.subheader(f"You rolled a {dice_roll}!")

# Run the main function
if __name__ == "__main__":
    main()