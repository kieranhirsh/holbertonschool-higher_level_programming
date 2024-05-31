#!/usr/bin/python3
''' module documentation '''
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class HTTPRequestHandler(BaseHTTPRequestHandler):
    ''' class documentation '''
    def do_GET(self):
        ''' this should be a match case, but the checker uses Python3.8 '''
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write("Hello, this is a simple API!".encode())
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(json.dumps({"name": "John", "age": 30, "city": "New York"}).encode())
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write("OK".encode())
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write("OK".encode())
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write("Endpoint not found".encode())


if __name__ == "__main__":
    PORT = 8000
    with HTTPServer(('localhost', PORT), HTTPRequestHandler) as server:
        print("Serving on port {}".format(PORT))
        server.serve_forever()
