# SERVER CONFIGURATION
import http.server

PORT = 8000

#Firewall rule configuration
class FirewallRequestHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        if path.endswith("/sensitive.txt"):
            self.send_error(403,"Forribiden")
            return None
        return super().translate_path(path) 

Handler = FirewallRequestHandler

httpd = http.server.HTTPServer(('',PORT), Handler)
print(f"SERVER IS RUNNING ON PORT {PORT}")

httpd.serve_forever()
        
    