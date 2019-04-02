## not new to rasa + nlu + unknown topic
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + tool recommendation
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* nlu_generation_tool_recommendation
    - utter_nlu_tools   <!-- predicted: utter_offer_recommendation -->


## not new to rasa + nlu + entity + no recommendation
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* deny
    - chitchat: utter_thumbsup
    - chitchat: utter_anything_else


## Prompt -> Contribute
* get_started_step4
    - greet_success: action_greet_user
* ask_why_contribute
    - utter_reasons_to_contribute   <!-- predicted: utter_possibilities_to_contribute -->
* ask_how_contribute
    - getstarted_4_success: utter_possibilities_to_contribute


## not new to rasa + nlu + entity + pipeline spacy
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "name"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_spacy"}
    - rasa_help_success: utter_spacy
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline spacy
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "name"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_spacy"}
    - rasa_help_success: utter_spacy
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline ner_crf
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "some custom entity"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_crf"}
    - rasa_help_success: utter_crf
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline ner_crf
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "some custom entity"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_crf"}
    - rasa_help_success: utter_crf
    - chitchat: utter_anything_else


## skip to info on nlu entities
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation


## switch immediately to luis
* switch{"current_api": "luis"}
    - slot{"current_api": "luis"}
    - utter_switch_luis   <!-- predicted: utter_switch_dialogflow -->
    - chitchat: utter_anything_else


## source code
* source_code
    - utter_source_code   <!-- predicted: utter_rasa_cost -->
    - chitchat: utter_anything_else


## bye
* bye
    - utter_bye   <!-- predicted: utter_nlu_tools -->


## next step prompt
* next_step
    - action_next_step   <!-- predicted: utter_bye -->


## Contribute
* ask_why_contribute
    - utter_reasons_to_contribute   <!-- predicted: utter_possibilities_to_contribute -->
* ask_how_contribute
    - getstarted_4_success: utter_possibilities_to_contribute


## positive reaction
* react_positive
    - utter_react_positive   <!-- predicted: utter_nohelp -->


## negative reaction
* react_negative
    - utter_react_negative   <!-- predicted: utter_react_positive -->


## feedback1
    - feedback: utter_ask_feedback
* out_of_scope
    - feedback_success: utter_thumbsup
    - utter_anything_else   <!-- predicted: action_listen -->


## feedback2
    - feedback: utter_ask_feedback
* enter_data
    - feedback_success: utter_thumbsup
    - utter_anything_else   <!-- predicted: action_listen -->


## feedback3
    - feedback: utter_ask_feedback
* affirm
    - utter_great   <!-- predicted: utter_thumbsup -->
    - utter_anything_else   <!-- predicted: utter_ask_pip_or_conda -->


## feedback deny
    - feedback: utter_ask_feedback
* deny
    - feedback_success: utter_thumbsup
    - utter_anything_else   <!-- predicted: action_listen -->


## Prompt -> Get help in forum
* get_started_step4
    - greet_success: action_greet_user
* ask_question_in_forum
    - utter_link_to_forum   <!-- predicted: utter_possibilities_to_contribute -->


## Get help in the forum
* ask_question_in_forum
    - utter_link_to_forum   <!-- predicted: utter_possibilities_to_contribute -->


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* ask_weather
    - chitchat: action_chitchat
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* ask_builder
    - chitchat: action_chitchat
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* ask_howdoing
    - chitchat: action_chitchat
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* ask_whoisit
    - chitchat: action_chitchat
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* ask_whatisrasa
    - chitchat: action_chitchat
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* ask_isbot
    - chitchat: action_chitchat
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* ask_howold
    - chitchat: action_chitchat
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* ask_languagesbot
    - chitchat: action_chitchat
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* ask_restaurant
    - chitchat: action_chitchat
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* ask_time
    - chitchat: action_chitchat
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* ask_wherefrom
    - chitchat: action_chitchat
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* ask_whoami
    - chitchat: action_chitchat
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* handleinsult
    - chitchat: action_chitchat
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nicetomeeyou
    - chitchat: action_chitchat
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* telljoke
    - chitchat: action_chitchat
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* ask_whatismyname
    - chitchat: action_chitchat
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* howwereyoubuilt
    - chitchat: action_chitchat
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## transition from step 2
* get_started_step2
    - greet_success: action_greet_user
    - slot{"step": "2"}
    - getstarted_2: utter_direct_step3
* get_started_step3
    - greet_success: action_greet_user
    - slot{"step": "3"}
* install_rasa
    - getstarted_3: utter_ask_python_installed
* affirm
    - utter_ask_pip_or_conda   <!-- predicted: utter_ask_python_installed -->


## transition from step 2
* get_started_step2
    - greet_success: action_greet_user
    - slot{"step": "2"}
    - getstarted_2: utter_direct_step3
* get_started_step3
    - greet_success: action_greet_user
    - slot{"step": "3"}
* affirm
    - getstarted_3: utter_ask_python_installed
* affirm
    - utter_ask_pip_or_conda   <!-- predicted: utter_ask_python_installed -->


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* ask_weather
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* ask_weather
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* ask_builder
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* ask_builder
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* ask_howdoing
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* ask_howdoing
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* ask_whoisit
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* ask_whoisit
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* ask_whatisrasa
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* ask_whatisrasa
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* ask_isbot
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* ask_isbot
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* ask_howold
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* ask_howold
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* ask_languagesbot
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* ask_languagesbot
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* ask_restaurant
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* ask_restaurant
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* ask_time
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* ask_time
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* ask_wherefrom
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* ask_wherefrom
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* ask_whoami
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* ask_whoami
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* handleinsult
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* handleinsult
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* nicetomeeyou
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* nicetomeeyou
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* telljoke
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* telljoke
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* ask_whatismyname
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* ask_whatismyname
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* howwereyoubuilt
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* howwereyoubuilt
    - chitchat: action_chitchat
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_weather
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_builder
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_howdoing
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_whoisit
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_whatisrasa
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_isbot
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_howold
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_languagesbot
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_restaurant
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_time
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_wherefrom
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_whoami
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* handleinsult
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* nicetomeeyou
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* telljoke
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_whatismyname
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* howwereyoubuilt
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_weather
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_builder
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_howdoing
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_whoisit
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_whatisrasa
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_isbot
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_howold
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_languagesbot
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_restaurant
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_time
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_wherefrom
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_whoami
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* handleinsult
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* nicetomeeyou
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* telljoke
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_whatismyname
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* howwereyoubuilt
    - chitchat: action_chitchat
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* ask_weather
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* ask_weather
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* ask_builder
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* ask_builder
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* ask_howdoing
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* ask_howdoing
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* ask_whoisit
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* ask_whoisit
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* ask_whatisrasa
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* ask_whatisrasa
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* ask_isbot
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* ask_isbot
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* ask_howold
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* ask_howold
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* ask_languagesbot
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* ask_languagesbot
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* ask_restaurant
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* ask_restaurant
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* ask_time
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* ask_time
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* ask_wherefrom
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* ask_wherefrom
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* ask_whoami
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* ask_whoami
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* handleinsult
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* handleinsult
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* nicetomeeyou
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* nicetomeeyou
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* telljoke
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* telljoke
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* ask_whatismyname
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* ask_whatismyname
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* howwereyoubuilt
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* howwereyoubuilt
    - chitchat: action_chitchat
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## Story from conversation with alan on November 16th 2018 2
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* enter_data{"language": "spanish"}
    - slot{"language": "spanish"}
    - slot{"language": "spanish"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa


## Story from conversation with dominik on November 19th 2018
* greet
    - greet_success: action_greet_user
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* switch{"current_api": "luis"}
    - slot{"current_api": "luis"}
    - slot{"current_api": "luis"}
    - utter_switch_luis   <!-- predicted: utter_switch_dialogflow -->
    - chitchat: utter_anything_else
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - slot{"product": "core"}
    - getstarted_1: utter_explain_core
    - chitchat: utter_anything_else
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - getstarted_1: utter_explain_nlu
    - chitchat: utter_anything_else


## Story from conversation with dominik
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* enter_data{"language": "spanish"}
    - slot{"language": "spanish"}
    - slot{"language": "spanish"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else
* enter_data{"language": "french"}
    - slot{"language": "french"}
    - slot{"language": "spanish"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## Story from conversation with af5a6b3c39d04c6db2b682960e63f01c on January 21st 2019
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_chitchat
* contact_sales
    - sales: utter_moreinformation
    - sales: utter_ask_jobfunction
* react_positive
    - utter_react_positive   <!-- predicted: utter_canthelp -->
* enter_data{"jobfunction": "dancer"}
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities


## Story from conversation with 4a4e903fc43940db9ccdb9153dfdadcb on January 21st 2019
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
    - slot{"step": "1"}
* install_rasa
    - getstarted_3: utter_ask_python_installed
* affirm
    - utter_ask_pip_or_conda   <!-- predicted: utter_ask_python_installed -->
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* enter_data
    - getstarted_3: action_store_problem_description
    - slot{"problem_description": "tensorflow 1.10.0 has requirement numpy<=1.14.5,>=1.13.3, but you'll have numpy 1.16.0 which is incompatible."}
    - utter_direct_to_forum_for_help   <!-- predicted: utter_direct_to_step4 -->
    - getstarted_3_success: utter_direct_to_step4
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities


## transition from step 2
* get_started_step2
    - greet_success: action_greet_user
    - slot{"step": "2"}
    - getstarted_2: utter_direct_step3
* get_started_step3
    - greet_success: action_greet_user
    - slot{"step": "3"}
* install_rasa
    - getstarted_3: utter_ask_python_installed
* deny
    - getstarted_3: utter_get_python
    - utter_ask_pip_or_conda   <!-- predicted: utter_ask_python_installed -->


## transition from step 2
* get_started_step2
    - greet_success: action_greet_user
    - slot{"step": "2"}
    - getstarted_2: utter_direct_step3
* get_started_step3
    - greet_success: action_greet_user
    - slot{"step": "3"}
* affirm
    - getstarted_3: utter_ask_python_installed
* deny
    - getstarted_3: utter_get_python
    - utter_ask_pip_or_conda   <!-- predicted: utter_ask_python_installed -->


## Install Rasa: Happy Path
* install_rasa
    - getstarted_3: utter_ask_python_installed
* affirm
    - utter_ask_pip_or_conda   <!-- predicted: utter_ask_python_installed -->
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* affirm
    - getstarted_3: utter_get_starter_pack
    - getstarted_3_success: utter_direct_to_step4


## Install Rasa: Happy Path
* get_started_step3
    - greet_success: action_greet_user
    - slot{"step": "3"}
* install_rasa
    - getstarted_3: utter_ask_python_installed
* affirm
    - utter_ask_pip_or_conda   <!-- predicted: utter_ask_python_installed -->
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* affirm
    - getstarted_3: utter_get_starter_pack
    - getstarted_3_success: utter_direct_to_step4


## Install Rasa: Happy Path
* get_started_step3
    - greet_success: action_greet_user
    - slot{"step": "3"}
* affirm
    - getstarted_3: utter_ask_python_installed
* affirm
    - utter_ask_pip_or_conda   <!-- predicted: utter_ask_python_installed -->
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* affirm
    - getstarted_3: utter_get_starter_pack
    - getstarted_3_success: utter_direct_to_step4


## Install Rasa: No Python installed
* install_rasa
    - getstarted_3: utter_ask_python_installed
* deny
    - getstarted_3: utter_get_python
    - utter_ask_pip_or_conda   <!-- predicted: utter_ask_python_installed -->
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build


## Install Rasa: Ask Python installed -> Which version
* install_rasa
    - getstarted_3: utter_ask_python_installed
* ask_faq_python_version
    - faq: action_faqs
    - utter_get_python   <!-- predicted: utter_ask_python_installed -->
    - utter_ask_pip_or_conda   <!-- predicted: utter_ask_python_installed -->
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build


## Install Rasa: Deny ready to build -> Ask if problem -> Yes
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* deny
    - getstarted_3: utter_ask_if_problem
* affirm
    - getstarted_3: utter_ask_describe_problem
* technical_question
    - getstarted_3: action_store_problem_description
    - utter_direct_to_forum_for_help   <!-- predicted: utter_direct_to_step4 -->
    - getstarted_3_success: utter_direct_to_step4


## Install Rasa: Deny ready to build -> Ask if problem -> Yes
* install_rasa{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* deny
    - getstarted_3: utter_ask_if_problem
* affirm
    - getstarted_3: utter_ask_describe_problem
* technical_question
    - getstarted_3: action_store_problem_description
    - utter_direct_to_forum_for_help   <!-- predicted: utter_direct_to_step4 -->
    - getstarted_3_success: utter_direct_to_step4


## Install Rasa: Deny ready to build -> Ask if problem -> Yes
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* deny
    - getstarted_3: utter_ask_if_problem
* affirm
    - getstarted_3: utter_ask_describe_problem
* enter_data
    - getstarted_3: action_store_problem_description
    - utter_direct_to_forum_for_help   <!-- predicted: utter_direct_to_step4 -->
    - getstarted_3_success: utter_direct_to_step4


## Install Rasa: Deny ready to build -> Ask if problem -> Yes
* install_rasa{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* deny
    - getstarted_3: utter_ask_if_problem
* affirm
    - getstarted_3: utter_ask_describe_problem
* enter_data
    - getstarted_3: action_store_problem_description
    - utter_direct_to_forum_for_help   <!-- predicted: utter_direct_to_step4 -->
    - getstarted_3_success: utter_direct_to_step4


## Install Rasa: Deny ready to build -> Ask if problem -> Yes
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* deny
    - getstarted_3: utter_ask_if_problem
* affirm
    - getstarted_3: utter_ask_describe_problem
* out_of_scope
    - getstarted_3: action_store_problem_description
    - utter_direct_to_forum_for_help   <!-- predicted: utter_direct_to_step4 -->
    - getstarted_3_success: utter_direct_to_step4


## Install Rasa: Deny ready to build -> Ask if problem -> Yes
* install_rasa{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* deny
    - getstarted_3: utter_ask_if_problem
* affirm
    - getstarted_3: utter_ask_describe_problem
* out_of_scope
    - getstarted_3: action_store_problem_description
    - utter_direct_to_forum_for_help   <!-- predicted: utter_direct_to_step4 -->
    - getstarted_3_success: utter_direct_to_step4


## Install Rasa: Deny ready to build -> Ask if problem -> technical question
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* deny
    - getstarted_3: utter_ask_if_problem
* technical_question
    - getstarted_3: action_store_problem_description
    - utter_direct_to_forum_for_help   <!-- predicted: utter_direct_to_step4 -->
    - getstarted_3_success: utter_direct_to_step4


## Install Rasa: Deny ready to build -> Ask if problem -> technical question
* install_rasa{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* deny
    - getstarted_3: utter_ask_if_problem
* technical_question
    - getstarted_3: action_store_problem_description
    - utter_direct_to_forum_for_help   <!-- predicted: utter_direct_to_step4 -->
    - getstarted_3_success: utter_direct_to_step4


## Install Rasa: Deny ready to build -> Ask if problem -> technical question
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* deny
    - getstarted_3: utter_ask_if_problem
* enter_data
    - getstarted_3: action_store_problem_description
    - utter_direct_to_forum_for_help   <!-- predicted: utter_direct_to_step4 -->
    - getstarted_3_success: utter_direct_to_step4


## Install Rasa: Deny ready to build -> Ask if problem -> technical question
* install_rasa{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* deny
    - getstarted_3: utter_ask_if_problem
* enter_data
    - getstarted_3: action_store_problem_description
    - utter_direct_to_forum_for_help   <!-- predicted: utter_direct_to_step4 -->
    - getstarted_3_success: utter_direct_to_step4


## Install Rasa: Deny ready to build -> Ask if problem -> technical question
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* deny
    - getstarted_3: utter_ask_if_problem
* out_of_scope
    - getstarted_3: action_store_problem_description
    - utter_direct_to_forum_for_help   <!-- predicted: utter_direct_to_step4 -->
    - getstarted_3_success: utter_direct_to_step4


## Install Rasa: Deny ready to build -> Ask if problem -> technical question
* install_rasa{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* deny
    - getstarted_3: utter_ask_if_problem
* out_of_scope
    - getstarted_3: action_store_problem_description
    - utter_direct_to_forum_for_help   <!-- predicted: utter_direct_to_step4 -->
    - getstarted_3_success: utter_direct_to_step4


## Install Rasa: Ask ready to build -> Problem
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* technical_question
    - getstarted_3: action_store_problem_description
    - utter_direct_to_forum_for_help   <!-- predicted: utter_direct_to_step4 -->
    - getstarted_3_success: utter_direct_to_step4


## Install Rasa: Ask ready to build -> Problem
* install_rasa{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* technical_question
    - getstarted_3: action_store_problem_description
    - utter_direct_to_forum_for_help   <!-- predicted: utter_direct_to_step4 -->
    - getstarted_3_success: utter_direct_to_step4


## Install Rasa: Ask ready to build -> Problem
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* enter_data
    - getstarted_3: action_store_problem_description
    - utter_direct_to_forum_for_help   <!-- predicted: utter_direct_to_step4 -->
    - getstarted_3_success: utter_direct_to_step4


## Install Rasa: Ask ready to build -> Problem
* install_rasa{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* enter_data
    - getstarted_3: action_store_problem_description
    - utter_direct_to_forum_for_help   <!-- predicted: utter_direct_to_step4 -->
    - getstarted_3_success: utter_direct_to_step4


## Install Rasa: Ask ready to build -> Problem
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* out_of_scope
    - getstarted_3: action_store_problem_description
    - utter_direct_to_forum_for_help   <!-- predicted: utter_direct_to_step4 -->
    - getstarted_3_success: utter_direct_to_step4


## Install Rasa: Ask ready to build -> Problem
* install_rasa{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* out_of_scope
    - getstarted_3: action_store_problem_description
    - utter_direct_to_forum_for_help   <!-- predicted: utter_direct_to_step4 -->
    - getstarted_3_success: utter_direct_to_step4


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* ask_faq_platform
    - faq: action_faqs
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* ask_faq_languages
    - faq: action_faqs
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* ask_faq_tutorialcore
    - faq: action_faqs
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* ask_faq_tutorialnlu
    - faq: action_faqs
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* ask_faq_opensource
    - faq: action_faqs
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* ask_faq_voice
    - faq: action_faqs
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* ask_faq_slots
    - faq: action_faqs
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* ask_faq_channels
    - faq: action_faqs
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* ask_faq_differencecorenlu
    - faq: action_faqs
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* ask_faq_python_version
    - faq: action_faqs
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* ask_faq_community_size
    - faq: action_faqs
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + unknown topic
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* ask_faq_what_is_forum
    - faq: action_faqs
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_dont_know_nlu_part -->
    - rasa_help: utter_dont_know_nlu_part
    - rasa_help: utter_search_bar
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* ask_faq_platform
    - faq: action_faqs
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* ask_faq_platform
    - faq: action_faqs
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* ask_faq_languages
    - faq: action_faqs
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* ask_faq_languages
    - faq: action_faqs
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* ask_faq_tutorialcore
    - faq: action_faqs
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* ask_faq_tutorialcore
    - faq: action_faqs
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* ask_faq_tutorialnlu
    - faq: action_faqs
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* ask_faq_tutorialnlu
    - faq: action_faqs
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* ask_faq_opensource
    - faq: action_faqs
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* ask_faq_opensource
    - faq: action_faqs
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* ask_faq_voice
    - faq: action_faqs
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* ask_faq_voice
    - faq: action_faqs
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* ask_faq_slots
    - faq: action_faqs
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* ask_faq_slots
    - faq: action_faqs
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* ask_faq_channels
    - faq: action_faqs
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* ask_faq_channels
    - faq: action_faqs
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* ask_faq_differencecorenlu
    - faq: action_faqs
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* ask_faq_differencecorenlu
    - faq: action_faqs
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* ask_faq_python_version
    - faq: action_faqs
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* ask_faq_python_version
    - faq: action_faqs
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* ask_faq_community_size
    - faq: action_faqs
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* ask_faq_community_size
    - faq: action_faqs
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_what_language
* ask_faq_what_is_forum
    - faq: action_faqs
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + intent + pipeline recommendation, spacy
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - rasa_help: utter_nlu_intent_tutorial
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_what_language
* ask_faq_what_is_forum
    - faq: action_faqs
    - rasa_help: utter_what_language
* enter_data{"language": "en"}
    - slot{"language": "en"}
    - rasa_help: action_store_bot_language
    - slot{"can_use_spacy": true}
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tensorflow -->
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_faq_platform
    - faq: action_faqs
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_faq_languages
    - faq: action_faqs
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_faq_tutorialcore
    - faq: action_faqs
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_faq_tutorialnlu
    - faq: action_faqs
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_faq_opensource
    - faq: action_faqs
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_faq_voice
    - faq: action_faqs
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_faq_slots
    - faq: action_faqs
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_faq_channels
    - faq: action_faqs
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_faq_differencecorenlu
    - faq: action_faqs
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_faq_python_version
    - faq: action_faqs
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_faq_community_size
    - faq: action_faqs
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_faq_what_is_forum
    - faq: action_faqs
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_faq_platform
    - faq: action_faqs
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_faq_languages
    - faq: action_faqs
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_faq_tutorialcore
    - faq: action_faqs
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_faq_tutorialnlu
    - faq: action_faqs
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_faq_opensource
    - faq: action_faqs
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_faq_voice
    - faq: action_faqs
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_faq_slots
    - faq: action_faqs
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_faq_channels
    - faq: action_faqs
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_faq_differencecorenlu
    - faq: action_faqs
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_faq_python_version
    - faq: action_faqs
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_faq_community_size
    - faq: action_faqs
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* ask_faq_what_is_forum
    - faq: action_faqs
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* ask_faq_platform
    - faq: action_faqs
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* ask_faq_platform
    - faq: action_faqs
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* ask_faq_languages
    - faq: action_faqs
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* ask_faq_languages
    - faq: action_faqs
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* ask_faq_tutorialcore
    - faq: action_faqs
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* ask_faq_tutorialcore
    - faq: action_faqs
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* ask_faq_tutorialnlu
    - faq: action_faqs
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* ask_faq_tutorialnlu
    - faq: action_faqs
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* ask_faq_opensource
    - faq: action_faqs
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* ask_faq_opensource
    - faq: action_faqs
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* ask_faq_voice
    - faq: action_faqs
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* ask_faq_voice
    - faq: action_faqs
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* ask_faq_slots
    - faq: action_faqs
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* ask_faq_slots
    - faq: action_faqs
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* ask_faq_channels
    - faq: action_faqs
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* ask_faq_channels
    - faq: action_faqs
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* ask_faq_differencecorenlu
    - faq: action_faqs
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* ask_faq_differencecorenlu
    - faq: action_faqs
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* ask_faq_python_version
    - faq: action_faqs
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* ask_faq_python_version
    - faq: action_faqs
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* ask_faq_community_size
    - faq: action_faqs
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* ask_faq_community_size
    - faq: action_faqs
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* pipeline_recommendation
    - rasa_help: utter_ask_entities
* ask_faq_what_is_forum
    - faq: action_faqs
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## not new to rasa + nlu + entity + pipeline duckling
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - rasa_help: utter_ask_for_nlu_specifics
* nlu_info{"nlu_part": "entity recognition"}
    - slot{"nlu_part": "entity recognition"}
    - utter_nlu_entity_tutorial   <!-- predicted: utter_nlu_intent_tutorial -->
    - rasa_help: utter_offer_recommendation
* affirm
    - rasa_help: utter_ask_entities
* ask_faq_what_is_forum
    - faq: action_faqs
    - rasa_help: utter_ask_entities
* enter_data{"entity": "date ranges"}
    - rasa_help: action_store_entity_extractor
    - slot{"entity_extractor": "ner_duckling_http"}
    - rasa_help_success: utter_duckling
    - chitchat: utter_anything_else


## new to rasa at start, built bot before
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration


## new to rasa at start
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore


## new to rasa + not new to chatbots + migrating from luis
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* switch{"current_api": "luis"}
    - slot{"current_api": "luis"}
    - utter_switch_luis   <!-- predicted: utter_switch_dialogflow -->
    - chitchat: utter_anything_else


## new to rasa + not new to chatbots + migrating from luis
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* switch{"current_api": "luis"}
    - slot{"current_api": "luis"}
    - utter_switch_luis   <!-- predicted: utter_switch_dialogflow -->
    - chitchat: utter_anything_else


## new to rasa + not new to chatbots + migrating from luis
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* affirm
    - getstarted_1: utter_ask_which_tool
* switch{"current_api": "luis"}
    - slot{"current_api": "luis"}
    - utter_switch_luis   <!-- predicted: utter_switch_dialogflow -->
    - chitchat: utter_anything_else


## new to rasa + not new to chatbots + migrating from luis
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* affirm
    - getstarted_1: utter_ask_which_tool
* switch{"current_api": "luis"}
    - slot{"current_api": "luis"}
    - utter_switch_luis   <!-- predicted: utter_switch_dialogflow -->
    - chitchat: utter_anything_else


