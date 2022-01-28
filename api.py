from fastapi import FastAPI
import uvicorn
import tensorflow as tf
from pydantic import BaseModel
import cv2
import numpy as np
from fastapi.middleware.cors import CORSMiddleware



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
class request_body(BaseModel):
        image: list


# Creating an Endpoint to receive the data
# to make prediction on.
@app.post('/predict')
def predict(data : request_body):
	# Making the data in a form suitable for prediction
	test_data = data.image
	test_data = np.array(test_data, dtype='uint8')	
	image = cv2.resize(test_data,(225, 225))
	image = np.array(image) /255
	image = image.reshape(-1, 225, 225, 3)
	
	# Predicting the Class
	prediction = model.predict(image)
	classes = np.argmax(prediction,axis=1)
	
	# Return the Result
	#return { 'class' : prediction.tolist()}
	return { 'class' : classes.tolist()}

