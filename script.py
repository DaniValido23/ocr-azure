from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials
from dotenv import load_dotenv

import os
import time

def extract_image(img_name):
    load_dotenv()

    subscription_key = os.getenv("subscription_key")
    endpoint = os.getenv("endpoint")
    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

    image_path = os.path.join("images", img_name)
    read_image = open(image_path, "rb")
    
    read_response = computervision_client.read_in_stream(read_image, raw= True)
    read_operation_location = read_response.headers["Operation-Location"]
    operation_id = read_operation_location.split("/")[-1]

    while True:
        read_result = computervision_client.get_read_result(operation_id)
        if read_result.status.lower() not in ["notstarted", "running"]:
            break
        
        print("Waiting for result")
        time.sleep(10)

    sentence_list = []
    if read_result.status == OperationStatusCodes.succeeded:
        for text_result in read_result.analyze_result.read_results:
            for line in text_result.lines:
                sentence_list.append(line.text)
        
    return sentence_list



def main():
    name = input("Introduce el nombre de tu archivo: ")

    list = extract_image(name)

    for info in list:
        print(info)

main()

