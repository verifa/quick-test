import json
import random

output_name = "../input.json"

if __name__ == "__main__":
    output = [{
        "colour": "blue" if random.random() < 0.5 else "red",
        "index": i
    } for i in range(1000)]

    with open(output_name, "w") as out_file: 
        json.dump(output, out_file, indent=4)
