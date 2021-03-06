#!/usr/bin/python

#desmet_t@hotmail.com
#10/10/2018

#SERVICE PROVIDER

#SimpleXMLRPCServer is the library to create an XML-RPC server

from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
import logging
import random

class RequestHandler(SimpleXMLRPCRequestHandler):
	rpc_paths = ('/RPC2',)

	def do_OPTIONS(self):
        	self.send_response(200)
        	self.end_headers()

	# Add these headers to all responses
	def end_headers(self):
        	self.send_header("Access-Control-Allow-Headers", 
                         "Origin, X-Requested-With, Content-Type, Accept")
        	self.send_header("Access-Control-Allow-Origin", "*")
        	SimpleXMLRPCRequestHandler.end_headers(self)

#Set up logging
logging.basicConfig(level=logging.DEBUG)

server = SimpleXMLRPCServer (('localhost', 9000),logRequests=True,requestHandler=RequestHandler)

#register XML-RPC introspextion functions such as system.listMethods()
server.register_introspection_functions()

#Expose functions

def get_weather_station_location():
	return "Oizy - Belgium"
server.register_function(get_weather_station_location)

def get_weather_station_coordinates():
	return "49.8966N-5.011E"
server.register_function(get_weather_station_coordinates)

def get_temperature():
	return random.randint(-20,40)
server.register_function(get_temperature)

def get_wind_direction():
	wind_directions = ['N','NE','E','SE','S','SW','W','NW']
	random.shuffle(wind_directions)
	return (wind_directions)[0]
server.register_function(get_wind_direction)

def get_wind_speed():
	return random.randint(0,12)
server.register_function(get_wind_speed)

try:
	print ('Use Control-C to EXIT')
	server.serve_forever()
except KeyboardInterrupt:
	print ('Exiting')	
