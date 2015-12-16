from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import json

def test(request):
	return HttpResponse("This is the first test view")	

def other(request):
	return HttpResponse("This is a different response, from an other view")

def parameter(request, value):
	return HttpResponse("You passed in the value %s" % value)

def home(request):
	return render(request, "data/index.html")

#gets random data formatted correctly
#the output is a dictionary where 'columns' is a list of data series
#each data series starts with the series name, followed by a set of data
#columns: [
#	['data1', 30, 200, 100, 400, 150, 250],
#	['data2', 50, 20, 10, 40, 15, 25]
#]

def get_data(request):
	columns = []

	for i in range(5):
		cur_series = ["Data " + str(i)]
		cur_series += list(np.random.randint(10, size=10))

		columns.append(cur_series)

	response = {"columns": columns}

	#return the response in JSON format
	return HttpResponse(json.dumps(response), content_type="application/json")

