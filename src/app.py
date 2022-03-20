from flask import Flask, send_file, request, Response
import mysql.connector
from constants import TARGET_WIDTH
from io import BytesIO

from constants import *
from lib import Parser, DB, Image, Auth

def prepareDB():
    image = Parser.getResizedImageFromCSV(CSV_PATH)

    DB.init(Image.imageToBlob(image))

prepareDB()

imageDB = mysql.connector.connect(**DB_CONFIG)

app = Flask(APP_NAME)

def sanitizeInput(min, max, imageHeight):
    if(min > max):
        tmp = max
        max = min
        min = tmp

    if(min < 0 or min > imageHeight):
        min = 0
    
    if(max > imageHeight):
        max = imageHeight
    
    return (min, max)


@app.route('/', methods = ['GET'])
def main():
    key = request.args.get("key", "", type=str)
    if not Auth.isAllowed(key):
        return "Authentication error", 401

    rawImage = Image.blobToImage(DB.queryImage())
    maxHeight = rawImage.height
    min = request.args.get("min", 0, type=int)
    max = request.args.get("max", maxHeight, type=int)

    verticalBounds = sanitizeInput(min, max, maxHeight)

    transformedImage = Image.applyTransformations(rawImage, verticalBounds)

    return send_file(Image.getImgIO(transformedImage), mimetype='image/jpeg')
