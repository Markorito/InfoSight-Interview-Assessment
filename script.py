#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from PIL import Image, ImageEnhance
import json
import numpy as np
import cv2


# In[3]:


data = {}
img = Image.open('id.jpg')

contrast_enhancer = ImageEnhance.Contrast(img)
pil_enhanced_image = contrast_enhancer.enhance(2)
enhanced_image = np.asarray(pil_enhanced_image)
r, g, b = cv2.split(enhanced_image)
enhanced_image = cv2.merge([b, g, r])
image_data = json.dumps(np.asarray(enhanced_image).tolist())


# In[8]:


headers = {
        'Content-Type': 'application/json',
        'accept': 'application/json',
    }
url = 'http://127.0.0.1:8000/predict'
params ={'image': image_data}
response = requests.get(url, params, headers = headers)
response.json()

