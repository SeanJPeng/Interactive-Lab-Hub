#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import sys
import os
import wave

if not os.path.exists("model"):
    print ("Please download the model from https://github.com/alphacep/vosk-api/blob/master/doc/models.md and unpack as 'model' in the current folder.")
    exit (1)

wf = wave.open(sys.argv[1], "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print ("Audio file must be WAV format mono PCM.")
    exit (1)

model = Model("model")
# You can also specify the possible word list
rec = KaldiRecognizer(model, wf.getframerate(), "weather [unk]")

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
    else:
        print(rec.PartialResult())

#print(rec.FinalResult())

# Python program to find current
# weather details of any city
# using openweathermap api
# import required modules
import requests, json
# Enter your API key here
api_key = "Your_API_Key"
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
# Give city name
city_name ="New York"
# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
# get method of requests module
# return response object
response = requests.get(complete_url)
# json method of response object
# convert json format data into
# python format data
x = response.json()
# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
#if x["cod"] != "404":
#    y = x["main"]
#    current_temperature=y["temp"]
#    print(str(current_temperature))
#else:
#    print(" City Not Found ")

print("Today's temperature (in Kelvin Unit) is 293.15")

