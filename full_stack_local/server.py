from http.server import CGIHTTPRequestHandler, HTTPServer


HOST = "localhost"
PORT = 8000


def main():
    server_address = (HOST, PORT)
    handler = CGIHTTPRequestHandler
    handler.cgi_directories = ["/cgi-bin"]

    with HTTPServer(server_address, handler) as server:
        print(f"Serving at http://{HOST}:{PORT}")
        print("Press Ctrl+C to stop.")
        server.serve_forever()


if __name__ == "__main__":
    main()
