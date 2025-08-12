# # import requests

# # # GET Request
# # response = requests.get("http://127.0.0.1:8000/")
# # print("GET Response:", response.json())

# # # POST Request
# # data = {
# #     "name": "Notebook",
# #     "price": 49.99
# # }
# # response = requests.post("http://127.0.0.1:8000/item/", json=data)
# # print("POST Response:", response.json())


# import requests
# from datetime import datetime

# # GET Request
# try:
#     response = requests.get("http://127.0.0.1:8000")
#     response.raise_for_status()
#     print("GET Response:", response.json())
# except requests.RequestException as e:
#     print("GET Request failed:", e)


# url = "http://127.0.0.1:8000/employee/"

# data = {
#     "Employee_id": 23,
#     "Employee_name": "Anand",
#     "Designation": "Software Engineer",
#     "Login_time": datetime.utcnow().isoformat(),
#     "logout_time": datetime.utcnow().isoformat()
# }

# try:
#     response = requests.post(url, json=data)
#     response.raise_for_status()
#     print("POST Response:", response.json())
# except requests.RequestException as e:
#     print("POST Request failed:", e)


import requests
from datetime import datetime

# GET request
response = requests.get("http://127.0.0.1:8000/")
print("GET Response:", response.json())

# POST request
data = {
    "Employee_id": 23,
    "Employee_name": "Anand",
    "Designation": "Software Engineer",
    "login_time": datetime.utcnow().isoformat(),
    "logout_time": datetime.utcnow().isoformat()
}

try:
    response = requests.post("http://127.0.0.1:8000/employee/", json=data)
    response.raise_for_status()
    print("POST Response:", response.json())
except requests.exceptions.RequestException as e:
    print("POST Request failed:", e)
