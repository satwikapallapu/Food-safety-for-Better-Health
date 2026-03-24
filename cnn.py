import redis
import cnn
import os

# connect to redis
r = redis.Redis(host="localhost", port=6379, decode_responses=True)

# folder where json files exist
folder = "models"

# loop through all files
for file in os.listdir(folder):

    if file.endswith(".json"):

        path = os.path.join(folder, file)

        with open(path) as f:
            data = json.load(f)

        name = file.replace(".json","")

        r.set(name, json.dumps(data))

        print(name, "stored")