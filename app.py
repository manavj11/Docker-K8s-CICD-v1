from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = "Hello from Kubernetes via GitHub Actions!\n"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

if __name__ == "__main__":
    server = HTTPServer(("", 8080), Handler)
    print("Listening on port 8080...")
    server.serve_forever()