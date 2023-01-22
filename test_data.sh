#!/bin/bash
# Test Data
# This is test data to simulate what will be written to the REST interface, paste each curl command into the command line to write it.
# The 1st time field is the time the data was inserted and the other time fields are when that temp reading was taken
# in theory this should be the same
today="2023-01-22"

curl -X POST http://localhost:3000/add -H "Content-Type: application/json" -d '{"time": "2023-01-22T11:25:00", "data": [
        {"id": "t1", "time": "2023-01-22T11:25:00", "temp": 20.432},
        {"id": "t2", "time": "2023-01-22T11:25:00", "temp": 21.672},
        {"id": "t3", "time": "2023-01-22T11:25:00", "temp": 25.245},
        {"id": "t4", "time": "2023-01-22T11:25:00", "temp": 60.223},
        {"id": "t5", "time": "2023-01-22T11:25:00", "temp": 74.232},
        {"id": "t6", "time": "2023-01-22T11:25:00", "temp": 75.232},
        {"id": "t7", "time": "2023-01-22T11:25:00", "temp": 75.232},
        {"id": "t8", "time": "2023-01-22T11:25:00", "temp": 75.232},
        {"id": "t9", "time": "2023-01-22T11:25:00", "temp": 75.232},
        {"id": "t10", "time": "2023-01-22T11:25:00", "temp": 75.232}]}'


curl -X POST http://localhost:3000/add -H "Content-Type: application/json" -d '{"time":"'${today}'T11:00:00.000", "data": [
        {"id": "t1", "time":"'${today}'T11:00:00.000", "temp": 20.432},
        {"id": "t2", "time":"'${today}'T11:00:00.000", "temp": 21.672},
        {"id": "t3", "time":"'${today}'T11:00:00.000", "temp": 25.245},
        {"id": "t4", "time":"'${today}'T11:00:00.000", "temp": 60.223},
        {"id": "t5", "time":"'${today}'T11:00:00.000", "temp": 74.232},
        {"id": "t6", "time":"'${today}'T11:00:00.000", "temp": 75.232},
        {"id": "t7", "time":"'${today}'T11:00:00.000", "temp": 75.232},
        {"id": "t8", "time":"'${today}'T11:00:00.000", "temp": 75.232},
        {"id": "t9", "time":"'${today}'T11:00:00.000", "temp": 75.232},
       {"id": "t10", "time":"'${today}'T11:00:00.000", "temp": 75.232}]}'

curl -X POST http://localhost:3000/add -H "Content-Type: application/json" -d '{"time":"'${today}'T11:05:00.000", "data": [
        {"id": "t1", "time":"'${today}'T11:05:00.000", "temp": 19.432},
        {"id": "t2", "time":"'${today}'T11:05:00.000", "temp": 20.872},
        {"id": "t3", "time":"'${today}'T11:05:00.000", "temp": 22.245},
        {"id": "t4", "time":"'${today}'T11:05:00.000", "temp": 44.223},
        {"id": "t5", "time":"'${today}'T11:05:00.000", "temp": 72.232},
        {"id": "t6", "time":"'${today}'T11:05:00.000", "temp": 74.232},
        {"id": "t7", "time":"'${today}'T11:05:00.000", "temp": 75.732},
        {"id": "t8", "time":"'${today}'T11:05:00.000", "temp": 75.332},
        {"id": "t9", "time":"'${today}'T11:05:00.000", "temp": 75.832},
       {"id": "t10", "time":"'${today}'T11:05:00.000", "temp": 75.132}]}'
	   
curl -X POST http://localhost:3000/add -H "Content-Type: application/json" -d '{"time":"'${today}'T11:10:00.000", "data": [
        {"id": "t1", "time":"'${today}'T11:10:00.000", "temp": 18.432},
        {"id": "t2", "time":"'${today}'T11:10:00.000", "temp": 20.172},
        {"id": "t3", "time":"'${today}'T11:10:00.000", "temp": 21.245},
        {"id": "t4", "time":"'${today}'T11:10:00.000", "temp": 25.223},
        {"id": "t5", "time":"'${today}'T11:10:00.000", "temp": 30.232},
        {"id": "t6", "time":"'${today}'T11:10:00.000", "temp": 75.232},
        {"id": "t7", "time":"'${today}'T11:10:00.000", "temp": 75.232},
        {"id": "t8", "time":"'${today}'T11:10:00.000", "temp": 75.232},
        {"id": "t9", "time":"'${today}'T11:10:00.000", "temp": 75.232},
       {"id": "t10", "time":"'${today}'T11:10:00.000", "temp": 75.232}]}'
	   
curl -X POST http://localhost:3000/add -H "Content-Type: application/json" -d '{"time":"$'{today}'T11:15:00.000", "data": [
        {"id": "t1", "time":"'${today}'T11:15:00.000", "temp": 18.432},
        {"id": "t2", "time":"'${today}'T11:15:00.000", "temp": 20.172},
        {"id": "t3", "time":"'${today}'T11:15:00.000", "temp": 21.245},
        {"id": "t4", "time":"'${today}'T11:15:00.000", "temp": 25.223},
        {"id": "t5", "time":"'${today}'T11:15:00.000", "temp": 23.232},
        {"id": "t6", "time":"'${today}'T11:15:00.000", "temp": 45.232},
        {"id": "t7", "time":"'${today}'T11:15:00.000", "temp": 75.232},
        {"id": "t8", "time":"'${today}'T11:15:00.000", "temp": 75.232},
        {"id": "t9", "time":"'${today}'T11:15:00.000", "temp": 75.232},
       {"id": "t10", "time":"'${today}'T11:15:00.000", "temp": 75.232}]}'

curl -X POST http://localhost:3000/add -H "Content-Type: application/json" -d '{"time":"'${today}'T11:20:00.000", "data": [
        {"id": "t1", "time":"'${today}'T11:20:00.000", "temp": 18.432},
        {"id": "t2", "time":"'${today}'T11:20:00.000", "temp": 20.172},
        {"id": "t3", "time":"'${today}'T11:20:00.000", "temp": 21.245},
        {"id": "t4", "time":"'${today}'T11:20:00.000", "temp": 25.223},
        {"id": "t5", "time":"'${today}'T11:20:00.000", "temp": 23.232},
        {"id": "t6", "time":"'${today}'T11:20:00.000", "temp": 30.232},
        {"id": "t7", "time":"'${today}'T11:20:00.000", "temp": 51.232},
        {"id": "t8", "time":"'${today}'T11:20:00.000", "temp": 75.232},
        {"id": "t9", "time":"'${today}'T11:20:00.000", "temp": 75.232},
       {"id": "t10", "time":"'${today}'T11:20:00.000", "temp": 75.232}]}'
	   
curl -X POST http://localhost:3000/add -H "Content-Type: application/json" -d '{"time":"'${today}'T11:25:00.000", "data": [
        {"id": "t1", "time":"$'{today}'T11:25:00.000", "temp": 18.432},
        {"id": "t2", "time":"$'{today}'T11:25:00.000", "temp": 20.172},
        {"id": "t3", "time":"$'{today}'T11:25:00.000", "temp": 21.245},
        {"id": "t4", "time":"$'{today}'T11:25:00.000", "temp": 25.223},
        {"id": "t5", "time":"$'{today}'T11:25:00.000", "temp": 23.232},
        {"id": "t6", "time":"$'{today}'T11:25:00.000", "temp": 30.232},
        {"id": "t7", "time":"$'{today}'T11:25:00.000", "temp": 32.232},
        {"id": "t8", "time":"$'{today}'T11:25:00.000", "temp": 49.232},
        {"id": "t9", "time":"$'{today}'T11:25:00.000", "temp": 75.232},
       {"id": "t10", "time":"$'{today}'T11:25:00.000", "temp": 75.232}]}'
	   
