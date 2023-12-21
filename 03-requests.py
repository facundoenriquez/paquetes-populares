import requests

# url = "https://jsonplaceholder.typicode.com/users"

# r = requests.get(url, timeout=10)
# print(
#     r.status_code,
#     r.text
# )
# r = r.json()
# for user in r:
#     print(user["name"])

# user_url = "https://jsonplaceholder.typicode.com/users/1"
# r = requests.get(user_url, timeout=10)
# print(r.json())

# url = "https://jsonplaceholder.typicode.com/users"
# user = {
#     "name": "Chanchito feliz"
# }
# r = requests.post(url, timeout=10, data=user)
# print(r.status_code)

url = "https://jsonplaceholder.typicode.com/users/2"
apikey = "12345"
headers = {
    "Authorization": f"Bearer {apikey}"
}
# user = {
#     "name": "Chanchito feliz"
# }
r = requests.delete(url, timeout=10, headers=headers)
print(r.status_code)
