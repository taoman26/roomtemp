#!/usr/bin/python

import datetime
import commands
import time
import boto3
import json
from boto3.session import Session
from boto3.dynamodb.conditions import Key, Attr
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

def update_data(temp):
    session = Session(profile_name="default")
    db = session.resource('dynamodb')
    table = db.Table('room-status')
    room = table.update_item(
        Key = {
            'room' : 1
        },
        UpdateExpression="set room_temp = :p",
        ExpressionAttributeValues={
            ':p': Decimal(temp)
        },
        ReturnValues="UPDATED_NEW"
    )

def getTemperature():
    cmd = "/usr/local/bin/temper | /usr/bin/cut -f2 -d','"
    temperature = commands.getoutput(cmd)
    temperature = Decimal(temperature).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
    return temperature

def main():
    result = getTemperature()
    update_data(result)
    print datetime.datetime.today(),"Temperature: %s C" % (result)

if __name__ == '__main__':
    main()
