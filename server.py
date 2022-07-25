from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
import json

from app.services.estates_services import get_estates
from app.utils.validates import valid_params_and_values

GET_METHODS = {}
PORT = 8001

def router(route_map, methods=["GET"]):
    def route_enclouse(f):
        for method in methods:
            if method == "GET":
                GET_METHODS[route_map] = f
        
        def call(*args, **kwargs):
            return f(*args, **kwargs)
        return call
    return route_enclouse


class HTTPHandlerHabi(BaseHTTPRequestHandler):

    def __bad_request(self, code: int = 500, message: dict = {'detail': 'Not Found'}):
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(message).encode('utf-8'))

    def do_GET(self):
        path_before_querys = self.path.split("?")[0]
        if path_before_querys not in GET_METHODS:
            self.__bad_request()
            return
            
        body={}
        headers={}
        parsed_path = parse.urlparse(self.path)
        if parsed_path.path in GET_METHODS:
            query_string={}
            for x in parsed_path.query.split('&'):
                y=x.split("=")
                if(len(y)>=2):
                    query_string[y[0]]=y[1]

            if error := valid_params_and_values(query_string):
                self.__bad_request(400, {"message": error["message"]})
                return
                
            content=GET_METHODS[parsed_path.path](query_string,body,headers)
            if "error" in content:
                message = {"message": json.loads(content)["message"]}
                self.__bad_request(message=message)
                return


            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))


@router('/casas', methods=["GET"])
def test(query, body, headers):
    try:
        response_sql = get_estates(filters=query)
    except Exception as e:
        response_sql = {"error": True, "message": str(e)}

    return json.dumps(response_sql)


if __name__ == "__main__":
    server_habi = HTTPServer(('', PORT), HTTPHandlerHabi)
    print(f"serving at port {PORT}")
    server_habi.serve_forever()