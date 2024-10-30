import json

# Sample JSON data (replace this with your actual JSON)
json_data = {
  "alert": {
    "rule": {
      "id": "1934759532",
      "carrierFsCodes": {
        "string": [
          "SQ"
        ]
      },
      "arrivalAirportFsCode": "FRA",
      "departure": "2024-10-09T23:55:00.000",
      "arrival": "2024-10-10T06:45:00.000",
      "name": "Baggage Belt Info for FRA PROD",
      "description": "Baggage Belt Info for FRA PROD",
      "ruleEvents": {
        "ruleEvent": [
          {
            "type": "BAGGAGE",
            "value": "525600"
          }
        ]
      },
      "delivery": {
        "format": "JSON",
        "destination": "https://api.singaporeair.com/msl-starling-prd/notification/flightglobal/alert"
      }
    },
    "flightStatus": {
      "flightId": "1278837076",
      "carrierFsCode": "SQ",
      "operatingCarrierFsCode": "SQ",
      "primaryCarrierFsCode": "SQ",
      "flightNumber": "26",
      "departureAirportFsCode": "SIN",
      "arrivalAirportFsCode": "FRA",
      "departureDate": {
        "dateUtc": "2024-10-09T15:55:00.000Z",
        "dateLocal": "2024-10-09T23:55:00.000"
      },
      "arrivalDate": {
        "dateUtc": "2024-10-10T04:45:00.000Z",
        "dateLocal": "2024-10-10T06:45:00.000"
      },
      "status": "A",
      "schedule": {
        "flightType": "J",
        "serviceClasses": "RFJY",
        "restrictions": "",
        "downlines": {
          "downline": [
            {
              "fsCode": "JFK",
              "flightId": "1278837085"
            }
          ]
        }
      },
      "operationalTimes": {
        "publishedDeparture": {
          "dateUtc": "2024-10-09T15:55:00.000Z",
          "dateLocal": "2024-10-09T23:55:00.000"
        },
        "scheduledGateDeparture": {
          "dateUtc": "2024-10-09T15:55:00.000Z",
          "dateLocal": "2024-10-09T23:55:00.000"
        },
        "estimatedGateDeparture": {
          "dateUtc": "2024-10-09T15:55:00.000Z",
          "dateLocal": "2024-10-09T23:55:00.000"
        },
        "actualGateDeparture": {
          "dateUtc": "2024-10-09T15:55:00.000Z",
          "dateLocal": "2024-10-09T23:55:00.000"
        },
        "estimatedRunwayDeparture": {
          "dateUtc": "2024-10-09T16:13:00.000Z",
          "dateLocal": "2024-10-10T00:13:00.000"
        },
        "actualRunwayDeparture": {
          "dateUtc": "2024-10-09T16:13:00.000Z",
          "dateLocal": "2024-10-10T00:13:00.000"
        },
        "publishedArrival": {
          "dateUtc": "2024-10-10T04:45:00.000Z",
          "dateLocal": "2024-10-10T06:45:00.000"
        },
        "scheduledGateArrival": {
          "dateUtc": "2024-10-10T04:45:00.000Z",
          "dateLocal": "2024-10-10T06:45:00.000"
        },
        "estimatedGateArrival": {
          "dateUtc": "2024-10-10T05:03:00.000Z",
          "dateLocal": "2024-10-10T07:03:00.000"
        },
        "estimatedRunwayArrival": {
          "dateUtc": "2024-10-10T04:54:00.000Z",
          "dateLocal": "2024-10-10T06:54:00.000"
        }
      },
      "codeshares": {
        "codeshare": [
          {
            "fsCode": "A3",
            "flightNumber": "1201",
            "relationship": "L"
          },
          {
            "fsCode": "AC",
            "flightNumber": "6296",
            "relationship": "L"
          },
          {
            "fsCode": "FJ",
            "flightNumber": "5903",
            "relationship": "L"
          },
          {
            "fsCode": "LH",
            "flightNumber": "9763",
            "relationship": "L"
          },
          {
            "fsCode": "NZ",
            "flightNumber": "3336",
            "relationship": "L"
          },
          {
            "fsCode": "OU",
            "flightNumber": "5809",
            "relationship": "L"
          },
          {
            "fsCode": "PR",
            "flightNumber": "3838",
            "relationship": "L"
          },
          {
            "fsCode": "TP",
            "flightNumber": "8416",
            "relationship": "L"
          },
          {
            "fsCode": "VA",
            "flightNumber": "5406",
            "relationship": "L"
          }
        ]
      },
      "delays": {
        "arrivalGateDelayMinutes": "18"
      },
      "flightDurations": {
        "scheduledBlockMinutes": "770",
        "taxiOutMinutes": "18"
      },
      "airportResources": {
        "departureTerminal": "3",
        "departureGate": "B10",
        "arrivalTerminal": "1",
        "arrivalGate": "B48A",
        "baggage": "21"
      },
      "flightEquipment": {
        "scheduledEquipmentIataCode": "77W",
        "actualEquipmentIataCode": "77W",
        "tailNumber": "9V-SNC",
        "fleetAircraftId": "47300"
      },
      "flightStatusUpdates": {
        "flightStatusUpdate": [
          {
            "updatedAt": {
              "dateUtc": "2024-10-06T18:42:20.128Z"
            },
            "source": "Schedule",
            "updatedTextFields": {
              "updatedTextField": [
                {
                  "field": "DTM",
                  "newText": "3"
                },
                {
                  "field": "ATM",
                  "newText": "1"
                },
                {
                  "field": "SQP",
                  "newText": "77W"
                },
                {
                  "field": "STS",
                  "newText": "S"
                }
              ]
            },
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "SGD",
                  "newDateLocal": "2024-10-09T23:55:00.000",
                  "newDateUtc": "2024-10-09T15:55:00.000Z"
                },
                {
                  "field": "SGA",
                  "newDateLocal": "2024-10-10T06:45:00.000",
                  "newDateUtc": "2024-10-10T04:45:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-08T14:47:12.107Z"
            },
            "source": "Airport",
            "updatedTextFields": {
              "updatedTextField": [
                {
                  "field": "AQP",
                  "newText": "77W"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-09T09:09:16.404Z"
            },
            "source": "Airport",
            "updatedTextFields": {
              "updatedTextField": [
                {
                  "field": "DGT",
                  "newText": "B10"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-09T11:42:25.473Z"
            },
            "source": "Airline",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "EGA",
                  "newDateLocal": "2024-10-10T07:08:00.000",
                  "newDateUtc": "2024-10-10T05:08:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-09T14:56:30.425Z"
            },
            "source": "Airport",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "EGD",
                  "newDateLocal": "2024-10-09T23:55:00.000",
                  "newDateUtc": "2024-10-09T15:55:00.000Z"
                },
                {
                  "field": "EGA",
                  "originalDateLocal": "2024-10-10T07:08:00.000",
                  "originalDateUtc": "2024-10-10T05:08:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-09T15:10:54.135Z"
            },
            "source": "Airline",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "EGA",
                  "newDateLocal": "2024-10-10T07:08:00.000",
                  "newDateUtc": "2024-10-10T05:08:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-09T15:26:44.305Z"
            },
            "source": "Airport",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "EGA",
                  "originalDateLocal": "2024-10-10T07:08:00.000",
                  "originalDateUtc": "2024-10-10T05:08:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-09T15:41:08.542Z"
            },
            "source": "Airline",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "EGA",
                  "newDateLocal": "2024-10-10T07:08:00.000",
                  "newDateUtc": "2024-10-10T05:08:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-09T15:56:53.147Z"
            },
            "source": "Airport",
            "updatedTextFields": {
              "updatedTextField": [
                {
                  "field": "STS",
                  "originalText": "S",
                  "newText": "A"
                }
              ]
            },
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "AGD",
                  "newDateLocal": "2024-10-09T23:55:00.000",
                  "newDateUtc": "2024-10-09T15:55:00.000Z"
                },
                {
                  "field": "EGA",
                  "originalDateLocal": "2024-10-10T07:08:00.000",
                  "originalDateUtc": "2024-10-10T05:08:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-09T15:58:15.219Z"
            },
            "source": "Airline",
            "updatedTextFields": {
              "updatedTextField": [
                {
                  "field": "TAL",
                  "newText": "9V-SNC"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-09T16:14:31.551Z"
            },
            "source": "Airline",
            "updatedTextFields": {
              "updatedTextField": [
                {
                  "field": "AGT",
                  "newText": "B48A"
                }
              ]
            },
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "EGA",
                  "newDateLocal": "2024-10-10T07:08:00.000",
                  "newDateUtc": "2024-10-10T05:08:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-09T16:14:52.681Z"
            },
            "source": "Cirium",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "ERA",
                  "newDateLocal": "2024-10-10T06:52:00.000",
                  "newDateUtc": "2024-10-10T04:52:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-09T16:16:04.081Z"
            },
            "source": "Positional",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "ERD",
                  "newDateLocal": "2024-10-10T00:13:00.000",
                  "newDateUtc": "2024-10-09T16:13:00.000Z"
                },
                {
                  "field": "ARD",
                  "newDateLocal": "2024-10-10T00:13:00.000",
                  "newDateUtc": "2024-10-09T16:13:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-09T16:17:14.379Z"
            },
            "source": "Airport",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "EGA",
                  "originalDateLocal": "2024-10-10T07:08:00.000",
                  "newDateLocal": "2024-10-10T07:04:00.000",
                  "originalDateUtc": "2024-10-10T05:08:00.000Z",
                  "newDateUtc": "2024-10-10T05:04:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-09T16:35:05.067Z"
            },
            "source": "Cirium",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "ERA",
                  "originalDateLocal": "2024-10-10T06:52:00.000",
                  "newDateLocal": "2024-10-10T06:56:00.000",
                  "originalDateUtc": "2024-10-10T04:52:00.000Z",
                  "newDateUtc": "2024-10-10T04:56:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-09T16:40:03.239Z"
            },
            "source": "Cirium",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "ERA",
                  "originalDateLocal": "2024-10-10T06:56:00.000",
                  "newDateLocal": "2024-10-10T06:47:00.000",
                  "originalDateUtc": "2024-10-10T04:56:00.000Z",
                  "newDateUtc": "2024-10-10T04:47:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-09T16:55:12.266Z"
            },
            "source": "Cirium",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "ERA",
                  "originalDateLocal": "2024-10-10T06:47:00.000",
                  "newDateLocal": "2024-10-10T06:52:00.000",
                  "originalDateUtc": "2024-10-10T04:47:00.000Z",
                  "newDateUtc": "2024-10-10T04:52:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-09T17:05:12.220Z"
            },
            "source": "Cirium",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "ERA",
                  "originalDateLocal": "2024-10-10T06:52:00.000",
                  "newDateLocal": "2024-10-10T06:55:00.000",
                  "originalDateUtc": "2024-10-10T04:52:00.000Z",
                  "newDateUtc": "2024-10-10T04:55:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-09T17:40:39.060Z"
            },
            "source": "Cirium",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "ERA",
                  "originalDateLocal": "2024-10-10T06:55:00.000",
                  "newDateLocal": "2024-10-10T06:59:00.000",
                  "originalDateUtc": "2024-10-10T04:55:00.000Z",
                  "newDateUtc": "2024-10-10T04:59:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-09T18:46:11.446Z"
            },
            "source": "Cirium",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "ERA",
                  "originalDateLocal": "2024-10-10T06:59:00.000",
                  "newDateLocal": "2024-10-10T06:55:00.000",
                  "originalDateUtc": "2024-10-10T04:59:00.000Z",
                  "newDateUtc": "2024-10-10T04:55:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-09T18:56:20.440Z"
            },
            "source": "Cirium",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "ERA",
                  "originalDateLocal": "2024-10-10T06:55:00.000",
                  "newDateLocal": "2024-10-10T06:59:00.000",
                  "originalDateUtc": "2024-10-10T04:55:00.000Z",
                  "newDateUtc": "2024-10-10T04:59:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-09T19:01:18.107Z"
            },
            "source": "Cirium",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "ERA",
                  "originalDateLocal": "2024-10-10T06:59:00.000",
                  "newDateLocal": "2024-10-10T07:02:00.000",
                  "originalDateUtc": "2024-10-10T04:59:00.000Z",
                  "newDateUtc": "2024-10-10T05:02:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-09T20:17:06.713Z"
            },
            "source": "Cirium",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "ERA",
                  "originalDateLocal": "2024-10-10T07:02:00.000",
                  "newDateLocal": "2024-10-10T07:06:00.000",
                  "originalDateUtc": "2024-10-10T05:02:00.000Z",
                  "newDateUtc": "2024-10-10T05:06:00.000Z"
                },
                {
                  "field": "EGA",
                  "originalDateLocal": "2024-10-10T07:04:00.000",
                  "newDateLocal": "2024-10-10T07:15:00.000",
                  "originalDateUtc": "2024-10-10T05:04:00.000Z",
                  "newDateUtc": "2024-10-10T05:15:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-09T21:13:05.531Z"
            },
            "source": "Cirium",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "ERA",
                  "originalDateLocal": "2024-10-10T07:06:00.000",
                  "newDateLocal": "2024-10-10T07:02:00.000",
                  "originalDateUtc": "2024-10-10T05:06:00.000Z",
                  "newDateUtc": "2024-10-10T05:02:00.000Z"
                },
                {
                  "field": "EGA",
                  "originalDateLocal": "2024-10-10T07:15:00.000",
                  "newDateLocal": "2024-10-10T07:11:00.000",
                  "originalDateUtc": "2024-10-10T05:15:00.000Z",
                  "newDateUtc": "2024-10-10T05:11:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-09T21:41:37.764Z"
            },
            "source": "Cirium",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "ERA",
                  "originalDateLocal": "2024-10-10T07:02:00.000",
                  "newDateLocal": "2024-10-10T06:59:00.000",
                  "originalDateUtc": "2024-10-10T05:02:00.000Z",
                  "newDateUtc": "2024-10-10T04:59:00.000Z"
                },
                {
                  "field": "EGA",
                  "originalDateLocal": "2024-10-10T07:11:00.000",
                  "newDateLocal": "2024-10-10T07:08:00.000",
                  "originalDateUtc": "2024-10-10T05:11:00.000Z",
                  "newDateUtc": "2024-10-10T05:08:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-09T21:51:16.268Z"
            },
            "source": "Cirium",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "ERA",
                  "originalDateLocal": "2024-10-10T06:59:00.000",
                  "newDateLocal": "2024-10-10T06:52:00.000",
                  "originalDateUtc": "2024-10-10T04:59:00.000Z",
                  "newDateUtc": "2024-10-10T04:52:00.000Z"
                },
                {
                  "field": "EGA",
                  "originalDateLocal": "2024-10-10T07:08:00.000",
                  "newDateLocal": "2024-10-10T07:01:00.000",
                  "originalDateUtc": "2024-10-10T05:08:00.000Z",
                  "newDateUtc": "2024-10-10T05:01:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-09T22:06:10.230Z"
            },
            "source": "Cirium",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "ERA",
                  "originalDateLocal": "2024-10-10T06:52:00.000",
                  "newDateLocal": "2024-10-10T07:03:00.000",
                  "originalDateUtc": "2024-10-10T04:52:00.000Z",
                  "newDateUtc": "2024-10-10T05:03:00.000Z"
                },
                {
                  "field": "EGA",
                  "originalDateLocal": "2024-10-10T07:01:00.000",
                  "newDateLocal": "2024-10-10T07:12:00.000",
                  "originalDateUtc": "2024-10-10T05:01:00.000Z",
                  "newDateUtc": "2024-10-10T05:12:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-09T22:16:16.456Z"
            },
            "source": "Cirium",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "ERA",
                  "originalDateLocal": "2024-10-10T07:03:00.000",
                  "newDateLocal": "2024-10-10T06:59:00.000",
                  "originalDateUtc": "2024-10-10T05:03:00.000Z",
                  "newDateUtc": "2024-10-10T04:59:00.000Z"
                },
                {
                  "field": "EGA",
                  "originalDateLocal": "2024-10-10T07:12:00.000",
                  "newDateLocal": "2024-10-10T07:08:00.000",
                  "originalDateUtc": "2024-10-10T05:12:00.000Z",
                  "newDateUtc": "2024-10-10T05:08:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-09T22:31:18.147Z"
            },
            "source": "Cirium",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "ERA",
                  "originalDateLocal": "2024-10-10T06:59:00.000",
                  "newDateLocal": "2024-10-10T07:03:00.000",
                  "originalDateUtc": "2024-10-10T04:59:00.000Z",
                  "newDateUtc": "2024-10-10T05:03:00.000Z"
                },
                {
                  "field": "EGA",
                  "originalDateLocal": "2024-10-10T07:08:00.000",
                  "newDateLocal": "2024-10-10T07:12:00.000",
                  "originalDateUtc": "2024-10-10T05:08:00.000Z",
                  "newDateUtc": "2024-10-10T05:12:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-09T23:35:15.513Z"
            },
            "source": "Cirium",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "ERA",
                  "originalDateLocal": "2024-10-10T07:03:00.000",
                  "newDateLocal": "2024-10-10T07:07:00.000",
                  "originalDateUtc": "2024-10-10T05:03:00.000Z",
                  "newDateUtc": "2024-10-10T05:07:00.000Z"
                },
                {
                  "field": "EGA",
                  "originalDateLocal": "2024-10-10T07:12:00.000",
                  "newDateLocal": "2024-10-10T07:16:00.000",
                  "originalDateUtc": "2024-10-10T05:12:00.000Z",
                  "newDateUtc": "2024-10-10T05:16:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-10T00:21:43.431Z"
            },
            "source": "Cirium",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "ERA",
                  "originalDateLocal": "2024-10-10T07:07:00.000",
                  "newDateLocal": "2024-10-10T07:04:00.000",
                  "originalDateUtc": "2024-10-10T05:07:00.000Z",
                  "newDateUtc": "2024-10-10T05:04:00.000Z"
                },
                {
                  "field": "EGA",
                  "originalDateLocal": "2024-10-10T07:16:00.000",
                  "newDateLocal": "2024-10-10T07:13:00.000",
                  "originalDateUtc": "2024-10-10T05:16:00.000Z",
                  "newDateUtc": "2024-10-10T05:13:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-10T00:37:04.329Z"
            },
            "source": "Cirium",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "ERA",
                  "originalDateLocal": "2024-10-10T07:04:00.000",
                  "newDateLocal": "2024-10-10T07:01:00.000",
                  "originalDateUtc": "2024-10-10T05:04:00.000Z",
                  "newDateUtc": "2024-10-10T05:01:00.000Z"
                },
                {
                  "field": "EGA",
                  "originalDateLocal": "2024-10-10T07:13:00.000",
                  "newDateLocal": "2024-10-10T07:10:00.000",
                  "originalDateUtc": "2024-10-10T05:13:00.000Z",
                  "newDateUtc": "2024-10-10T05:10:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-10T01:12:48.482Z"
            },
            "source": "Cirium",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "ERA",
                  "originalDateLocal": "2024-10-10T07:01:00.000",
                  "newDateLocal": "2024-10-10T06:57:00.000",
                  "originalDateUtc": "2024-10-10T05:01:00.000Z",
                  "newDateUtc": "2024-10-10T04:57:00.000Z"
                },
                {
                  "field": "EGA",
                  "originalDateLocal": "2024-10-10T07:10:00.000",
                  "newDateLocal": "2024-10-10T07:06:00.000",
                  "originalDateUtc": "2024-10-10T05:10:00.000Z",
                  "newDateUtc": "2024-10-10T05:06:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-10T01:50:01.981Z"
            },
            "source": "Airport",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "EGA",
                  "originalDateLocal": "2024-10-10T07:06:00.000",
                  "newDateLocal": "2024-10-10T07:23:00.000",
                  "originalDateUtc": "2024-10-10T05:06:00.000Z",
                  "newDateUtc": "2024-10-10T05:23:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-10T02:25:00.307Z"
            },
            "source": "Airport",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "EGA",
                  "originalDateLocal": "2024-10-10T07:23:00.000",
                  "newDateLocal": "2024-10-10T07:03:00.000",
                  "originalDateUtc": "2024-10-10T05:23:00.000Z",
                  "newDateUtc": "2024-10-10T05:03:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-10T03:44:58.915Z"
            },
            "source": "Cirium",
            "updatedDateFields": {
              "updatedDateField": [
                {
                  "field": "ERA",
                  "originalDateLocal": "2024-10-10T06:57:00.000",
                  "newDateLocal": "2024-10-10T06:54:00.000",
                  "originalDateUtc": "2024-10-10T04:57:00.000Z",
                  "newDateUtc": "2024-10-10T04:54:00.000Z"
                }
              ]
            }
          },
          {
            "updatedAt": {
              "dateUtc": "2024-10-10T04:05:26.330Z"
            },
            "source": "Airport",
            "updatedTextFields": {
              "updatedTextField": [
                {
                  "field": "BGG",
                  "newText": "21"
                }
              ]
            }
          }
        ]
      }
    },
    "event": {
      "type": "BAGGAGE"
    },
    "dataSource": "Airport",
    "dateTimeRecorded": "2024-10-10T04:05:26.330Z"
  },
  "appendix": {
    "airlines": {
      "airline": [
        {
          "fs": "A3",
          "iata": "A3",
          "icao": "AEE",
          "name": "Aegean Airlines",
          "active": "true"
        },
        {
          "fs": "AC",
          "iata": "AC",
          "icao": "ACA",
          "name": "Air Canada",
          "active": "true"
        },
        {
          "fs": "PR",
          "iata": "PR",
          "icao": "PAL",
          "name": "Philippine Airlines",
          "active": "true"
        },
        {
          "fs": "FJ",
          "iata": "FJ",
          "icao": "FJI",
          "name": "Fiji Airways",
          "active": "true"
        },
        {
          "fs": "OU",
          "iata": "OU",
          "icao": "CTN",
          "name": "Croatia Airlines",
          "active": "true"
        },
        {
          "fs": "VA",
          "iata": "VA",
          "icao": "VOZ",
          "name": "Virgin Australia",
          "active": "true"
        },
        {
          "fs": "LH",
          "iata": "LH",
          "icao": "DLH",
          "name": "Lufthansa",
          "active": "true"
        },
        {
          "fs": "NZ",
          "iata": "NZ",
          "icao": "ANZ",
          "name": "Air New Zealand",
          "active": "true"
        },
        {
          "fs": "TP",
          "iata": "TP",
          "icao": "TAP",
          "name": "TAP Air Portugal",
          "active": "true"
        },
        {
          "fs": "SQ",
          "iata": "SQ",
          "icao": "SIA",
          "name": "Singapore Airlines",
          "active": "true"
        }
      ]
    },
    "airports": {
      "airport": [
        {
          "fs": "FRA",
          "iata": "FRA",
          "icao": "EDDF",
          "faa": "",
          "name": "Frankfurt Airport",
          "city": "Frankfurt",
          "cityCode": "FRA",
          "countryCode": "DE",
          "countryName": "Germany",
          "regionName": "Europe",
          "timeZoneRegionName": "Europe/Berlin",
          "weatherZone": "",
          "localTime": "2024-10-10T06:05:54.659",
          "utcOffsetHours": "2.0",
          "latitude": "50.048952",
          "longitude": "8.573678",
          "elevationFeet": "381",
          "classification": "1",
          "active": "true"
        },
        {
          "fs": "SIN",
          "iata": "SIN",
          "icao": "WSSS",
          "faa": "",
          "name": "Singapore Changi Airport",
          "city": "Singapore",
          "cityCode": "SIN",
          "countryCode": "SG",
          "countryName": "Singapore",
          "regionName": "Asia",
          "timeZoneRegionName": "Asia/Singapore",
          "weatherZone": "",
          "localTime": "2024-10-10T12:05:54.659",
          "utcOffsetHours": "8.0",
          "latitude": "1.361173",
          "longitude": "103.990201",
          "elevationFeet": "22",
          "classification": "1",
          "active": "true"
        },
        {
          "fs": "JFK",
          "iata": "JFK",
          "icao": "KJFK",
          "faa": "JFK",
          "name": "New York John F. Kennedy International Airport",
          "street1": "JFK Airport",
          "city": "New York",
          "cityCode": "NYC",
          "stateCode": "NY",
          "postalCode": "11430",
          "countryCode": "US",
          "countryName": "United States",
          "regionName": "North America",
          "timeZoneRegionName": "America/New_York",
          "weatherZone": "NYZ178",
          "localTime": "2024-10-10T00:05:54.659",
          "utcOffsetHours": "-4.0",
          "latitude": "40.642335",
          "longitude": "-73.78817",
          "elevationFeet": "13",
          "classification": "1",
          "active": "true"
        }
      ]
    },
    "equipments": {
      "equipment": [
        {
          "iata": "77W",
          "name": "Boeing 777-300ER",
          "turboProp": "false",
          "jet": "true",
          "widebody": "true",
          "regional": "false"
        }
      ]
    }
  }
}

# Function to collect all keys from JSON
def collect_keys(data, keys=None):
    if keys is None:
        keys = []
    if isinstance(data, dict):
        for key, value in data.items():
            keys.append(key)
            collect_keys(value, keys)
    elif isinstance(data, list):
        for item in data:
            collect_keys(item, keys)
    return keys

# Load JSON and collect keys
all_keys = collect_keys(json_data)
print("List of all parameters (keys) in JSON:", all_keys)
