# Server configuration
import http.server

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

httpd = http.server.HTTPServer(('',PORT),Handler)
print(f"Http server is running on {PORT}")

httpd.serve_forever()