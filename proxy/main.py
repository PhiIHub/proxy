import requests
import random
import time

class setup_proxy():
	
	def get_new_proxies():
		def format_proxy_data(proxy_data):
			formatted_data = []
			for proxy in proxy_data.splitlines():
				formatted_proxy = {
					'ip': proxy.split(":")[0],
					'port': proxy.split(":")[1],
					'protocol': 'http'
				}
				if formatted_proxy['ip'].split(".")[0] in ["3", "45", "46", "47"]:
					formatted_data.append(formatted_proxy)
			return formatted_data
		response = requests.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt")
		proxy_data = response.text
		formatted_proxies = format_proxy_data(proxy_data)
		return formatted_proxies
		
	@staticmethod
	def get_working_proxy():
		proxies = setup_proxy.get_new_proxies()
		finish = 0
		while finish == 0:
			try:
				proxy = random.choice(proxies)
				response = requests.get("http://ident.me/", proxies={'http': f"http://{proxy['ip']}:{proxy['port']}"}, timeout=0.4)
				if proxy['ip'] == response.text:
					finish = 1
			except:
				pass
		return proxy
		
	def __init__(self):
		print("finding proxy...")
		self.proxy = setup_proxy.get_working_proxy()
	
	def send_request(self, url, method, headers={}, cookies={}, data={}):
		
		proxy = self.proxy
		try:
			if method == "POST":
				response = requests.post(url, headers=headers, cookies=cookies, data=data, proxies={'http': f"http://{proxy['ip']}:{proxy['port']}"})
				return response
			elif method == "GET":
				response = requests.get(url, headers=headers, cookies=cookies, data=data, proxies={'http': f"http://{proxy['ip']}:{proxy['port']}"})
				return response
			elif method == "OPTIONS":
				response = requests.options(url, headers=headers, cookies=cookies, data=data, proxies={'http': f"http://{proxy['ip']}:{proxy['port']}"})
				return response
			elif method == "PUT":
				response = requests.put(url, headers=headers, cookies=cookies, data=data, proxies={'http': f"http://{proxy['ip']}:{proxy['port']}"})
				return response
			elif method == "DELETE":
				response = requests.delete(url, headers=headers, cookies=cookies, data=data, proxies={'http': f"http://{proxy['ip']}:{proxy['port']}"})
				return response
			elif method == "PATCH":
				response = requests.patch(url, headers=headers, cookies=cookies, data=data, proxies={'http': f"http://{proxy['ip']}:{proxy['port']}"})
				return response
			elif method == "HEAD":
				response = requests.head(url, headers=headers, cookies=cookies, data=data, proxies={'http': f"http://{proxy['ip']}:{proxy['port']}"})
				return response
			elif method == "TRACE":
				response = requests.trace(url, headers=headers, cookies=cookies, data=data, proxies={'http': f"http://{proxy['ip']}:{proxy['port']}"})
				return response
			elif method == "CONNECT":
				response = requests.connect(url, headers=headers, cookies=cookies, data=data, proxies={'http': f"http://{proxy['ip']}:{proxy['port']}"})
				return response
			else:
				return None
		except Exception as e:
			print(e)
