# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from services.apis import RestaurantAPI, HotelAPI


class ActionSearchRestaurant(Action):

    def name(self):
        return "action_search_restaurant"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_search', tracker)
        restaurant_api = RestaurantAPI()
        restaurant = restaurant_api.search(tracker.get_slot('cuisine'))

        return [SlotSet('restaurant', restaurant)]


class ActionSearchHotel(Action):

    def name(self):
        return "action_search_hotel"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_search', tracker)
        hotel_api = HotelAPI()
        hotel = hotel_api.search(tracker.get_slot('location'))

        return [SlotSet('hotel', hotel)]
