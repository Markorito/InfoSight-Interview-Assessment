from fastapi import FastAPI, UploadFile, File
import uvicorn
import tensorflow as tf
from pydantic import BaseModel
import cv2
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image



# Creating FastAPI instance
app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

model = tf.keras.models.load_model('id passport classifier')

# Creating class to define the request body
# and the type hints of each attribute



# Creating an Endpoint to receive the data
# to make prediction on.
@app.post('/predict')
async def predict(file: UploadFile):
	# Making the data in a form suitable for prediction
	test_data = Image.open(file.file)
	test_data = np.array(test_data, dtype='uint8')	
	image = cv2.resize(test_data,(225, 225))
	image = np.array(image) /255
	image = image.reshape(-1, 225, 225, 3)
	
	# Predicting the Class
	prediction = model.predict(image)
	classes = np.argmax(prediction,axis=1)
               
	
	# Return the Result
	return { 'class' : classes.tolist()[0]}


