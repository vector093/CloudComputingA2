import requests, time

requests.post("http://localhost:5000/api/key/test1")
requests.post("http://localhost:5000/api/key/test2")
time.sleep(60)
requests.post("http://localhost:5000/api/key/test1")
requests.post("http://localhost:5000/api/key/test3")
time.sleep(60)
requests.post("http://localhost:5000/api/key/test1")
requests.post("http://localhost:5000/api/key/test4")
time.sleep(60)
requests.post("http://localhost:5000/api/key/test1")
requests.post("http://localhost:5000/api/key/test5")
time.sleep(60)
requests.post("http://localhost:5000/api/key/test1")
requests.post("http://localhost:5000/api/key/test6")
