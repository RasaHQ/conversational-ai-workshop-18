## Generated Story -7886542752391645811
* request_hotel
    - utter_ask_details
* inform{"people": "4"}
    - slot{"people": "4"}
    - utter_ask_location
* correct{"people": "2"}
    - slot{"people": "2"}
    - utter_correct_people_hotel
    - utter_ask_location
* chitchat
    - utter_chitchat
    - utter_ask_location
* inform{"location": "rome"}
    - slot{"location": "rome"}
    - utter_ask_price
* inform{"price": "expensive"}
    - slot{"price": "expensive"}
    - utter_ask_startdate
* inform{"startdate": "next week", "enddate": "tomorrow"}
    - slot{"startdate": "next week"}
    - slot{"enddate": "tomorrow"}
    - utter_filled_slots
    - utter_search_hotel
    - slot{"hotel": "hotel"}
    - utter_suggest_hotel
* correct{"enddate": "May 26th"}
    - slot{"enddate": "May 26th"}
    - utter_correct_enddate_hotel
    - utter_search_hotel
    - slot{"hotel": "hotel"}
    - utter_suggest_hotel
* correct{"location": "rome"}
    - slot{"location": "rome"}
    - utter_correct_location_hotel
    - utter_search_hotel
    - slot{"hotel": "hotel"}
    - utter_suggest_hotel
* did_that_work
    - utter_worked_hotel
    - utter_suggest_hotel
* affirm
    - utter_happy
* chitchat