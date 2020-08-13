import json
import requests
def check_rates(request_postal_code,reciepent_postal_code,weight):
    try:
        auth = 'grant_type=client_credentials&client_id=l751be1ed19c9b466c83c17565665323d4&client_secret=3746874d2d894e65a31d1d9475772db3'
        payload = {
          "rateRequestControlParameters": {
            "returnTransitTimes": True
          },
          "requestedShipment": {
            "shipper": {
              "address": {
                "postalCode": request_postal_code,
                "countryCode": "US"
              }
            },
            "recipient": {
              "address": {
                "postalCode": reciepent_postal_code,
                "countryCode": "US"
              }
            },
            "pickupType": "DROPOFF_AT_FEDEX_LOCATION",
            "shippingChargesPayment": {
              "paymentType": "SENDER",
              "payor": {
                "responsibleParty": {
                  "accountNumber": {
                    "value": "740561073"
                  }
                }
              }
            },
            "rateRequestType": [
              "ACCOUNT",
              "LIST"
            ],
            "requestedPackageLineItems": [
              {
                "weight": {
                  "units": "LB",
                  "value": weight
                }
              }
            ]
          }
        }

        url_auth = "https://apis-sandbox.fedex.com/oauth/token"

        headers_auth = {
            'Content-Type': "application/x-www-form-urlencoded"
            }

        token = requests.request("POST", url_auth, data=auth, headers=headers_auth)

        token_text =  token.text
        token_text=json.loads(token_text)


        payload = json.dumps(payload)


        url = "https://apis-sandbox.fedex.com/rate/v1/rates/quotes"

        # payload = input # 'input' refers to JSON Payload
        headers = {
            'Content-Type': "application/json",
            'X-locale': "en_US",
            'Authorization': "Bearer "+ token_text['access_token']
            }

        response = requests.request("POST", url, data=payload, headers=headers)
        response_text =  response.text
        response_text=json.loads(response_text)
        message =response_text['output']['rateReplyDetails'][0]['ratedShipmentDetails'][0]['totalNetCharge']
        return message
    except Exception as e:
        message  = response_text['errors'][0]['message']
        return message