This cheat sheet covers the most common patterns you'll use when working with the **Requests** library, from basic fetching to handling secure API authentication.

---

## **Requests Syntax Cheat Sheet**

### **1. Basic Request Methods**

The core functions used to interact with RESTful APIs.

* **GET (Fetch Data):** `response = requests.get(url, params={'key': 'value'})`
* **POST (Send Data):** `response = requests.post(url, json={'id': 101})`
* **PUT (Update Data):** `response = requests.put(url, data={'key': 'new_value'})`
* **DELETE (Remove Data):** `response = requests.delete(url)`

### **2. Handling the Response**

Once you have the `response` object, use these attributes to extract information.

* **Status Code:** `response.status_code` (e.g., 200 for Success, 404 for Not Found).
* **JSON Content:** `data = response.json()` (Converts response body directly to a Python Dict).
* **Raw Text:** `response.text` (Returns the body as a Unicode string).
* **Binary Content:** `response.content` (Used for downloading images or PDFs).

### **3. Common Configuration Syntaxes**

How to pass headers, timeouts, and authentication.

* **Headers:** `requests.get(url, headers={'Authorization': 'Bearer Token'})`
* **Timeouts:** `requests.get(url, timeout=5)` (Prevents the script from hanging indefinitely).
* **Basic Auth:** `requests.get(url, auth=('username', 'password'))`

---

## **Practical Examples for Your Slides**

### **Example A: Fetching & Parsing JSON**

```python
import requests

response = requests.get("https://api.example.com/data")

if response.status_code == 200:
    results = response.json()
    print(results['item_name'])

```

### **Example B: Sending Data with Headers**

```python
import requests

payload = {"title": "New Post", "body": "Content here"}
my_headers = {"Content-Type": "application/json"}

# sending a POST request with JSON payload
res = requests.post("https://api.example.com/posts", json=payload, headers=my_headers)

```

---

### **Quick Troubleshooting Tips**

* **`response.raise_for_status()`**: Call this immediately after your request; it will raise an exception if the server returned an error code (4xx or 5xx).
* **`params` vs `json**`: Use `params` for URL query strings (`?key=val`) and `json` for the body of a POST/PUT request.