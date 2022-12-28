def get_items():
    return [
        {
            "country": "US",
            "city": "Boston",
            "currency": "USD",
            "amount": 100
        },
        {
            "country": "FR",
            "city": "Paris",
            "currency": "EUR",
            "amount": 20
        },
        {
            "country": "FR",
            "city": "Lyon",
            "currency": "EUR",
            "amount": 11.4
        },
        {
            "country": "ES",
            "city": "Madrid",
            "currency": "EUR",
            "amount": 8.9
        },
        {
            "country": "UK",
            "city": "London",
            "currency": "GBP",
            "amount": 12.2
        },
        {
            "country": "UK",
            "city": "London",
            "currency": "FBP",
            "amount": 10.9
        }
    ]


def get_grouped_by_currency_expected():
    return {
        'EUR': [
            {
                'country': 'FR',
                'city': 'Paris',
                'amount': 20
            },
            {
                'country': 'FR',
                'city': 'Lyon',
                'amount': 11.4
            },
            {
                'country': 'ES',
                'city': 'Madrid',
                'amount': 8.9
            }
        ],
        'FBP': [
            {
                'country': 'UK',
                'city': 'London',
                'amount': 10.9
            }
        ],
        'GBP': [
            {
                'country': 'UK',
                'city': 'London',
                'amount': 12.2
            }
        ],
        'USD': [
            {
                'country': 'US',
                'city': 'Boston',
                'amount': 100
            }
        ]
    }


def get_grouped_by_multiple_keys():
    return {
      "EUR": {
        "ES": {
          "Madrid": [
            {
              "amount": 8.9
            }
          ]
        },
        "FR": {
          "Lyon": [
            {
              "amount": 11.4
            }
          ],
          "Paris": [
            {
              "amount": 20
            }
          ]
        }
      },
      "FBP": {
        "UK": {
          "London": [
            {
              "amount": 10.9
            }
          ]
        }
      },
      "GBP": {
        "UK": {
          "London": [
            {
              "amount": 12.2
            }
          ]
        }
      },
      "USD": {
        "US": {
          "Boston": [
            {
              "amount": 100
            }
          ]
        }
      }
    }