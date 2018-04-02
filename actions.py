# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from rasa_core.actions.forms import EntityFormField, FormAction


class ActionRestaurant(FormAction):

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
        dispatcher.utter_template('utter_search')
        return [SlotSet('restaurant', 'restaurant 1')]


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
        dispatcher.utter_template('utter_search')
        return [SlotSet('hotel', 'hotel 1')]
