## restaurant explain 1.1.1
* request_restaurant
    - utter_ask_details
* chitchat
    - utter_chitchat
    - utter_ask_details
* explain
    - utter_explain_details_restaurant
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
* affirm
    - utter_happy


## restaurant explain 1.1.2
* request_restaurant
    - utter_ask_details
* chitchat
    - utter_chitchat
    - utter_ask_details
* chitchat
    - utter_chitchat
    - utter_ask_details
* explain
    - utter_explain_details_restaurant
    - utter_ask_details
* inform{"location": "paris"}
    - utter_ask_people
* inform{"people": "4"}
    - utter_ask_price
* chitchat
    - utter_chitchat
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

## restaurant explain 1.3.1
* request_restaurant
    - utter_ask_details
* chitchat
    - utter_chitchat
    - utter_ask_details
* inform{"location": "paris"}
    - utter_ask_people
* inform{"people": "4"}
    - utter_ask_price
* explain
    - utter_explain_price_restaurant
    - utter_ask_price
* chitchat
    - utter_chitchat
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_cuisine
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_cuisine
* chitchat
    - utter_chitchat
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* did_that_work
    - utter_worked_restaurant
    - utter_suggest_restaurant
* affirm
    - utter_happy

## restaurant explain 1.4.1
* request_restaurant
    - utter_ask_details
* inform{"location": "paris"}
    - utter_ask_people
* explain
    - utter_explain_people_restaurant
    - utter_ask_people
* inform{"people": "4"}
    - utter_ask_price
* chitchat
    - utter_chitchat
    - utter_ask_price
* chitchat
    - utter_chitchat
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_cuisine
* explain
    - utter_explain_cuisine_restaurant
    - utter_ask_cuisine
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_cuisine
* chitchat
    - utter_chitchat
    - utter_ask_cuisine
* chitchat
    - utter_chitchat
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* chitchat
    - utter_chitchat
    - utter_suggest_restaurant
* affirm
    - utter_happy


## restaurant explain 1.4.2
* request_restaurant
    - utter_ask_details
* chitchat
    - utter_chitchat
    - utter_ask_details
* inform{"location": "paris"}
    - utter_ask_people
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_people
* explain
    - utter_explain_people_restaurant
    - utter_ask_people
* inform{"people": "4"}
    - utter_ask_price
* chitchat
    - utter_chitchat
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_cuisine
* chitchat
    - utter_chitchat
    - utter_ask_cuisine
* explain
    - utter_explain_cuisine_restaurant
    - utter_ask_cuisine
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_cuisine
* chitchat
    - utter_chitchat
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* chitchat
    - utter_chitchat
    - utter_suggest_restaurant
* affirm
    - utter_happy


## restaurant explain 2.1.1
* request_restaurant
    - utter_ask_details
* chitchat
    - utter_chitchat
    - utter_ask_details
* explain
    - utter_explain_details_restaurant
    - utter_ask_details
* inform{"people": "4"}
    - utter_ask_location
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_location
* chitchat
    - utter_chitchat
    - utter_ask_location
* inform{"location": "paris"}
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_cuisine
* correct{"location": "rome"}
    - utter_correct_location_restaurant
    - utter_ask_cuisine
* chitchat
    - utter_chitchat
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy


## restaurant explain 2.1.2
* request_restaurant
    - utter_ask_details
* explain
    - utter_explain_details_restaurant
    - utter_ask_details
* inform{"people": "4"}
    - utter_ask_location
* explain
    - utter_explain_location_restaurant
    - utter_ask_location
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_location
* chitchat
    - utter_chitchat
    - utter_ask_location
* inform{"location": "paris"}
    - utter_ask_price
* chitchat
    - utter_chitchat
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_cuisine
* correct{"price": "cheap"}
    - utter_correct_price_restaurant
    - utter_ask_cuisine
* chitchat
    - utter_chitchat
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy


## restaurant correction 1.4.1
* request_restaurant
    - utter_ask_details
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_details
* explain
    - utter_explain_details_restaurant
    - utter_ask_details
* inform{"location": "paris"}
    - utter_ask_people
* inform{"people": "4"}
    - utter_ask_price
* explain
    - utter_explain_price_restaurant
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_cuisine
* correct{"price": "cheap"}
    - utter_correct_price_restaurant
    - utter_ask_cuisine
* correct{"price": "expensive"}
    - utter_correct_price_restaurant
    - utter_ask_cuisine
* correct{"location": "rome"}
    - utter_correct_location_restaurant
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy


## restaurant correction 1.4.2
* request_restaurant
    - utter_ask_details
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_details
* chitchat
    - utter_chitchat
    - utter_ask_details
* inform{"location": "paris"}
    - utter_ask_people
* correct{"location": "paris"}
    - utter_correct_location_restaurant
    - utter_ask_people
* inform{"people": "4"}
    - utter_ask_price
* correct{"people": "3"}
    - utter_correct_people_restaurant
    - utter_ask_price
* explain
    - utter_explain_price_restaurant
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_cuisine
* correct{"price": "cheap"}
    - utter_correct_price_restaurant
    - utter_ask_cuisine
* chitchat
    - utter_chitchat
    - utter_ask_cuisine
* correct{"price": "expensive"}
    - utter_correct_price_restaurant
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy


## restaurant explain 4.4
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
* explain
    - utter_explain_people_restaurant
    - utter_ask_people
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_people
* chitchat
    - utter_chitchat
    - utter_ask_people
* chitchat
    - utter_chitchat
    - utter_ask_people
* correct{"price": "expensive"}
    - utter_correct_price_restaurant
    - utter_ask_people
* correct{"location": "london"}
    - utter_correct_location_restaurant
    - utter_ask_people
* inform{"people": "4"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy
