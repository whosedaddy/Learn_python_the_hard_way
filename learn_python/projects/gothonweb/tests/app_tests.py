from nose.tools import *
from bin.app import app
from tests.tools import assert_response
from gothonweb import map

def test_index():
	
	#test our first GET request to /
	resp = app.request("/")
	assert_response(resp,status='303')
	
	#test our first GET request to /
	resp = app.request("/game")
	assert_response(resp)
	
	#make sure default values work for the form
	resp = app.request("/game",method="POST")
	assert_response(resp,contains="None",status='303')
	
	#test that we get expected values
#	data = {'action':"123"}
#	resp = app.request("/game",method='POST',data=data)
#	assert_response(resp,contains="123",status='303')