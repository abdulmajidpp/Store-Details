# Customer Details Fetcher

This is a simple Python application built using Tkinter and pandas, which allows you to input a `Customer ID` and fetch relevant details from an Excel dataset. The details include information like `Unit Price`, `Discount`, `Shipping Cost`, `Quantity Ordered`, `Customer Name`, and `Product Name`.

## Features

- User can input a `Customer ID` to search for.
- Displays corresponding details like `Customer ID`, `Unit Price`, `Discount`, `Shipping Cost`, `Quantity Ordered`, `Customer Name`, and `Product Name`.
- Handles empty or incorrect `Customer ID` input by showing a message if no results are found.
- Built with Tkinter for the GUI and pandas for reading and processing the Excel data.

## Requirements

- Python 3.x
- pandas
- openpyxl (for reading `.xlsx` files)
- Tkinter (usually included with Python, but make sure it's installed)


Make sure you have an Excel file with the correct data, such as `SuperStoreUS-2015.xlsx`, or adjust the path in the code to point to your own file.

## Usage

1. Run the application:
    ```bash
    python app.py
    ```
2. Enter a `Customer ID` in the input field.
3. Click on the "Click here" button to fetch the details for that customer.
4. The relevant information will be displayed below the input field.

## Example

If you enter a valid `Customer ID`, you will see the following data displayed:

- Customer ID: `12345`
- Unit Price: `50.00`
- Discount: `0.1`
- Shipping Cost: `5.00`
- Quantity Ordered: `2`
- Customer Name: `John Doe`
- Product: `Laptop`

## Contributing

Feel free to fork the repository, make changes, and create pull requests. All contributions are welcome!

