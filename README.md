Autocomplete API Data Fetcher
This script fetches autocomplete query results from an API and saves the collected data into an Excel file.

Prerequisites
Ensure you have the following installed on your system:
Python 3.x
Required Python packages:
requests
pandas
openpyxl
You can install the required dependencies using:
pip install requests pandas openpyxl

How to Run the Script
Clone or download this repository.
Open a terminal and navigate to the script's directory.
Run the script using:
python test.py

How the Script Works
The script generates queries using a combination of digits (0-9) and lowercase letters (a-z).
It sends requests to the API endpoint: http://35.200.185.69:8000/v2/autocomplete?query=<query>.
The API response is parsed to extract results and count.
If the API rate limit is reached (status code 429), the script waits for 60 seconds before retrying.
The retrieved words are stored in a Pandas DataFrame.
The final dataset is saved as output2.xlsx.

Output
The script prints real-time updates on the console.
The collected words are stored in output2.xlsx.
Example Console Output

Completed 00, called 1, collected 50 words so far.
Completed 01, called 2, collected 100 words so far.
...
Saved to output2.xlsx. Total words count: 5000

Notes
The API rate limits might delay execution.
Modify the arr list to include more characters if needed.
The script handles API rate limits automatically.
License

This project is for educational purposes. Modify and use it as needed.
