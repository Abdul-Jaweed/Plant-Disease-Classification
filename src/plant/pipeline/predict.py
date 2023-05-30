import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class Plant:
    def __init__(self,filename):
        self.filename =filename
        
        def prediction(self):
            model = load_model(os.path.join("artifacts","training", "model.h5"))
            img = imageio.imread(self.filename)
            img = Image.fromarray(img).resize((224, 224))
            x = img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = x / 255.0
            prediction = model.predict(x)
            predicted_label = target_names[np.argmax(prediction)]
            return predicted_label