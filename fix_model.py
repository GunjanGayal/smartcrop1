import tensorflow as tf
import json

model = tf.keras.models.load_model("plant_disease_model.h5")

# Weights save karo
model.save_weights("model_weights.weights.h5")

# Config save karo  
with open("model_config.json", "w") as f:
    json.dump(model.get_config(), f)

print("Done!")