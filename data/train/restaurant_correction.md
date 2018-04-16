## restaurant correction 1
* request_restaurant
    - action_restaurant
* inform{"location": "paris"}
    - action_restaurant
* correct{"location": "italy"}
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

## restaurant correction 2
* request_restaurant
    - action_restaurant
* inform{"location": "paris"}
    - action_restaurant
* inform{"people": "4"}
    - action_restaurant
* correct{"people:"5""}
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

## restaurant correction 3
* request_restaurant
    - action_restaurant
* inform{"location": "paris"}
    - action_restaurant
* inform{"people": "4"}
    - action_restaurant
* inform{"price": "expensive"}
    - action_restaurant
* correct{"price": "cheap"}
    - action_restaurant
* inform{"cuisine": "italian"}
    - action_restaurant
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy

## restaurant correction 4
* request_restaurant
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
* correct{"cuisine": "italian"}
    - action_restaurant
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy
