## restaurant correction 1.2
* request_restaurant
    - utter_ask_details
* inform{"location": "paris"}
    - utter_ask_people
* correct{"location": "rome"}
    - utter_correct_location_restaurant
    - utter_ask_people
* inform{"people": "4"}
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy

## restaurant correction 1.3
* request_restaurant
    - utter_ask_details
* inform{"location": "paris"}
    - utter_ask_people
* inform{"people": "4"}
    - utter_ask_price
* correct{"people": "3"}
    - utter_correct_people_restaurant
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy

## restaurant correction 1.4
* request_restaurant
    - utter_ask_details
* inform{"location": "paris"}
    - utter_ask_people
* inform{"people": "4"}
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_cuisine
* correct{"price": "cheap"}
    - utter_correct_price_restaurant
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy

## restaurant correction 1.5
* request_restaurant
    - utter_ask_details
* inform{"location": "paris"}
    - utter_ask_people
* inform{"people": "4"}
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* correct{"cuisine": "french"}
    - utter_correct_cuisine_restaurant
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy

## restaurant correction 2.2
* request_restaurant
    - utter_ask_details
* inform{"people": "4"}
    - utter_ask_location
* correct{"people": "3"}
    - utter_correct_people_restaurant
    - utter_ask_location
* inform{"location": "paris"}
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy

## restaurant correction 2.3
* request_restaurant
    - utter_ask_details
* inform{"people": "4"}
    - utter_ask_location
* inform{"location": "paris"}
    - utter_ask_price
* correct{"location": "rome"}
    - utter_correct_location_restaurant
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy

## restaurant correction 2.4
* request_restaurant
    - utter_ask_details
* inform{"people": "4"}
    - utter_ask_location
* inform{"location": "paris"}
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_cuisine
* correct{"price": "cheap"}
    - utter_correct_price_restaurant
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy

## restaurant correction 2.5
* request_restaurant
    - utter_ask_details
* inform{"people": "4"}
    - utter_ask_location
* inform{"location": "paris"}
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* correct{"cuisine": "french"}
    - utter_correct_cuisine_restaurant
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy

## restaurant correction 3.2
* request_restaurant
    - utter_ask_details
* inform{"price": "expensive"}
    - utter_ask_people
* correct{"price": "cheap"}
    - utter_correct_price_restaurant
    - utter_ask_people
* inform{"people": "4"}
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - utter_ask_location
* inform{"location": "paris"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy

## restaurant correction 3.3
* request_restaurant
    - utter_ask_details
* inform{"price": "expensive"}
    - utter_ask_people
* inform{"people": "4"}
    - utter_ask_cuisine
* correct{"people": "5"}
    - utter_correct_people_restaurant
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - utter_ask_location
* inform{"location": "paris"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy

## restaurant correction 3.4
* request_restaurant
    - utter_ask_details
* inform{"price": "expensive"}
    - utter_ask_people
* inform{"people": "4"}
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - utter_ask_location
* correct{"cuisine": "french"}
    - utter_correct_cuisine_restaurant
    - utter_ask_location
* inform{"location": "paris"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy

## restaurant correction 3.5
* request_restaurant
    - utter_ask_details
* inform{"price": "expensive"}
    - utter_ask_people
* inform{"people": "4"}
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - utter_ask_location
* inform{"location": "paris"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* correct{"location": "rome"}
    - utter_correct_location_restaurant
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy

## restaurant correction 4.2
* request_restaurant
    - utter_ask_details
* inform{"cuisine": "italian"}
    - utter_ask_price
* correct{"cuisine": "french"}
    - utter_correct_cuisine_restaurant
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_location
* inform{"location": "paris"}
    - utter_ask_people
* inform{"people": "4"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy

## restaurant correction 4.3
* request_restaurant
    - utter_ask_details
* inform{"cuisine": "italian"}
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_location
* correct{"price": "cheap"}
    - utter_correct_price_restaurant
    - utter_ask_location
* inform{"location": "paris"}
    - utter_ask_people
* inform{"people": "4"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy

## restaurant correction 4.4
* request_restaurant
    - utter_ask_details
* inform{"cuisine": "italian"}
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_location
* inform{"location": "paris"}
    - utter_ask_people
* correct{"location": "rome"}
    - utter_correct_location_restaurant
    - utter_ask_people
* inform{"people": "4"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy

## restaurant correction 4.5
* request_restaurant
    - utter_ask_details
* inform{"cuisine": "italian"}
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_location
* inform{"location": "paris"}
    - utter_ask_people
* inform{"people": "4"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* correct{"people": "5"}
    - utter_correct_people_restaurant
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy
