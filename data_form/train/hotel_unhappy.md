## hotel explain
* request_hotel
    - action_hotel
* inform{"location": "paris"}
    - action_hotel
* about
    - action_explain
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

## hotel didthatwork
* request_hotel
    - action_hotel
* inform{"location": "paris"}
    - action_hotel
* inform{"people": "4"}
    - action_hotel
* inform{"price": "expensive"}
    - action_hotel
* did_that_work
    - utter_worked
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
