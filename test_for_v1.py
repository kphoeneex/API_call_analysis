import requests
import string
import pandas as pd
import time
import os

url="http://35.200.185.69:8000/v1/autocomplete?query="
rows=[]
rate_limit=100
total_count=0
request_count=0
execution_count=0

def fetch_results(query):
    global request_count,total_count,execution_count
    if request_count>=rate_limit:
        print("Limit Reached,Waiting...")
        time.sleep(60)
        request_count=0

    response=requests.get(url+query,timeout=10)
    request_count+=1

    if response.status_code==429:
        print("Limit Reached,Waiting...")
        time.sleep(60)
        return fetch_results(query)
    execution_count+=1
    data=response.json()
    results=data.get("results",[])
    count=data.get("count",0)
    total_count+=count
    return results,count
        

for i in string.ascii_lowercase:
    for j in string.ascii_lowercase:
        current_combination = i + j

        results,count=fetch_results(i+j)
        rows.extend(results)

        if results and count>=10:
            last_element=results[-1]
            if len(last_element)>=3:
                third_char=last_element[2]

            for ch in range(ord(third_char),ord('z')+1):
                new_char=chr(ch)
                deep_results,deep_counts = fetch_results(i + j + new_char)
                rows.extend(results)

        print(f"Completed {i}{j},executed {execution_count} times and collected {total_count} words so far.")
df=pd.DataFrame({"Words":rows})
df.to_excel("output_v1.xlsx",index=False)
print(f"Saved to output_v1.xlsx. Total words count: {total_count}. Total execution count :{execution_count}")

