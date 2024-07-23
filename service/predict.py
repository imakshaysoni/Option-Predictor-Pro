import logging


class Predict:
    def __init__(self, data, model):
        self.data = data
        self.model = model

    def process_request(self):
        try:
            logging.info("Model prediction started.")
            option_type = self.data["option_type"]
            strike_price = float(self.data["strike_price"])
            option_closing_price = float(self.data["option_closing_price"])
            opening_price = float(self.data["opening_price"])
            closing_price = float(self.data["closing_price"])
            days_to_expire = int(self.data["days_to_expiry"])
            change_in_price = opening_price - closing_price
            if option_type == "Call":
                option_type = 0
            elif option_type == "Put":
                option_type = 1
            else:
                return False, "Invalid Input"

            # Defining model parameters
            model_parameters = [
                option_type,
                strike_price,
                closing_price,
                opening_price,
                change_in_price,
                option_closing_price,
                days_to_expire,
            ]
            prediction = self.model.predict([model_parameters])
            output = round(prediction[0], 2)
            logging.info(f"Model Response: {output}")
            logging.info("Model prediction finished.")
            return True, output
        except Exception as err:
            logging.error(f"Model predictor failed, Error: {err}")
            return False, err
