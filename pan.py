import pandas as pd
import math

def clean_phone_number(phone_number):
    # Apply cleaning operations
    cleaned_number = str(phone_number)
    if len(cleaned_number) > 10:
     print(cleaned_number[2:])
     cleaned_number = cleaned_number[2:]
    else:
     print(cleaned_number)

    # if math.isnan(cleaned_number):
    #   cleaned_number = '8888888888'
      
      

    return cleaned_number


data = pd.read_csv('enquiry.csv')

print(data["Phone"])

print(data.iloc[:, 5].to_string())

data.iloc[:, 5] = data.iloc[:, 5].apply(clean_phone_number)

data.to_csv('cleaned_data.csv', index=False)


