# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
# he afegit l'acció de dir l'hora https://learning.rasa.com/conversational-ai-with-rasa/custom-actions/

from typing import Any, Text, Dict, List

import arrow 
from datetime import datetime, timezone

import pytz
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import lingua_franca
from lingua_franca.format import nice_date, nice_date_time, nice_time
from lingua_franca.time import default_timezone

lingua_franca.load_language('ca')


dies_db = {"Sun": "diumenge",
    "Mon": "dilluns",
    "Tue": "dimarts",
    "Wed": "dimecres",
    "Thu": "dijous",
    "Fri": "divendres",
    "Sat": "dissabte"}

mesos_db = {1: "gener",
    2: "febrer",
    3: "març",
    4: "abril",
    5: "maig",
    6: "juny",
    7: "juliol",
    8: "agost",
    9: "setembre",
    10: "octubre",
    11: "novembre",
    12: "desembre"}

class ActionTellCatalanTime(Action):

    def name(self) -> Text:
        return "action_tell_catalan_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
        x = datetime.now()        
        hora = nice_time(datetime.now(pytz.timezone('Europe/Madrid')), variant="full_bell")
        dia = x.strftime("%a")    
        if x.hour <= 13:
            salut = "Bon dia"
        elif x.hour < 21:
            salut = "Bona tarda"
        else:
            salut = "Bona nit"
        msg = f"{salut}, són {hora} del {dies_db[dia]} {x.day} de {mesos_db[x.month]}."
        #msg = "hola rata"
        dispatcher.utter_message(text=msg)
        
        return []


city_db = {
    'brussels': 'Europe/Brussels', 
    'zagreb': 'Europe/Zagreb',
    'london': 'Europe/Dublin',
    'lisbon': 'Europe/Lisbon',
    'amsterdam': 'Europe/Amsterdam',
    'seattle': 'US/Pacific'
}

class ActionTellTime(Action):

    def name(self) -> Text:
        return "action_tell_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        current_place = next(tracker.get_latest_entity_values("place"), None)
        utc = arrow.utcnow()
        
        if not current_place:
            msg = f"It's {utc.format('HH:mm')} utc now. You can also give me a place."
            dispatcher.utter_message(text=msg)
            return []
        
        tz_string = city_db.get(current_place, None)
        if not tz_string:
            msg = f"I didn't recognize {current_place}. Is it spelled correctly?"
            dispatcher.utter_message(text=msg)
            return []
                
        msg = f"It's {utc.to(city_db[current_place]).format('HH:mm')} in {current_place} now."
        dispatcher.utter_message(text=msg)
        
        return []

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []
