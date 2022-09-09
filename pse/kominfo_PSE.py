# Importing the http.client module.
import http.client

# Creating a connection to the server.
conn = http.client.HTTPSConnection("pse.kominfo.go.id")

# A dictionary of headers.
headersList = {
    "Accept": "*/*",
}

# A placeholder for the body of the request.
payload = ""

# Sending a GET request to the server.
conn.request("GET", "/static/json-static/ASING_TERDAFTAR/0.json?page[page]=1&page[limit]=10&filter[search_term]=", payload, headersList)
response = conn.getresponse()
result = response.read()

# Printing the result of the request.
print(result.decode("utf-8"))