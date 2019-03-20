## Generated Story 7766790119829507991
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"people": "4"}
    - slot{"people": "4"}
    - hotel: utter_ask_location
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_location
* explain
    - explain: utter_explain_location_hotel
    - explain: utter_ask_location
* inform{"location": "paris"}
    - hotel: utter_ask_price
* inform{"price": "expensive"}
    - hotel: utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - hotel: utter_ask_enddate
* explain
    - explain: utter_explain_enddate_hotel
    - explain: utter_ask_enddate
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* did_that_work
    - did_that_work: utter_worked_hotel
    - did_that_work: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story -2030870466415802501
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"startdate": "today"}
    - slot{"startdate": "today"}
    - hotel: utter_ask_enddate
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_enddate
* inform{"enddate": "May 26th"}
    - slot{"enddate": "May 26th"}
    - hotel: utter_ask_price
* inform{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - hotel: utter_ask_location
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_location
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_location
* explain
    - explain: utter_explain_location_hotel
    - explain: utter_ask_location
* inform{"location": "paris"}
    - hotel: utter_ask_people
* inform{"people": "4"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* did_that_work
    - did_that_work: utter_worked_hotel
    - did_that_work: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story -299760704668345064
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"price": "expensive"}
    - slot{"price": "expensive"}
    - hotel: utter_ask_people
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_people
* explain
    - explain: utter_explain_people_hotel
    - explain: utter_ask_people
* inform{"people": "4"}
    - hotel: utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - hotel: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_ask_location
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_location
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_location
* inform{"location": "paris"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story -7795096423415267175
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"people": "1", "location": "rome"}
    - slot{"people": "1"}
    - slot{"location": "rome"}
    - hotel: utter_ask_price
* inform{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - hotel: utter_ask_startdate
* inform{"startdate": "May 25th"}
    - slot{"startdate": "May 25th"}
    - hotel: utter_ask_enddate
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_enddate
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* did_that_work
    - did_that_work: utter_worked_hotel
    - did_that_work: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story -3239466931270169949
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"location": "london"}
    - slot{"location": "london"}
    - hotel: utter_ask_people
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_people
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_people
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_people
* correct{"location": "london"}
    - slot{"location": "london"}
    - correct: utter_correct_location_hotel
    - correct: utter_ask_people
* inform{"people": "4"}
    - hotel: utter_ask_price
* inform{"price": "expensive"}
    - hotel: utter_ask_startdate
* explain
    - explain: utter_explain_startdate_hotel
    - explain: utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - hotel: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* correct{"enddate": "tomorrow"}
    - slot{"enddate": "tomorrow"}
    - correct: utter_correct_enddate_hotel
    - correct: action_search_hotel
    - slot{"hotel": "hotel"}
    - correct: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story -237418450323459652
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"enddate": "next week"}
    - slot{"enddate": "next week"}
    - hotel: utter_ask_startdate
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_startdate
* inform{"startdate": "May 25th"}
    - slot{"startdate": "May 25th"}
    - hotel: utter_ask_location
* correct{"enddate": "tomorrow"}
    - slot{"enddate": "tomorrow"}
    - correct: utter_correct_enddate_hotel
    - correct: utter_ask_location
* explain
    - explain: utter_explain_location_hotel
    - explain: utter_ask_location
* inform{"location": "paris"}
    - hotel: utter_ask_price
* inform{"price": "expensive"}
    - hotel: utter_ask_people
* inform{"people": "4"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* did_that_work
    - did_that_work: utter_worked_hotel
    - did_that_work: utter_suggest_hotel
* did_that_work
    - did_that_work: utter_worked_hotel
    - did_that_work: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story -602327959866684522
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - hotel: utter_ask_people
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_people
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_people
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_people
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_people
* correct{"price": "expensive"}
    - slot{"price": "expensive"}
    - correct: utter_correct_price_hotel
    - correct: utter_ask_people
* inform{"people": "4"}
    - hotel: utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - hotel: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_ask_location
* inform{"location": "paris"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* did_that_work
    - did_that_work: utter_worked_hotel
    - did_that_work: utter_suggest_hotel
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story -6156085551550358362
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - hotel: utter_ask_people
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_people
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_people
* inform{"people": "4"}
    - hotel: utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - hotel: utter_ask_enddate
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_enddate
* explain
    - explain: utter_explain_enddate_hotel
    - explain: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_ask_location
* inform{"location": "paris"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_suggest_hotel
* did_that_work
    - did_that_work: utter_worked_hotel
    - did_that_work: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story -3053018598832044299
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"enddate": "May 26th", "people": "2"}
    - slot{"enddate": "May 26th"}
    - slot{"people": "2"}
    - hotel: utter_ask_location
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
    - explain: utter_explain_location_hotel
    - explain: utter_ask_location
* inform{"location": "paris"}
    - hotel: utter_ask_startdate
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_startdate
* inform{"startdate": "May 25th"}
    - hotel: utter_ask_price
* explain
    - explain: utter_explain_price_hotel
    - explain: utter_ask_price
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_price
* inform{"price": "cheap"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story 7818253770017259687
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"enddate": "tomorrow"}
    - slot{"enddate": "tomorrow"}
    - hotel: utter_ask_startdate
* inform{"startdate": "today"}
    - slot{"startdate": "today"}
    - hotel: utter_ask_location
* inform{"location": "rome"}
    - slot{"location": "rome"}
    - hotel: utter_ask_price
* explain
    - explain: utter_explain_price_hotel
    - explain: utter_ask_price
* correct{"enddate": "May 26th"}
    - slot{"enddate": "May 26th"}
    - correct: utter_correct_enddate_hotel
    - correct: utter_ask_price
* inform{"price": "expensive"}
    - hotel: utter_ask_people
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_people
* inform{"people": "4"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story -7495521714392799214
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"people": "6"}
    - slot{"people": "6"}
    - hotel: utter_ask_location
* explain
    - explain: utter_explain_location_hotel
    - explain: utter_ask_location
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_location
* inform{"location": "paris"}
    - hotel: utter_ask_price
* inform{"price": "expensive"}
    - hotel: utter_ask_startdate
* inform{"startdate": "x"}
    - hotel: utter_ask_enddate
* correct{"startdate": "x"}
    - correct: utter_correct_startdate_hotel
    - correct: utter_ask_enddate
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_enddate
* inform{"startdate": "10.03.2018"}
    - hotel: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story -6349392819907338742
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"people": "6"}
    - slot{"people": "6"}
    - hotel: utter_ask_location
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_location
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_location
* inform{"location": "rome"}
    - slot{"location": "rome"}
    - hotel: utter_ask_price
* explain
    - explain: utter_explain_price_hotel
    - explain: utter_ask_price
* inform{"price": "expensive"}
    - slot{"price": "expensive"}
    - hotel: utter_ask_startdate
* inform{"startdate": "May 25th"}
    - slot{"startdate": "May 25th"}
    - hotel: utter_ask_enddate
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* did_that_work
    - did_that_work: utter_worked_hotel
    - did_that_work: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story 7949095044941412672
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"location": "paris"}
    - slot{"location": "paris"}
    - hotel: utter_ask_people
* inform{"people": "1"}
    - slot{"people": "1"}
    - hotel: utter_ask_price
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_price
* inform{"price": "expensive"}
    - hotel: utter_ask_startdate
* explain
    - explain: utter_explain_startdate_hotel
    - explain: utter_ask_startdate
* explain
    - explain: utter_explain_startdate_hotel
    - explain: utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - hotel: utter_ask_enddate
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_enddate
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* did_that_work
    - did_that_work: utter_worked_hotel
    - did_that_work: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story 3476594150763939797
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - hotel: utter_ask_people
* correct{"price": "cheap"}
    - slot{"price": "cheap"}
    - correct: utter_correct_price_hotel
    - correct: utter_ask_people
* explain
    - explain: utter_explain_people_hotel
    - explain: utter_ask_people
* explain
    - explain: utter_explain_people_hotel
    - explain: utter_ask_people
* inform{"people": "2"}
    - slot{"people": "2"}
    - hotel: utter_ask_startdate
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_startdate
* explain
    - explain: utter_explain_startdate_hotel
    - explain: utter_ask_startdate
* correct{"people": "4"}
    - slot{"people": "4"}
    - correct: utter_correct_people_hotel
    - correct: utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - hotel: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_ask_location
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_location
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_location
* inform{"location": "paris"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* did_that_work
    - did_that_work: utter_worked_hotel
    - did_that_work: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story 3617952478188475803
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"price": "cheap"}
    - slot{"price": "cheap"}
    - hotel: utter_ask_people
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_people
* explain
    - explain: utter_explain_people_hotel
    - explain: utter_ask_people
* inform{"people": "4"}
    - hotel: utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - hotel: utter_ask_enddate
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_ask_location
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_location
* inform{"location": "paris"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story 4414493161134452794
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"enddate": "May 26th"}
    - slot{"enddate": "May 26th"}
    - hotel: utter_ask_startdate
* correct{"enddate": "May 26th"}
    - slot{"enddate": "May 26th"}
    - correct: utter_correct_enddate_hotel
    - correct: utter_ask_startdate
* explain
    - explain: utter_explain_startdate_hotel
    - explain: utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - hotel: utter_ask_location
* inform{"location": "paris"}
    - hotel: utter_ask_price
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_price
* explain
    - explain: utter_explain_price_hotel
    - explain: utter_ask_price
* inform{"price": "expensive"}
    - hotel: utter_ask_people
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_people
* inform{"people": "4"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* did_that_work
    - did_that_work: utter_worked_hotel
    - did_that_work: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story -4910041025741432607
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"people": "2"}
    - slot{"people": "2"}
    - hotel: utter_ask_location
* inform{"location": "rome"}
    - slot{"location": "rome"}
    - hotel: utter_ask_price
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_price
* inform{"price": "expensive"}
    - hotel: utter_ask_startdate
* correct{"location": "x"}
    - correct: utter_correct_location_hotel
    - correct: utter_ask_startdate
* correct{"people": "x"}
    - correct: utter_correct_people_hotel
    - correct: utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - hotel: utter_ask_enddate
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* did_that_work
    - did_that_work: utter_worked_hotel
    - did_that_work: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story 6324047640260901740
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"people": "6"}
    - slot{"people": "6"}
    - hotel: utter_ask_location
* correct{"people": "4"}
    - slot{"people": "4"}
    - correct: utter_correct_people_hotel
    - correct: utter_ask_location
* correct{"people": "1"}
    - slot{"people": "1"}
    - correct: utter_correct_people_hotel
    - correct: utter_ask_location
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_location
* explain
    - explain: utter_explain_location_hotel
    - explain: utter_ask_location
* inform{"location": "paris"}
    - hotel: utter_ask_price
* inform{"price": "expensive"}
    - hotel: utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - hotel: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* did_that_work
    - did_that_work: utter_worked_hotel
    - did_that_work: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story -4599886154708247544
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"people": "2"}
    - slot{"people": "2"}
    - hotel: utter_ask_location
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_location
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_location
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_location
* inform{"location": "paris"}
    - hotel: utter_ask_price
* inform{"price": "expensive"}
    - hotel: utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - hotel: utter_ask_enddate
* explain
    - explain: utter_explain_enddate_hotel
    - explain: utter_ask_enddate
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_enddate
* explain
    - explain: utter_explain_enddate_hotel
    - explain: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story -1624530263152194104
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - hotel: utter_ask_people
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_people
* correct{"price": "expensive"}
    - slot{"price": "expensive"}
    - correct: utter_correct_price_hotel
    - correct: utter_ask_people
* inform{"people": "4"}
    - hotel: utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - hotel: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_ask_location
* correct{"price": "expensive"}
    - slot{"price": "expensive"}
    - correct: utter_correct_price_hotel
    - correct: utter_ask_location
* correct{"price": "expensive"}
    - slot{"price": "expensive"}
    - correct: utter_correct_price_hotel
    - correct: utter_ask_location
* correct{"price": "expensive"}
    - slot{"price": "expensive"}
    - correct: utter_correct_price_hotel
    - correct: utter_ask_location
* inform{"location": "paris"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* did_that_work
    - did_that_work: utter_worked_hotel
    - did_that_work: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story 7259100936302585405
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"people": "2"}
    - slot{"people": "2"}
    - hotel: utter_ask_location
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_location
* inform{"location": "rome"}
    - slot{"location": "rome"}
    - hotel: utter_ask_price
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_price
* correct{"people": "1"}
    - slot{"people": "1"}
    - correct: utter_correct_people_hotel
    - correct: utter_ask_price
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_price
* inform{"price": "expensive"}
    - hotel: utter_ask_startdate
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - hotel: utter_ask_enddate
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* did_that_work
    - did_that_work: utter_worked_hotel
    - did_that_work: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story 3133736278245936594
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"people": "1"}
    - slot{"people": "1"}
    - hotel: utter_ask_location
* correct{"people": "1"}
    - slot{"people": "1"}
    - correct: utter_correct_people_hotel
    - correct: utter_ask_location
* explain
    - explain: utter_explain_location_hotel
    - explain: utter_ask_location
* inform{"location": "paris"}
    - hotel: utter_ask_price
* inform{"price": "expensive"}
    - hotel: utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - hotel: utter_ask_enddate
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_enddate
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_enddate
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_enddate
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story -7134039207768445094
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"price": "expensive"}
    - slot{"price": "expensive"}
    - hotel: utter_ask_people
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_people
* correct{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - correct: utter_correct_price_hotel
    - correct: utter_ask_people
* inform{"people": "4"}
    - hotel: utter_ask_startdate
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_startdate
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_startdate
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_startdate
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - hotel: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_ask_location
* inform{"location": "paris"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* did_that_work
    - did_that_work: utter_worked_hotel
    - did_that_work: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story -4990020259764681915
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"enddate": "May 26th"}
    - slot{"enddate": "May 26th"}
    - hotel: utter_ask_startdate
* correct{"enddate": "tomorrow"}
    - slot{"enddate": "tomorrow"}
    - correct: utter_correct_enddate_hotel
    - correct: utter_ask_startdate
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - hotel: utter_ask_location
* inform{"location": "paris"}
    - hotel: utter_ask_price
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_price
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_price
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_price
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_price
* inform{"price": "expensive"}
    - hotel: utter_ask_people
* inform{"people": "4"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* did_that_work
    - did_that_work: utter_worked_hotel
    - did_that_work: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story 7206195975968153047
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"price": "cheap"}
    - slot{"price": "cheap"}
    - hotel: utter_ask_people
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_people
* correct{"price": "cheap"}
    - slot{"price": "cheap"}
    - correct: utter_correct_price_hotel
    - correct: utter_ask_people
* inform{"people": "4"}
    - hotel: utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - hotel: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_ask_location
* inform{"location": "paris"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* did_that_work
    - did_that_work: utter_worked_hotel
    - did_that_work: utter_suggest_hotel
* did_that_work
    - did_that_work: utter_worked_hotel
    - did_that_work: utter_suggest_hotel
* did_that_work
    - did_that_work: utter_worked_hotel
    - did_that_work: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story -1942533987084426839
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"startdate": "May 25th", "location": "paris", "people": "6"}
    - slot{"startdate": "May 25th"}
    - slot{"location": "paris"}
    - slot{"people": "6"}
    - hotel: utter_ask_price
* correct{"startdate": "May 25th"}
    - slot{"startdate": "May 25th"}
    - correct: utter_correct_startdate_hotel
    - correct: utter_ask_price
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_price
* inform{"price": "expensive"}
    - hotel: utter_ask_enddate
* explain
    - explain: utter_explain_enddate_hotel
    - explain: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* did_that_work
    - did_that_work: utter_worked_hotel
    - did_that_work: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story -5573273196872942075
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"people": "2"}
    - slot{"people": "2"}
    - hotel: utter_ask_location
* correct{"people": "2"}
    - slot{"people": "2"}
    - correct: utter_correct_people_hotel
    - correct: utter_ask_location
* explain
    - explain: utter_explain_location_hotel
    - explain: utter_ask_location
* inform{"location": "paris"}
    - hotel: utter_ask_price
* inform{"price": "expensive"}
    - hotel: utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - hotel: utter_ask_enddate
* explain
    - explain: utter_explain_enddate_hotel
    - explain: utter_ask_enddate
* explain
    - explain: utter_explain_enddate_hotel
    - explain: utter_ask_enddate
* explain
    - explain: utter_explain_enddate_hotel
    - explain: utter_ask_enddate
* explain
    - explain: utter_explain_enddate_hotel
    - explain: utter_ask_enddate
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* did_that_work
    - did_that_work: utter_worked_hotel
    - did_that_work: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story 7692376286038639225
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"startdate": "today", "price": "expensive"}
    - slot{"startdate": "today"}
    - slot{"price": "expensive"}
    - hotel: utter_ask_enddate
* correct{"startdate": "May 25th"}
    - slot{"startdate": "May 25th"}
    - correct: utter_correct_startdate_hotel
    - correct: utter_ask_enddate
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_ask_location
* inform{"location": "paris"}
    - hotel: utter_ask_people
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_people
* inform{"people": "4"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* did_that_work
    - did_that_work: utter_worked_hotel
    - did_that_work: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story 2895329045844006457
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"enddate": "next week"}
    - slot{"enddate": "next week"}
    - hotel: utter_ask_startdate
* explain
    - explain: utter_explain_startdate_hotel
    - explain: utter_ask_startdate
* explain
    - explain: utter_explain_startdate_hotel
    - explain: utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - hotel: utter_ask_location
* inform{"location": "paris"}
    - hotel: utter_ask_price
* inform{"price": "expensive"}
    - hotel: utter_ask_people
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_people
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_people
* inform{"people": "4"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* did_that_work
    - did_that_work: utter_worked_hotel
    - did_that_work: utter_suggest_hotel
* affirm
    - hotel: utter_happy

## Generated Story 3386821266887612770
* request_hotel
    - hotel: utter_ask_details
    - slot{"hotel": null}
* inform{"startdate": "May 25th"}
    - slot{"startdate": "May 25th"}
    - hotel: utter_ask_enddate
* correct{"startdate": "next week"}
    - slot{"startdate": "next week"}
    - correct: utter_correct_startdate_hotel
    - correct: utter_ask_enddate
* correct{"startdate": "next week"}
    - slot{"startdate": "next week"}
    - correct: utter_correct_startdate_hotel
    - correct: utter_ask_enddate
* chitchat
    - chitchat: utter_chitchat
    - chitchat: utter_ask_enddate
* explain
    - explain: utter_explain_enddate_hotel
    - explain: utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - hotel: utter_ask_price
* inform{"price": "expensive"}
    - hotel: utter_ask_location
* inform{"location": "paris"}
    - hotel: utter_ask_people
* correct{"location": "rome"}
    - correct: utter_correct_location_hotel
    - correct: utter_ask_people
* correct{"price": "cheap"}
    - correct: utter_correct_price_hotel
    - correct: utter_ask_people
* did_that_work
    - did_that_work: utter_more_info_hotel
    - did_that_work: utter_ask_people
* inform{"people": "4"}
    - hotel: utter_filled_slots
    - hotel: action_search_hotel
    - slot{"hotel": "hotel"}
    - hotel: utter_suggest_hotel
* did_that_work
    - did_that_work: utter_worked_hotel
    - did_that_work: utter_suggest_hotel
* affirm
    - hotel: utter_happy

