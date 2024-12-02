import requests
import pandas as pd

try:
    users_api = requests.get('http://127.0.0.1:8000/users')
    users_api.raise_for_status()  
    users_api_data = users_api.json()  
    
    
    employees_api = requests.get(f'http://127.0.0.1:8000/employees/')
    employees_api.raise_for_status()  
    employees_api_data = employees_api.json() 
        

    employees_df = pd.DataFrame(employees_api_data if isinstance(employees_api_data, list) else employees_api_data.get('employees', []))
    print("The employee data frame is:\n{}".format(employees_df))

    users_df = pd.DataFrame(users_api_data if isinstance(users_api_data, list) else users_api_data.get('users', []))
    print("The user data frame is:\n{}".format(users_df))

    merged_df = pd.merge(employees_df, users_df, on='user_id', how='inner')
    merged_df.head()

    # print("the null points are: {}".format(merged_df.isnull()))
    # print("the sum of null points is: {}".format(merged_df.isnull().sum()))

    employees_df["hire_date"] = pd.to_datetime(merged_df["hire_date"], errors="coerce" )
    print(merged_df.head())














except requests.exceptions.RequestException as e:
    print(f"Error fetching data from API: {e}")
