import xmlrpc.client

url = 'http://localhost:8069/'
db = 'shweyeeodoo_db'
username ='shweyeewinmaung@gmail.com'
password='odoouser'

common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid=common.authenticate(db,username,password,{})
if uid:
	print(f"Authenticated with UID:{uid}")
else:

	print("Failed")

models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')