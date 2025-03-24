
The intuition is to start exploring the API by using random strings. First, I tried random lowercase alphabets, then uppercase, then used numbers and special characters.

For V1, only the lowercase alphabets were used in the returned string.

For V2, along with lowercase alphabets, numbers were also present.

For V3, lowercase alphabets, numbers, as well as a few special characters, were present. After exploring further, there were four special characters: ['.', ' ', '+', '-'].

Now that we know what type of strings are present, we can explore other constraints.
For V1, the number of strings returned per call was limited to 10, and there was a limit of 100 calls per minute.

For V2, the number of strings returned per call was 12, and there was a limit of 50 calls per minute.

For V3, the number of strings returned per call was increased to 15, and there was a limit of 80 calls per minute.

Other Inferences:
For V1, there were multiple instances where just running two nested loops was not enough, as the number of strings was frequently outside the set return limit. A third loop had to be initialized, starting from the position where the last string ended. However, this approach increases the complexity of the code by a lot.

For V2, the majority of the results returned had the number of strings well within the boundary of 12. As a result, just two loops were enough to quickly process through all available options.

For V3, there was a similar observation. The majority of the results returned had the number of strings well within the boundary of 15. As a result, just two loops were enough to quickly process through all available options.

While having an additional loop in both V2 and V3 will improve precision, it will vastly increase the number of API calls, even if we apply the constraint that the returned result should have at least 15 to proceed further.

So, between improved accuracy and improved timing:

For V1, since many values fall outside the limit, we chose to use an additional loop.

For V2 and V3, we only used two loops to avoid too many redundant calls. However, this may result in missing some values.


------------------------**************************--------------------------


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
