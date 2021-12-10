from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
import json

def get_customers_list():
    print("get_customers_list start")
    r_value = {};
    with open('data.txt', 'r') as data_file:
        data = json.load(data_file)
        for customer_id, customer_info in data.items():
            r_value[customer_id] = [customer_info['name'],customer_info['type'],customer_info['age']]
        print(r_value)

    return json.dumps(r_value)

def get_customers_info(cust_id):
    print("get_customers_info start")
    r_value = {};
    with open('data.txt', 'r') as data_file:
        data = json.load(data_file)
        customer_info = data.get(cust_id)
        if customer_info == None:
            r_value["Customer Doesn't Exist"] = None
            return json.dumps(r_value)
        customer_info.pop('orders')
        r_value=customer_info

        print(r_value)
    return json.dumps(r_value)

def get_order_list(cust_id):
    print("get_order_list start")
    r_value = {};
    with open('data.txt', 'r') as data_file:
        data = json.load(data_file)
        customer_info = data.get(cust_id)
        
        if customer_info == None:
            r_value["Customer Doesn't Exist"] = None
            return json.dumps(r_value)
        customer_orders = customer_info.pop('orders')
        r_value=customer_orders
        print(r_value)
    return json.dumps(r_value)

def get_order_info(cust_id, order_id):
    print("get_order_info start")
    r_value = [];
    with open('data.txt', 'r') as data_file:
        data = json.load(data_file)
        customer_info = data.get(cust_id)
        
        if customer_info == None:
            r_value.append("Customer Doesn't Exist")
            return json.dumps(r_value)

        customer_orders = customer_info.pop('orders')
        the_order=customer_orders.get(order_id)
        if the_order == None:
            r_value.append("Customer's Order Doesn't Exist")
            return json.dumps(r_value)
        r_value=the_order
        print(r_value)
    return json.dumps(r_value)

class BoyangHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin","*")
        self.end_headers()
        url = urlparse(self.path)
        print("url: '%s' url.path: '%s'" % (url, url.path))
        command_list = self.path.split('/')
        print(command_list)
        print('length of command list is :',len(command_list))

        if (len(command_list) < 1 or command_list[0]!=''):
            self.wfile.write(b'Invalid Request1')
        elif(len(command_list)>1 and command_list[1] == 'customers'):
                if(len(command_list)>2):

                    if(len(command_list)>3 and command_list[3] == 'orders'):

                        if (len(command_list)>4):
                            
                            #/customers/int/orders/int
                            return_str = get_order_info(command_list[2],command_list[4])
                            print(return_str,"----------------")
                            self.wfile.write(return_str.encode())
                            # self.wfile.write(b'/customers/int/orders/int reqeust')
                            return
                        #/customers/int/orders
                        return_str = get_order_list(command_list[2])
                        print(return_str,"----------------")
                        self.wfile.write(return_str.encode())
                        # self.wfile.write(b'/customers/int/orders reqeust - list of orders')
                        return

                    #/customers/int
                    return_str = get_customers_info(command_list[2])
                    print(return_str,"----------------")
                    self.wfile.write(return_str.encode())
                    # self.wfile.write(b'/customers/int reqeust - customer information')
                    return

                #/customers/int
                return_str = get_customers_list()
                print(return_str,"----------------")
                self.wfile.write(return_str.encode())
                # self.wfile.write(b'/customers reqeust - List of customers')
                return
        else:
             self.wfile.write(b'Nothing request')
        print("here")
        self.wfile.write(b'end!!')

def run():
    server_address = ('0.0.0.0', 8000)
    httpd = HTTPServer(server_address, BoyangHandler)
    httpd.serve_forever()

run()
