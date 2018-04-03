# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from rasa_core.actions.forms import EntityFormField, FormAction
from services.apis import RestaurantAPI, HotelAPI


class ActionRestaurant(FormAction):

    RANDOMIZE = True

    REQUIRED_FIELDS = [
        EntityFormField("people", "people"),
        EntityFormField("location", "location"),
        EntityFormField("price", "price"),
        EntityFormField("cuisine", "cuisine")
    ]

    OPTIONAL_FIELDS = [
        EntityFormField("outdoor_seating", "outdoor_seating"),
        EntityFormField("reservations", "reservations"),
        EntityFormField("date_suitable", "date_suitable")
    ]

    def name(self):
        return "action_restaurant"

    def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_finish')
        return []


class ActionHotel(FormAction):

    REQUIRED_FIELDS = [
        EntityFormField("people", "people"),
        EntityFormField("location", "location"),
        EntityFormField("price", "price"),
        EntityFormField("date", "start_date"),
        EntityFormField("date", "end_date")
    ]

    OPTIONAL_FIELDS = [
        EntityFormField("has_gym", "has_gym"),
        EntityFormField("has_spa", "has_spa"),
        EntityFormField("breakfast", "breakfast")
    ]

    def name(self):
        return "action_hotel"

    def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_finish')
        return []


class ActionSearchRestaurant(Action):

    def name(self):
        return "action_search_restaurant"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_search')
        restaurant_api = RestaurantAPI()
        restaurant = restaurant_api.search(tracker.get_slot('cuisine'))

        return [SlotSet('restaurant', restaurant)]


class ActionSearchHotel(Action):

    def name(self):
        return "action_search_hotel"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_search')
        hotel_api = HotelAPI()
        hotel = hotel_api.search(tracker.get_slot('location'))

        return [SlotSet('hotel', hotel)]


class ActionExplain(Action):

    def name(self):
        return "action_explain"

    def run(self, dispatcher, tracker, domain):
        # TODO: actually implement this
        dispatcher.utter_message('This means blabla')

        return []
