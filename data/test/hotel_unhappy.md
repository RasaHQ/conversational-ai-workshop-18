## hotel explain 1
* request_hotel
    - action_hotel
* about
    - action_explain
    - action_hotel
* inform{"location": "paris"}
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

## hotel explain 2
* request_hotel
    - action_hotel
* inform{"location": "paris"}
    - action_hotel
* inform{"people": "4"}
    - action_hotel
* about
    - action_explain
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

## hotel explain 3
* request_hotel
    - action_hotel
* inform{"location": "paris"}
    - action_hotel
* inform{"people": "4"}
    - action_hotel
* inform{"price": "expensive"}
    - action_hotel
* about
    - action_explain
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

## hotel explain 4
* request_hotel
    - action_hotel
* inform{"location": "paris"}
    - action_hotel
* inform{"people": "4"}
    - action_hotel
* inform{"price": "expensive"}
    - action_hotel
* inform{"date": "10.03.2018"}
    - action_hotel
* about
    - action_explain
    - action_hotel
* inform{"date": "10.03.2018"}
    - action_hotel
    - action_search_hotel
    - slot{"hotel": "hotel"}
    - utter_suggest_hotel
* affirm
    - utter_happy

## hotel didthatwork 1
* request_hotel
    - action_hotel
* inform{"location": "paris"}
    - action_hotel
* did_that_work
    - utter_worked
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

## hotel didthatwork 2
* request_hotel
    - action_hotel
* inform{"location": "paris"}
    - action_hotel
* inform{"people": "4"}
    - action_hotel
* did_that_work
    - utter_worked
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

## hotel didthatwork 3
* request_hotel
    - action_hotel
* inform{"location": "paris"}
    - action_hotel
* inform{"people": "4"}
    - action_hotel
* inform{"price": "expensive"}
    - action_hotel
* inform{"date": "10.03.2018"}
    - action_hotel
* did_that_work
    - utter_worked
    - action_hotel
* inform{"date": "10.03.2018"}
    - action_hotel
    - action_search_hotel
    - slot{"hotel": "hotel"}
    - utter_suggest_hotel
* affirm
    - utter_happy

## hotel correct 1
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

## hotel correct 2
* request_hotel
    - action_hotel
* inform{"location": "paris"}
    - action_hotel
* inform{"people": "4"}
    - action_hotel
* correct{"people": "3"}
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

## hotel didthatwork 3
* request_hotel
    - action_hotel
* inform{"location": "paris"}
    - action_hotel
* inform{"people": "4"}
    - action_hotel
* inform{"price": "expensive"}
    - action_hotel
* inform{"date": "10.03.2018"}
    - action_hotel
* correct{"date": "10.03.2018"}
    - action_hotel
* inform{"date": "10.03.2018"}
    - action_hotel
    - action_search_hotel
    - slot{"hotel": "hotel"}
    - utter_suggest_hotel
* affirm
    - utter_happy
