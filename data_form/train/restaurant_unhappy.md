## restaurant explain 1
* request_restaurant
    - action_restaurant
* inform{"location": "paris"}
    - action_restaurant
* about
    - action_explain
    - action_restaurant
* inform{"people": "4"}
    - action_restaurant
* inform{"price": "expensive"}
    - action_restaurant
* inform{"cuisine": "italian"}
    - action_restaurant
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy

## restaurant explain 2
* request_restaurant
    - action_restaurant
* inform{"location": "paris"}
    - action_restaurant
* inform{"people": "4"}
    - action_restaurant
* about
    - action_explain
    - action_restaurant
* inform{"price": "expensive"}
    - action_restaurant
* inform{"cuisine": "italian"}
    - action_restaurant
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy

## restaurant explain 3
* request_restaurant
    - action_restaurant
* inform{"location": "paris"}
    - action_restaurant
* inform{"people": "4"}
    - action_restaurant
* inform{"price": "expensive"}
    - action_restaurant
* about
    - action_explain
    - action_restaurant
* inform{"cuisine": "italian"}
    - action_restaurant
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy

## restaurant explain 4
* request_restaurant
    - action_restaurant
* about
    - action_explain
    - action_restaurant
* inform{"location": "paris"}
    - action_restaurant
* inform{"people": "4"}
    - action_restaurant
* inform{"price": "expensive"}
    - action_restaurant
* inform{"cuisine": "italian"}
    - action_restaurant
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy

## restaurant didthatwork 2
* request_restaurant
    - action_restaurant
* inform{"location": "paris"}
    - action_restaurant
* did_that_work
    - utter_worked
    - action_restaurant
* inform{"people": "4"}
    - action_restaurant
* inform{"price": "expensive"}
    - action_restaurant
* inform{"cuisine": "italian"}
    - action_restaurant
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy

## restaurant didthatwork 3
* request_restaurant
    - action_restaurant
* inform{"location": "paris"}
    - action_restaurant
* inform{"people": "4"}
    - action_restaurant
* did_that_work
    - utter_worked
    - action_restaurant
* inform{"price": "expensive"}
    - action_restaurant
* inform{"cuisine": "italian"}
    - action_restaurant
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy

## restaurant didthatwork 3
* request_restaurant
    - action_restaurant
* inform{"location": "paris"}
    - action_restaurant
* inform{"people": "4"}
    - action_restaurant
* inform{"price": "expensive"}
    - action_restaurant
* did_that_work
    - utter_worked
    - action_restaurant
* inform{"cuisine": "italian"}
    - action_restaurant
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy
