from zeep import Client

def soap_to_json():
    wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"  # Replace with actual WSDL URL
    client = Client(wsdl=wsdl_url)
    response = client.service.GetData()
    return {"data": response}
