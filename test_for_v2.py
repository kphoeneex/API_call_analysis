import requests
import string
import pandas as pd
import time

url="http://35.200.185.69:8000/v2/autocomplete?query="
arr=list(string.digits)+list(string.ascii_lowercase)
rows=[]
rate_limit=100
total_count=0
request_count=0

def fetch_results(query):
    global request_count,total_count

    response=requests.get(url+query,timeout=10)

    if response.status_code==429:
        print("Limit Reached,Waiting...")
        time.sleep(60)
        return fetch_results(query)
    
    request_count+=1
    data=response.json()
    results=data.get("results",[])
    count=data.get("count",0)
    total_count+=count
    return results,count



for i in arr:
    for j in arr:
        results,count=fetch_results(i+j)
        rows.extend(results)

        print(f"Completed {i}{j},called {request_count}, collected {total_count} words so far.")
df=pd.DataFrame({"Words":rows})
df.to_excel("output2.xlsx",index=False)
print(f"Saved to output2.xlsx. Total words count: {total_count}")

