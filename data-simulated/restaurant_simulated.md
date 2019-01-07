## Generated Story -5272153381260553507
* request_restaurant
    - restaurant: utter_ask_details
    - slot{"restaurant": null}
* inform{"people": "6"}
    - slot{"people": "6"}
    - restaurant: utter_ask_location
* did_that_work
    - did_that_work: utter_more_info_restaurant
    - did_that_work: utter_ask_location
* explain
    - explain: utter_explain_location_restaurant
    - explain: utter_ask_location
* inform{"location": "rome"}
    - slot{"location": "rome"}
    - restaurant: utter_ask_price
* inform{"price": "expensive"}
    - restaurant: utter_ask_cuisine
* inform{"cuisine": "italian"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* did_that_work
    - did_that_work: utter_worked_restaurant
    - did_that_work: utter_suggest_restaurant
* did_that_work
    - did_that_work: utter_worked_restaurant
    - did_that_work: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy


## Generated Story 8910081089962091554
* request_restaurant
    - restaurant: utter_ask_details
    - slot{"restaurant": null}
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - restaurant: utter_ask_price
* correct{"cuisine": "french"}
    - slot{"cuisine": "french"}
    - correct: utter_correct_cuisine_restaurant
    - correct: utter_ask_price
* correct{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - correct: utter_correct_cuisine_restaurant
    - correct: utter_ask_price
* inform{"price": "expensive"}
    - restaurant: utter_ask_location
* inform{"location": "london"}
    - slot{"location": "london"}
    - restaurant: utter_ask_people
* inform{"people": "1"}
    - slot{"people": "1"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* did_that_work
    - did_that_work: utter_worked_restaurant
    - did_that_work: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy


## Generated Story 8407838656397991270
* request_restaurant
    - restaurant: utter_ask_details
    - slot{"restaurant": null}
* inform{"cuisine": "french"}
    - slot{"cuisine": "french"}
    - restaurant: utter_ask_price
* inform{"price": "cheap"}
    - slot{"price": "cheap"}
    - restaurant: utter_ask_location
* inform{"location": "london"}
    - slot{"location": "london"}
    - restaurant: utter_ask_people
* inform{"people": "2"}
    - slot{"people": "2"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - slot{"restaurant":"results"}
    - restaurant: utter_suggest_restaurant
* correct{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - correct: utter_correct_cuisine_restaurant
    - correct: action_search_restaurant
    - slot{"restaurant":"results"}
    - correct: utter_suggest_restaurant
* correct{"people": "2"}
    - slot{"people": "2"}
    - correct: utter_correct_people_restaurant
    - correct: action_search_restaurant
    - slot{"restaurant":"results"}
    - correct: utter_suggest_restaurant
* correct{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - correct: utter_correct_price_restaurant
    - correct: action_search_restaurant
    - slot{"restaurant":"results"}
    - correct: utter_suggest_restaurant
* correct{"people": "4"}
    - slot{"people": "4"}
    - correct: utter_correct_people_restaurant
    - correct: action_search_restaurant
    - slot{"restaurant":"results"}
    - correct: utter_suggest_restaurant
* did_that_work
    - did_that_work: utter_worked_restaurant
    - did_that_work: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy

## Generated Story -3230699913544241199
* request_restaurant
    - restaurant: utter_ask_details
    - slot{"restaurant": null}
* inform{"cuisine": "french"}
    - slot{"cuisine": "french"}
    - restaurant: utter_ask_price
* inform{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - restaurant: utter_ask_location
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_location
* did_that_work
    - did_that_work: utter_more_info_restaurant
    - did_that_work: utter_ask_location
* did_that_work
    - did_that_work: utter_more_info_restaurant
    - did_that_work: utter_ask_location
* correct{"price": "expensive"}
    - slot{"price": "expensive"}
    - correct: utter_correct_price_restaurant
    - correct: utter_ask_location
* inform{"location": "paris"}
    - slot{"location": "paris"}
    - restaurant: utter_ask_people
* inform{"people": "2"}
    - slot{"people": "2"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* did_that_work
    - did_that_work: utter_worked_restaurant
    - did_that_work: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy


## Generated Story 1452092598283439681
* request_restaurant
    - restaurant: utter_ask_details
    - slot{"restaurant": null}
* inform{"location": "paris"}
    - slot{"location": "paris"}
    - restaurant: utter_ask_people
* correct{"location": "rome"}
    - slot{"location": "rome"}
    - correct: utter_correct_location_restaurant
    - correct: utter_ask_people
* explain
    - explain: utter_explain_people_restaurant
    - explain: utter_ask_people
* inform{"people": "4"}
    - slot{"people": "4"}
    - restaurant: utter_ask_price
* inform{"price": "expensive"}
    - slot{"price": "expensive"}
    - restaurant: utter_ask_cuisine
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* did_that_work
    - did_that_work: utter_worked_restaurant
    - did_that_work: utter_suggest_restaurant
* did_that_work
    - did_that_work: utter_worked_restaurant
    - did_that_work: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy


## Generated Story -1347297960370112371
* request_restaurant
    - restaurant: utter_ask_details
    - slot{"restaurant": null}
* inform{"location": "london"}
    - slot{"location": "london"}
    - restaurant: utter_ask_people
* explain
    - explain: utter_explain_people_restaurant
    - explain: utter_ask_people
* did_that_work
    - did_that_work: utter_more_info_restaurant
    - did_that_work: utter_ask_people
* inform{"people": "4"}
    - slot{"people": "4"}
    - restaurant: utter_ask_price
* inform{"price": "expensive"}
    - slot{"price": "expensive"}
    - restaurant: utter_ask_cuisine
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* did_that_work
    - did_that_work: utter_worked_restaurant
    - did_that_work: utter_suggest_restaurant
* did_that_work
    - did_that_work: utter_worked_restaurant
    - did_that_work: utter_suggest_restaurant
* did_that_work
    - did_that_work: utter_worked_restaurant
    - did_that_work: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy

## Generated Story 8130156986372571232
* request_restaurant
    - restaurant: utter_ask_details
    - slot{"restaurant": null}
* inform{"people": "4", "location": "paris"}
    - slot{"people": "4"}
    - slot{"location": "paris"}
    - restaurant: utter_ask_price
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_price
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_price
* did_that_work
    - did_that_work: utter_more_info_restaurant
    - did_that_work: utter_ask_price
* inform{"price": "expensive"}
    - slot{"price": "expensive"}
    - restaurant: utter_ask_cuisine
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* did_that_work
    - did_that_work: utter_worked_restaurant
    - did_that_work: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy


## Generated Story -800153815489499233
* request_restaurant
    - restaurant: utter_ask_details
    - slot{"restaurant": null}
* inform{"people": "6"}
    - slot{"people": "6"}
    - restaurant: utter_ask_location
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_location
* inform{"location": "paris"}
    - slot{"location": "paris"}
    - restaurant: utter_ask_price
* correct{"location": "rome"}
    - slot{"location": "rome"}
    - correct: utter_correct_location_restaurant
    - correct: utter_ask_price
* did_that_work
    - did_that_work: utter_more_info_restaurant
    - did_that_work: utter_ask_price
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_price
* inform{"price": "expensive"}
    - slot{"price": "expensive"}
    - restaurant: utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* did_that_work
    - did_that_work: utter_worked_restaurant
    - did_that_work: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy



## Generated Story 5854594747809472876
* request_restaurant
    - restaurant: utter_ask_details
    - slot{"restaurant": null}
* inform{"people": "6"}
    - slot{"people": "6"}
    - restaurant: utter_ask_location
* explain
    - explain: utter_explain_location_restaurant
    - explain: utter_ask_location
* inform{"location": "paris"}
    - slot{"location": "paris"}
    - restaurant: utter_ask_price
* inform{"price": "expensive"}
    - slot{"price": "expensive"}
    - restaurant: utter_ask_cuisine
* did_that_work
    - did_that_work: utter_more_info_restaurant
    - did_that_work: utter_ask_cuisine
* explain
    - explain: utter_explain_cuisine_restaurant
    - explain: utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* did_that_work
    - did_that_work: utter_worked_restaurant
    - did_that_work: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy




## Generated Story -6924676699065688022
* request_restaurant
    - restaurant: utter_ask_details
    - slot{"restaurant": null}
* inform{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - restaurant: utter_ask_people
* did_that_work
    - did_that_work: utter_more_info_restaurant
    - did_that_work: utter_ask_people
* correct{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - correct: utter_correct_price_restaurant
    - correct: utter_ask_people
* inform{"people": "2"}
    - slot{"people": "2"}
    - restaurant: utter_ask_location
* inform{"location": "paris"}
    - slot{"location": "paris"}
    - restaurant: utter_ask_cuisine
* inform{"cuisine": "italian"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* did_that_work
    - did_that_work: utter_worked_restaurant
    - did_that_work: utter_suggest_restaurant
* did_that_work
    - did_that_work: utter_worked_restaurant
    - did_that_work: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy


## Generated Story 8482744598176193653
* request_restaurant
    - restaurant: utter_ask_details
    - slot{"restaurant": null}
* inform{"cuisine": "french"}
    - slot{"cuisine": "french"}
    - restaurant: utter_ask_price
* explain
    - explain: utter_explain_price_restaurant
    - explain: utter_ask_price
* explain
    - explain: utter_explain_price_restaurant
    - explain: utter_ask_price
* inform{"price": "expensive"}
    - slot{"price": "expensive"}
    - restaurant: utter_ask_location
* inform{"location": "paris"}
    - slot{"location": "paris"}
    - restaurant: utter_ask_people
* inform{"people": "6"}
    - slot{"people": "6"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* did_that_work
    - did_that_work: utter_worked_restaurant
    - did_that_work: utter_suggest_restaurant
* did_that_work
    - did_that_work: utter_worked_restaurant
    - did_that_work: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy

 
## Generated Story -34984309837927831
* request_restaurant
    - restaurant: utter_ask_details
    - slot{"restaurant": null}
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - restaurant: utter_ask_price
* inform{"price": "expensive"}
    - slot{"price": "expensive"}
    - restaurant: utter_ask_location
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_location
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_location
* inform{"location": "london"}
    - slot{"location": "london"}
    - restaurant: utter_ask_people
* inform{"people": "4"}
    - slot{"people": "4"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - slot{"restaurant":"results"}
    - restaurant: utter_suggest_restaurant
* correct{"people": "4"}
    - slot{"people": "4"}
    - correct: utter_correct_people_restaurant
    - correct: action_search_restaurant
    - slot{"restaurant":"results"}
    - correct: utter_suggest_restaurant
* correct{"location": "rome"}
    - slot{"location": "rome"}
    - correct: utter_correct_location_restaurant
    - correct: action_search_restaurant
    - slot{"restaurant":"results"}
    - correct: utter_suggest_restaurant
* did_that_work
    - did_that_work: utter_worked_restaurant
    - did_that_work: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy

## Generated Story 3166112699919947742
* request_restaurant
    - restaurant: utter_ask_details
    - slot{"restaurant": null}
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - restaurant: utter_ask_price
* explain
    - explain: utter_explain_price_restaurant
    - explain: utter_ask_price
* inform{"price": "expensive"}
    - slot{"price": "expensive"}
    - restaurant: utter_ask_location
* inform{"location": "paris"}
    - slot{"location": "paris"}
    - restaurant: utter_ask_people
* did_that_work
    - did_that_work: utter_more_info_restaurant
    - did_that_work: utter_ask_people
* explain
    - explain: utter_explain_people_restaurant
    - explain: utter_ask_people
* inform{"people": "4"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* did_that_work
    - did_that_work: utter_worked_restaurant
    - did_that_work: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy


## Generated Story 8415484272864759934
* request_restaurant
    - restaurant: utter_ask_details
    - slot{"restaurant": null}
* inform{"people": "1"}
    - slot{"people": "1"}
    - restaurant: utter_ask_location
* inform{"location": "rome"}
    - slot{"location": "rome"}
    - restaurant: utter_ask_price
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_price
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_price
* correct{"people": "1"}
    - slot{"people": "1"}
    - correct: utter_correct_people_restaurant
    - correct: utter_ask_price
* inform{"price": "expensive"}
    - restaurant: utter_ask_cuisine
* inform{"cuisine": "italian"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* did_that_work
    - did_that_work: utter_worked_restaurant
    - did_that_work: utter_suggest_restaurant
* did_that_work
    - did_that_work: utter_worked_restaurant
    - did_that_work: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy


## Generated Story 8816761424745395625
* request_restaurant
    - restaurant: utter_ask_details
    - slot{"restaurant": null}
* inform{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - restaurant: utter_ask_people
* correct{"price": "expensive"}
    - slot{"price": "expensive"}
    - correct: utter_correct_price_restaurant
    - correct: utter_ask_people
* inform{"people": "6"}
    - slot{"people": "6"}
    - restaurant: utter_ask_cuisine
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - restaurant: utter_ask_location
* did_that_work
    - did_that_work: utter_more_info_restaurant
    - did_that_work: utter_ask_location
* explain
    - explain: utter_explain_location_restaurant
    - explain: utter_ask_location
* inform{"location": "paris"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* did_that_work
    - did_that_work: utter_worked_restaurant
    - did_that_work: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy


## Generated Story 1074034796281423152
* request_restaurant
    - restaurant: utter_ask_details
    - slot{"restaurant": null}
* inform{"people": "4", "cuisine": "french"}
    - slot{"people": "4"}
    - slot{"cuisine": "french"}
    - restaurant: utter_ask_price
* inform{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - restaurant: utter_ask_location
* explain
    - explain: utter_explain_location_restaurant
    - explain: utter_ask_location
* explain
    - explain: utter_explain_location_restaurant
    - explain: utter_ask_location
* inform{"location": "paris"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy


## Generated Story 5703123541088815095
* request_restaurant
    - restaurant: utter_ask_details
    - slot{"restaurant": null}
* inform{"location": "paris"}
    - slot{"location": "paris"}
    - restaurant: utter_ask_people
* correct{"location": "rome"}
    - slot{"location": "rome"}
    - correct: utter_correct_location_restaurant
    - correct: utter_ask_people
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_people
* correct{"location": "rome"}
    - slot{"location": "rome"}
    - correct: utter_correct_location_restaurant
    - correct: utter_ask_people
* inform{"people": "4"}
    - restaurant: utter_ask_price
* inform{"price": "expensive"}
    - restaurant: utter_ask_cuisine
* inform{"cuisine": "italian"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy


## Generated Story -1455208811812364750
* request_restaurant
    - restaurant: utter_ask_details
    - slot{"restaurant": null}
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - restaurant: utter_ask_price
* explain
    - explain: utter_explain_price_restaurant
    - explain: utter_ask_price
* inform{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - restaurant: utter_ask_location
* explain
    - explain: utter_explain_location_restaurant
    - explain: utter_ask_location
* inform{"location": "paris"}
    - restaurant: utter_ask_people
* inform{"people": "4"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy


## Generated Story 4438794933926816664
* request_restaurant
    - restaurant: utter_ask_details
    - slot{"restaurant": null}
* inform{"price": "expensive"}
    - slot{"price": "expensive"}
    - restaurant: utter_ask_people
* inform{"people": "6"}
    - slot{"people": "6"}
    - restaurant: utter_ask_cuisine
* did_that_work
    - did_that_work: utter_more_info_restaurant
    - did_that_work: utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - restaurant: utter_ask_location
* did_that_work
    - did_that_work: utter_more_info_restaurant
    - did_that_work: utter_ask_location
* inform{"location": "paris"}
    - slot{"location": "paris"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - slot{"restaurant":"results"}
    - restaurant: utter_suggest_restaurant
* correct{"cuisine": "french"}
    - slot{"cuisine": "french"}
    - correct: utter_correct_cuisine_restaurant
    - correct: action_search_restaurant
    - slot{"restaurant":"results"}
    - correct: utter_suggest_restaurant
* correct{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - correct: utter_correct_cuisine_restaurant
    - correct: action_search_restaurant
    - slot{"restaurant":"results"}
    - correct: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy


## Generated Story -6672029863110169452
* request_restaurant
    - restaurant: utter_ask_details
    - slot{"restaurant": null}
* inform{"location": "rome"}
    - slot{"location": "rome"}
    - restaurant: utter_ask_people
* correct{"location": "rome"}
    - slot{"location": "rome"}
    - correct: utter_correct_location_restaurant
    - correct: utter_ask_people
* inform{"people": "6"}
    - slot{"people": "6"}
    - restaurant: utter_ask_price
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_price
* explain
    - explain: utter_explain_price_restaurant
    - explain: utter_ask_price
* inform{"price": "expensive"}
    - restaurant: utter_ask_cuisine
* inform{"cuisine": "italian"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy


## Generated Story 5030307886271057142
* request_restaurant
    - restaurant: utter_ask_details
    - slot{"restaurant": null}
* inform{"location": "paris"}
    - slot{"location": "paris"}
    - restaurant: utter_ask_people
* explain
    - explain: utter_explain_people_restaurant
    - explain: utter_ask_people
* correct{"location": "paris"}
    - slot{"location": "paris"}
    - correct: utter_correct_location_restaurant
    - correct: utter_ask_people
* inform{"people": "4"}
    - restaurant: utter_ask_price
* inform{"price": "expensive"}
    - restaurant: utter_ask_cuisine
* inform{"cuisine": "italian"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy


## Generated Story 61924096214932807
* request_restaurant
    - restaurant: utter_ask_details
    - slot{"restaurant": null}
* inform{"location": "rome"}
    - slot{"location": "rome"}
    - restaurant: utter_ask_people
* inform{"people": "6"}
    - slot{"people": "6"}
    - restaurant: utter_ask_price
* explain
    - explain: utter_explain_price_restaurant
    - explain: utter_ask_price
* explain
    - explain: utter_explain_price_restaurant
    - explain: utter_ask_price
* inform{"price": "expensive"}
    - restaurant: utter_ask_cuisine
* inform{"cuisine": "italian"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy


## Generated Story -2820988936373814771
* request_restaurant
    - restaurant: utter_ask_details
    - slot{"restaurant": null}
* inform{"cuisine": "french"}
    - slot{"cuisine": "french"}
    - restaurant: utter_ask_price
* did_that_work
    - did_that_work: utter_more_info_restaurant
    - did_that_work: utter_ask_price
* inform{"price": "expensive"}
    - slot{"price": "expensive"}
    - restaurant: utter_ask_location
* did_that_work
    - did_that_work: utter_more_info_restaurant
    - did_that_work: utter_ask_location
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_location
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_location
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_location
* explain
    - explain: utter_explain_location_restaurant
    - explain: utter_ask_location
* inform{"location": "paris"}
    - restaurant: utter_ask_people
* inform{"people": "4"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy


## Generated Story -1960358913774682002
* request_restaurant
    - restaurant: utter_ask_details
    - slot{"restaurant": null}
* inform{"people": "4"}
    - slot{"people": "4"}
    - restaurant: utter_ask_location
* inform{"location": "paris"}
    - slot{"location": "paris"}
    - restaurant: utter_ask_price
* explain
    - explain: utter_explain_price_restaurant
    - explain: utter_ask_price
* did_that_work
    - did_that_work: utter_more_info_restaurant
    - did_that_work: utter_ask_price
* correct{"location": "london"}
    - slot{"location": "london"}
    - correct: utter_correct_location_restaurant
    - correct: utter_ask_price
* inform{"price": "expensive"}
    - restaurant: utter_ask_cuisine
* inform{"cuisine": "italian"}
    - restaurant: utter_filled_slots
    - restaurant: action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - restaurant: utter_suggest_restaurant
* affirm
    - restaurant: utter_happy
