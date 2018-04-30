## hotel happy 6
* request_hotel
    - utter_ask_details
* inform{"location": "paris", "startdate": "10.03.2018", "enddate": "10.03.2018"}
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_people
* inform{"people": "4"}
    - utter_filled_slots
    - action_search_hotel
    - slot{"hotel": "hotel"}
    - utter_suggest_hotel
* affirm
    - utter_happy


## hotel happy 7
* request_hotel
    - utter_ask_details
* inform{"location": "paris", "price": "expensive", "people": "4"}
    - utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - utter_ask_enddate
* inform{"enddate": "13.03.2018"}
    - utter_filled_slots
    - action_search_hotel
    - slot{"hotel": "hotel"}
    - utter_suggest_hotel
* affirm
    - utter_happy

## hotel happy 8
* request_hotel{"location": "paris", "price": "expensive", "people": "4"}
    - utter_ask_startdate
* inform{"startdate": "10.03.2018", "enddate": "13.03.2018"}
    - utter_filled_slots
    - action_search_hotel
    - slot{"hotel": "hotel"}
    - utter_suggest_hotel
* affirm
    - utter_happy
