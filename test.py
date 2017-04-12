myString = "GET /hello HTTP/1.1"

A = "class http_response :def __init__(self, response):self.response = response.split(' ')self.type = self.response[0]self.path = self.response[1]self.http_version = self.response[2]"
B = "class http_response :def __init__(self, response):self.response = response.split(' ')self.type = self.response[0]self.path = self.response[1]self.http_version = self.response[2]"

print(A==B)
#---------------------------------------------------------
class http_response :
	def __init__(self, response):
		self.response = response.split(' ')
		self.type = self.response[0]
		self.path = self.response[1]
		self.http_version = self.response[2]

hello = http_response(myString)

print(hello.http_version)



class HTTP_Response :
    def __init__(self, response):
        self.response = response.split(' ')
        self.type = self.response[0]
        self.path = self.response[1]
        self.http_version = self.response[2]

x = HTTP_Response(myString)

print(str(x.http_version))