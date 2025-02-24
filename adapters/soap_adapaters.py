from zeep import Client

def soap_to_json():
    wsdl_url = "https://www.example.com/legacy.wsdl"  # Replace with actual WSDL URL
    client = Client(wsdl=wsdl_url)
    response = client.service.GetData()
    return {"data": response}
