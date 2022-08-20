import http.client

conn = http.client.HTTPSConnection("pse.kominfo.go.id")

headersList = {
    "Accept": "*/*",
}

payload = ""

conn.request("GET", "/static/json-static/ASING_TERDAFTAR/0.json?page[page]=1&page[limit]=10&filter[search_term]=", payload, headersList)
response = conn.getresponse()
result = response.read()

print(result.decode("utf-8"))