import socket
import os

#---------------------------------------------------------

def IsHTTPRequestGet(request) :
	request_category = request.split("\r\n")

	request_line = request_category[0].split(' ')

	if len(request_line) < 3 :
	
		return False

	request_type = request_line[0]
	if request_type not in ["GET"]:
		return False

	path = request_line[1]

	http_version = request_line[2]
	if http_version not in ["HTTP/1.1","HTTP/1.0"] :
		return False

	return request_type, path, http_version

#---------------------------------------------------------
class HTTP_Request :

	def __init__(self, request_type, path, http_version):
	    self.request_type = request_type
	    self.path = path
	    self.full_path = os.getcwd() + self.path
	    self.http_version = http_version

	def response(self) :

		if os.path.isfile(self.full_path) :
			_, file_extension = os.path.splitext(self.full_path)
			file_size = os.path.getsize(self.full_path)
			code_here = "200"
			status_here = "OK"
			header_here = "Content-Type: text/html"

			if file_extension == ".png" :
				header_here = "Content-Type: image/png"
			elif file_extension == ".ico" :
				header_here = "Content-Type: image/x-icon"

			f = open (self.full_path, "rb")
			l = f.read(file_size)
			msg_here = l

		elif os.path.isdir(self.full_path) :
			code_here = "200"
			status_here = "OK"
			header_here = "Content-Type: text/html"
			entries = os.listdir(self.full_path)
			entry_list = ""
			for i in entries :
				if i[0] != "." :
					entry_list = entry_list + "<br><a href =' ./"+self.path +"/" + str(i)+"' >" + str(i) +"</a>"
				else :
					pass
			msg_here = "<h1>this directory exists</h1>" + str(entry_list)

		else :
			code_here = "400"
			status_here = "Not Found"
			header_here = "Content-Type: text/html"
			msg_here = "<h1>this does not exist<h1>"


		message = """\
HTTP/1.1 {code} {status}
{headers}

{msg}
"""
		return message.format(code = code_here, status =status_here , headers = header_here, msg = msg_here)

#---------------------------------------------------------

HOST, PORT = '', 8888

#Create Socket W/ options
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#bind socket to host and port
listen_socket.bind((HOST, PORT))

#socket.listen(backlog) :Listen for connections made to the socket. 
#The backlog argument specifies the maximum number of queued connections 
#and should be at least 0; the maximum value is system-dependent (usually 5), 
#the minimum value is forced to 0.
listen_socket.listen(1)
print ('Serving HTTP on port %s ...' % PORT)

while True:
    client_connection, _ = listen_socket.accept()
    #connection object (new socket object --> cf request)
    #adress of the client socket

    #get the data transmitted by the socket
    conn = client_connection.recv(1024)

    request = IsHTTPRequestGet(conn )

    if request!= False :

    	request_get = HTTP_Request(request[0],request[1], request[2] )
    	http_response = request_get.response()

    else :
    	http_response ="""\
		There is an error
		"""
	
    client_connection.sendall(http_response)
    client_connection.close()





