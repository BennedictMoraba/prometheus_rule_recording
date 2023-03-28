import http.server

class HandleRequests(http.server.BaseHTTPRequestHandler):
    def do_Get(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.writable(bytes("<html><head><title>MyFirst Application</title></head><body><center><h2>Welcome stranger lets get started</h2></center></body></html>","utf-8"))
        self.wfile.close

        if __name__ == "__main__":
            server = http.server.HTTPServer(('localhost','5000'), HandleRequests)
            server.serve_forever()