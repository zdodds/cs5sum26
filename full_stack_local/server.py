from http.server import CGIHTTPRequestHandler, HTTPServer     # crossed-out == deprecated. It's ok for now!

HOST = "localhost"
PORT = 8000

def main():
    server_address = (HOST, PORT)
    handler = CGIHTTPRequestHandler          # although deprecated, this mirrors the workings of the knuth server
    handler.cgi_directories = ["/cgi-bin"]   # location of the Python scripts that handle webpage requests

    with HTTPServer(server_address, handler) as server:
        print(f"Serving at http://{HOST}:{PORT}")
        print("Press Ctrl+C to stop.")
        server.serve_forever()
        # the above line is an "infinite loop" 
        # it keeps the server running until it's stopped with Ctrl+c (or killing the window) Ctrl+c is better!

if __name__ == "__main__":                   # This test is True when this file is run directly. (False when imported)
    main()
