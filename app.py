import pickle

import streamlit as st

from enums.enums import (
    max_days,
    max_option_price,
    max_strike_price,
    min_days,
    min_option_price,
    min_strike_price,
)
from service.predict import Predict
from templates.layout import streamlit_footer, streamlit_sidebar

streamlit_sidebar()
# Define the Streamlit app

ml_model = pickle.load(open("option_predictor_model.pkl", "rb"))


def isValid(data):
    if None in data.values():
        return False
    if (
        data["opening_price"] < min_strike_price
        or data["opening_price"] > max_strike_price
    ):
        return False
    if (
        data["closing_price"] < min_strike_price
        or data["closing_price"] > max_strike_price
    ):
        return False
    if (
        data["strike_price"] < min_strike_price
        or data["strike_price"] > max_strike_price
    ):
        return False
    if (
        data["option_closing_price"] < min_option_price
        or data["option_closing_price"] > max_option_price
    ):
        return False
    if data["days_to_expiry"] < min_days or data["days_to_expiry"] > max_days:
        return False
    return True


def main():
    st.set_page_config(page_title="Option Predictor Pro")
    st.header("Option Predictor Pro", divider="grey")
    description = """Option Predictor Pro forecasts striker put and call option 
    opening prices based on premarket data, aiding in strategic trading decisions.
    """
    st.markdown(description)

    # Define input fields
    call_option = st.selectbox("Select an option:", ["Call", "Put"], index=0)
    opening_price = st.number_input(
        "Opening Price",
        min_value=min_strike_price,
        max_value=max_strike_price,
        value=None,
    )
    closing_price = st.number_input(
        "Closing Price",
        min_value=min_strike_price,
        max_value=max_strike_price,
        value=None,
    )
    strike_price = st.number_input(
        "Option Strike Price",
        min_value=min_strike_price,
        max_value=max_strike_price,
        value=None,
    )
    option_closing_price = st.number_input(
        "Option Closing Price",
        min_value=min_option_price,
        max_value=max_option_price,
        value=None,
    )
    days_to_expiry = st.number_input(
        "Days Remaining For Next Expiry",
        min_value=min_days,
        max_value=max_days,
        value=None,
    )

    # Collect input data
    data = {
        "option_type": call_option,
        "opening_price": opening_price,
        "closing_price": closing_price,
        "strike_price": strike_price,
        "option_closing_price": option_closing_price,
        "days_to_expiry": days_to_expiry,
    }

    # Disable submit button if there are errors
    submit_button = st.button("Submit")

    if submit_button:
        is_valid = isValid(data)
        if not is_valid:
            st.error("Invalid Input data")
        else:
            model_object = Predict(data, ml_model)
            status, response = model_object.process_request()
            if status:
                st.success(
                    f"Option with strike price {strike_price} will open at approx. price of {response}."
                )
            else:
                st.error(response)

    st.subheader("Happy Trading :blue[!!] :sunglasses:")

    st.divider()
    st.markdown(
        '**Source Code:**<a href="https://github.com/imakshaysoni/Option_Price_Prediction_ML" target="_blank" class="icon"><img src="https://github.com/favicon.ico" style="margin-left:10px" width="30" height="30"></a>',
        unsafe_allow_html=True,
    )


main()
streamlit_footer()
