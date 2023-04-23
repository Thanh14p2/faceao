import requests,threading
id =input("nhap id:")
tk = input("nhap token")
loai=input("nhap loai")
while True:
	x = requests.get(f"https://faceslitevn.site/grap/graph.php?fbid={id}&access_token={tk}&limit=all&type={loai}").json()
print(x)
   
threads=[]
for i in range(3000):
  a = threading.Thread(target=x)
  a.start()
  


