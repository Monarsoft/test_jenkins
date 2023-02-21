import requests

class GetText:
	def get_text(self):
		response = requests.get("http://baidu.com")
		print(response.stauts_code)
		
GetText().get_text()
