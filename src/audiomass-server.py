# python3.8
from http import server
import socketserver
PORT = 5055 
Handler = server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print(serving at port", PORT)
httpd.serve_forever()
