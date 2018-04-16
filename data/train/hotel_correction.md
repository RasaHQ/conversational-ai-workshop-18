## hotel correction
* request_hotel
    - action_hotel
* inform{"location": "paris"}
    - action_hotel
* correct{"location": "italy"}
    - action_hotel
* inform{"people": "4"}
    - action_hotel
* inform{"price": "expensive"}
    - action_hotel
* inform{"date": "10.03.2018"}
    - action_hotel
* inform{"date": "10.03.2018"}
    - action_hotel
    - action_search_hotel
    - slot{"hotel": "hotel"}
    - utter_suggest_hotel
* affirm
    - utter_happy
