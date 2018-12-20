## restaurant happy 1
* request_restaurant
    - restaurant: utter_ask_details
* inform{"location": "paris"}
    - restaurant: utter_ask_people
* inform{"people": "4"}
    - restaurant: utter_ask_price
* inform{"price": "expensive"}
    - restaurant: utter_ask_cuisine
* inform{"cuisine": "italian"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - restaurant: slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy

## restaurant happy 2
* request_restaurant
    - restaurant: utter_ask_details
* inform{"people": "4"}
    - restaurant: utter_ask_location
* inform{"location": "paris"}
    - restaurant: utter_ask_price
* inform{"price": "expensive"}
    - restaurant: utter_ask_cuisine
* inform{"cuisine": "italian"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - restaurant: slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy

## restaurant happy 3
* request_restaurant
    - restaurant: utter_ask_details
* inform{"price": "expensive"}
    - restaurant: utter_ask_people
* inform{"people": "4"}
    - restaurant: utter_ask_cuisine
* inform{"cuisine": "italian"}
    - restaurant: utter_ask_location
* inform{"location": "paris"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - restaurant: slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy

## restaurant happy 4
* request_restaurant
    - restaurant: utter_ask_details
* inform{"cuisine": "italian"}
    - restaurant: utter_ask_price
* inform{"price": "expensive"}
    - restaurant: utter_ask_location
* inform{"location": "paris"}
    - restaurant: utter_ask_people
* inform{"people": "4"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - restaurant: slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy


## Generated Story 8130156986372571232
* request_restaurant
    - restaurant: utter_ask_details
* inform{"people": "4", "location": "paris"}
    - restaurant: slot{"people": "4"}
    - restaurant: slot{"location": "paris"}
    - restaurant: utter_ask_price
* inform{"price": "expensive"}
    - restaurant: slot{"price":"expensive"}
    - restaurant: utter_ask_cuisine
* inform{"cuisine": "french"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - restaurant: slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy

## Generated Story 1074034796281423152
* request_restaurant
    - restaurant: utter_ask_details
* inform{"people": "4", "cuisine": "french"}
    - restaurant: slot{"people": "4"}
    - restaurant: slot{"cuisine": "french"}
    - restaurant: utter_ask_price
* inform{"price": "mid-range"}
    - restaurant: slot{"price": "mid-range"}
    - restaurant: utter_ask_location
* inform{"location": "paris"}
    - restaurant: slot{"location": "paris"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - restaurant: slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy


## Generated Story -4597439819468904984
* request_restaurant
    - restaurant: utter_ask_details
* inform{"people": "2", "cuisine": "french"}
    - restaurant: slot{"people": "2"}
    - restaurant: slot{"cuisine": "french"}
    - restaurant: utter_ask_price
* inform{"price": "cheap"}
    - restaurant: slot{"price": "cheap"}
    - restaurant: utter_ask_location
* inform{"location": "paris"}
    - restaurant: slot{"location": "paris"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - restaurant: slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy

## Generated Story 584180253540252584
* request_restaurant
    - restaurant: utter_ask_details
* inform{"people": "4", "cuisine": "italian"}
    - restaurant: slot{"people": "4"}
    - restaurant: slot{"cuisine": "italian"}
    - restaurant: utter_ask_price
* inform{"price": "cheap"}
    - restaurant: slot{"price": "cheap"}
    - restaurant: utter_ask_location
* inform{"location": "paris"}
    - restaurant: slot{"location": "paris"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - restaurant: slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy
