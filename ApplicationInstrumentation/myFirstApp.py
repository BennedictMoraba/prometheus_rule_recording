from http.server import BaseHTTPRequestHandler, HTTPServer
from prometheus_client import start_http_server


class HandleRequests(BaseHTTPRequestHandler):
    def do_Get(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>MyFirst Application</title></head><body style ='color: #333; margin-top: 30px'><center><h2>Welcome stranger lets get started</center></h2></body></html>","utf-8"))
        self.wfile.close

        if __name__ == "__main__":
            start_http_server(5001)
            server = HTTPServer(('localhost',5000), HandleRequests)
            server.serve_forever()