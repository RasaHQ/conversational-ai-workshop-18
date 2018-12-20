## hotel happy 1
* request_hotel
    - hotel: utter_ask_details
* inform{"location": "paris"}
    - hotel: utter_ask_people
* inform{"people": "4"}
    - hotel: utter_ask_price
* inform{"price": "expensive"}
    - hotel: utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - hotel: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - hotel: slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## hotel happy 2
* request_hotel
    - hotel: utter_ask_details
* inform{"people": "4"}
    - hotel: utter_ask_location
* inform{"location": "paris"}
    - hotel: utter_ask_price
* inform{"price": "expensive"}
    - hotel: utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - hotel: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - hotel: slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## hotel happy 3
* request_hotel
    - hotel: utter_ask_details
* inform{"price": "expensive"}
    - hotel: utter_ask_people
* inform{"people": "4"}
    - hotel: utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - hotel: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_ask_location
* inform{"location": "paris"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - hotel: slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## hotel happy 4
* request_hotel
    - hotel: utter_ask_details
* inform{"startdate": "10.03.2018"}
    - hotel: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_ask_price
* inform{"price": "expensive"}
    - hotel: utter_ask_location
* inform{"location": "paris"}
    - hotel: utter_ask_people
* inform{"people": "4"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - hotel: slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## hotel happy 5
* request_hotel
    - hotel: utter_ask_details
* inform{"enddate": "10.03.2018"}
    - hotel: utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - hotel: utter_ask_location
* inform{"location": "paris"}
    - hotel: utter_ask_price
* inform{"price": "expensive"}
    - hotel: utter_ask_people
* inform{"people": "4"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - hotel: slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story 6377256771280559561
* request_hotel
    - hotel: utter_ask_details
* inform{"price": "mid-range", "enddate": "next week"}
    - hotel: slot{"price": "mid-range"}
    - hotel: slot{"enddate": "next week"}
    - hotel: utter_ask_startdate
* inform{"startdate": "tomorrow"}
    - hotel: slot{"startdate": "tomorrow"}
    - hotel: utter_ask_location
* inform{"location": "london"}
    - hotel: slot{"location": "london"}
    - hotel: utter_ask_people
* inform{"people": "4"}
    - hotel: slot{"people": "4"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - hotel: slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story -6821548152705280771
* request_hotel
    - hotel: utter_ask_details
* inform{"people": "2", "enddate": "May 26th"}
    - hotel: slot{"people": "2"}
    - hotel: slot{"enddate": "May 26th"}
    - hotel: utter_ask_location
* inform{"location": "london"}
    - hotel: slot{"location": "london"}
    - hotel: utter_ask_startdate
* inform{"startdate": "May 25th"}
    - hotel: slot{"startdate": "May 25th"}
    - hotel: utter_ask_price
* inform{"price": "cheap"}
    - hotel: slot{"price": "cheap"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - hotel: slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story 6118400076211702408
* request_hotel
    - hotel: utter_ask_details
* inform{"startdate": "today", "location": "rome"}
    - hotel: slot{"startdate": "today"}
    - hotel: slot{"location": "rome"}
    - hotel: utter_ask_people
* inform{"people": "6"}
    - hotel: slot{"people": "6"}
    - hotel: utter_ask_price
* inform{"price": "mid-range"}
    - hotel: slot{"price": "mid-range"}
    - hotel: utter_ask_enddate
* inform{"enddate": "tomorrow"}
    - hotel: slot{"enddate": "tomorrow"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - hotel: slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story -7795096423415267175
* request_hotel
    - hotel: utter_ask_details
* inform{"people": "1", "location": "rome"}
    - hotel: slot{"people": "1"}
    - hotel: slot{"location": "rome"}
    - hotel: utter_ask_price
* inform{"price": "mid-range"}
    - hotel: slot{"price": "mid-range"}
    - hotel: utter_ask_startdate
* inform{"startdate": "May 25th"}
    - hotel: slot{"startdate": "May 25th"}
    - hotel: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - hotel: slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story -633443905704416777
* request_hotel
    - hotel: utter_ask_details
* inform{"startdate": "today", "people": "2"}
    - hotel: slot{"startdate": "today"}
    - hotel: slot{"people": "2"}
    - hotel: utter_ask_location
* inform{"location": "london"}
    - hotel: slot{"location": "london"}
    - hotel: utter_ask_price
* inform{"price": "expensive"}
    - hotel: slot{"price": "expensive"}
    - hotel: utter_ask_enddate
* inform{"enddate": "tomorrow"}
    - hotel: slot{"enddate": "tomorrow"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - hotel: slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story 7692376286038639225
* request_hotel
    - hotel: utter_ask_details
* inform{"startdate": "today", "price": "expensive"}
    - hotel: slot{"startdate": "today"}
    - hotel: slot{"price": "expensive"}
    - hotel: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_ask_location
* inform{"location": "paris"}
    - hotel: utter_ask_people
* inform{"people": "4"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - hotel: slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story 1942533987084426839
* request_hotel
    - hotel: utter_ask_details
* inform{"startdate": "May 25th", "location": "paris", "people": "6"}
    - hotel: slot{"startdate": "May 25th"}
    - hotel: slot{"location": "paris"}
    - hotel: slot{"people": "6"}
    - hotel: utter_ask_price
* inform{"price": "expensive"}
    - hotel: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - hotel: slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* affirm
    - hotel: utter_happy
