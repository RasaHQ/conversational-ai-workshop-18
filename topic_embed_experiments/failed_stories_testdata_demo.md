## Generated Story goal:1 step, id:cd10afdfaab74996a3e1ed1b712366d3, 05/01/19 -245718514312788239
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* technical_question
    - utter_not_sure   <!-- predicted: utter_canthelp -->
    - chitchat: utter_possibilities -> fail
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* enter_data
    - action_default_ask_affirmation   <!-- predicted: utter_not_sure -->
* how_to_get_started
    - action_default_fallback   <!-- predicted: utter_getstarted -->
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "teach me nlp"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_listen   <!-- predicted: utter_first_bot_with_rasa -->
* ask_isbot
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->
* ask_isbot
    - action_revert_fallback_events   <!-- predicted: action_chitchat -->


## Generated Story goal:1 step, id:cd10afdfaab74996a3e1ed1b712366d3, 05/01/19 -245718514312788239
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* technical_question
    - utter_not_sure   <!-- predicted: utter_canthelp -->
    - chitchat: utter_possibilities -> fail
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* enter_data
    - action_default_ask_affirmation   <!-- predicted: utter_not_sure -->
* how_to_get_started
    - action_default_fallback   <!-- predicted: utter_getstarted -->
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "teach me nlp"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_listen   <!-- predicted: utter_first_bot_with_rasa -->
* ask_isbot
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->


## Generated Story goal:1 step, id:cd10afdfaab74996a3e1ed1b712366d3, 05/01/19 -245718514312788239
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* technical_question
    - utter_not_sure   <!-- predicted: utter_canthelp -->
    - chitchat: utter_possibilities -> fail
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* enter_data
    - action_default_ask_affirmation   <!-- predicted: utter_not_sure -->
* how_to_get_started
    - action_default_fallback   <!-- predicted: utter_getstarted -->
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "teach me nlp"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_listen   <!-- predicted: utter_first_bot_with_rasa -->
* ask_isbot
    - chitchat: action_chitchat
* handleinsult
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->
* how_to_get_started
    - action_revert_fallback_events   <!-- predicted: utter_getstarted -->


## Generated Story goal:1 step, id:cd10afdfaab74996a3e1ed1b712366d3, 05/01/19 -245718514312788239
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* technical_question
    - utter_not_sure   <!-- predicted: utter_canthelp -->
    - chitchat: utter_possibilities -> fail
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* enter_data
    - action_default_ask_affirmation   <!-- predicted: utter_not_sure -->
* how_to_get_started
    - action_default_fallback   <!-- predicted: utter_getstarted -->
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "teach me nlp"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_listen   <!-- predicted: utter_first_bot_with_rasa -->
* ask_isbot
    - chitchat: action_chitchat
* handleinsult
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->


## Generated Story goal:1 step, id:cd10afdfaab74996a3e1ed1b712366d3, 05/01/19 -245718514312788239
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* technical_question
    - utter_not_sure   <!-- predicted: utter_canthelp -->
    - chitchat: utter_possibilities -> fail
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* enter_data
    - action_default_ask_affirmation   <!-- predicted: utter_not_sure -->
* how_to_get_started
    - action_default_fallback   <!-- predicted: utter_getstarted -->
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "teach me nlp"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_listen   <!-- predicted: utter_first_bot_with_rasa -->
* ask_isbot
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* enter_data
    - action_chitchat   <!-- predicted: action_store_email -->
    - utter_built_bot_before   <!-- predicted: utter_tryout -->
* enter_data
    - utter_explain_stack   <!-- predicted: action_store_email -->
    - utter_stack_details   <!-- predicted: utter_tryout -->
    - utter_explain_nlucore   <!-- predicted: utter_explain_stack -->
* affirm
    - utter_explain_nlu   <!-- predicted: utter_ask_migration -->
    - utter_explain_core   <!-- predicted: utter_explain_nlucore -->
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* thank
    - action_default_ask_affirmation   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* bye
    - action_revert_fallback_events   <!-- predicted: utter_tryout -->


## Generated Story goal:1 step, id:cd10afdfaab74996a3e1ed1b712366d3, 05/01/19 -245718514312788239
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* technical_question
    - utter_not_sure   <!-- predicted: utter_canthelp -->
    - chitchat: utter_possibilities -> fail
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* enter_data
    - action_default_ask_affirmation   <!-- predicted: utter_not_sure -->
* how_to_get_started
    - action_default_fallback   <!-- predicted: utter_getstarted -->
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "teach me nlp"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_listen   <!-- predicted: utter_first_bot_with_rasa -->
* ask_isbot
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* enter_data
    - action_chitchat   <!-- predicted: action_store_email -->
    - utter_built_bot_before   <!-- predicted: utter_tryout -->
* enter_data
    - utter_explain_stack   <!-- predicted: action_store_email -->
    - utter_stack_details   <!-- predicted: utter_tryout -->
    - utter_explain_nlucore   <!-- predicted: utter_explain_stack -->
* affirm
    - utter_explain_nlu   <!-- predicted: utter_ask_migration -->
    - utter_explain_core   <!-- predicted: utter_explain_nlucore -->
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* thank
    - action_default_ask_affirmation   <!-- predicted: utter_tryout -->


## Generated Story goal:1 step, id:cd10afdfaab74996a3e1ed1b712366d3, 05/01/19 -245718514312788239
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* technical_question
    - utter_not_sure   <!-- predicted: utter_canthelp -->
    - chitchat: utter_possibilities -> fail
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* enter_data
    - action_default_ask_affirmation   <!-- predicted: utter_not_sure -->
* how_to_get_started
    - action_default_fallback   <!-- predicted: utter_getstarted -->
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "teach me nlp"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_listen   <!-- predicted: utter_first_bot_with_rasa -->
* ask_isbot
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* enter_data
    - action_chitchat   <!-- predicted: action_store_email -->
    - utter_built_bot_before   <!-- predicted: utter_tryout -->
* enter_data
    - utter_explain_stack   <!-- predicted: action_store_email -->
    - utter_stack_details   <!-- predicted: utter_tryout -->
    - utter_explain_nlucore   <!-- predicted: utter_explain_stack -->
* affirm
    - utter_explain_nlu   <!-- predicted: utter_ask_migration -->
    - utter_explain_core   <!-- predicted: utter_explain_nlucore -->
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* bye
    - utter_bye   <!-- predicted: utter_not_sure -->
* greet
    - action_greet_user   <!-- predicted: utter_explain_stack -->
* enter_data
    - utter_not_sure   <!-- predicted: utter_tryout -->
    - utter_possibilities   <!-- predicted: utter_anything_else -->
* ask_howdoing
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* enter_data
    - utter_not_sure   <!-- predicted: utter_possibilities -->
    - utter_possibilities   <!-- predicted: utter_anything_else -->
* ask_time
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* handleinsult
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* ask_why_contribute
    - utter_reasons_to_contribute   <!-- predicted: action_chitchat -->
* handleinsult
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->
    - action_listen   <!-- predicted: utter_anything_else -->
* handleinsult
    - action_default_fallback   <!-- predicted: action_chitchat -->
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_listen   <!-- predicted: utter_anything_else -->
* restart
    - action_restart


## Generated Story goal:chitchat, id:67a8696eb5894b25a800b6cbd7a695bb, 12/15/18 -1322664348979395741
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_howdoing
    - chitchat: action_chitchat
* ask_whoisit
    - chitchat: action_chitchat
* enter_data
    - action_select_installation_command   <!-- predicted: utter_not_sure -->
    - utter_ask_ready_to_build   <!-- predicted: utter_possibilities -->
* ask_faq_languages
    - action_store_problem_description   <!-- predicted: action_faqs -->
    - slot{"problem_description": "what languages do you support?"}
    - action_faqs   <!-- predicted: action_listen -->
* enter_data
    - action_select_installation_command   <!-- predicted: utter_possibilities -->
    - utter_ask_ready_to_build   <!-- predicted: utter_possibilities -->
* enter_data
    - action_store_problem_description   <!-- predicted: utter_possibilities -->
    - slot{"problem_description": "ofcouse"}
    - utter_direct_to_forum_for_help   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: utter_possibilities -->
* affirm
    - utter_anything_else   <!-- predicted: action_listen -->
* handleinsult
    - action_default_fallback   <!-- predicted: utter_possibilities -->


## Generated Story goal:chitchat, id:67a8696eb5894b25a800b6cbd7a695bb, 12/15/18 -1322664348979395741
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_howdoing
    - chitchat: action_chitchat
* ask_whoisit
    - chitchat: action_chitchat
* enter_data
    - action_select_installation_command   <!-- predicted: utter_not_sure -->
    - utter_ask_ready_to_build   <!-- predicted: utter_possibilities -->
* ask_faq_languages
    - action_store_problem_description   <!-- predicted: action_faqs -->
    - slot{"problem_description": "what languages do you support?"}
    - action_faqs   <!-- predicted: action_listen -->
* enter_data
    - action_select_installation_command   <!-- predicted: utter_possibilities -->
    - utter_ask_ready_to_build   <!-- predicted: utter_possibilities -->
* enter_data
    - action_store_problem_description   <!-- predicted: utter_possibilities -->
    - slot{"problem_description": "ofcouse"}
    - utter_direct_to_forum_for_help   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: utter_possibilities -->
* affirm
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: utter_possibilities -->
* out_of_scope
    - action_default_fallback   <!-- predicted: utter_possibilities -->


## Generated Story goal:1 step, id:2979714d45bc445e9d7241fdc3ad64c1, 12/15/18 -3947067250872774786
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* handleinsult
    - chitchat: action_chitchat
* deny
    - action_default_fallback   <!-- predicted: utter_nohelp -->


## Generated Story goal:1 step, id:32111c2c24bb44dba5da72e6978f29fe, 12/17/18 7799571079686222516
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whoisit
    - chitchat: action_chitchat
* ask_whatisrasa
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->
* ask_whatisrasa
    - action_revert_fallback_events   <!-- predicted: action_chitchat -->


## Generated Story goal:1 step, id:32111c2c24bb44dba5da72e6978f29fe, 12/17/18 7799571079686222516
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whoisit
    - chitchat: action_chitchat
* ask_whatisrasa
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->


## Generated Story goal:1 step, id:32111c2c24bb44dba5da72e6978f29fe, 12/17/18 7799571079686222516
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whoisit
    - chitchat: action_chitchat
* ask_whatisrasa
    - chitchat: action_chitchat
* out_of_scope
    - oos: utter_out_of_scope
    - utter_possibilities   <!-- predicted: action_listen -->
* ask_wherefrom
    - chitchat: action_chitchat
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* greet
    - greet_success: action_greet_user
* ask_whatisrasa
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->
* how_to_get_started
    - action_revert_fallback_events   <!-- predicted: utter_getstarted -->


## Generated Story goal:1 step, id:32111c2c24bb44dba5da72e6978f29fe, 12/17/18 7799571079686222516
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whoisit
    - chitchat: action_chitchat
* ask_whatisrasa
    - chitchat: action_chitchat
* out_of_scope
    - oos: utter_out_of_scope
    - utter_possibilities   <!-- predicted: action_listen -->
* ask_wherefrom
    - chitchat: action_chitchat
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* greet
    - greet_success: action_greet_user
* ask_whatisrasa
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->


## Generated Story goal:1 step, id:8affa7a6082945a09f031db186ec22eb, 12/15/18 -5307346528120334917
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatspossible
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:1 step, id:b2a4da8d7bf6494893801a9ef6a6f81f, 12/15/18 1767757702730525150
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* deny
    - getstarted_1: utter_tryout
* ask_howold
    - chitchat: action_chitchat
    - getstarted_1: utter_tryout
* deny
    - getstarted_1_success: utter_direct_install
    - chitchat: utter_anything_else
* affirm
    - utter_what_help   <!-- predicted: action_listen -->
* ask_isbot
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:1 step, id:b2a4da8d7bf6494893801a9ef6a6f81f, 12/15/18 1767757702730525150
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* deny
    - getstarted_1: utter_tryout
* ask_howold
    - chitchat: action_chitchat
    - getstarted_1: utter_tryout
* deny
    - getstarted_1_success: utter_direct_install
    - chitchat: utter_anything_else
* affirm
    - utter_what_help   <!-- predicted: action_listen -->
* affirm
    - utter_quickstart   <!-- predicted: utter_ask_migration -->
    - utter_anything_else   <!-- predicted: action_listen -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_howold
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* greet
    - action_greet_user   <!-- predicted: utter_tryout -->
* ask_howdoing
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* ask_weather
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_chitchat -->
* ask_weather
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_chitchat -->
* enter_data
    - utter_possibilities   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* greet
    - action_greet_user   <!-- predicted: utter_tryout -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_howdoing
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* out_of_scope
    - utter_out_of_scope   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: action_chitchat -->
* ask_whatisrasa
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->
    - action_listen   <!-- predicted: action_greet_user -->
* deny
    - action_default_ask_rephrase   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_direct_install -->
* deny
    - action_revert_fallback_events   <!-- predicted: utter_direct_install -->


## Generated Story goal:1 step, id:b2a4da8d7bf6494893801a9ef6a6f81f, 12/15/18 1767757702730525150
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* deny
    - getstarted_1: utter_tryout
* ask_howold
    - chitchat: action_chitchat
    - getstarted_1: utter_tryout
* deny
    - getstarted_1_success: utter_direct_install
    - chitchat: utter_anything_else
* affirm
    - utter_what_help   <!-- predicted: action_listen -->
* affirm
    - utter_quickstart   <!-- predicted: utter_ask_migration -->
    - utter_anything_else   <!-- predicted: action_listen -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_howold
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* greet
    - action_greet_user   <!-- predicted: utter_tryout -->
* ask_howdoing
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* ask_weather
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_chitchat -->
* ask_weather
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_chitchat -->
* enter_data
    - utter_possibilities   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* greet
    - action_greet_user   <!-- predicted: utter_tryout -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_howdoing
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* out_of_scope
    - utter_out_of_scope   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: action_chitchat -->
* ask_whatisrasa
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->
    - action_listen   <!-- predicted: action_greet_user -->
* deny
    - action_default_ask_rephrase   <!-- predicted: utter_tryout -->


## Generated Story goal:1 step, id:b2a4da8d7bf6494893801a9ef6a6f81f, 12/15/18 1767757702730525150
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* deny
    - getstarted_1: utter_tryout
* ask_howold
    - chitchat: action_chitchat
    - getstarted_1: utter_tryout
* deny
    - getstarted_1_success: utter_direct_install
    - chitchat: utter_anything_else
* affirm
    - utter_what_help   <!-- predicted: action_listen -->
* affirm
    - utter_quickstart   <!-- predicted: utter_ask_migration -->
    - utter_anything_else   <!-- predicted: action_listen -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_howold
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* greet
    - action_greet_user   <!-- predicted: utter_tryout -->
* ask_howdoing
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* ask_weather
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_chitchat -->
* ask_weather
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_chitchat -->
* enter_data
    - utter_possibilities   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* greet
    - action_greet_user   <!-- predicted: utter_tryout -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_howdoing
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* out_of_scope
    - utter_out_of_scope   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: action_chitchat -->
* ask_whatisrasa
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->


## Generated Story goal:1 step, id:b2a4da8d7bf6494893801a9ef6a6f81f, 12/15/18 1767757702730525150
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* deny
    - getstarted_1: utter_tryout
* ask_howold
    - chitchat: action_chitchat
    - getstarted_1: utter_tryout
* deny
    - getstarted_1_success: utter_direct_install
    - chitchat: utter_anything_else
* affirm
    - utter_what_help   <!-- predicted: action_listen -->
* affirm
    - utter_quickstart   <!-- predicted: utter_ask_migration -->
    - utter_anything_else   <!-- predicted: action_listen -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_howold
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* greet
    - action_greet_user   <!-- predicted: utter_tryout -->
* ask_howdoing
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* ask_weather
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_chitchat -->
* ask_weather
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_chitchat -->
* enter_data
    - utter_possibilities   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* greet
    - action_greet_user   <!-- predicted: utter_tryout -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_howdoing
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* out_of_scope
    - utter_out_of_scope   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: action_chitchat -->
* deny
    - utter_nohelp   <!-- predicted: utter_tryout -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatisrasa
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* thank
    - utter_noworries   <!-- predicted: utter_tryout -->
    - utter_anything_else   <!-- predicted: action_greet_user -->
* bye
    - utter_bye   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: utter_ask_migration -->
    - utter_first_bot_with_rasa   <!-- predicted: utter_tryout -->
* deny
    - action_set_onboarding   <!-- predicted: utter_explain_stack -->
    - slot{"onboarding": false}
    - utter_ask_which_product   <!-- predicted: utter_stack_details -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_ask_for_nlu_specifics   <!-- predicted: utter_great -->
* enter_data
    - utter_quickstart_nlu_only   <!-- predicted: utter_tryout -->
    - utter_anything_else   <!-- predicted: utter_tryout -->
* affirm
    - utter_thumbsup   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_anything_else -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* enter_data
    - utter_not_sure   <!-- predicted: utter_tryout -->
    - utter_possibilities   <!-- predicted: utter_anything_else -->
* ask_weather
    - chitchat: action_chitchat
* ask_whatspossible
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->
* out_of_scope
    - action_default_ask_rephrase   <!-- predicted: utter_out_of_scope -->
* deny
    - action_revert_fallback_events   <!-- predicted: utter_contact_email -->


## Generated Story goal:1 step, id:b2a4da8d7bf6494893801a9ef6a6f81f, 12/15/18 1767757702730525150
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* deny
    - getstarted_1: utter_tryout
* ask_howold
    - chitchat: action_chitchat
    - getstarted_1: utter_tryout
* deny
    - getstarted_1_success: utter_direct_install
    - chitchat: utter_anything_else
* affirm
    - utter_what_help   <!-- predicted: action_listen -->
* affirm
    - utter_quickstart   <!-- predicted: utter_ask_migration -->
    - utter_anything_else   <!-- predicted: action_listen -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_howold
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* greet
    - action_greet_user   <!-- predicted: utter_tryout -->
* ask_howdoing
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* ask_weather
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_chitchat -->
* ask_weather
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_chitchat -->
* enter_data
    - utter_possibilities   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* greet
    - action_greet_user   <!-- predicted: utter_tryout -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_howdoing
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* out_of_scope
    - utter_out_of_scope   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: action_chitchat -->
* deny
    - utter_nohelp   <!-- predicted: utter_tryout -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatisrasa
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* thank
    - utter_noworries   <!-- predicted: utter_tryout -->
    - utter_anything_else   <!-- predicted: action_greet_user -->
* bye
    - utter_bye   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: utter_ask_migration -->
    - utter_first_bot_with_rasa   <!-- predicted: utter_tryout -->
* deny
    - action_set_onboarding   <!-- predicted: utter_explain_stack -->
    - slot{"onboarding": false}
    - utter_ask_which_product   <!-- predicted: utter_stack_details -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_ask_for_nlu_specifics   <!-- predicted: utter_great -->
* enter_data
    - utter_quickstart_nlu_only   <!-- predicted: utter_tryout -->
    - utter_anything_else   <!-- predicted: utter_tryout -->
* affirm
    - utter_thumbsup   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_anything_else -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* enter_data
    - utter_not_sure   <!-- predicted: utter_tryout -->
    - utter_possibilities   <!-- predicted: utter_anything_else -->
* ask_weather
    - chitchat: action_chitchat
* ask_whatspossible
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->
* out_of_scope
    - action_default_ask_rephrase   <!-- predicted: utter_out_of_scope -->


## Generated Story goal:1 step, id:b2a4da8d7bf6494893801a9ef6a6f81f, 12/15/18 1767757702730525150
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* deny
    - getstarted_1: utter_tryout
* ask_howold
    - chitchat: action_chitchat
    - getstarted_1: utter_tryout
* deny
    - getstarted_1_success: utter_direct_install
    - chitchat: utter_anything_else
* affirm
    - utter_what_help   <!-- predicted: action_listen -->
* affirm
    - utter_quickstart   <!-- predicted: utter_ask_migration -->
    - utter_anything_else   <!-- predicted: action_listen -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_howold
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* greet
    - action_greet_user   <!-- predicted: utter_tryout -->
* ask_howdoing
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* ask_weather
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_chitchat -->
* ask_weather
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_chitchat -->
* enter_data
    - utter_possibilities   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* greet
    - action_greet_user   <!-- predicted: utter_tryout -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_howdoing
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* out_of_scope
    - utter_out_of_scope   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: action_chitchat -->
* deny
    - utter_nohelp   <!-- predicted: utter_tryout -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatisrasa
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* thank
    - utter_noworries   <!-- predicted: utter_tryout -->
    - utter_anything_else   <!-- predicted: action_greet_user -->
* bye
    - utter_bye   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: utter_ask_migration -->
    - utter_first_bot_with_rasa   <!-- predicted: utter_tryout -->
* deny
    - action_set_onboarding   <!-- predicted: utter_explain_stack -->
    - slot{"onboarding": false}
    - utter_ask_which_product   <!-- predicted: utter_stack_details -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_ask_for_nlu_specifics   <!-- predicted: utter_great -->
* enter_data
    - utter_quickstart_nlu_only   <!-- predicted: utter_tryout -->
    - utter_anything_else   <!-- predicted: utter_tryout -->
* affirm
    - utter_thumbsup   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_anything_else -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* enter_data
    - utter_not_sure   <!-- predicted: utter_tryout -->
    - utter_possibilities   <!-- predicted: utter_anything_else -->
* ask_weather
    - chitchat: action_chitchat
* ask_whatspossible
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->


## Generated Story goal:1 step, id:8861ebbcdb684fb98a66f65a357d07b0, 12/15/18 -217273042631869968
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_howdoing
    - chitchat: action_chitchat
* ask_whatspossible
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:oos, id:1e680f8682a44338a9c68496bc8ac9ba, 05/01/19 9069131845960195647
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whoisit
    - chitchat: action_chitchat
* enter_data
    - action_default_ask_affirmation   <!-- predicted: utter_not_sure -->
* deny
    - action_default_ask_rephrase   <!-- predicted: utter_nohelp -->
* ask_whatisrasa
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->
* deny
    - action_default_fallback   <!-- predicted: utter_nohelp -->
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "what is your address?"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_listen   <!-- predicted: utter_anything_else -->
* restart
    - action_restart


## Generated Story goal:oos, id:1e680f8682a44338a9c68496bc8ac9ba, 05/01/19 9069131845960195647
* ask_wherefrom
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->
* ask_wherefrom
    - action_revert_fallback_events   <!-- predicted: action_chitchat -->


## Generated Story goal:oos, id:1e680f8682a44338a9c68496bc8ac9ba, 05/01/19 9069131845960195647
* ask_wherefrom
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->


## Generated Story goal:FAQ, id:3256c66e60aa42c7bc33f915dfa0d728, 05/01/19 -7313640270495983501
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* rasa_cost
    - utter_rasa_cost   <!-- predicted: action_faqs -->
    - chitchat: utter_anything_else
* rasa_cost
    - action_default_ask_affirmation   <!-- predicted: action_faqs -->
* rasa_cost
    - action_revert_fallback_events   <!-- predicted: action_faqs -->


## Generated Story goal:FAQ, id:3256c66e60aa42c7bc33f915dfa0d728, 05/01/19 -7313640270495983501
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* rasa_cost
    - utter_rasa_cost   <!-- predicted: action_faqs -->
    - chitchat: utter_anything_else
* rasa_cost
    - action_default_ask_affirmation   <!-- predicted: action_faqs -->


## Generated Story goal:sales, id:c08c1942644d489ea1995880bf043a85, 12/15/18 8980344777735687263
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whatspossible
    - chitchat: action_chitchat
* how_to_get_started
    - action_default_fallback   <!-- predicted: utter_getstarted -->


## Generated Story goal:1 step, id:0da3c44e9839403eafaa89050e2b8d3e, 12/15/18 726412975159353253
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:sales, id:c1e80e11d95e47bba78eeabb843bc897, 12/15/18 -6282839839722846955
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whatspossible
    - chitchat: action_chitchat
* contact_sales
    - sales: utter_moreinformation
    - sales: utter_ask_jobfunction
* ask_howdoing
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:sales, id:c1e80e11d95e47bba78eeabb843bc897, 12/15/18 -6282839839722846955
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whatspossible
    - chitchat: action_chitchat
* contact_sales
    - sales: utter_moreinformation
    - sales: utter_ask_jobfunction
* ask_howdoing
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:sales, id:c1e80e11d95e47bba78eeabb843bc897, 12/15/18 -6282839839722846955
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whatspossible
    - chitchat: action_chitchat
* contact_sales
    - sales: utter_moreinformation
    - sales: utter_ask_jobfunction
* enter_data
    - sales: action_store_job
    - slot{"job_function": "ohh sorry then"}
    - sales: utter_ask_usecase
* ask_faq_languages
    - action_default_fallback   <!-- predicted: action_faqs -->


## Generated Story goal:1 step, id:172015966d6b4687bdd65f3a5c7be107, 12/15/18 -2390059780872131662
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* nlu_info
    - action_default_fallback   <!-- predicted: utter_link_to_forum -->


## Generated Story goal:1 step, id:172015966d6b4687bdd65f3a5c7be107, 12/15/18 -2390059780872131662
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:1 step, id:172015966d6b4687bdd65f3a5c7be107, 12/15/18 -2390059780872131662
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whatspossible
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:1 step, id:172015966d6b4687bdd65f3a5c7be107, 12/15/18 -2390059780872131662
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - action_default_fallback   <!-- predicted: action_set_onboarding -->


## Generated Story goal:1 step, id:172015966d6b4687bdd65f3a5c7be107, 12/15/18 -2390059780872131662
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* enter_data
    - utter_possibilities   <!-- predicted: utter_explain_nlucore -->
    - utter_stack_details   <!-- predicted: utter_built_bot_before -->
    - utter_explain_nlucore   <!-- predicted: utter_built_bot_before -->
* affirm
    - utter_explain_nlu   <!-- predicted: utter_ask_migration -->
    - getstarted_1: utter_tryout
* enter_data
    - action_default_fallback   <!-- predicted: utter_not_sure -->


## Generated Story goal:chitchat, id:2ca65157d22b43caad664589ee29524e, 12/15/18 3415830769284134354
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_howdoing
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_chitchat
* ask_howold{"number": 42}
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_chitchat
* ask_whatspossible
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:0430099345234226aecbf5260cd864b8, 12/15/18 4509295789363688221
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_time
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* ask_weather
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:0430099345234226aecbf5260cd864b8, 12/15/18 4509295789363688221
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_time
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* handleinsult
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:0430099345234226aecbf5260cd864b8, 12/15/18 4509295789363688221
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_time
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* handleinsult
    - chitchat: action_chitchat
* greet
    - greet_success: action_greet_user
* ask_howold
    - chitchat: action_chitchat
* out_of_scope
    - action_default_ask_affirmation   <!-- predicted: utter_out_of_scope -->
* out_of_scope
    - action_default_fallback   <!-- predicted: utter_out_of_scope -->
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "docs"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_listen   <!-- predicted: utter_possibilities -->
* restart
    - action_restart


## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14, 12/15/18 2244534826485528312
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - chitchat: action_chitchat
* enter_data
    - action_default_fallback   <!-- predicted: utter_not_sure -->


## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14, 12/15/18 2244534826485528312
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - chitchat: action_chitchat
* handleinsult
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14, 12/15/18 2244534826485528312
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - chitchat: action_chitchat
* nicetomeeyou
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14, 12/15/18 2244534826485528312
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - chitchat: action_chitchat
* nicetomeeyou
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14, 12/15/18 2244534826485528312
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - chitchat: action_chitchat
* nicetomeeyou
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14, 12/15/18 2244534826485528312
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - chitchat: action_chitchat
* nicetomeeyou
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14, 12/15/18 2244534826485528312
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - chitchat: action_chitchat
* canthelp
    - action_default_fallback   <!-- predicted: utter_canthelp -->


## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14, 12/15/18 2244534826485528312
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - chitchat: action_chitchat
* ask_faq_opensource
    - action_default_fallback   <!-- predicted: action_faqs -->


## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14, 12/15/18 2244534826485528312
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - chitchat: action_chitchat
* out_of_scope
    - oos: utter_out_of_scope
    - utter_possibilities   <!-- predicted: action_listen -->
* affirm
    - action_default_fallback   <!-- predicted: utter_what_help -->


## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14, 12/15/18 2244534826485528312
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - chitchat: action_chitchat
* out_of_scope
    - oos: utter_out_of_scope
    - utter_possibilities   <!-- predicted: action_listen -->
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* deny
    - subscribe: utter_cantsignup
* deny
    - action_default_fallback   <!-- predicted: utter_cantsignup -->


## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14, 12/15/18 2244534826485528312
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - chitchat: action_chitchat
* out_of_scope
    - oos: utter_out_of_scope
    - utter_possibilities   <!-- predicted: action_listen -->
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* deny
    - subscribe: utter_cantsignup
* enter_data
    - subscribe: action_store_email


## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14, 12/15/18 2244534826485528312
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - chitchat: action_chitchat
* out_of_scope
    - oos: utter_out_of_scope
    - utter_possibilities   <!-- predicted: action_listen -->
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* deny
    - subscribe: utter_cantsignup
* bye
    - action_default_fallback   <!-- predicted: utter_nohelp -->


## Generated Story goal:oos, id:ed1418fcc3884157bcc96a7c43d21ec0, 05/01/19 2178899423323461626
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - chitchat: action_chitchat
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* ask_faq_languages
    - faq: action_faqs
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* affirm
    - action_default_ask_affirmation   <!-- predicted: utter_possibilities -->
* enter_data
    - action_revert_fallback_events   <!-- predicted: utter_not_sure -->


## Generated Story goal:oos, id:ed1418fcc3884157bcc96a7c43d21ec0, 05/01/19 2178899423323461626
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - chitchat: action_chitchat
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* ask_faq_languages
    - faq: action_faqs
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* affirm
    - action_default_ask_affirmation   <!-- predicted: utter_possibilities -->


## Generated Story goal:1 step, id:f48bb43d6f5645d69b0c1cd1cfc9c62b, 12/15/18 923590105913609100
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:cd932f93d47c4cb6a408a61b8e74c2be, 12/17/18 2968378781313327835
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_howdoing
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_chitchat
* ask_howdoing
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->
* enter_data
    - action_revert_fallback_events   <!-- predicted: utter_not_sure -->


## Generated Story goal:chitchat, id:cd932f93d47c4cb6a408a61b8e74c2be, 12/17/18 2968378781313327835
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_howdoing
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_chitchat
* ask_howdoing
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:cd932f93d47c4cb6a408a61b8e74c2be, 12/17/18 2968378781313327835
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_howdoing
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_chitchat
* enter_data
    - action_greet_user   <!-- predicted: utter_not_sure -->
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_whatspossible
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - action_revert_fallback_events   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:cd932f93d47c4cb6a408a61b8e74c2be, 12/17/18 2968378781313327835
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_howdoing
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_chitchat
* enter_data
    - action_greet_user   <!-- predicted: utter_not_sure -->
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_whatspossible
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:cd932f93d47c4cb6a408a61b8e74c2be, 12/17/18 2968378781313327835
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_howdoing
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_chitchat
* enter_data
    - action_greet_user   <!-- predicted: utter_not_sure -->
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_whatspossible
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat
* ask_wherefrom
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->
* install_rasa
    - action_revert_fallback_events   <!-- predicted: utter_ask_python_installed -->


## Generated Story goal:chitchat, id:cd932f93d47c4cb6a408a61b8e74c2be, 12/17/18 2968378781313327835
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_howdoing
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_chitchat
* enter_data
    - action_greet_user   <!-- predicted: utter_not_sure -->
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_whatspossible
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat
* ask_wherefrom
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->


## Generated Story goal:oos, id:864df094a24a4cc3a6b55a824c1f3a35, 12/17/18 -7699038322326118938
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_getstarted   <!-- predicted: utter_not_sure -->
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* ask_whatspossible
    - chitchat: action_chitchat
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* affirm
    - getstarted_1: action_set_onboarding -> fail
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before -> fail
* affirm
    - getstarted_1: utter_ask_migration -> fail
* affirm
    - getstarted_1: utter_ask_which_tool -> fail
* enter_data
    - getstarted_1: action_store_unknown_product -> fail
    - slot{"unknown_product": "Cleverbot"}
    - getstarted_1_success: utter_no_guide_for_switch -> fail
    - chitchat: utter_anything_else -> fail
* deny
    - utter_nohelp   <!-- predicted: utter_thumbsup -->
* affirm
    - action_default_ask_affirmation   <!-- predicted: utter_ask_migration -->
    - action_listen   <!-- predicted: utter_built_bot_before -->
* deny
    - action_default_ask_rephrase   <!-- predicted: utter_explain_stack -->
    - action_listen   <!-- predicted: utter_stack_details -->
* ask_weather
    - action_revert_fallback_events   <!-- predicted: action_chitchat -->


## Generated Story goal:oos, id:864df094a24a4cc3a6b55a824c1f3a35, 12/17/18 -7699038322326118938
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_getstarted   <!-- predicted: utter_not_sure -->
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* ask_whatspossible
    - chitchat: action_chitchat
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* affirm
    - getstarted_1: action_set_onboarding -> fail
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before -> fail
* affirm
    - getstarted_1: utter_ask_migration -> fail
* affirm
    - getstarted_1: utter_ask_which_tool -> fail
* enter_data
    - getstarted_1: action_store_unknown_product -> fail
    - slot{"unknown_product": "Cleverbot"}
    - getstarted_1_success: utter_no_guide_for_switch -> fail
    - chitchat: utter_anything_else -> fail
* deny
    - utter_nohelp   <!-- predicted: utter_thumbsup -->
* affirm
    - action_default_ask_affirmation   <!-- predicted: utter_ask_migration -->
    - action_listen   <!-- predicted: utter_built_bot_before -->
* deny
    - action_default_ask_rephrase   <!-- predicted: utter_explain_stack -->


## Generated Story goal:oos, id:864df094a24a4cc3a6b55a824c1f3a35, 12/17/18 -7699038322326118938
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_getstarted   <!-- predicted: utter_not_sure -->
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* ask_whatspossible
    - chitchat: action_chitchat
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* affirm
    - getstarted_1: action_set_onboarding -> fail
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before -> fail
* affirm
    - getstarted_1: utter_ask_migration -> fail
* affirm
    - getstarted_1: utter_ask_which_tool -> fail
* enter_data
    - getstarted_1: action_store_unknown_product -> fail
    - slot{"unknown_product": "Cleverbot"}
    - getstarted_1_success: utter_no_guide_for_switch -> fail
    - chitchat: utter_anything_else -> fail
* deny
    - utter_nohelp   <!-- predicted: utter_thumbsup -->
* affirm
    - action_default_ask_affirmation   <!-- predicted: utter_ask_migration -->


## Generated Story goal:3 step, id:9cbbe8c0fa0841deb30fe973cd80c614, 05/01/19 -1765672058575339702
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* install_rasa
    - getstarted_3: utter_ask_python_installed
* affirm
    - utter_ask_pip_or_conda   <!-- predicted: utter_ask_python_installed -->
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* affirm
    - getstarted_3: utter_get_starter_pack
    - getstarted_3_success: utter_direct_to_step4
    - utter_anything_else   <!-- predicted: action_listen -->
* affirm
    - action_default_ask_affirmation   <!-- predicted: utter_direct_to_step4 -->
* enter_data
    - action_revert_fallback_events   <!-- predicted: action_store_problem_description -->


## Generated Story goal:3 step, id:9cbbe8c0fa0841deb30fe973cd80c614, 05/01/19 -1765672058575339702
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* install_rasa
    - getstarted_3: utter_ask_python_installed
* affirm
    - utter_ask_pip_or_conda   <!-- predicted: utter_ask_python_installed -->
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* affirm
    - getstarted_3: utter_get_starter_pack
    - getstarted_3_success: utter_direct_to_step4
    - utter_anything_else   <!-- predicted: action_listen -->
* affirm
    - action_default_ask_affirmation   <!-- predicted: utter_direct_to_step4 -->


## Generated Story goal:3 step, id:9cbbe8c0fa0841deb30fe973cd80c614, 05/01/19 -1765672058575339702
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* install_rasa
    - getstarted_3: utter_ask_python_installed
* affirm
    - utter_ask_pip_or_conda   <!-- predicted: utter_ask_python_installed -->
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* affirm
    - getstarted_3: utter_get_starter_pack
    - getstarted_3_success: utter_direct_to_step4
    - utter_anything_else   <!-- predicted: action_listen -->
* enter_data
    - action_select_installation_command   <!-- predicted: action_store_problem_description -->
    - utter_ask_ready_to_build   <!-- predicted: utter_direct_to_step4 -->
* affirm
    - action_default_ask_affirmation   <!-- predicted: utter_direct_to_step4 -->
* ask_whatspossible
    - action_default_fallback   <!-- predicted: action_store_problem_description -->
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "what i have to do"}
    - form{"name": null}
    - slot{"requested_slot": null}
* restart
    - action_restart


## Generated Story goal:1 step, id:d1f0cdf624a74a2ea7323b0817353037, 12/15/18 1731815793411691019
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - utter_tryout   <!-- predicted: utter_built_bot_before -->
* how_to_get_started
    - action_default_fallback   <!-- predicted: utter_getstarted -->


## Generated Story goal:1 step, id:d1f0cdf624a74a2ea7323b0817353037, 12/15/18 1731815793411691019
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - utter_tryout   <!-- predicted: utter_built_bot_before -->
* how_to_get_started
    - utter_quickstart_nlu_only   <!-- predicted: utter_getstarted -->
    - utter_anything_else   <!-- predicted: utter_first_bot_with_rasa -->
* enter_data
    - action_default_fallback   <!-- predicted: utter_first_bot_with_rasa -->


## Generated Story goal:1 step, id:d1f0cdf624a74a2ea7323b0817353037, 12/15/18 1731815793411691019
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - utter_tryout   <!-- predicted: utter_built_bot_before -->
* how_to_get_started
    - utter_quickstart_nlu_only   <!-- predicted: utter_getstarted -->
    - utter_anything_else   <!-- predicted: utter_first_bot_with_rasa -->
* enter_data
    - action_default_fallback   <!-- predicted: utter_first_bot_with_rasa -->


## Generated Story goal:chitchat, id:624b61bee53b411bac4a3855343dd0c7, 12/15/18 -8806002753186605917
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* affirm
    - chitchat: utter_thumbsup
* out_of_scope
    - action_default_fallback   <!-- predicted: utter_out_of_scope -->


## Generated Story goal:1 step, id:bfdc18480a8a48e19aacf281bdd5db46, 05/01/19 9082912409352129743
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whatisrasa{"language": "Japanese"}
    - slot{"language": "Japanese"}
    - slot{"language": "Japanese"}
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->
* deny
    - action_default_ask_rephrase   <!-- predicted: utter_nohelp -->
* ask_faq_languages
    - action_revert_fallback_events   <!-- predicted: action_faqs -->


## Generated Story goal:1 step, id:bfdc18480a8a48e19aacf281bdd5db46, 05/01/19 9082912409352129743
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whatisrasa{"language": "Japanese"}
    - slot{"language": "Japanese"}
    - slot{"language": "Japanese"}
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->
* deny
    - action_default_ask_rephrase   <!-- predicted: utter_nohelp -->


## Generated Story goal:1 step, id:bfdc18480a8a48e19aacf281bdd5db46, 05/01/19 9082912409352129743
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whatisrasa{"language": "Japanese"}
    - slot{"language": "Japanese"}
    - slot{"language": "Japanese"}
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:455210c2c7c9471194a7faaf2e63579f, 12/15/18 7957735631208973079
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* handleinsult
    - chitchat: action_chitchat
* out_of_scope
    - oos: utter_out_of_scope
    - utter_possibilities   <!-- predicted: action_listen -->
* how_to_get_started
    - action_default_fallback   <!-- predicted: utter_getstarted -->


## Generated Story goal:1 step, id:9724aac6adda47a38271574fddb1529d, 05/01/19 6727944383445682358
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_getstarted -->
    - action_listen   <!-- predicted: utter_first_bot_with_rasa -->
* ask_faq_platform
    - action_revert_fallback_events   <!-- predicted: action_faqs -->


## Generated Story goal:1 step, id:9724aac6adda47a38271574fddb1529d, 05/01/19 6727944383445682358
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_getstarted -->


## Generated Story goal:1 step, id:9724aac6adda47a38271574fddb1529d, 05/01/19 6727944383445682358
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_faq_platform
    - faq: action_faqs
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - action_default_ask_affirmation   <!-- predicted: utter_ask_migration -->
    - action_listen   <!-- predicted: utter_ask_migration -->
* affirm
    - action_revert_fallback_events   <!-- predicted: utter_ask_which_tool -->


## Generated Story goal:1 step, id:9724aac6adda47a38271574fddb1529d, 05/01/19 6727944383445682358
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_faq_platform
    - faq: action_faqs
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - action_default_ask_affirmation   <!-- predicted: utter_ask_migration -->


## Generated Story goal:oos, id:47f2fe45cd5f463cbaf2bc72def8f569, 05/01/19 -763810754505424450
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* out_of_scope
    - action_default_ask_affirmation   <!-- predicted: utter_out_of_scope -->
* deny
    - action_default_ask_rephrase   <!-- predicted: utter_nohelp -->
* install_rasa
    - action_revert_fallback_events   <!-- predicted: utter_ask_python_installed -->


## Generated Story goal:oos, id:47f2fe45cd5f463cbaf2bc72def8f569, 05/01/19 -763810754505424450
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* out_of_scope
    - action_default_ask_affirmation   <!-- predicted: utter_out_of_scope -->
* deny
    - action_default_ask_rephrase   <!-- predicted: utter_nohelp -->


## Generated Story goal:oos, id:47f2fe45cd5f463cbaf2bc72def8f569, 05/01/19 -763810754505424450
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* out_of_scope
    - action_default_ask_affirmation   <!-- predicted: utter_out_of_scope -->


## Generated Story goal:1 step, id:ff826c3d37f64c61b6488cfbd2aeb547, 12/15/18 -7283527111737167069
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* affirm
    - utter_thumbsup   <!-- predicted: utter_not_sure -->
    - utter_anything_else   <!-- predicted: action_listen -->
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - utter_built_bot_before   <!-- predicted: action_listen -->
* enter_data
    - action_select_installation_command   <!-- predicted: action_get_community_events -->
    - utter_ask_ready_to_build   <!-- predicted: action_get_community_events -->
* rasa_cost
    - utter_rasa_cost   <!-- predicted: action_store_bot_language -->
    - utter_anything_else   <!-- predicted: utter_possibilities -->
* enter_data
    - action_greet_user   <!-- predicted: utter_not_sure -->
* bye
    - action_default_fallback   <!-- predicted: utter_not_sure -->


## Generated Story goal:1 step, id:ff826c3d37f64c61b6488cfbd2aeb547, 12/15/18 -7283527111737167069
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* affirm
    - utter_thumbsup   <!-- predicted: utter_not_sure -->
    - utter_anything_else   <!-- predicted: action_listen -->
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - utter_built_bot_before   <!-- predicted: action_listen -->
* enter_data
    - action_select_installation_command   <!-- predicted: action_get_community_events -->
    - utter_ask_ready_to_build   <!-- predicted: action_get_community_events -->
* rasa_cost
    - utter_rasa_cost   <!-- predicted: action_store_bot_language -->
    - utter_anything_else   <!-- predicted: utter_possibilities -->
* enter_data
    - action_greet_user   <!-- predicted: utter_not_sure -->
* technical_question
    - action_default_fallback   <!-- predicted: utter_not_sure -->


## Generated Story goal:1 step, id:ff826c3d37f64c61b6488cfbd2aeb547, 12/15/18 -7283527111737167069
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* affirm
    - utter_thumbsup   <!-- predicted: utter_not_sure -->
    - utter_anything_else   <!-- predicted: action_listen -->
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - utter_built_bot_before   <!-- predicted: action_listen -->
* enter_data
    - action_select_installation_command   <!-- predicted: action_get_community_events -->
    - utter_ask_ready_to_build   <!-- predicted: action_get_community_events -->
* rasa_cost
    - utter_rasa_cost   <!-- predicted: action_store_bot_language -->
    - utter_anything_else   <!-- predicted: utter_possibilities -->
* enter_data
    - action_greet_user   <!-- predicted: utter_not_sure -->
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* enter_data
    - action_greet_user   <!-- predicted: action_store_bot_language -->
    - utter_stack_details   <!-- predicted: action_listen -->
    - utter_anything_else   <!-- predicted: utter_built_bot_before -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: utter_ask_migration -->
    - utter_first_bot_with_rasa   <!-- predicted: utter_built_bot_before -->
* ask_howdoing
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:1 step, id:ff826c3d37f64c61b6488cfbd2aeb547, 12/15/18 -7283527111737167069
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* affirm
    - utter_thumbsup   <!-- predicted: utter_not_sure -->
    - utter_anything_else   <!-- predicted: action_listen -->
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - utter_built_bot_before   <!-- predicted: action_listen -->
* enter_data
    - action_select_installation_command   <!-- predicted: action_get_community_events -->
    - utter_ask_ready_to_build   <!-- predicted: action_get_community_events -->
* rasa_cost
    - utter_rasa_cost   <!-- predicted: action_store_bot_language -->
    - utter_anything_else   <!-- predicted: utter_possibilities -->
* enter_data
    - action_greet_user   <!-- predicted: utter_not_sure -->
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* enter_data
    - action_greet_user   <!-- predicted: action_store_bot_language -->
    - utter_stack_details   <!-- predicted: action_listen -->
    - utter_anything_else   <!-- predicted: utter_built_bot_before -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: utter_ask_migration -->
    - utter_first_bot_with_rasa   <!-- predicted: utter_built_bot_before -->
* handleinsult
    - chitchat: action_chitchat
    - onboarding: utter_first_bot_with_rasa
* affirm
    - action_set_onboarding   <!-- predicted: utter_ask_migration -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: utter_ask_migration -->
* deny
    - action_default_fallback   <!-- predicted: utter_explain_stack -->


## Generated Story goal:1 step, id:ff826c3d37f64c61b6488cfbd2aeb547, 12/15/18 -7283527111737167069
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* affirm
    - utter_thumbsup   <!-- predicted: utter_not_sure -->
    - utter_anything_else   <!-- predicted: action_listen -->
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - utter_built_bot_before   <!-- predicted: action_listen -->
* enter_data
    - action_select_installation_command   <!-- predicted: action_get_community_events -->
    - utter_ask_ready_to_build   <!-- predicted: action_get_community_events -->
* rasa_cost
    - utter_rasa_cost   <!-- predicted: action_store_bot_language -->
    - utter_anything_else   <!-- predicted: utter_possibilities -->
* enter_data
    - action_greet_user   <!-- predicted: utter_not_sure -->
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* enter_data
    - action_greet_user   <!-- predicted: action_store_bot_language -->
    - utter_stack_details   <!-- predicted: action_listen -->
    - utter_anything_else   <!-- predicted: utter_built_bot_before -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: utter_ask_migration -->
    - utter_first_bot_with_rasa   <!-- predicted: utter_built_bot_before -->
* handleinsult
    - chitchat: action_chitchat
    - onboarding: utter_first_bot_with_rasa
* affirm
    - action_set_onboarding   <!-- predicted: utter_ask_migration -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: utter_ask_migration -->
* enter_data
    - action_default_fallback   <!-- predicted: action_store_unknown_product -->


## Generated Story goal:1 step, id:ff826c3d37f64c61b6488cfbd2aeb547, 12/15/18 -7283527111737167069
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* affirm
    - utter_thumbsup   <!-- predicted: utter_not_sure -->
    - utter_anything_else   <!-- predicted: action_listen -->
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - utter_built_bot_before   <!-- predicted: action_listen -->
* enter_data
    - action_select_installation_command   <!-- predicted: action_get_community_events -->
    - utter_ask_ready_to_build   <!-- predicted: action_get_community_events -->
* rasa_cost
    - utter_rasa_cost   <!-- predicted: action_store_bot_language -->
    - utter_anything_else   <!-- predicted: utter_possibilities -->
* enter_data
    - action_greet_user   <!-- predicted: utter_not_sure -->
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* enter_data
    - action_greet_user   <!-- predicted: action_store_bot_language -->
    - utter_stack_details   <!-- predicted: action_listen -->
    - utter_anything_else   <!-- predicted: utter_built_bot_before -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: utter_ask_migration -->
    - utter_first_bot_with_rasa   <!-- predicted: utter_built_bot_before -->
* handleinsult
    - chitchat: action_chitchat
    - onboarding: utter_first_bot_with_rasa
* affirm
    - action_set_onboarding   <!-- predicted: utter_ask_migration -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: utter_ask_migration -->
* bye
    - utter_bye   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_built_bot_before -->
* nlu_info
    - action_default_fallback   <!-- predicted: utter_get_python -->


## Generated Story goal:1 step, id:ff826c3d37f64c61b6488cfbd2aeb547, 12/15/18 -7283527111737167069
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* affirm
    - utter_thumbsup   <!-- predicted: utter_not_sure -->
    - utter_anything_else   <!-- predicted: action_listen -->
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - utter_built_bot_before   <!-- predicted: action_listen -->
* enter_data
    - action_select_installation_command   <!-- predicted: action_get_community_events -->
    - utter_ask_ready_to_build   <!-- predicted: action_get_community_events -->
* rasa_cost
    - utter_rasa_cost   <!-- predicted: action_store_bot_language -->
    - utter_anything_else   <!-- predicted: utter_possibilities -->
* enter_data
    - action_greet_user   <!-- predicted: utter_not_sure -->
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* enter_data
    - action_greet_user   <!-- predicted: action_store_bot_language -->
    - utter_stack_details   <!-- predicted: action_listen -->
    - utter_anything_else   <!-- predicted: utter_built_bot_before -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: utter_ask_migration -->
    - utter_first_bot_with_rasa   <!-- predicted: utter_built_bot_before -->
* handleinsult
    - chitchat: action_chitchat
    - onboarding: utter_first_bot_with_rasa
* affirm
    - action_set_onboarding   <!-- predicted: utter_ask_migration -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: utter_ask_migration -->
* bye
    - utter_bye   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_built_bot_before -->
* deny
    - action_default_fallback   <!-- predicted: utter_explain_stack -->


## Generated Story goal:1 step, id:79e8dd05329946a8963c170d920e0144, 05/01/19 -5283482436135596936
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - getstarted_1: utter_built_bot_before
* enter_data
    - utter_ask_migration   <!-- predicted: action_get_community_events -->
* enter_data
    - utter_contact_email   <!-- predicted: action_get_community_events -->
* ask_howdoing
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->
* telljoke
    - action_revert_fallback_events   <!-- predicted: action_chitchat -->


## Generated Story goal:1 step, id:79e8dd05329946a8963c170d920e0144, 05/01/19 -5283482436135596936
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - getstarted_1: utter_built_bot_before
* enter_data
    - utter_ask_migration   <!-- predicted: action_get_community_events -->
* enter_data
    - utter_contact_email   <!-- predicted: action_get_community_events -->
* ask_howdoing
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->


## Generated Story goal:1 step, id:79e8dd05329946a8963c170d920e0144, 05/01/19 -5283482436135596936
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - getstarted_1: utter_built_bot_before
* enter_data
    - utter_ask_migration   <!-- predicted: action_get_community_events -->
* enter_data
    - utter_contact_email   <!-- predicted: action_get_community_events -->
* telljoke
    - chitchat: action_chitchat
* telljoke
    - chitchat: action_chitchat
* react_negative
    - action_default_ask_affirmation   <!-- predicted: utter_canthelp -->
* ask_faq_channels
    - action_revert_fallback_events   <!-- predicted: action_faqs -->


## Generated Story goal:1 step, id:79e8dd05329946a8963c170d920e0144, 05/01/19 -5283482436135596936
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - getstarted_1: utter_built_bot_before
* enter_data
    - utter_ask_migration   <!-- predicted: action_get_community_events -->
* enter_data
    - utter_contact_email   <!-- predicted: action_get_community_events -->
* telljoke
    - chitchat: action_chitchat
* telljoke
    - chitchat: action_chitchat
* react_negative
    - action_default_ask_affirmation   <!-- predicted: utter_canthelp -->


## Generated Story goal:1 step, id:79e8dd05329946a8963c170d920e0144, 05/01/19 -5283482436135596936
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - getstarted_1: utter_built_bot_before
* enter_data
    - utter_ask_migration   <!-- predicted: action_get_community_events -->
* enter_data
    - utter_contact_email   <!-- predicted: action_get_community_events -->
* telljoke
    - chitchat: action_chitchat
* telljoke
    - chitchat: action_chitchat
* ask_faq_channels
    - faq: action_faqs
* technical_question
    - action_default_ask_affirmation   <!-- predicted: action_faqs -->
* how_to_get_started
    - action_revert_fallback_events   <!-- predicted: utter_getstarted -->


## Generated Story goal:1 step, id:79e8dd05329946a8963c170d920e0144, 05/01/19 -5283482436135596936
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - getstarted_1: utter_built_bot_before
* enter_data
    - utter_ask_migration   <!-- predicted: action_get_community_events -->
* enter_data
    - utter_contact_email   <!-- predicted: action_get_community_events -->
* telljoke
    - chitchat: action_chitchat
* telljoke
    - chitchat: action_chitchat
* ask_faq_channels
    - faq: action_faqs
* technical_question
    - action_default_ask_affirmation   <!-- predicted: action_faqs -->


## Generated Story goal:1 step, id:de903a69d7524115a8affa517ba1df0c, 12/15/18 4546830120439352871
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"name": "sara"}
    - slot{"name": "sara"}
    - slot{"name": "sara"}
    - action_default_fallback   <!-- predicted: utter_getstarted -->


## Generated Story goal:1 step, id:de903a69d7524115a8affa517ba1df0c, 12/15/18 4546830120439352871
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatisrasa
    - chitchat: action_chitchat
* how_to_get_started
    - action_default_fallback   <!-- predicted: utter_getstarted -->


## Generated Story goal:1 step, id:f425b3ba996e4eaeacbc82becd473dbf, 12/17/18 4246660389998784195
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* ask_whoisit
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* ask_howdoing
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_chitchat -->
* ask_howold
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->
* deny
    - action_default_ask_rephrase   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* ask_whatspossible
    - action_revert_fallback_events   <!-- predicted: action_chitchat -->


## Generated Story goal:1 step, id:f425b3ba996e4eaeacbc82becd473dbf, 12/17/18 4246660389998784195
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* ask_whoisit
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* ask_howdoing
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_chitchat -->
* ask_howold
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->
* deny
    - action_default_ask_rephrase   <!-- predicted: utter_tryout -->


## Generated Story goal:1 step, id:f425b3ba996e4eaeacbc82becd473dbf, 12/17/18 4246660389998784195
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* ask_whoisit
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* ask_howdoing
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_chitchat -->
* ask_howold
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:9a569475596347ad9d181b33f887a87f, 12/15/18 2802758851923456977
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whoisit
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_chitchat
* enter_data
    - action_store_email   <!-- predicted: utter_not_sure -->


## Generated Story goal:chitchat, id:9a569475596347ad9d181b33f887a87f, 12/15/18 2802758851923456977
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whoisit
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_chitchat
* enter_data{"email": "tens@da.ok"}
    - slot{"email": "tens@da.ok"}
    - slot{"email": "tens@da.ok"}
    - action_store_email   <!-- predicted: utter_not_sure -->
    - slot{"email": "tens@da.ok"}
    - subscribe: action_subscribe_newsletter -> fail
    - slot{"subscribed": true}
    - subscribe: utter_awesome -> fail
    - subscribe_success: utter_confirmationemail -> fail
    - subscribe: utter_docu -> fail
    - feedback: utter_ask_feedback -> fail
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* ask_restaurant
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:9a569475596347ad9d181b33f887a87f, 12/15/18 2802758851923456977
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whoisit
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_chitchat
* enter_data{"email": "tens@da.ok"}
    - slot{"email": "tens@da.ok"}
    - slot{"email": "tens@da.ok"}
    - action_store_email   <!-- predicted: utter_not_sure -->
    - slot{"email": "tens@da.ok"}
    - subscribe: action_subscribe_newsletter -> fail
    - slot{"subscribed": true}
    - subscribe: utter_awesome -> fail
    - subscribe_success: utter_confirmationemail -> fail
    - subscribe: utter_docu -> fail
    - feedback: utter_ask_feedback -> fail
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* enter_data
    - utter_great   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* affirm
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* affirm
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* ask_whoisit
    - action_default_fallback   <!-- predicted: utter_great -->


## Generated Story goal:chitchat, id:9a569475596347ad9d181b33f887a87f, 12/15/18 2802758851923456977
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whoisit
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_chitchat
* enter_data{"email": "tens@da.ok"}
    - slot{"email": "tens@da.ok"}
    - slot{"email": "tens@da.ok"}
    - action_store_email   <!-- predicted: utter_not_sure -->
    - slot{"email": "tens@da.ok"}
    - subscribe: action_subscribe_newsletter -> fail
    - slot{"subscribed": true}
    - subscribe: utter_awesome -> fail
    - subscribe_success: utter_confirmationemail -> fail
    - subscribe: utter_docu -> fail
    - feedback: utter_ask_feedback -> fail
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* enter_data
    - utter_great   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* affirm
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* affirm
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* deny
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* ask_wherefrom
    - action_chitchat   <!-- predicted: utter_great -->
* enter_data
    - action_default_fallback   <!-- predicted: utter_great -->


## Generated Story goal:chitchat, id:9a569475596347ad9d181b33f887a87f, 12/15/18 2802758851923456977
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whoisit
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_chitchat
* enter_data{"email": "tens@da.ok"}
    - slot{"email": "tens@da.ok"}
    - slot{"email": "tens@da.ok"}
    - action_store_email   <!-- predicted: utter_not_sure -->
    - slot{"email": "tens@da.ok"}
    - subscribe: action_subscribe_newsletter -> fail
    - slot{"subscribed": true}
    - subscribe: utter_awesome -> fail
    - subscribe_success: utter_confirmationemail -> fail
    - subscribe: utter_docu -> fail
    - feedback: utter_ask_feedback -> fail
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* enter_data
    - utter_great   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* affirm
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* affirm
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* deny
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* ask_wherefrom
    - action_chitchat   <!-- predicted: utter_great -->
* affirm
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* enter_data
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* handleinsult
    - action_chitchat   <!-- predicted: utter_great -->
* enter_data
    - action_default_fallback   <!-- predicted: utter_great -->


## Generated Story goal:oos, id:174129b4be704f47b76aa8dc5b2f3ab6, 12/15/18 -5421971901023397932
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* enter_data
    - action_default_fallback   <!-- predicted: utter_not_sure -->


## Generated Story goal:oos, id:174129b4be704f47b76aa8dc5b2f3ab6, 12/15/18 -5421971901023397932
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* out_of_scope
    - oos: utter_out_of_scope
* enter_data{"email": "lavi@email.com"}
    - slot{"email": "lavi@email.com"}
    - slot{"email": "lavi@email.com"}
    - action_greet_user   <!-- predicted: utter_not_sure -->
* greet
    - greet_success: action_greet_user
* enter_data
    - action_default_fallback   <!-- predicted: action_store_email -->


## Generated Story goal:1 step, id:9e28b5d02f08459b9cb19e2888976813, 12/15/18 523765784065373811
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_python_installed -->
* ask_howdoing
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: action_set_onboarding -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_greet_user -->
* signup_newsletter
    - utter_great   <!-- predicted: utter_tryout -->
    - utter_ask_email   <!-- predicted: utter_tryout -->
* enter_data{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - action_store_email   <!-- predicted: utter_tryout -->
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed   <!-- predicted: action_store_email -->
    - utter_docu   <!-- predicted: utter_tryout -->
    - utter_ask_feedback   <!-- predicted: utter_tryout -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* greet
    - action_default_ask_affirmation   <!-- predicted: utter_anything_else -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_restaurant
    - action_revert_fallback_events   <!-- predicted: action_chitchat -->


## Generated Story goal:1 step, id:9e28b5d02f08459b9cb19e2888976813, 12/15/18 523765784065373811
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_python_installed -->
* ask_howdoing
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: action_set_onboarding -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_greet_user -->
* signup_newsletter
    - utter_great   <!-- predicted: utter_tryout -->
    - utter_ask_email   <!-- predicted: utter_tryout -->
* enter_data{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - action_store_email   <!-- predicted: utter_tryout -->
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed   <!-- predicted: action_store_email -->
    - utter_docu   <!-- predicted: utter_tryout -->
    - utter_ask_feedback   <!-- predicted: utter_tryout -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* greet
    - action_default_ask_affirmation   <!-- predicted: utter_anything_else -->


## Generated Story goal:1 step, id:9e28b5d02f08459b9cb19e2888976813, 12/15/18 523765784065373811
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_python_installed -->
* ask_howdoing
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: action_set_onboarding -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_greet_user -->
* signup_newsletter
    - utter_great   <!-- predicted: utter_tryout -->
    - utter_ask_email   <!-- predicted: utter_tryout -->
* enter_data{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - action_store_email   <!-- predicted: utter_tryout -->
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed   <!-- predicted: action_store_email -->
    - utter_docu   <!-- predicted: utter_tryout -->
    - utter_ask_feedback   <!-- predicted: utter_tryout -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* ask_restaurant
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_anything_else -->
* affirm
    - action_default_fallback   <!-- predicted: utter_great -->


## Generated Story goal:1 step, id:9e28b5d02f08459b9cb19e2888976813, 12/15/18 523765784065373811
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_python_installed -->
* ask_howdoing
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: action_set_onboarding -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_greet_user -->
* signup_newsletter
    - utter_great   <!-- predicted: utter_tryout -->
    - utter_ask_email   <!-- predicted: utter_tryout -->
* enter_data{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - action_store_email   <!-- predicted: utter_tryout -->
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed   <!-- predicted: action_store_email -->
    - utter_docu   <!-- predicted: utter_tryout -->
    - utter_ask_feedback   <!-- predicted: utter_tryout -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* ask_restaurant
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_anything_else -->
* out_of_scope
    - action_default_fallback   <!-- predicted: utter_anything_else -->


## Generated Story goal:1 step, id:9e28b5d02f08459b9cb19e2888976813, 12/15/18 523765784065373811
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_python_installed -->
* ask_howdoing
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: action_set_onboarding -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_greet_user -->
* signup_newsletter
    - utter_great   <!-- predicted: utter_tryout -->
    - utter_ask_email   <!-- predicted: utter_tryout -->
* enter_data{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - action_store_email   <!-- predicted: utter_tryout -->
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed   <!-- predicted: action_store_email -->
    - utter_docu   <!-- predicted: utter_tryout -->
    - utter_ask_feedback   <!-- predicted: utter_tryout -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* ask_restaurant
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_anything_else -->
* deny
    - action_default_fallback   <!-- predicted: utter_great -->


## Generated Story goal:1 step, id:9e28b5d02f08459b9cb19e2888976813, 12/15/18 523765784065373811
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_python_installed -->
* ask_howdoing
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: action_set_onboarding -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_greet_user -->
* signup_newsletter
    - utter_great   <!-- predicted: utter_tryout -->
    - utter_ask_email   <!-- predicted: utter_tryout -->
* enter_data{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - action_store_email   <!-- predicted: utter_tryout -->
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed   <!-- predicted: action_store_email -->
    - utter_docu   <!-- predicted: utter_tryout -->
    - utter_ask_feedback   <!-- predicted: utter_tryout -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* ask_restaurant
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_anything_else -->
* bye
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:1 step, id:9e28b5d02f08459b9cb19e2888976813, 12/15/18 523765784065373811
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_python_installed -->
* ask_howdoing
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: action_set_onboarding -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_greet_user -->
* signup_newsletter
    - utter_great   <!-- predicted: utter_tryout -->
    - utter_ask_email   <!-- predicted: utter_tryout -->
* enter_data{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - action_store_email   <!-- predicted: utter_tryout -->
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed   <!-- predicted: action_store_email -->
    - utter_docu   <!-- predicted: utter_tryout -->
    - utter_ask_feedback   <!-- predicted: utter_tryout -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* ask_restaurant
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_anything_else -->
* deny
    - action_default_fallback   <!-- predicted: utter_great -->


## Generated Story goal:1 step, id:9e28b5d02f08459b9cb19e2888976813, 12/15/18 523765784065373811
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_python_installed -->
* ask_howdoing
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: action_set_onboarding -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_greet_user -->
* signup_newsletter
    - utter_great   <!-- predicted: utter_tryout -->
    - utter_ask_email   <!-- predicted: utter_tryout -->
* enter_data{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - action_store_email   <!-- predicted: utter_tryout -->
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed   <!-- predicted: action_store_email -->
    - utter_docu   <!-- predicted: utter_tryout -->
    - utter_ask_feedback   <!-- predicted: utter_tryout -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* ask_restaurant
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_anything_else -->
* greet
    - action_default_fallback   <!-- predicted: utter_anything_else -->


## Generated Story goal:1 step, id:9e28b5d02f08459b9cb19e2888976813, 12/15/18 523765784065373811
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_python_installed -->
* ask_howdoing
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: action_set_onboarding -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_greet_user -->
* signup_newsletter
    - utter_great   <!-- predicted: utter_tryout -->
    - utter_ask_email   <!-- predicted: utter_tryout -->
* enter_data{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - action_store_email   <!-- predicted: utter_tryout -->
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed   <!-- predicted: action_store_email -->
    - utter_docu   <!-- predicted: utter_tryout -->
    - utter_ask_feedback   <!-- predicted: utter_tryout -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* ask_restaurant
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_anything_else -->
* bye
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:1 step, id:9e28b5d02f08459b9cb19e2888976813, 12/15/18 523765784065373811
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_python_installed -->
* ask_howdoing
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: action_set_onboarding -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_greet_user -->
* signup_newsletter
    - utter_great   <!-- predicted: utter_tryout -->
    - utter_ask_email   <!-- predicted: utter_tryout -->
* enter_data{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - action_store_email   <!-- predicted: utter_tryout -->
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed   <!-- predicted: action_store_email -->
    - utter_docu   <!-- predicted: utter_tryout -->
    - utter_ask_feedback   <!-- predicted: utter_tryout -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* ask_restaurant
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_anything_else -->
* canthelp
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:1 step, id:9e28b5d02f08459b9cb19e2888976813, 12/15/18 523765784065373811
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_python_installed -->
* ask_howdoing
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: action_set_onboarding -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_greet_user -->
* signup_newsletter
    - utter_great   <!-- predicted: utter_tryout -->
    - utter_ask_email   <!-- predicted: utter_tryout -->
* enter_data{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - action_store_email   <!-- predicted: utter_tryout -->
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed   <!-- predicted: action_store_email -->
    - utter_docu   <!-- predicted: utter_tryout -->
    - utter_ask_feedback   <!-- predicted: utter_tryout -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* ask_restaurant
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_anything_else -->
* bye
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:1 step, id:9e28b5d02f08459b9cb19e2888976813, 12/15/18 523765784065373811
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_python_installed -->
* ask_howdoing
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: action_set_onboarding -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_greet_user -->
* signup_newsletter
    - utter_great   <!-- predicted: utter_tryout -->
    - utter_ask_email   <!-- predicted: utter_tryout -->
* enter_data{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - action_store_email   <!-- predicted: utter_tryout -->
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed   <!-- predicted: action_store_email -->
    - utter_docu   <!-- predicted: utter_tryout -->
    - utter_ask_feedback   <!-- predicted: utter_tryout -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* ask_restaurant
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_anything_else -->
* enter_data
    - action_default_fallback   <!-- predicted: utter_great -->


## Generated Story goal:1 step, id:9e28b5d02f08459b9cb19e2888976813, 12/15/18 523765784065373811
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_python_installed -->
* ask_howdoing
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: action_set_onboarding -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_greet_user -->
* signup_newsletter
    - utter_great   <!-- predicted: utter_tryout -->
    - utter_ask_email   <!-- predicted: utter_tryout -->
* enter_data{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - action_store_email   <!-- predicted: utter_tryout -->
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed   <!-- predicted: action_store_email -->
    - utter_docu   <!-- predicted: utter_tryout -->
    - utter_ask_feedback   <!-- predicted: utter_tryout -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* ask_restaurant
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_anything_else -->
* signup_newsletter
    - subscribe: utter_great
    - action_listen   <!-- predicted: utter_anything_else -->
* out_of_scope
    - utter_great   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - utter_ask_name   <!-- predicted: utter_great -->
    - utter_anything_else   <!-- predicted: action_listen -->
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* enter_data
    - utter_spacy_or_tensorflow   <!-- predicted: utter_great -->
    - chitchat: utter_anything_else -> fail
* signup_newsletter
    - action_default_ask_affirmation   <!-- predicted: utter_great -->
* deny
    - action_default_ask_rephrase   <!-- predicted: utter_great -->
* canthelp
    - action_revert_fallback_events   <!-- predicted: utter_great -->


## Generated Story goal:1 step, id:9e28b5d02f08459b9cb19e2888976813, 12/15/18 523765784065373811
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_python_installed -->
* ask_howdoing
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: action_set_onboarding -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_greet_user -->
* signup_newsletter
    - utter_great   <!-- predicted: utter_tryout -->
    - utter_ask_email   <!-- predicted: utter_tryout -->
* enter_data{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - action_store_email   <!-- predicted: utter_tryout -->
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed   <!-- predicted: action_store_email -->
    - utter_docu   <!-- predicted: utter_tryout -->
    - utter_ask_feedback   <!-- predicted: utter_tryout -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* ask_restaurant
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_anything_else -->
* signup_newsletter
    - subscribe: utter_great
    - action_listen   <!-- predicted: utter_anything_else -->
* out_of_scope
    - utter_great   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - utter_ask_name   <!-- predicted: utter_great -->
    - utter_anything_else   <!-- predicted: action_listen -->
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* enter_data
    - utter_spacy_or_tensorflow   <!-- predicted: utter_great -->
    - chitchat: utter_anything_else -> fail
* signup_newsletter
    - action_default_ask_affirmation   <!-- predicted: utter_great -->
* deny
    - action_default_ask_rephrase   <!-- predicted: utter_great -->


## Generated Story goal:1 step, id:9e28b5d02f08459b9cb19e2888976813, 12/15/18 523765784065373811
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_python_installed -->
* ask_howdoing
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: action_set_onboarding -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_greet_user -->
* signup_newsletter
    - utter_great   <!-- predicted: utter_tryout -->
    - utter_ask_email   <!-- predicted: utter_tryout -->
* enter_data{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - action_store_email   <!-- predicted: utter_tryout -->
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed   <!-- predicted: action_store_email -->
    - utter_docu   <!-- predicted: utter_tryout -->
    - utter_ask_feedback   <!-- predicted: utter_tryout -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* ask_restaurant
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_anything_else -->
* signup_newsletter
    - subscribe: utter_great
    - action_listen   <!-- predicted: utter_anything_else -->
* out_of_scope
    - utter_great   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - utter_ask_name   <!-- predicted: utter_great -->
    - utter_anything_else   <!-- predicted: action_listen -->
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* enter_data
    - utter_spacy_or_tensorflow   <!-- predicted: utter_great -->
    - chitchat: utter_anything_else -> fail
* signup_newsletter
    - action_default_ask_affirmation   <!-- predicted: utter_great -->


## Generated Story goal:1 step, id:9e28b5d02f08459b9cb19e2888976813, 12/15/18 523765784065373811
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_python_installed -->
* ask_howdoing
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: action_set_onboarding -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_greet_user -->
* signup_newsletter
    - utter_great   <!-- predicted: utter_tryout -->
    - utter_ask_email   <!-- predicted: utter_tryout -->
* enter_data{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - action_store_email   <!-- predicted: utter_tryout -->
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed   <!-- predicted: action_store_email -->
    - utter_docu   <!-- predicted: utter_tryout -->
    - utter_ask_feedback   <!-- predicted: utter_tryout -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* ask_restaurant
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_anything_else -->
* signup_newsletter
    - subscribe: utter_great
    - action_listen   <!-- predicted: utter_anything_else -->
* out_of_scope
    - utter_great   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - utter_ask_name   <!-- predicted: utter_great -->
    - utter_anything_else   <!-- predicted: action_listen -->
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* enter_data
    - utter_spacy_or_tensorflow   <!-- predicted: utter_great -->
    - chitchat: utter_anything_else -> fail
* canthelp
    - utter_canthelp   <!-- predicted: utter_great -->
* bye
    - action_default_fallback   <!-- predicted: utter_great -->


## Generated Story goal:1 step, id:9e28b5d02f08459b9cb19e2888976813, 12/15/18 523765784065373811
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_python_installed -->
* ask_howdoing
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: action_set_onboarding -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_greet_user -->
* signup_newsletter
    - utter_great   <!-- predicted: utter_tryout -->
    - utter_ask_email   <!-- predicted: utter_tryout -->
* enter_data{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - action_store_email   <!-- predicted: utter_tryout -->
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed   <!-- predicted: action_store_email -->
    - utter_docu   <!-- predicted: utter_tryout -->
    - utter_ask_feedback   <!-- predicted: utter_tryout -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* ask_restaurant
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_anything_else -->
* signup_newsletter
    - subscribe: utter_great
    - action_listen   <!-- predicted: utter_anything_else -->
* out_of_scope
    - utter_great   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - utter_ask_name   <!-- predicted: utter_great -->
    - utter_anything_else   <!-- predicted: action_listen -->
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* enter_data
    - utter_spacy_or_tensorflow   <!-- predicted: utter_great -->
    - chitchat: utter_anything_else -> fail
* canthelp
    - utter_canthelp   <!-- predicted: utter_great -->
* bye
    - action_default_fallback   <!-- predicted: utter_great -->


## Generated Story goal:1 step, id:9e28b5d02f08459b9cb19e2888976813, 12/15/18 523765784065373811
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_python_installed -->
* ask_howdoing
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: action_set_onboarding -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_greet_user -->
* signup_newsletter
    - utter_great   <!-- predicted: utter_tryout -->
    - utter_ask_email   <!-- predicted: utter_tryout -->
* enter_data{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - action_store_email   <!-- predicted: utter_tryout -->
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed   <!-- predicted: action_store_email -->
    - utter_docu   <!-- predicted: utter_tryout -->
    - utter_ask_feedback   <!-- predicted: utter_tryout -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* ask_restaurant
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_anything_else -->
* signup_newsletter
    - subscribe: utter_great
    - action_listen   <!-- predicted: utter_anything_else -->
* out_of_scope
    - utter_great   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - utter_ask_name   <!-- predicted: utter_great -->
    - utter_anything_else   <!-- predicted: action_listen -->
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* enter_data
    - utter_spacy_or_tensorflow   <!-- predicted: utter_great -->
    - chitchat: utter_anything_else -> fail
* canthelp
    - utter_canthelp   <!-- predicted: utter_great -->
* bye
    - action_default_fallback   <!-- predicted: utter_great -->


## Generated Story goal:1 step, id:9e28b5d02f08459b9cb19e2888976813, 12/15/18 523765784065373811
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_python_installed -->
* ask_howdoing
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: action_set_onboarding -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_greet_user -->
* signup_newsletter
    - utter_great   <!-- predicted: utter_tryout -->
    - utter_ask_email   <!-- predicted: utter_tryout -->
* enter_data{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - action_store_email   <!-- predicted: utter_tryout -->
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed   <!-- predicted: action_store_email -->
    - utter_docu   <!-- predicted: utter_tryout -->
    - utter_ask_feedback   <!-- predicted: utter_tryout -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* ask_restaurant
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_anything_else -->
* signup_newsletter
    - subscribe: utter_great
    - action_listen   <!-- predicted: utter_anything_else -->
* out_of_scope
    - utter_great   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - utter_ask_name   <!-- predicted: utter_great -->
    - utter_anything_else   <!-- predicted: action_listen -->
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* enter_data
    - utter_spacy_or_tensorflow   <!-- predicted: utter_great -->
    - chitchat: utter_anything_else -> fail
* canthelp
    - utter_canthelp   <!-- predicted: utter_great -->
* bye
    - action_default_fallback   <!-- predicted: utter_great -->


## Generated Story goal:1 step, id:9e28b5d02f08459b9cb19e2888976813, 12/15/18 523765784065373811
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_python_installed -->
* ask_howdoing
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: action_set_onboarding -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_greet_user -->
* signup_newsletter
    - utter_great   <!-- predicted: utter_tryout -->
    - utter_ask_email   <!-- predicted: utter_tryout -->
* enter_data{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - action_store_email   <!-- predicted: utter_tryout -->
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed   <!-- predicted: action_store_email -->
    - utter_docu   <!-- predicted: utter_tryout -->
    - utter_ask_feedback   <!-- predicted: utter_tryout -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* ask_restaurant
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_anything_else -->
* signup_newsletter
    - subscribe: utter_great
    - action_listen   <!-- predicted: utter_anything_else -->
* out_of_scope
    - utter_great   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - utter_ask_name   <!-- predicted: utter_great -->
    - utter_anything_else   <!-- predicted: action_listen -->
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* enter_data
    - utter_spacy_or_tensorflow   <!-- predicted: utter_great -->
    - chitchat: utter_anything_else -> fail
* canthelp
    - utter_canthelp   <!-- predicted: utter_great -->
* greet
    - action_greet_user   <!-- predicted: utter_great -->
* bye
    - utter_ask_company   <!-- predicted: utter_great -->
* enter_data{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - action_store_company   <!-- predicted: utter_anything_else -->
    - slot{"company_name": "google"}
    - utter_ask_businessmail   <!-- predicted: utter_anything_else -->
* enter_data{"email": "arvind@google.com"}
    - slot{"email": "arvind@google.com"}
    - slot{"email": "arvind@google.com"}
    - action_store_email   <!-- predicted: utter_great -->
    - slot{"email": "arvind@google.com"}
    - action_subscribe_newsletter   <!-- predicted: action_listen -->
    - slot{"subscribed": true}
    - utter_awesome   <!-- predicted: action_listen -->
    - utter_confirmationemail   <!-- predicted: action_listen -->
    - utter_docu   <!-- predicted: action_listen -->
    - utter_ask_feedback   <!-- predicted: action_listen -->
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - utter_thumbsup   <!-- predicted: utter_switch_dialogflow -->
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_thumbsup   <!-- predicted: utter_anything_else -->
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_thumbsup   <!-- predicted: utter_anything_else -->
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - chitchat: utter_anything_else -> fail
* thank
    - utter_anything_else   <!-- predicted: utter_moreinformation -->
* bye
    - utter_bye   <!-- predicted: action_store_email -->
* greet
    - action_get_community_events   <!-- predicted: action_store_email -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_whoisit
    - action_chitchat   <!-- predicted: utter_not_sure -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_howold
    - action_chitchat   <!-- predicted: utter_not_sure -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_howold
    - action_faqs   <!-- predicted: utter_not_sure -->
    - action_listen   <!-- predicted: utter_anything_else -->
* greet
    - action_default_fallback   <!-- predicted: action_store_email -->


## Generated Story goal:1 step, id:9e28b5d02f08459b9cb19e2888976813, 12/15/18 523765784065373811
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_python_installed -->
* ask_howdoing
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: action_set_onboarding -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_greet_user -->
* signup_newsletter
    - utter_great   <!-- predicted: utter_tryout -->
    - utter_ask_email   <!-- predicted: utter_tryout -->
* enter_data{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - action_store_email   <!-- predicted: utter_tryout -->
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed   <!-- predicted: action_store_email -->
    - utter_docu   <!-- predicted: utter_tryout -->
    - utter_ask_feedback   <!-- predicted: utter_tryout -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* ask_restaurant
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_anything_else -->
* signup_newsletter
    - subscribe: utter_great
    - action_listen   <!-- predicted: utter_anything_else -->
* out_of_scope
    - utter_great   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - utter_ask_name   <!-- predicted: utter_great -->
    - utter_anything_else   <!-- predicted: action_listen -->
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* enter_data
    - utter_spacy_or_tensorflow   <!-- predicted: utter_great -->
    - chitchat: utter_anything_else -> fail
* canthelp
    - utter_canthelp   <!-- predicted: utter_great -->
* greet
    - action_greet_user   <!-- predicted: utter_great -->
* bye
    - utter_ask_company   <!-- predicted: utter_great -->
* enter_data{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - action_store_company   <!-- predicted: utter_anything_else -->
    - slot{"company_name": "google"}
    - utter_ask_businessmail   <!-- predicted: utter_anything_else -->
* enter_data{"email": "arvind@google.com"}
    - slot{"email": "arvind@google.com"}
    - slot{"email": "arvind@google.com"}
    - action_store_email   <!-- predicted: utter_great -->
    - slot{"email": "arvind@google.com"}
    - action_subscribe_newsletter   <!-- predicted: action_listen -->
    - slot{"subscribed": true}
    - utter_awesome   <!-- predicted: action_listen -->
    - utter_confirmationemail   <!-- predicted: action_listen -->
    - utter_docu   <!-- predicted: action_listen -->
    - utter_ask_feedback   <!-- predicted: action_listen -->
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - utter_thumbsup   <!-- predicted: utter_switch_dialogflow -->
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_thumbsup   <!-- predicted: utter_anything_else -->
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_thumbsup   <!-- predicted: utter_anything_else -->
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - chitchat: utter_anything_else -> fail
* thank
    - utter_anything_else   <!-- predicted: utter_moreinformation -->
* bye
    - utter_bye   <!-- predicted: action_store_email -->
* greet
    - action_get_community_events   <!-- predicted: action_store_email -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_whoisit
    - action_chitchat   <!-- predicted: utter_not_sure -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_howold
    - action_chitchat   <!-- predicted: utter_not_sure -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_howold
    - action_faqs   <!-- predicted: utter_not_sure -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_howold
    - action_default_ask_affirmation   <!-- predicted: utter_not_sure -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_howold
    - action_revert_fallback_events   <!-- predicted: utter_not_sure -->


## Generated Story goal:1 step, id:9e28b5d02f08459b9cb19e2888976813, 12/15/18 523765784065373811
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_python_installed -->
* ask_howdoing
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: action_set_onboarding -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_greet_user -->
* signup_newsletter
    - utter_great   <!-- predicted: utter_tryout -->
    - utter_ask_email   <!-- predicted: utter_tryout -->
* enter_data{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - action_store_email   <!-- predicted: utter_tryout -->
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed   <!-- predicted: action_store_email -->
    - utter_docu   <!-- predicted: utter_tryout -->
    - utter_ask_feedback   <!-- predicted: utter_tryout -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* ask_restaurant
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_anything_else -->
* signup_newsletter
    - subscribe: utter_great
    - action_listen   <!-- predicted: utter_anything_else -->
* out_of_scope
    - utter_great   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - utter_ask_name   <!-- predicted: utter_great -->
    - utter_anything_else   <!-- predicted: action_listen -->
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* enter_data
    - utter_spacy_or_tensorflow   <!-- predicted: utter_great -->
    - chitchat: utter_anything_else -> fail
* canthelp
    - utter_canthelp   <!-- predicted: utter_great -->
* greet
    - action_greet_user   <!-- predicted: utter_great -->
* bye
    - utter_ask_company   <!-- predicted: utter_great -->
* enter_data{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - action_store_company   <!-- predicted: utter_anything_else -->
    - slot{"company_name": "google"}
    - utter_ask_businessmail   <!-- predicted: utter_anything_else -->
* enter_data{"email": "arvind@google.com"}
    - slot{"email": "arvind@google.com"}
    - slot{"email": "arvind@google.com"}
    - action_store_email   <!-- predicted: utter_great -->
    - slot{"email": "arvind@google.com"}
    - action_subscribe_newsletter   <!-- predicted: action_listen -->
    - slot{"subscribed": true}
    - utter_awesome   <!-- predicted: action_listen -->
    - utter_confirmationemail   <!-- predicted: action_listen -->
    - utter_docu   <!-- predicted: action_listen -->
    - utter_ask_feedback   <!-- predicted: action_listen -->
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - utter_thumbsup   <!-- predicted: utter_switch_dialogflow -->
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_thumbsup   <!-- predicted: utter_anything_else -->
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_thumbsup   <!-- predicted: utter_anything_else -->
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - chitchat: utter_anything_else -> fail
* thank
    - utter_anything_else   <!-- predicted: utter_moreinformation -->
* bye
    - utter_bye   <!-- predicted: action_store_email -->
* greet
    - action_get_community_events   <!-- predicted: action_store_email -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_whoisit
    - action_chitchat   <!-- predicted: utter_not_sure -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_howold
    - action_chitchat   <!-- predicted: utter_not_sure -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_howold
    - action_faqs   <!-- predicted: utter_not_sure -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_howold
    - action_default_ask_affirmation   <!-- predicted: utter_not_sure -->


## Generated Story goal:1 step, id:9e28b5d02f08459b9cb19e2888976813, 12/15/18 523765784065373811
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_python_installed -->
* ask_howdoing
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: action_set_onboarding -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_greet_user -->
* signup_newsletter
    - utter_great   <!-- predicted: utter_tryout -->
    - utter_ask_email   <!-- predicted: utter_tryout -->
* enter_data{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - action_store_email   <!-- predicted: utter_tryout -->
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed   <!-- predicted: action_store_email -->
    - utter_docu   <!-- predicted: utter_tryout -->
    - utter_ask_feedback   <!-- predicted: utter_tryout -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* ask_restaurant
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_anything_else -->
* signup_newsletter
    - subscribe: utter_great
    - action_listen   <!-- predicted: utter_anything_else -->
* out_of_scope
    - utter_great   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - utter_ask_name   <!-- predicted: utter_great -->
    - utter_anything_else   <!-- predicted: action_listen -->
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* enter_data
    - utter_spacy_or_tensorflow   <!-- predicted: utter_great -->
    - chitchat: utter_anything_else -> fail
* canthelp
    - utter_canthelp   <!-- predicted: utter_great -->
* greet
    - action_greet_user   <!-- predicted: utter_great -->
* bye
    - utter_ask_company   <!-- predicted: utter_great -->
* enter_data{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - action_store_company   <!-- predicted: utter_anything_else -->
    - slot{"company_name": "google"}
    - utter_ask_businessmail   <!-- predicted: utter_anything_else -->
* enter_data{"email": "arvind@google.com"}
    - slot{"email": "arvind@google.com"}
    - slot{"email": "arvind@google.com"}
    - action_store_email   <!-- predicted: utter_great -->
    - slot{"email": "arvind@google.com"}
    - action_subscribe_newsletter   <!-- predicted: action_listen -->
    - slot{"subscribed": true}
    - utter_awesome   <!-- predicted: action_listen -->
    - utter_confirmationemail   <!-- predicted: action_listen -->
    - utter_docu   <!-- predicted: action_listen -->
    - utter_ask_feedback   <!-- predicted: action_listen -->
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - utter_thumbsup   <!-- predicted: utter_switch_dialogflow -->
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_thumbsup   <!-- predicted: utter_anything_else -->
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_thumbsup   <!-- predicted: utter_anything_else -->
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - chitchat: utter_anything_else -> fail
* thank
    - utter_anything_else   <!-- predicted: utter_moreinformation -->
* bye
    - utter_bye   <!-- predicted: action_store_email -->
* greet
    - action_get_community_events   <!-- predicted: action_store_email -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_whoisit
    - action_chitchat   <!-- predicted: utter_not_sure -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_howold
    - action_chitchat   <!-- predicted: utter_not_sure -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_howold
    - action_faqs   <!-- predicted: utter_not_sure -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_howold
    - action_default_fallback   <!-- predicted: utter_not_sure -->


## Generated Story goal:1 step, id:9e28b5d02f08459b9cb19e2888976813, 12/15/18 523765784065373811
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_python_installed -->
* ask_howdoing
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: action_set_onboarding -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_greet_user -->
* signup_newsletter
    - utter_great   <!-- predicted: utter_tryout -->
    - utter_ask_email   <!-- predicted: utter_tryout -->
* enter_data{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - action_store_email   <!-- predicted: utter_tryout -->
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed   <!-- predicted: action_store_email -->
    - utter_docu   <!-- predicted: utter_tryout -->
    - utter_ask_feedback   <!-- predicted: utter_tryout -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* ask_restaurant
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_anything_else -->
* signup_newsletter
    - subscribe: utter_great
    - action_listen   <!-- predicted: utter_anything_else -->
* out_of_scope
    - utter_great   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - utter_ask_name   <!-- predicted: utter_great -->
    - utter_anything_else   <!-- predicted: action_listen -->
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* enter_data
    - utter_spacy_or_tensorflow   <!-- predicted: utter_great -->
    - chitchat: utter_anything_else -> fail
* canthelp
    - utter_canthelp   <!-- predicted: utter_great -->
* greet
    - action_greet_user   <!-- predicted: utter_great -->
* bye
    - utter_ask_company   <!-- predicted: utter_great -->
* enter_data{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - action_store_company   <!-- predicted: utter_anything_else -->
    - slot{"company_name": "google"}
    - utter_ask_businessmail   <!-- predicted: utter_anything_else -->
* enter_data{"email": "arvind@google.com"}
    - slot{"email": "arvind@google.com"}
    - slot{"email": "arvind@google.com"}
    - action_store_email   <!-- predicted: utter_great -->
    - slot{"email": "arvind@google.com"}
    - action_subscribe_newsletter   <!-- predicted: action_listen -->
    - slot{"subscribed": true}
    - utter_awesome   <!-- predicted: action_listen -->
    - utter_confirmationemail   <!-- predicted: action_listen -->
    - utter_docu   <!-- predicted: action_listen -->
    - utter_ask_feedback   <!-- predicted: action_listen -->
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - utter_thumbsup   <!-- predicted: utter_switch_dialogflow -->
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_thumbsup   <!-- predicted: utter_anything_else -->
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_thumbsup   <!-- predicted: utter_anything_else -->
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - chitchat: utter_anything_else -> fail
* thank
    - utter_anything_else   <!-- predicted: utter_moreinformation -->
* bye
    - utter_bye   <!-- predicted: action_store_email -->
* greet
    - action_get_community_events   <!-- predicted: action_store_email -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_whoisit
    - action_chitchat   <!-- predicted: utter_not_sure -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_howold
    - action_chitchat   <!-- predicted: utter_not_sure -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_howold
    - action_faqs   <!-- predicted: utter_not_sure -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_howold
    - action_default_fallback   <!-- predicted: utter_not_sure -->


## Generated Story goal:1 step, id:9e28b5d02f08459b9cb19e2888976813, 12/15/18 523765784065373811
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_python_installed -->
* ask_howdoing
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: action_set_onboarding -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_greet_user -->
* signup_newsletter
    - utter_great   <!-- predicted: utter_tryout -->
    - utter_ask_email   <!-- predicted: utter_tryout -->
* enter_data{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - action_store_email   <!-- predicted: utter_tryout -->
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed   <!-- predicted: action_store_email -->
    - utter_docu   <!-- predicted: utter_tryout -->
    - utter_ask_feedback   <!-- predicted: utter_tryout -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* ask_restaurant
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_anything_else -->
* signup_newsletter
    - subscribe: utter_great
    - action_listen   <!-- predicted: utter_anything_else -->
* out_of_scope
    - utter_great   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - utter_ask_name   <!-- predicted: utter_great -->
    - utter_anything_else   <!-- predicted: action_listen -->
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* enter_data
    - utter_spacy_or_tensorflow   <!-- predicted: utter_great -->
    - chitchat: utter_anything_else -> fail
* canthelp
    - utter_canthelp   <!-- predicted: utter_great -->
* greet
    - action_greet_user   <!-- predicted: utter_great -->
* bye
    - utter_ask_company   <!-- predicted: utter_great -->
* enter_data{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - action_store_company   <!-- predicted: utter_anything_else -->
    - slot{"company_name": "google"}
    - utter_ask_businessmail   <!-- predicted: utter_anything_else -->
* enter_data{"email": "arvind@google.com"}
    - slot{"email": "arvind@google.com"}
    - slot{"email": "arvind@google.com"}
    - action_store_email   <!-- predicted: utter_great -->
    - slot{"email": "arvind@google.com"}
    - action_subscribe_newsletter   <!-- predicted: action_listen -->
    - slot{"subscribed": true}
    - utter_awesome   <!-- predicted: action_listen -->
    - utter_confirmationemail   <!-- predicted: action_listen -->
    - utter_docu   <!-- predicted: action_listen -->
    - utter_ask_feedback   <!-- predicted: action_listen -->
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - utter_thumbsup   <!-- predicted: utter_switch_dialogflow -->
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_thumbsup   <!-- predicted: utter_anything_else -->
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_thumbsup   <!-- predicted: utter_anything_else -->
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - chitchat: utter_anything_else -> fail
* thank
    - utter_anything_else   <!-- predicted: utter_moreinformation -->
* bye
    - utter_bye   <!-- predicted: action_store_email -->
* greet
    - action_get_community_events   <!-- predicted: action_store_email -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_whoisit
    - action_chitchat   <!-- predicted: utter_not_sure -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_howold
    - action_chitchat   <!-- predicted: utter_not_sure -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_howold
    - action_faqs   <!-- predicted: utter_not_sure -->
    - action_listen   <!-- predicted: utter_anything_else -->
* enter_data
    - action_store_unknown_nlu_part   <!-- predicted: utter_not_sure -->
    - slot{"unknown_nlu_part": "nopes"}
    - action_store_unknown_nlu_part   <!-- predicted: utter_anything_else -->
    - slot{"unknown_nlu_part": "nopes"}
    - utter_dont_know_nlu_part   <!-- predicted: utter_moreinformation -->
    - utter_duckling   <!-- predicted: utter_moreinformation -->
    - utter_anything_else   <!-- predicted: utter_moreinformation -->
* enter_data
    - utter_switch_dialogflow   <!-- predicted: utter_not_sure -->
    - chitchat: utter_anything_else -> fail
* ask_weather
    - action_default_ask_affirmation   <!-- predicted: utter_not_sure -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_languagesbot
    - action_revert_fallback_events   <!-- predicted: utter_not_sure -->


## Generated Story goal:1 step, id:9e28b5d02f08459b9cb19e2888976813, 12/15/18 523765784065373811
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_python_installed -->
* ask_howdoing
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: action_set_onboarding -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_greet_user -->
* signup_newsletter
    - utter_great   <!-- predicted: utter_tryout -->
    - utter_ask_email   <!-- predicted: utter_tryout -->
* enter_data{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - action_store_email   <!-- predicted: utter_tryout -->
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed   <!-- predicted: action_store_email -->
    - utter_docu   <!-- predicted: utter_tryout -->
    - utter_ask_feedback   <!-- predicted: utter_tryout -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* ask_restaurant
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_anything_else -->
* signup_newsletter
    - subscribe: utter_great
    - action_listen   <!-- predicted: utter_anything_else -->
* out_of_scope
    - utter_great   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - utter_ask_name   <!-- predicted: utter_great -->
    - utter_anything_else   <!-- predicted: action_listen -->
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* enter_data
    - utter_spacy_or_tensorflow   <!-- predicted: utter_great -->
    - chitchat: utter_anything_else -> fail
* canthelp
    - utter_canthelp   <!-- predicted: utter_great -->
* greet
    - action_greet_user   <!-- predicted: utter_great -->
* bye
    - utter_ask_company   <!-- predicted: utter_great -->
* enter_data{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - action_store_company   <!-- predicted: utter_anything_else -->
    - slot{"company_name": "google"}
    - utter_ask_businessmail   <!-- predicted: utter_anything_else -->
* enter_data{"email": "arvind@google.com"}
    - slot{"email": "arvind@google.com"}
    - slot{"email": "arvind@google.com"}
    - action_store_email   <!-- predicted: utter_great -->
    - slot{"email": "arvind@google.com"}
    - action_subscribe_newsletter   <!-- predicted: action_listen -->
    - slot{"subscribed": true}
    - utter_awesome   <!-- predicted: action_listen -->
    - utter_confirmationemail   <!-- predicted: action_listen -->
    - utter_docu   <!-- predicted: action_listen -->
    - utter_ask_feedback   <!-- predicted: action_listen -->
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - utter_thumbsup   <!-- predicted: utter_switch_dialogflow -->
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_thumbsup   <!-- predicted: utter_anything_else -->
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_thumbsup   <!-- predicted: utter_anything_else -->
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - chitchat: utter_anything_else -> fail
* thank
    - utter_anything_else   <!-- predicted: utter_moreinformation -->
* bye
    - utter_bye   <!-- predicted: action_store_email -->
* greet
    - action_get_community_events   <!-- predicted: action_store_email -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_whoisit
    - action_chitchat   <!-- predicted: utter_not_sure -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_howold
    - action_chitchat   <!-- predicted: utter_not_sure -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_howold
    - action_faqs   <!-- predicted: utter_not_sure -->
    - action_listen   <!-- predicted: utter_anything_else -->
* enter_data
    - action_store_unknown_nlu_part   <!-- predicted: utter_not_sure -->
    - slot{"unknown_nlu_part": "nopes"}
    - action_store_unknown_nlu_part   <!-- predicted: utter_anything_else -->
    - slot{"unknown_nlu_part": "nopes"}
    - utter_dont_know_nlu_part   <!-- predicted: utter_moreinformation -->
    - utter_duckling   <!-- predicted: utter_moreinformation -->
    - utter_anything_else   <!-- predicted: utter_moreinformation -->
* enter_data
    - utter_switch_dialogflow   <!-- predicted: utter_not_sure -->
    - chitchat: utter_anything_else -> fail
* ask_weather
    - action_default_ask_affirmation   <!-- predicted: utter_not_sure -->


## Generated Story goal:1 step, id:c1413213af684cbd952299e5b640a174, 12/15/18 5367922669514830768
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* technical_question
    - action_default_fallback   <!-- predicted: action_faqs -->


## Generated Story goal:chitchat, id:ed1418fcc3884157bcc96a7c43d21ec0, 12/15/18 2178899423323461626
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - chitchat: action_chitchat
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* ask_faq_languages
    - faq: action_faqs
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* affirm
    - action_default_ask_affirmation   <!-- predicted: utter_possibilities -->
* enter_data
    - action_revert_fallback_events   <!-- predicted: utter_not_sure -->


## Generated Story goal:chitchat, id:ed1418fcc3884157bcc96a7c43d21ec0, 12/15/18 2178899423323461626
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - chitchat: action_chitchat
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* ask_faq_languages
    - faq: action_faqs
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* affirm
    - action_default_ask_affirmation   <!-- predicted: utter_possibilities -->


## Generated Story goal:1 step, id:321d95bf0cb14dc8b09f3f9a62827081, 12/15/18 6069986032596098095
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - action_default_fallback   <!-- predicted: utter_not_sure -->


## Generated Story goal:chitchat, id:39d029c35a994bf4bffc36e2a9a4c6de, 12/17/18 7695879941084586485
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* thank
    - utter_noworries   <!-- predicted: utter_canthelp -->
    - utter_anything_else   <!-- predicted: utter_possibilities -->
* affirm
    - utter_what_help   <!-- predicted: utter_thumbsup -->
* enter_data
    - action_default_ask_affirmation   <!-- predicted: utter_not_sure -->
* enter_data
    - action_revert_fallback_events   <!-- predicted: utter_not_sure -->


## Generated Story goal:chitchat, id:39d029c35a994bf4bffc36e2a9a4c6de, 12/17/18 7695879941084586485
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* thank
    - utter_noworries   <!-- predicted: utter_canthelp -->
    - utter_anything_else   <!-- predicted: utter_possibilities -->
* affirm
    - utter_what_help   <!-- predicted: utter_thumbsup -->
* enter_data
    - action_default_ask_affirmation   <!-- predicted: utter_not_sure -->


## Generated Story goal:chitchat, id:39d029c35a994bf4bffc36e2a9a4c6de, 12/17/18 7695879941084586485
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* thank
    - utter_noworries   <!-- predicted: utter_canthelp -->
    - utter_anything_else   <!-- predicted: utter_possibilities -->
* affirm
    - utter_what_help   <!-- predicted: utter_thumbsup -->
* enter_data
    - action_select_installation_command   <!-- predicted: utter_not_sure -->
    - utter_ask_ready_to_build   <!-- predicted: utter_possibilities -->
* deny
    - utter_ask_if_problem   <!-- predicted: utter_canthelp -->
* deny
    - utter_anything_else   <!-- predicted: utter_canthelp -->
* affirm
    - utter_ask_describe_problem   <!-- predicted: utter_thumbsup -->
* enter_data
    - action_default_ask_affirmation   <!-- predicted: utter_not_sure -->
* greet
    - action_revert_fallback_events   <!-- predicted: action_greet_user -->


## Generated Story goal:chitchat, id:39d029c35a994bf4bffc36e2a9a4c6de, 12/17/18 7695879941084586485
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* thank
    - utter_noworries   <!-- predicted: utter_canthelp -->
    - utter_anything_else   <!-- predicted: utter_possibilities -->
* affirm
    - utter_what_help   <!-- predicted: utter_thumbsup -->
* enter_data
    - action_select_installation_command   <!-- predicted: utter_not_sure -->
    - utter_ask_ready_to_build   <!-- predicted: utter_possibilities -->
* deny
    - utter_ask_if_problem   <!-- predicted: utter_canthelp -->
* deny
    - utter_anything_else   <!-- predicted: utter_canthelp -->
* affirm
    - utter_ask_describe_problem   <!-- predicted: utter_thumbsup -->
* enter_data
    - action_default_ask_affirmation   <!-- predicted: utter_not_sure -->


## Generated Story goal:chitchat, id:39d029c35a994bf4bffc36e2a9a4c6de, 12/17/18 7695879941084586485
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* thank
    - utter_noworries   <!-- predicted: utter_canthelp -->
    - utter_anything_else   <!-- predicted: utter_possibilities -->
* affirm
    - utter_what_help   <!-- predicted: utter_thumbsup -->
* enter_data
    - action_select_installation_command   <!-- predicted: utter_not_sure -->
    - utter_ask_ready_to_build   <!-- predicted: utter_possibilities -->
* deny
    - utter_ask_if_problem   <!-- predicted: utter_canthelp -->
* deny
    - utter_anything_else   <!-- predicted: utter_canthelp -->
* affirm
    - utter_ask_describe_problem   <!-- predicted: utter_thumbsup -->
* greet
    - action_default_fallback   <!-- predicted: action_greet_user -->


## Generated Story goal:chitchat, id:39d029c35a994bf4bffc36e2a9a4c6de, 12/17/18 7695879941084586485
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* thank
    - utter_noworries   <!-- predicted: utter_canthelp -->
    - utter_anything_else   <!-- predicted: utter_possibilities -->
* affirm
    - utter_what_help   <!-- predicted: utter_thumbsup -->
* enter_data
    - action_select_installation_command   <!-- predicted: utter_not_sure -->
    - utter_ask_ready_to_build   <!-- predicted: utter_possibilities -->
* deny
    - utter_ask_if_problem   <!-- predicted: utter_canthelp -->
* deny
    - utter_anything_else   <!-- predicted: utter_canthelp -->
* affirm
    - utter_ask_describe_problem   <!-- predicted: utter_thumbsup -->
* affirm
    - action_store_problem_description   <!-- predicted: utter_thumbsup -->
    - slot{"problem_description": "yes"}
    - action_faqs   <!-- predicted: action_listen -->
* greet
    - action_greet_user   <!-- predicted: action_listen -->
* ask_howdoing
    - action_chitchat   <!-- predicted: utter_canthelp -->
* ask_whatspossible
    - action_chitchat   <!-- predicted: action_listen -->
* affirm
    - action_default_ask_affirmation   <!-- predicted: utter_not_sure -->
* telljoke
    - action_revert_fallback_events   <!-- predicted: action_listen -->


## Generated Story goal:chitchat, id:39d029c35a994bf4bffc36e2a9a4c6de, 12/17/18 7695879941084586485
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* thank
    - utter_noworries   <!-- predicted: utter_canthelp -->
    - utter_anything_else   <!-- predicted: utter_possibilities -->
* affirm
    - utter_what_help   <!-- predicted: utter_thumbsup -->
* enter_data
    - action_select_installation_command   <!-- predicted: utter_not_sure -->
    - utter_ask_ready_to_build   <!-- predicted: utter_possibilities -->
* deny
    - utter_ask_if_problem   <!-- predicted: utter_canthelp -->
* deny
    - utter_anything_else   <!-- predicted: utter_canthelp -->
* affirm
    - utter_ask_describe_problem   <!-- predicted: utter_thumbsup -->
* affirm
    - action_store_problem_description   <!-- predicted: utter_thumbsup -->
    - slot{"problem_description": "yes"}
    - action_faqs   <!-- predicted: action_listen -->
* greet
    - action_greet_user   <!-- predicted: action_listen -->
* ask_howdoing
    - action_chitchat   <!-- predicted: utter_canthelp -->
* ask_whatspossible
    - action_chitchat   <!-- predicted: action_listen -->
* affirm
    - action_default_ask_affirmation   <!-- predicted: utter_not_sure -->


## Generated Story goal:1 step, id:c96f626b26e444c2ba743af283e3e5b5, 12/17/18 8581107588372252626
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_faq_slots
    - faq: action_faqs
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - utter_explain_stack   <!-- predicted: utter_tryout -->
    - utter_stack_details   <!-- predicted: utter_tryout -->
    - utter_explain_nlucore   <!-- predicted: utter_explain_stack -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_explain_nlu   <!-- predicted: utter_anything_else -->
    - utter_also_explain_core   <!-- predicted: utter_tryout -->
* affirm
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* affirm
    - utter_what_help   <!-- predicted: action_listen -->
* enter_data
    - action_select_installation_command   <!-- predicted: utter_not_sure -->
    - utter_ask_ready_to_build   <!-- predicted: utter_tryout -->
* nlu_generation_tool_recommendation
    - utter_already_subscribed   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* nlu_generation_tool_recommendation
    - action_default_fallback   <!-- predicted: utter_already_subscribed -->


## Generated Story goal:1 step, id:c96f626b26e444c2ba743af283e3e5b5, 12/17/18 8581107588372252626
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_faq_slots
    - faq: action_faqs
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - utter_explain_stack   <!-- predicted: utter_tryout -->
    - utter_stack_details   <!-- predicted: utter_tryout -->
    - utter_explain_nlucore   <!-- predicted: utter_explain_stack -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_explain_nlu   <!-- predicted: utter_anything_else -->
    - utter_also_explain_core   <!-- predicted: utter_tryout -->
* affirm
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* affirm
    - utter_what_help   <!-- predicted: action_listen -->
* enter_data
    - action_select_installation_command   <!-- predicted: utter_not_sure -->
    - utter_ask_ready_to_build   <!-- predicted: utter_tryout -->
* nlu_generation_tool_recommendation
    - utter_already_subscribed   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* nlu_generation_tool_recommendation
    - action_default_fallback   <!-- predicted: utter_already_subscribed -->


## Generated Story goal:1 step, id:c96f626b26e444c2ba743af283e3e5b5, 12/17/18 8581107588372252626
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_faq_slots
    - faq: action_faqs
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - utter_explain_stack   <!-- predicted: utter_tryout -->
    - utter_stack_details   <!-- predicted: utter_tryout -->
    - utter_explain_nlucore   <!-- predicted: utter_explain_stack -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_explain_nlu   <!-- predicted: utter_anything_else -->
    - utter_also_explain_core   <!-- predicted: utter_tryout -->
* affirm
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* affirm
    - utter_what_help   <!-- predicted: action_listen -->
* enter_data
    - action_select_installation_command   <!-- predicted: utter_not_sure -->
    - utter_ask_ready_to_build   <!-- predicted: utter_tryout -->
* nlu_generation_tool_recommendation
    - utter_already_subscribed   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* greet
    - action_store_problem_description   <!-- predicted: utter_explain_nlu -->
    - slot{"problem_description": "Hello"}
    - action_faqs   <!-- predicted: action_store_budget -->
* ask_whoisit
    - action_chitchat   <!-- predicted: utter_not_sure -->
* nlu_generation_tool_recommendation
    - action_default_fallback   <!-- predicted: utter_not_sure -->


## Generated Story goal:1 step, id:c96f626b26e444c2ba743af283e3e5b5, 12/17/18 8581107588372252626
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_faq_slots
    - faq: action_faqs
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - utter_explain_stack   <!-- predicted: utter_tryout -->
    - utter_stack_details   <!-- predicted: utter_tryout -->
    - utter_explain_nlucore   <!-- predicted: utter_explain_stack -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_explain_nlu   <!-- predicted: utter_anything_else -->
    - utter_also_explain_core   <!-- predicted: utter_tryout -->
* affirm
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* affirm
    - utter_what_help   <!-- predicted: action_listen -->
* enter_data
    - action_select_installation_command   <!-- predicted: utter_not_sure -->
    - utter_ask_ready_to_build   <!-- predicted: utter_tryout -->
* nlu_generation_tool_recommendation
    - utter_already_subscribed   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* greet
    - action_store_problem_description   <!-- predicted: utter_explain_nlu -->
    - slot{"problem_description": "Hello"}
    - action_faqs   <!-- predicted: action_store_budget -->
* ask_whoisit
    - action_chitchat   <!-- predicted: utter_not_sure -->
* nlu_generation_tool_recommendation{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - action_default_fallback   <!-- predicted: action_listen -->


## Generated Story goal:1 step, id:c96f626b26e444c2ba743af283e3e5b5, 12/17/18 8581107588372252626
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_faq_slots
    - faq: action_faqs
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - utter_explain_stack   <!-- predicted: utter_tryout -->
    - utter_stack_details   <!-- predicted: utter_tryout -->
    - utter_explain_nlucore   <!-- predicted: utter_explain_stack -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_explain_nlu   <!-- predicted: utter_anything_else -->
    - utter_also_explain_core   <!-- predicted: utter_tryout -->
* affirm
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* affirm
    - utter_what_help   <!-- predicted: action_listen -->
* enter_data
    - action_select_installation_command   <!-- predicted: utter_not_sure -->
    - utter_ask_ready_to_build   <!-- predicted: utter_tryout -->
* nlu_generation_tool_recommendation
    - utter_already_subscribed   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* greet
    - action_store_problem_description   <!-- predicted: utter_explain_nlu -->
    - slot{"problem_description": "Hello"}
    - action_faqs   <!-- predicted: action_store_budget -->
* ask_whoisit
    - action_chitchat   <!-- predicted: utter_not_sure -->
* nlu_generation_tool_recommendation
    - action_default_fallback   <!-- predicted: utter_not_sure -->


## Generated Story goal:1 step, id:dab1fc88af214c1abb57334f72b8cfb2, 12/17/18 1502159966905958231
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatspossible
    - chitchat: action_chitchat
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
* enter_data
    - action_default_ask_affirmation   <!-- predicted: action_store_unknown_product -->
    - action_listen   <!-- predicted: utter_built_bot_before -->
* switch{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - action_revert_fallback_events   <!-- predicted: utter_switch_dialogflow -->


## Generated Story goal:1 step, id:dab1fc88af214c1abb57334f72b8cfb2, 12/17/18 1502159966905958231
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatspossible
    - chitchat: action_chitchat
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
* enter_data
    - action_default_ask_affirmation   <!-- predicted: action_store_unknown_product -->


## Generated Story goal:1 step, id:318f6636b6c842f6a330b015599e8f7d, 05/01/19 -2612547548431379099
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* enter_data{"number": 1}
    - action_default_ask_affirmation   <!-- predicted: utter_explain_nlucore -->
    - action_listen   <!-- predicted: utter_built_bot_before -->
* enter_data
    - action_revert_fallback_events   <!-- predicted: action_store_unknown_product -->


## Generated Story goal:1 step, id:318f6636b6c842f6a330b015599e8f7d, 05/01/19 -2612547548431379099
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* enter_data{"number": 1}
    - action_default_ask_affirmation   <!-- predicted: utter_explain_nlucore -->


## Generated Story goal:1 step, id:dbb64f3d387441949443e4e6a7c83520, 05/01/19 982787949487219313
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatisrasa
    - chitchat: action_chitchat
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_getstarted -->
    - action_listen   <!-- predicted: utter_first_bot_with_rasa -->
* deny
    - action_default_ask_rephrase   <!-- predicted: utter_first_bot_with_rasa -->
    - action_listen   <!-- predicted: utter_anything_else -->
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_getstarted -->
* technical_question
    - action_revert_fallback_events   <!-- predicted: action_set_onboarding -->


## Generated Story goal:1 step, id:dbb64f3d387441949443e4e6a7c83520, 05/01/19 982787949487219313
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatisrasa
    - chitchat: action_chitchat
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_getstarted -->
    - action_listen   <!-- predicted: utter_first_bot_with_rasa -->
* deny
    - action_default_ask_rephrase   <!-- predicted: utter_first_bot_with_rasa -->
    - action_listen   <!-- predicted: utter_anything_else -->
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_getstarted -->


## Generated Story goal:1 step, id:dbb64f3d387441949443e4e6a7c83520, 05/01/19 982787949487219313
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatisrasa
    - chitchat: action_chitchat
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_getstarted -->
    - action_listen   <!-- predicted: utter_first_bot_with_rasa -->
* deny
    - action_default_ask_rephrase   <!-- predicted: utter_first_bot_with_rasa -->
    - action_listen   <!-- predicted: utter_anything_else -->
* technical_question
    - action_revert_fallback_events   <!-- predicted: utter_first_bot_with_rasa -->


## Generated Story goal:1 step, id:dbb64f3d387441949443e4e6a7c83520, 05/01/19 982787949487219313
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatisrasa
    - chitchat: action_chitchat
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_getstarted -->
    - action_listen   <!-- predicted: utter_first_bot_with_rasa -->
* deny
    - action_default_ask_rephrase   <!-- predicted: utter_first_bot_with_rasa -->


## Generated Story goal:1 step, id:dbb64f3d387441949443e4e6a7c83520, 05/01/19 982787949487219313
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatisrasa
    - chitchat: action_chitchat
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_getstarted -->


## Generated Story goal:chitchat, id:1277dc2ceae04fe0b963c7786a41f750, 05/01/19 806262383242887293
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatisrasa
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->
* ask_time
    - action_revert_fallback_events   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:1277dc2ceae04fe0b963c7786a41f750, 05/01/19 806262383242887293
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatisrasa
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->


## Generated Story goal:1 step , id:7146d879adc44cf5947ffe723015f02a, 12/15/18 7977723706233268217
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_howdoing
    - chitchat: action_chitchat
* install_rasa
    - getstarted_3: utter_ask_python_installed
* affirm
    - utter_ask_pip_or_conda   <!-- predicted: utter_ask_python_installed -->
* enter_data{"package_manager": "conda"}
    - slot{"package_manager": "conda"}
    - slot{"package_manager": "conda"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* enter_data
    - getstarted_3: action_store_problem_description
    - slot{"problem_description": "done"}
    - utter_direct_to_forum_for_help   <!-- predicted: utter_direct_to_step4 -->
    - action_listen   <!-- predicted: utter_direct_to_step4 -->
* affirm
    - utter_anything_else   <!-- predicted: utter_direct_to_forum_for_help -->
* how_to_get_started
    - onboarding: utter_getstarted
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* affirm
    - action_set_onboarding   <!-- predicted: utter_getstarted -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: action_listen -->
* deny
    - utter_explain_stack   <!-- predicted: utter_direct_to_step4 -->
    - utter_stack_details   <!-- predicted: action_listen -->
    - utter_explain_nlucore   <!-- predicted: action_listen -->
* affirm
    - utter_explain_nlu   <!-- predicted: action_listen -->
    - utter_explain_core   <!-- predicted: action_listen -->
    - utter_tryout   <!-- predicted: action_listen -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart_nlu_only   <!-- predicted: action_listen -->
    - utter_anything_else   <!-- predicted: utter_tryout -->
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - slot{"product": "core"}
    - utter_core_tutorial   <!-- predicted: action_listen -->
    - utter_anything_else   <!-- predicted: action_listen -->
* signup_newsletter
    - utter_great   <!-- predicted: action_listen -->
    - utter_ask_email   <!-- predicted: utter_getstarted -->
* greet
    - action_default_fallback   <!-- predicted: utter_getstarted -->


## Generated Story goal:1 step, id:ad02fffc3bd841788f5b10e283fe2ab8, 12/17/18 7345417199532554495
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_getstarted   <!-- predicted: utter_not_sure -->
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* affirm
    - action_faqs   <!-- predicted: action_set_onboarding -->
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* affirm
    - action_set_onboarding   <!-- predicted: utter_ask_entities -->
    - utter_ask_which_product   <!-- predicted: action_set_onboarding -->
    - action_listen   <!-- predicted: utter_built_bot_before -->
* affirm
    - utter_ask_migration   <!-- predicted: action_set_onboarding -->
* deny
    - rasa_help: utter_explain_stack -> fail
    - rasa_help: utter_stack_details -> fail
    - rasa_help: utter_explain_nlucore -> fail
* affirm
    - rasa_help: utter_explain_nlu -> fail
    - utter_also_explain_core   <!-- predicted: utter_explain_core -->
* affirm
    - utter_tryout   <!-- predicted: action_set_onboarding -->
* enter_data
    - action_store_email   <!-- predicted: utter_not_sure -->


## Generated Story goal:sales, id:e1ae1d77ce414451966eae0e29478965, 12/15/18 5656589108300468794
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whatspossible
    - chitchat: action_chitchat
* enter_data
    - action_default_fallback   <!-- predicted: utter_not_sure -->


## Generated Story goal:sales, id:e1ae1d77ce414451966eae0e29478965, 12/15/18 5656589108300468794
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whatspossible
    - chitchat: action_chitchat
* contact_sales
    - sales: utter_moreinformation
    - sales: utter_ask_jobfunction
* enter_data
    - sales: action_store_job
    - slot{"job_function": "it"}
    - sales: utter_ask_usecase
* ask_whatspossible
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:7280484f234c47c98952837077cff3fc, 12/15/18 1673539480913407606
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatspossible
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:7280484f234c47c98952837077cff3fc, 12/15/18 1673539480913407606
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat
* affirm
    - action_default_fallback   <!-- predicted: utter_thumbsup -->


## Generated Story goal:chitchat, id:7280484f234c47c98952837077cff3fc, 12/15/18 1673539480913407606
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat
* affirm
    - action_default_fallback   <!-- predicted: utter_thumbsup -->


## Generated Story goal:3 step, id:424bba9c6020412c920724ae7c0444ad, 05/01/19 -2955948574844971987
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* install_rasa
    - action_faqs   <!-- predicted: utter_explain_nlu -->
    - utter_explain_nlucore   <!-- predicted: utter_explain_core -->
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_ask_migration -->
    - action_listen   <!-- predicted: utter_tryout -->
* deny
    - action_default_ask_rephrase   <!-- predicted: utter_explain_stack -->
    - action_listen   <!-- predicted: utter_stack_details -->
* out_of_scope
    - action_default_ask_affirmation   <!-- predicted: utter_explain_nlucore -->
    - action_listen   <!-- predicted: utter_explain_nlu -->
* greet
    - action_revert_fallback_events   <!-- predicted: utter_get_python -->


## Generated Story goal:3 step, id:424bba9c6020412c920724ae7c0444ad, 05/01/19 -2955948574844971987
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* install_rasa
    - action_faqs   <!-- predicted: utter_explain_nlu -->
    - utter_explain_nlucore   <!-- predicted: utter_explain_core -->
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_ask_migration -->
    - action_listen   <!-- predicted: utter_tryout -->
* deny
    - action_default_ask_rephrase   <!-- predicted: utter_explain_stack -->
    - action_listen   <!-- predicted: utter_stack_details -->
* out_of_scope
    - action_default_ask_affirmation   <!-- predicted: utter_explain_nlucore -->


## Generated Story goal:3 step, id:424bba9c6020412c920724ae7c0444ad, 05/01/19 -2955948574844971987
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* install_rasa
    - action_faqs   <!-- predicted: utter_explain_nlu -->
    - utter_explain_nlucore   <!-- predicted: utter_explain_core -->
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_ask_migration -->
    - action_listen   <!-- predicted: utter_tryout -->
* deny
    - action_default_ask_rephrase   <!-- predicted: utter_explain_stack -->
    - action_listen   <!-- predicted: utter_stack_details -->
* greet
    - action_revert_fallback_events   <!-- predicted: utter_explain_nlucore -->


## Generated Story goal:3 step, id:424bba9c6020412c920724ae7c0444ad, 05/01/19 -2955948574844971987
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* install_rasa
    - action_faqs   <!-- predicted: utter_explain_nlu -->
    - utter_explain_nlucore   <!-- predicted: utter_explain_core -->
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_ask_migration -->
    - action_listen   <!-- predicted: utter_tryout -->
* deny
    - action_default_ask_rephrase   <!-- predicted: utter_explain_stack -->


## Generated Story goal:3 step, id:424bba9c6020412c920724ae7c0444ad, 05/01/19 -2955948574844971987
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* install_rasa
    - action_faqs   <!-- predicted: utter_explain_nlu -->
    - utter_explain_nlucore   <!-- predicted: utter_explain_core -->
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_ask_migration -->


## Generated Story goal:3 step, id:424bba9c6020412c920724ae7c0444ad, 05/01/19 -2955948574844971987
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* install_rasa
    - action_faqs   <!-- predicted: utter_explain_nlu -->
    - utter_explain_nlucore   <!-- predicted: utter_explain_core -->
* greet
    - action_greet_user   <!-- predicted: utter_getstarted -->
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding   <!-- predicted: utter_tryout -->
    - utter_ask_which_product   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* technical_question
    - action_greet_user   <!-- predicted: action_store_sales_info -->
* greet
    - action_greet_user   <!-- predicted: utter_getstarted -->
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_ask_migration -->
    - action_listen   <!-- predicted: utter_built_bot_before -->
* enter_data
    - action_default_fallback   <!-- predicted: action_store_unknown_product -->
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "hi"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_listen   <!-- predicted: utter_tryout -->
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_ask_migration -->
    - action_listen   <!-- predicted: utter_built_bot_before -->
* how_to_get_started{"user_type": "new"}
    - action_revert_fallback_events   <!-- predicted: utter_react_positive -->


## Generated Story goal:3 step, id:424bba9c6020412c920724ae7c0444ad, 05/01/19 -2955948574844971987
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* install_rasa
    - action_faqs   <!-- predicted: utter_explain_nlu -->
    - utter_explain_nlucore   <!-- predicted: utter_explain_core -->
* greet
    - action_greet_user   <!-- predicted: utter_getstarted -->
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding   <!-- predicted: utter_tryout -->
    - utter_ask_which_product   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* technical_question
    - action_greet_user   <!-- predicted: action_store_sales_info -->
* greet
    - action_greet_user   <!-- predicted: utter_getstarted -->
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_ask_migration -->
    - action_listen   <!-- predicted: utter_built_bot_before -->
* enter_data
    - action_default_fallback   <!-- predicted: action_store_unknown_product -->
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "hi"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_listen   <!-- predicted: utter_tryout -->
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_ask_migration -->


## Generated Story goal:3 step, id:424bba9c6020412c920724ae7c0444ad, 05/01/19 -2955948574844971987
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* install_rasa
    - action_faqs   <!-- predicted: utter_explain_nlu -->
    - utter_explain_nlucore   <!-- predicted: utter_explain_core -->
* greet
    - action_greet_user   <!-- predicted: utter_getstarted -->
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding   <!-- predicted: utter_tryout -->
    - utter_ask_which_product   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* technical_question
    - action_greet_user   <!-- predicted: action_store_sales_info -->
* greet
    - action_greet_user   <!-- predicted: utter_getstarted -->
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_ask_migration -->
    - action_listen   <!-- predicted: utter_built_bot_before -->
* enter_data
    - action_default_fallback   <!-- predicted: action_store_unknown_product -->
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "hi"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_listen   <!-- predicted: utter_tryout -->
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding   <!-- predicted: utter_ask_migration -->
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - utter_built_bot_before   <!-- predicted: action_set_onboarding -->
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - utter_explain_nlucore   <!-- predicted: action_store_email -->
* affirm
    - getstarted_1: utter_explain_nlu
    - utter_explain_core   <!-- predicted: utter_tryout -->
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_migration -->
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_ask_migration -->
    - action_listen   <!-- predicted: utter_built_bot_before -->
* install_rasa
    - action_revert_fallback_events   <!-- predicted: utter_tryout -->


## Generated Story goal:3 step, id:424bba9c6020412c920724ae7c0444ad, 05/01/19 -2955948574844971987
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* install_rasa
    - action_faqs   <!-- predicted: utter_explain_nlu -->
    - utter_explain_nlucore   <!-- predicted: utter_explain_core -->
* greet
    - action_greet_user   <!-- predicted: utter_getstarted -->
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding   <!-- predicted: utter_tryout -->
    - utter_ask_which_product   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* technical_question
    - action_greet_user   <!-- predicted: action_store_sales_info -->
* greet
    - action_greet_user   <!-- predicted: utter_getstarted -->
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_ask_migration -->
    - action_listen   <!-- predicted: utter_built_bot_before -->
* enter_data
    - action_default_fallback   <!-- predicted: action_store_unknown_product -->
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "hi"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_listen   <!-- predicted: utter_tryout -->
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding   <!-- predicted: utter_ask_migration -->
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - utter_built_bot_before   <!-- predicted: action_set_onboarding -->
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - utter_explain_nlucore   <!-- predicted: action_store_email -->
* affirm
    - getstarted_1: utter_explain_nlu
    - utter_explain_core   <!-- predicted: utter_tryout -->
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_migration -->
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_ask_migration -->


## Generated Story goal:3 step, id:424bba9c6020412c920724ae7c0444ad, 05/01/19 -2955948574844971987
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* install_rasa
    - action_faqs   <!-- predicted: utter_explain_nlu -->
    - utter_explain_nlucore   <!-- predicted: utter_explain_core -->
* greet
    - action_greet_user   <!-- predicted: utter_getstarted -->
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding   <!-- predicted: utter_tryout -->
    - utter_ask_which_product   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* technical_question
    - action_greet_user   <!-- predicted: action_store_sales_info -->
* greet
    - action_greet_user   <!-- predicted: utter_getstarted -->
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_ask_migration -->
    - action_listen   <!-- predicted: utter_built_bot_before -->
* enter_data
    - action_default_fallback   <!-- predicted: action_store_unknown_product -->
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "hi"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_listen   <!-- predicted: utter_tryout -->
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding   <!-- predicted: utter_ask_migration -->
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - utter_built_bot_before   <!-- predicted: action_set_onboarding -->
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - utter_explain_nlucore   <!-- predicted: action_store_email -->
* affirm
    - getstarted_1: utter_explain_nlu
    - utter_explain_core   <!-- predicted: utter_tryout -->
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_migration -->
* install_rasa
    - utter_ask_python_installed   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* deny
    - utter_get_python   <!-- predicted: utter_tryout -->
    - utter_ask_pip_or_conda   <!-- predicted: utter_anything_else -->
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - action_select_installation_command   <!-- predicted: action_listen -->
    - utter_ask_ready_to_build   <!-- predicted: utter_explain_stack -->
* technical_question
    - action_store_problem_description   <!-- predicted: utter_direct_install -->
    - slot{"problem_description": "error syntax"}
    - utter_direct_to_forum_for_help   <!-- predicted: utter_great -->
    - action_listen   <!-- predicted: utter_anything_else -->
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - action_store_entity_extractor   <!-- predicted: utter_not_sure -->
    - slot{"entity_extractor": "ner_crf"}
    - utter_duckling   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* install_rasa
    - action_store_budget   <!-- predicted: utter_moreinformation -->
    - slot{"budget": "i need to install in my computer"}
    - utter_sales_contact   <!-- predicted: utter_anything_else -->
    - action_listen   <!-- predicted: utter_moreinformation -->
* install_rasa
    - action_faqs   <!-- predicted: action_listen -->
* install_rasa
    - action_default_fallback   <!-- predicted: action_listen -->


## Generated Story goal:3 step, id:424bba9c6020412c920724ae7c0444ad, 05/01/19 -2955948574844971987
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* install_rasa
    - action_faqs   <!-- predicted: utter_explain_nlu -->
    - utter_explain_nlucore   <!-- predicted: utter_explain_core -->
* greet
    - action_greet_user   <!-- predicted: utter_getstarted -->
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding   <!-- predicted: utter_tryout -->
    - utter_ask_which_product   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* technical_question
    - action_greet_user   <!-- predicted: action_store_sales_info -->
* greet
    - action_greet_user   <!-- predicted: utter_getstarted -->
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_ask_migration -->
    - action_listen   <!-- predicted: utter_built_bot_before -->
* enter_data
    - action_default_fallback   <!-- predicted: action_store_unknown_product -->
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "hi"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_listen   <!-- predicted: utter_tryout -->
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding   <!-- predicted: utter_ask_migration -->
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - utter_built_bot_before   <!-- predicted: action_set_onboarding -->
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - utter_explain_nlucore   <!-- predicted: action_store_email -->
* affirm
    - getstarted_1: utter_explain_nlu
    - utter_explain_core   <!-- predicted: utter_tryout -->
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_migration -->
* install_rasa
    - utter_ask_python_installed   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* deny
    - utter_get_python   <!-- predicted: utter_tryout -->
    - utter_ask_pip_or_conda   <!-- predicted: utter_anything_else -->
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - action_select_installation_command   <!-- predicted: action_listen -->
    - utter_ask_ready_to_build   <!-- predicted: utter_explain_stack -->
* technical_question
    - action_store_problem_description   <!-- predicted: utter_direct_install -->
    - slot{"problem_description": "error syntax"}
    - utter_direct_to_forum_for_help   <!-- predicted: utter_great -->
    - action_listen   <!-- predicted: utter_anything_else -->
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - action_store_entity_extractor   <!-- predicted: utter_not_sure -->
    - slot{"entity_extractor": "ner_crf"}
    - utter_duckling   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* install_rasa
    - action_store_budget   <!-- predicted: utter_moreinformation -->
    - slot{"budget": "i need to install in my computer"}
    - utter_sales_contact   <!-- predicted: utter_anything_else -->
    - action_listen   <!-- predicted: utter_moreinformation -->
* install_rasa
    - action_faqs   <!-- predicted: action_listen -->
* greet
    - action_store_budget   <!-- predicted: utter_confirmationemail -->
    - slot{"budget": "hello"}
    - utter_quickstart_nlu_only   <!-- predicted: utter_confirmationemail -->
    - utter_quickstart   <!-- predicted: utter_anything_else -->
    - utter_direct_install   <!-- predicted: action_listen -->
    - utter_anything_else   <!-- predicted: utter_confirmationemail -->
* greet
    - action_greet_user   <!-- predicted: utter_moreinformation -->
* install_rasa
    - action_default_ask_affirmation   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: action_greet_user -->
* install_rasa
    - action_revert_fallback_events   <!-- predicted: action_listen -->


## Generated Story goal:3 step, id:424bba9c6020412c920724ae7c0444ad, 05/01/19 -2955948574844971987
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* install_rasa
    - action_faqs   <!-- predicted: utter_explain_nlu -->
    - utter_explain_nlucore   <!-- predicted: utter_explain_core -->
* greet
    - action_greet_user   <!-- predicted: utter_getstarted -->
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding   <!-- predicted: utter_tryout -->
    - utter_ask_which_product   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* technical_question
    - action_greet_user   <!-- predicted: action_store_sales_info -->
* greet
    - action_greet_user   <!-- predicted: utter_getstarted -->
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_ask_migration -->
    - action_listen   <!-- predicted: utter_built_bot_before -->
* enter_data
    - action_default_fallback   <!-- predicted: action_store_unknown_product -->
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "hi"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_listen   <!-- predicted: utter_tryout -->
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding   <!-- predicted: utter_ask_migration -->
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - utter_built_bot_before   <!-- predicted: action_set_onboarding -->
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - utter_explain_nlucore   <!-- predicted: action_store_email -->
* affirm
    - getstarted_1: utter_explain_nlu
    - utter_explain_core   <!-- predicted: utter_tryout -->
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_migration -->
* install_rasa
    - utter_ask_python_installed   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* deny
    - utter_get_python   <!-- predicted: utter_tryout -->
    - utter_ask_pip_or_conda   <!-- predicted: utter_anything_else -->
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - action_select_installation_command   <!-- predicted: action_listen -->
    - utter_ask_ready_to_build   <!-- predicted: utter_explain_stack -->
* technical_question
    - action_store_problem_description   <!-- predicted: utter_direct_install -->
    - slot{"problem_description": "error syntax"}
    - utter_direct_to_forum_for_help   <!-- predicted: utter_great -->
    - action_listen   <!-- predicted: utter_anything_else -->
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - action_store_entity_extractor   <!-- predicted: utter_not_sure -->
    - slot{"entity_extractor": "ner_crf"}
    - utter_duckling   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* install_rasa
    - action_store_budget   <!-- predicted: utter_moreinformation -->
    - slot{"budget": "i need to install in my computer"}
    - utter_sales_contact   <!-- predicted: utter_anything_else -->
    - action_listen   <!-- predicted: utter_moreinformation -->
* install_rasa
    - action_faqs   <!-- predicted: action_listen -->
* greet
    - action_store_budget   <!-- predicted: utter_confirmationemail -->
    - slot{"budget": "hello"}
    - utter_quickstart_nlu_only   <!-- predicted: utter_confirmationemail -->
    - utter_quickstart   <!-- predicted: utter_anything_else -->
    - utter_direct_install   <!-- predicted: action_listen -->
    - utter_anything_else   <!-- predicted: utter_confirmationemail -->
* greet
    - action_greet_user   <!-- predicted: utter_moreinformation -->
* install_rasa
    - action_default_ask_affirmation   <!-- predicted: action_listen -->


## Generated Story goal:3 step, id:424bba9c6020412c920724ae7c0444ad, 05/01/19 -2955948574844971987
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* install_rasa
    - action_faqs   <!-- predicted: utter_explain_nlu -->
    - utter_explain_nlucore   <!-- predicted: utter_explain_core -->
* greet
    - action_greet_user   <!-- predicted: utter_getstarted -->
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding   <!-- predicted: utter_tryout -->
    - utter_ask_which_product   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* technical_question
    - action_greet_user   <!-- predicted: action_store_sales_info -->
* greet
    - action_greet_user   <!-- predicted: utter_getstarted -->
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_ask_migration -->
    - action_listen   <!-- predicted: utter_built_bot_before -->
* enter_data
    - action_default_fallback   <!-- predicted: action_store_unknown_product -->
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "hi"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_listen   <!-- predicted: utter_tryout -->
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding   <!-- predicted: utter_ask_migration -->
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - utter_built_bot_before   <!-- predicted: action_set_onboarding -->
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - utter_explain_nlucore   <!-- predicted: action_store_email -->
* affirm
    - getstarted_1: utter_explain_nlu
    - utter_explain_core   <!-- predicted: utter_tryout -->
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_migration -->
* install_rasa
    - utter_ask_python_installed   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* deny
    - utter_get_python   <!-- predicted: utter_tryout -->
    - utter_ask_pip_or_conda   <!-- predicted: utter_anything_else -->
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - action_select_installation_command   <!-- predicted: action_listen -->
    - utter_ask_ready_to_build   <!-- predicted: utter_explain_stack -->
* technical_question
    - action_store_problem_description   <!-- predicted: utter_direct_install -->
    - slot{"problem_description": "error syntax"}
    - utter_direct_to_forum_for_help   <!-- predicted: utter_great -->
    - action_listen   <!-- predicted: utter_anything_else -->
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - action_store_entity_extractor   <!-- predicted: utter_not_sure -->
    - slot{"entity_extractor": "ner_crf"}
    - utter_duckling   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* install_rasa
    - action_store_budget   <!-- predicted: utter_moreinformation -->
    - slot{"budget": "i need to install in my computer"}
    - utter_sales_contact   <!-- predicted: utter_anything_else -->
    - action_listen   <!-- predicted: utter_moreinformation -->
* install_rasa
    - action_faqs   <!-- predicted: action_listen -->
* greet
    - action_store_budget   <!-- predicted: utter_confirmationemail -->
    - slot{"budget": "hello"}
    - utter_quickstart_nlu_only   <!-- predicted: utter_confirmationemail -->
    - utter_quickstart   <!-- predicted: utter_anything_else -->
    - utter_direct_install   <!-- predicted: action_listen -->
    - utter_anything_else   <!-- predicted: utter_confirmationemail -->
* greet
    - action_greet_user   <!-- predicted: utter_moreinformation -->
* install_rasa
    - utter_quickstart_nlu_only   <!-- predicted: action_listen -->
    - utter_anything_else   <!-- predicted: action_greet_user -->
* greet
    - action_greet_user   <!-- predicted: action_store_sales_info -->
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: action_greet_user -->
    - action_listen   <!-- predicted: utter_confirmationemail -->
* how_to_get_started
    - action_revert_fallback_events   <!-- predicted: action_listen -->


## Generated Story goal:3 step, id:424bba9c6020412c920724ae7c0444ad, 05/01/19 -2955948574844971987
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* install_rasa
    - action_faqs   <!-- predicted: utter_explain_nlu -->
    - utter_explain_nlucore   <!-- predicted: utter_explain_core -->
* greet
    - action_greet_user   <!-- predicted: utter_getstarted -->
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding   <!-- predicted: utter_tryout -->
    - utter_ask_which_product   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* technical_question
    - action_greet_user   <!-- predicted: action_store_sales_info -->
* greet
    - action_greet_user   <!-- predicted: utter_getstarted -->
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_ask_migration -->
    - action_listen   <!-- predicted: utter_built_bot_before -->
* enter_data
    - action_default_fallback   <!-- predicted: action_store_unknown_product -->
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "hi"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_listen   <!-- predicted: utter_tryout -->
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding   <!-- predicted: utter_ask_migration -->
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - utter_built_bot_before   <!-- predicted: action_set_onboarding -->
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - utter_explain_nlucore   <!-- predicted: action_store_email -->
* affirm
    - getstarted_1: utter_explain_nlu
    - utter_explain_core   <!-- predicted: utter_tryout -->
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_migration -->
* install_rasa
    - utter_ask_python_installed   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* deny
    - utter_get_python   <!-- predicted: utter_tryout -->
    - utter_ask_pip_or_conda   <!-- predicted: utter_anything_else -->
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - action_select_installation_command   <!-- predicted: action_listen -->
    - utter_ask_ready_to_build   <!-- predicted: utter_explain_stack -->
* technical_question
    - action_store_problem_description   <!-- predicted: utter_direct_install -->
    - slot{"problem_description": "error syntax"}
    - utter_direct_to_forum_for_help   <!-- predicted: utter_great -->
    - action_listen   <!-- predicted: utter_anything_else -->
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - action_store_entity_extractor   <!-- predicted: utter_not_sure -->
    - slot{"entity_extractor": "ner_crf"}
    - utter_duckling   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* install_rasa
    - action_store_budget   <!-- predicted: utter_moreinformation -->
    - slot{"budget": "i need to install in my computer"}
    - utter_sales_contact   <!-- predicted: utter_anything_else -->
    - action_listen   <!-- predicted: utter_moreinformation -->
* install_rasa
    - action_faqs   <!-- predicted: action_listen -->
* greet
    - action_store_budget   <!-- predicted: utter_confirmationemail -->
    - slot{"budget": "hello"}
    - utter_quickstart_nlu_only   <!-- predicted: utter_confirmationemail -->
    - utter_quickstart   <!-- predicted: utter_anything_else -->
    - utter_direct_install   <!-- predicted: action_listen -->
    - utter_anything_else   <!-- predicted: utter_confirmationemail -->
* greet
    - action_greet_user   <!-- predicted: utter_moreinformation -->
* install_rasa
    - utter_quickstart_nlu_only   <!-- predicted: action_listen -->
    - utter_anything_else   <!-- predicted: action_greet_user -->
* greet
    - action_greet_user   <!-- predicted: action_store_sales_info -->
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: action_greet_user -->


## Generated Story goal:oos, id:ee962c4c1af542f8952d6082ceb9c208, 05/01/19 1544238638038077071
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatisrasa
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->
* ask_whoisit
    - action_revert_fallback_events   <!-- predicted: action_chitchat -->


## Generated Story goal:oos, id:ee962c4c1af542f8952d6082ceb9c208, 05/01/19 1544238638038077071
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatisrasa
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->


## Generated Story goal:oos, id:ee962c4c1af542f8952d6082ceb9c208, 05/01/19 1544238638038077071
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whoisit
    - chitchat: action_chitchat
* ask_why_contribute
    - action_default_ask_affirmation   <!-- predicted: utter_possibilities_to_contribute -->
* enter_data
    - action_revert_fallback_events   <!-- predicted: utter_not_sure -->


## Generated Story goal:oos, id:ee962c4c1af542f8952d6082ceb9c208, 05/01/19 1544238638038077071
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whoisit
    - chitchat: action_chitchat
* ask_why_contribute
    - action_default_ask_affirmation   <!-- predicted: utter_possibilities_to_contribute -->


## Generated Story goal:oos, id:ee962c4c1af542f8952d6082ceb9c208, 05/01/19 1544238638038077071
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whoisit
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* ask_whatisrasa
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->
* canthelp
    - action_revert_fallback_events   <!-- predicted: utter_canthelp -->


## Generated Story goal:oos, id:ee962c4c1af542f8952d6082ceb9c208, 05/01/19 1544238638038077071
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whoisit
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* ask_whatisrasa
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->


## Generated Story goal:faq, id:b7c01a1b3b034a59b74a25e4ffd94b12, 12/15/18 1531624798006099569
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_builder
    - action_default_fallback   <!-- predicted: action_chitchat -->


## Generated Story goal:chitchat, id:912897e570334aa0bf5360977052e95b, 12/17/18 -1934419123625089053
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_whoisit
    - chitchat: action_chitchat
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* deny
    - chitchat: utter_nohelp
* human_handoff
    - action_default_ask_affirmation   <!-- predicted: utter_contact_email -->
* human_handoff
    - action_revert_fallback_events   <!-- predicted: utter_contact_email -->


## Generated Story goal:chitchat, id:912897e570334aa0bf5360977052e95b, 12/17/18 -1934419123625089053
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_whoisit
    - chitchat: action_chitchat
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* deny
    - chitchat: utter_nohelp
* human_handoff
    - action_default_ask_affirmation   <!-- predicted: utter_contact_email -->


## Generated Story goal:1 step, id:e8fc2e0b2c374353a63da30fb64748f3, 05/01/19 -1435447685661180167
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* nicetomeeyou
    - chitchat: action_chitchat
* enter_data
    - action_default_ask_affirmation   <!-- predicted: utter_not_sure -->
* deny
    - action_default_ask_rephrase   <!-- predicted: utter_nohelp -->
* how_to_get_started
    - action_revert_fallback_events   <!-- predicted: utter_getstarted -->


## Generated Story goal:1 step, id:e8fc2e0b2c374353a63da30fb64748f3, 05/01/19 -1435447685661180167
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* nicetomeeyou
    - chitchat: action_chitchat
* enter_data
    - action_default_ask_affirmation   <!-- predicted: utter_not_sure -->
* deny
    - action_default_ask_rephrase   <!-- predicted: utter_nohelp -->


## Generated Story goal:1 step, id:e8fc2e0b2c374353a63da30fb64748f3, 05/01/19 -1435447685661180167
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* nicetomeeyou
    - chitchat: action_chitchat
* enter_data
    - action_default_ask_affirmation   <!-- predicted: utter_not_sure -->


## Generated Story goal:1 step, id:e8fc2e0b2c374353a63da30fb64748f3, 05/01/19 -1435447685661180167
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* nicetomeeyou
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* ask_faq_differencecorenlu
    - faq: action_faqs
    - getstarted_1: utter_explain_nlucore
* ask_faq_differencecorenlu{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - action_default_ask_affirmation   <!-- predicted: action_faqs -->
    - action_listen   <!-- predicted: utter_explain_nlucore -->
* deny
    - action_default_ask_rephrase   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_get_started_step3 -->
* enter_data
    - action_revert_fallback_events   <!-- predicted: utter_tryout -->


## Generated Story goal:1 step, id:e8fc2e0b2c374353a63da30fb64748f3, 05/01/19 -1435447685661180167
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* nicetomeeyou
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* ask_faq_differencecorenlu
    - faq: action_faqs
    - getstarted_1: utter_explain_nlucore
* ask_faq_differencecorenlu{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - action_default_ask_affirmation   <!-- predicted: action_faqs -->
    - action_listen   <!-- predicted: utter_explain_nlucore -->
* deny
    - action_default_ask_rephrase   <!-- predicted: utter_tryout -->


## Generated Story goal:1 step, id:e8fc2e0b2c374353a63da30fb64748f3, 05/01/19 -1435447685661180167
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* nicetomeeyou
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* ask_faq_differencecorenlu
    - faq: action_faqs
    - getstarted_1: utter_explain_nlucore
* ask_faq_differencecorenlu{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - action_default_ask_affirmation   <!-- predicted: action_faqs -->


## Generated Story goal:1 step, id:cd10afdfaab74996a3e1ed1b712366d3, 05/01/19 -245718514312788239


## Generated Story goal:chitchat, id:67a8696eb5894b25a800b6cbd7a695bb, 12/15/18 -1322664348979395741
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_howdoing
    - chitchat: action_chitchat
* ask_whoisit
    - chitchat: action_chitchat
* enter_data
    - action_select_installation_command   <!-- predicted: utter_not_sure -->
    - utter_ask_ready_to_build   <!-- predicted: utter_possibilities -->
* ask_faq_languages
    - action_store_problem_description   <!-- predicted: action_faqs -->
    - slot{"problem_description": "what languages do you support?"}
    - action_faqs   <!-- predicted: action_listen -->
* enter_data
    - action_select_installation_command   <!-- predicted: utter_possibilities -->
    - utter_ask_ready_to_build   <!-- predicted: utter_possibilities -->
* enter_data
    - action_store_problem_description   <!-- predicted: utter_possibilities -->
    - slot{"problem_description": "ofcouse"}
    - utter_direct_to_forum_for_help   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: utter_possibilities -->
* affirm
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: utter_possibilities -->
* deny
    - utter_nohelp   <!-- predicted: utter_possibilities -->


## Generated Story goal:1 step, id:2979714d45bc445e9d7241fdc3ad64c1, 12/15/18 -3947067250872774786
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* handleinsult
    - chitchat: action_chitchat
* handleinsult
    - chitchat: action_chitchat
* handleinsult
    - chitchat: action_chitchat
* handleinsult
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* enter_data
    - action_set_onboarding   <!-- predicted: action_get_community_events -->
    - utter_built_bot_before   <!-- predicted: action_get_community_events -->
* enter_data
    - action_select_installation_command   <!-- predicted: action_get_community_events -->
    - utter_ask_ready_to_build   <!-- predicted: utter_explain_nlucore -->
* deny
    - utter_ask_if_problem   <!-- predicted: utter_tryout -->


## Generated Story goal:1 step, id:1cf5bff6668140a3978700059f6edb83, 12/17/18 -303270644112371083
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* switch{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - getstarted_1_success: utter_switch_dialogflow
    - chitchat: utter_anything_else
* enter_data
    - action_greet_user   <!-- predicted: utter_possibilities -->
* enter_data
    - chitchat: utter_possibilities -> fail


## Generated Story goal:1 step, id:32111c2c24bb44dba5da72e6978f29fe, 12/17/18 7799571079686222516
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whoisit
    - chitchat: action_chitchat
* ask_whatisrasa
    - chitchat: action_chitchat
* out_of_scope
    - oos: utter_out_of_scope
    - utter_possibilities   <!-- predicted: action_listen -->
* ask_wherefrom
    - chitchat: action_chitchat
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout


## Generated Story goal:1 step, id:15f92cc91e4e4c86826ffd023f4d1ef7, 12/15/18 -5922610915225646491
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - getstarted_1_success: utter_quickstart_nlu_only
    - chitchat: utter_anything_else
* enter_data
    - action_select_installation_command   <!-- predicted: utter_not_sure -->
    - utter_ask_ready_to_build   <!-- predicted: utter_possibilities -->
* affirm
    - action_store_problem_description   <!-- predicted: utter_explain_core -->
    - slot{"problem_description": "yes"}
    - utter_direct_to_forum_for_help   <!-- predicted: action_listen -->


## Generated Story goal:1 step, id:8affa7a6082945a09f031db186ec22eb, 12/15/18 -5307346528120334917
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* enter_data
    - action_greet_user   <!-- predicted: utter_not_sure -->
* greet
    - action_greet_user   <!-- predicted: utter_not_sure -->
* ask_howdoing
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->


## Generated Story goal:1 step, id:b2a4da8d7bf6494893801a9ef6a6f81f, 12/15/18 1767757702730525150
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* deny
    - getstarted_1: utter_tryout
* ask_howold
    - chitchat: action_chitchat
    - getstarted_1: utter_tryout
* deny
    - getstarted_1_success: utter_direct_install
    - chitchat: utter_anything_else
* affirm
    - utter_what_help   <!-- predicted: action_listen -->
* affirm
    - utter_quickstart   <!-- predicted: utter_ask_migration -->
    - utter_anything_else   <!-- predicted: action_listen -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_howold
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* greet
    - action_greet_user   <!-- predicted: utter_tryout -->
* ask_howdoing
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* ask_weather
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_chitchat -->
* ask_weather
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_chitchat -->
* enter_data
    - utter_possibilities   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* greet
    - action_greet_user   <!-- predicted: utter_tryout -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_howdoing
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* out_of_scope
    - utter_out_of_scope   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: action_chitchat -->
* deny
    - utter_nohelp   <!-- predicted: utter_tryout -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatisrasa
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* thank
    - utter_noworries   <!-- predicted: utter_tryout -->
    - utter_anything_else   <!-- predicted: action_greet_user -->
* bye
    - utter_bye   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: utter_ask_migration -->
    - utter_first_bot_with_rasa   <!-- predicted: utter_tryout -->
* deny
    - action_set_onboarding   <!-- predicted: utter_explain_stack -->
    - slot{"onboarding": false}
    - utter_ask_which_product   <!-- predicted: utter_stack_details -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_ask_for_nlu_specifics   <!-- predicted: utter_great -->
* enter_data
    - utter_quickstart_nlu_only   <!-- predicted: utter_tryout -->
    - utter_anything_else   <!-- predicted: utter_tryout -->
* affirm
    - utter_thumbsup   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_anything_else -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* enter_data
    - utter_not_sure   <!-- predicted: utter_tryout -->
    - utter_possibilities   <!-- predicted: utter_anything_else -->
* ask_weather
    - chitchat: action_chitchat
* deny
    - utter_nohelp   <!-- predicted: utter_direct_install -->


## Generated Story goal:1 step, id:8861ebbcdb684fb98a66f65a357d07b0, 12/15/18 -217273042631869968
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_howdoing
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout


## Generated Story goal:1 step, id:120a458cbe094db9b49c0d2a9adca7ca, 12/15/18 -7037911620927207371
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started
    - utter_quickstart_nlu_only   <!-- predicted: utter_quickstart -->
    - chitchat: utter_anything_else -> fail


## Generated Story goal:1 step, id:3c9cd2509a78495bb5fd306618a9ba8e, 12/17/18 3076997113982385599
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_getstarted   <!-- predicted: utter_not_sure -->
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* enter_data
    - action_greet_user   <!-- predicted: utter_not_sure -->
* affirm
    - utter_explain_nlu   <!-- predicted: utter_not_sure -->
    - utter_tryout   <!-- predicted: utter_ask_jobfunction -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart -> fail
    - utter_anything_else   <!-- predicted: action_listen -->
* source_code
    - utter_source_code   <!-- predicted: utter_not_sure -->
    - chitchat: utter_anything_else


## Generated Story goal:3 step, id:a1abb0d5bd294bb083c03f73eeb5e786, 05/01/19 -8888358178538347654
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* install_rasa{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - utter_getstarted   <!-- predicted: action_get_community_events -->
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* affirm
    - action_set_onboarding   <!-- predicted: utter_not_sure -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: utter_tryout -->
* deny
    - utter_explain_stack   <!-- predicted: action_store_email -->
    - utter_stack_details   <!-- predicted: utter_built_bot_before -->
    - utter_explain_nlucore   <!-- predicted: utter_built_bot_before -->
* affirm
    - utter_explain_nlu   <!-- predicted: utter_ask_migration -->
    - utter_explain_core   <!-- predicted: utter_tryout -->
    - getstarted_1: utter_tryout -> fail
* enter_data
    - action_greet_user   <!-- predicted: utter_not_sure -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: utter_ask_migration -->
    - utter_first_bot_with_rasa   <!-- predicted: utter_tryout -->


## Generated Story goal:oos, id:1e680f8682a44338a9c68496bc8ac9ba, 05/01/19 9069131845960195647
* ask_wherefrom
    - chitchat: action_chitchat


## Generated Story goal:FAQ, id:3256c66e60aa42c7bc33f915dfa0d728, 05/01/19 -7313640270495983501
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* rasa_cost
    - utter_rasa_cost   <!-- predicted: action_faqs -->
    - chitchat: utter_anything_else
* rasa_cost
    - utter_rasa_cost   <!-- predicted: action_faqs -->
    - chitchat: utter_anything_else


## Generated Story goal:sales, id:c08c1942644d489ea1995880bf043a85, 12/15/18 8980344777735687263
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whatspossible
    - chitchat: action_chitchat
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* contact_sales
    - sales: utter_moreinformation
    - sales: utter_ask_jobfunction


## Generated Story goal:chitchat, id:8ea529575d1e471383b23c054caf3673, 12/17/18 -4775544525012944248
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_howdoing
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_chitchat
* ask_whatisrasa
    - chitchat: action_chitchat
* enter_data
    - action_default_ask_affirmation   <!-- predicted: utter_not_sure -->


## Generated Story goal:1 step, id:0da3c44e9839403eafaa89050e2b8d3e, 12/15/18 726412975159353253
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_whatspossible
    - chitchat: action_chitchat
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
* enter_data
    - utter_explain_stack   <!-- predicted: action_store_unknown_product -->
    - utter_stack_details   <!-- predicted: utter_built_bot_before -->
    - utter_explain_nlucore   <!-- predicted: utter_built_bot_before -->
* affirm
    - utter_explain_nlu   <!-- predicted: utter_ask_migration -->
    - utter_tryout   <!-- predicted: utter_ask_migration -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->


## Generated Story goal:sales, id:c1e80e11d95e47bba78eeabb843bc897, 12/15/18 -6282839839722846955
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whatspossible
    - chitchat: action_chitchat
* contact_sales
    - sales: utter_moreinformation
    - sales: utter_ask_jobfunction
* enter_data
    - sales: action_store_job
    - slot{"job_function": "ohh sorry then"}
    - sales: utter_ask_usecase


## Generated Story goal:1 step, id:172015966d6b4687bdd65f3a5c7be107, 12/15/18 -2390059780872131662
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* enter_data
    - utter_possibilities   <!-- predicted: utter_explain_nlucore -->
    - utter_stack_details   <!-- predicted: utter_built_bot_before -->
    - utter_explain_nlucore   <!-- predicted: utter_built_bot_before -->
* affirm
    - utter_explain_nlu   <!-- predicted: utter_ask_migration -->
    - getstarted_1: utter_tryout
* bye
    - utter_bye   <!-- predicted: utter_thumbsup -->
    - action_listen   <!-- predicted: utter_tryout -->


## Generated Story goal:chitchat, id:2ca65157d22b43caad664589ee29524e, 12/15/18 3415830769284134354
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_howdoing
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_chitchat
* ask_howold{"number": 42}
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_chitchat
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->


## Generated Story goal:chitchat, id:b68bec79922b42b1b60bd13f3a3a5a14, 12/15/18 2244534826485528312
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - chitchat: action_chitchat
* out_of_scope
    - oos: utter_out_of_scope
    - utter_possibilities   <!-- predicted: action_listen -->
* signup_newsletter
    - subscribe: utter_great
    - subscribe: utter_ask_email
* deny
    - subscribe: utter_cantsignup
* handleinsult
    - chitchat: action_chitchat
    - subscribe: utter_ask_email -> fail
* deny
    - subscribe: utter_cantsignup -> fail
* deny
    - utter_direct_install   <!-- predicted: utter_cantsignup -->
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: utter_cantsignup -->


## Generated Story goal:3 step, id:953db2ccbe0748c586f5904a1b9b4432, 12/15/18 -2802431565840004587
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* install_rasa
    - getstarted_3: utter_ask_python_installed
* deny
    - getstarted_3: utter_get_python
    - utter_ask_pip_or_conda   <!-- predicted: utter_ask_python_installed -->
* enter_data
    - action_select_installation_command   <!-- predicted: utter_ask_pip_or_conda -->
    - utter_ask_ready_to_build   <!-- predicted: utter_ask_python_installed -->
* affirm
    - utter_get_starter_pack   <!-- predicted: utter_ask_python_installed -->
    - utter_direct_to_step4   <!-- predicted: utter_ask_python_installed -->
    - utter_anything_else   <!-- predicted: action_listen -->
* ask_howdoing
    - chitchat: action_chitchat


## Generated Story goal:oos, id:ed1418fcc3884157bcc96a7c43d21ec0, 05/01/19 2178899423323461626
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_languagesbot
    - chitchat: action_chitchat
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* ask_faq_languages
    - faq: action_faqs
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities


## Generated Story goal:1 step, id:f48bb43d6f5645d69b0c1cd1cfc9c62b, 12/15/18 923590105913609100
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - getstarted_1_success: utter_quickstart_nlu_only
    - chitchat: utter_anything_else


## Generated Story goal:chitchat, id:cd932f93d47c4cb6a408a61b8e74c2be, 12/17/18 2968378781313327835
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_howdoing
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_chitchat
* enter_data
    - action_greet_user   <!-- predicted: utter_not_sure -->
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_whatspossible
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat
* install_rasa
    - getstarted_3: utter_ask_python_installed
* enter_data
    - utter_get_python   <!-- predicted: utter_ask_pip_or_conda -->
    - getstarted_3: utter_ask_pip_or_conda
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build


## Generated Story goal:oos, id:864df094a24a4cc3a6b55a824c1f3a35, 12/17/18 -7699038322326118938
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_getstarted   <!-- predicted: utter_not_sure -->
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* out_of_scope
    - oos: utter_out_of_scope
    - chitchat: utter_possibilities
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* ask_whatspossible
    - chitchat: action_chitchat
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* affirm
    - getstarted_1: action_set_onboarding -> fail
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before -> fail
* affirm
    - getstarted_1: utter_ask_migration -> fail
* affirm
    - getstarted_1: utter_ask_which_tool -> fail
* enter_data
    - getstarted_1: action_store_unknown_product -> fail
    - slot{"unknown_product": "Cleverbot"}
    - getstarted_1_success: utter_no_guide_for_switch -> fail
    - chitchat: utter_anything_else -> fail
* deny
    - utter_nohelp   <!-- predicted: utter_thumbsup -->
* ask_weather
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_canthelp -->


## Generated Story goal:faq, id:db852c1fc7144db09e449fec4567614e, 12/17/18 -5129452726289215743
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* rasa_cost
    - utter_rasa_cost   <!-- predicted: action_faqs -->
    - chitchat: utter_anything_else


## Generated Story goal:1 step, id:d1f0cdf624a74a2ea7323b0817353037, 12/15/18 1731815793411691019
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - utter_tryout   <!-- predicted: utter_built_bot_before -->
* how_to_get_started
    - utter_quickstart_nlu_only   <!-- predicted: utter_getstarted -->
    - utter_anything_else   <!-- predicted: utter_first_bot_with_rasa -->


## Generated Story goal:oos, id:697db34a22db4c089e85f2c9ae3ee88f, 05/01/19 8439639792622345614
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_getstarted -->
    - action_listen   <!-- predicted: utter_first_bot_with_rasa -->


## Generated Story goal:1 step, id:4f647cb2427c495dbff5cf6fa1d7feb9, 12/15/18 -1171376024735749581
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* enter_data
    - action_greet_user   <!-- predicted: action_store_bot_language -->
    - utter_stack_details   <!-- predicted: action_listen -->
    - utter_anything_else   <!-- predicted: utter_built_bot_before -->
* affirm
    - utter_quickstart   <!-- predicted: utter_ask_migration -->
    - utter_anything_else   <!-- predicted: action_listen -->


## Generated Story goal:1 step, id:99ca2d48ec6b4563a09b13303f4b6960, 12/17/18 4281123642591350586
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_getstarted   <!-- predicted: utter_not_sure -->
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* affirm
    - getstarted_1: action_set_onboarding -> fail
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before -> fail
* affirm
    - getstarted_1: utter_ask_migration -> fail
* deny
    - getstarted_1: utter_explain_stack -> fail
    - getstarted_1: utter_stack_details -> fail
    - getstarted_1: utter_explain_nlucore -> fail
* telljoke
    - chitchat: action_chitchat
    - getstarted_1: utter_explain_nlucore -> fail


## Generated Story goal:chitchat, id:debe18e2325840aeb5313ad18a27fa42, 05/01/19 1747852281231103127
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_isbot
    - chitchat: action_chitchat
* bye
    - utter_bye   <!-- predicted: utter_nohelp -->


## Generated Story goal:chitchat, id:624b61bee53b411bac4a3855343dd0c7, 12/15/18 -8806002753186605917
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* affirm
    - chitchat: utter_thumbsup
* ask_howold
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_chitchat


## Generated Story goal:1 step, id:bfdc18480a8a48e19aacf281bdd5db46, 05/01/19 9082912409352129743
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_faq_languages
    - faq: action_faqs
* enter_data{"language": "Japanese"}
    - slot{"language": "Japanese"}
    - slot{"language": "Japanese"}
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
* enter_data
    - action_chitchat   <!-- predicted: action_store_unknown_product -->
    - utter_ask_migration   <!-- predicted: utter_built_bot_before -->
* ask_whatisrasa
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->
    - action_listen   <!-- predicted: utter_built_bot_before -->


## Generated Story goal:chitchat, id:455210c2c7c9471194a7faaf2e63579f, 12/15/18 7957735631208973079
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* handleinsult
    - chitchat: action_chitchat
* out_of_scope
    - oos: utter_out_of_scope
    - utter_possibilities   <!-- predicted: action_listen -->
* rasa_cost
    - utter_rasa_cost   <!-- predicted: action_faqs -->
    - chitchat: utter_anything_else
* ask_isbot
    - chitchat: action_chitchat


## Generated Story goal:1 step, id:93b8b449ab074a6f973da26067b5c163, 12/17/18 -6676267086559597786
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* technical_question
    - utter_getstarted   <!-- predicted: utter_ask_pip_or_conda -->
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* affirm
    - getstarted_1: action_set_onboarding -> fail
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before -> fail
* deny
    - getstarted_1: utter_explain_stack -> fail
    - getstarted_1: utter_stack_details -> fail
    - getstarted_1: utter_explain_nlucore -> fail
* enter_data{"number": 1}
    - utter_great   <!-- predicted: utter_explain_nlucore -->
    - utter_ask_email   <!-- predicted: utter_built_bot_before -->
* deny
    - utter_cantsignup   <!-- predicted: utter_explain_stack -->
    - action_listen   <!-- predicted: utter_stack_details -->


## Generated Story goal:1 step, id:9724aac6adda47a38271574fddb1529d, 05/01/19 6727944383445682358
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_faq_platform
    - faq: action_faqs
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout


## Generated Story goal:1 step, id:2f822433f6a9427c8bff569c676d824e, 12/15/18 -6375541493127917237
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* handleinsult
    - chitchat: action_chitchat
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* deny
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* ask_whoisit
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->


## Generated Story goal:oos, id:47f2fe45cd5f463cbaf2bc72def8f569, 05/01/19 -763810754505424450
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* install_rasa
    - getstarted_3: utter_ask_python_installed
* affirm
    - utter_ask_pip_or_conda   <!-- predicted: utter_ask_python_installed -->
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* affirm
    - getstarted_3: utter_get_starter_pack
    - getstarted_3_success: utter_direct_to_step4
    - utter_anything_else   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: utter_direct_to_step4 -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: utter_direct_to_step4 -->
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* affirm
    - action_set_onboarding   <!-- predicted: utter_ask_describe_problem -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: action_listen -->
* deny
    - utter_explain_stack   <!-- predicted: utter_ask_if_problem -->
    - utter_stack_details   <!-- predicted: action_listen -->
    - utter_explain_nlucore   <!-- predicted: action_listen -->
* affirm
    - utter_explain_nlu   <!-- predicted: utter_ask_if_problem -->
    - utter_explain_core   <!-- predicted: utter_direct_to_step4 -->
    - utter_tryout   <!-- predicted: action_listen -->
* deny
    - utter_direct_install   <!-- predicted: utter_ask_if_problem -->
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: utter_ask_if_problem -->


## Generated Story goal:chitchat, id:0f8142515810483a8c2e777909c37c2c, 12/17/18 -8573563216604908022
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whoisit
    - chitchat: action_chitchat
* telljoke
    - chitchat: action_chitchat
* enter_data
    - action_select_installation_command   <!-- predicted: utter_not_sure -->
    - utter_ask_ready_to_build   <!-- predicted: utter_possibilities -->
* enter_data
    - action_store_problem_description   <!-- predicted: utter_not_sure -->
    - slot{"problem_description": "i have installed rasa_core"}
    - utter_direct_to_forum_for_help   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: utter_possibilities -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: action_listen -->
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* affirm
    - action_set_onboarding   <!-- predicted: utter_possibilities -->
    - utter_ask_which_product   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: action_listen -->
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - slot{"product": "core"}
    - utter_core_tutorial   <!-- predicted: action_listen -->
    - utter_anything_else   <!-- predicted: action_listen -->


## Generated Story goal:3 step, id:f509c57ec8014ac9b4bd1eb7fde32f87, 12/17/18 -6498136812331561160
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat
* affirm
    - utter_what_help   <!-- predicted: utter_thumbsup -->
* ask_whatspossible
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* install_rasa{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - utter_ask_python_installed   <!-- predicted: utter_not_sure -->
* affirm
    - utter_ask_pip_or_conda   <!-- predicted: utter_quickstart -->
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - action_select_installation_command   <!-- predicted: utter_quickstart -->
    - utter_ask_ready_to_build   <!-- predicted: utter_direct_install -->
* affirm
    - utter_get_starter_pack   <!-- predicted: utter_ask_ready_to_build -->
    - utter_direct_to_step4   <!-- predicted: utter_anything_else -->
    - utter_anything_else   <!-- predicted: action_listen -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: utter_ask_ready_to_build -->
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->


## Generated Story goal:1 step, id:ff826c3d37f64c61b6488cfbd2aeb547, 12/15/18 -7283527111737167069
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* affirm
    - utter_thumbsup   <!-- predicted: utter_not_sure -->
    - utter_anything_else   <!-- predicted: action_listen -->
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - utter_built_bot_before   <!-- predicted: action_listen -->
* enter_data
    - action_select_installation_command   <!-- predicted: action_get_community_events -->
    - utter_ask_ready_to_build   <!-- predicted: action_get_community_events -->
* rasa_cost
    - utter_rasa_cost   <!-- predicted: action_store_bot_language -->
    - utter_anything_else   <!-- predicted: utter_possibilities -->
* enter_data
    - action_greet_user   <!-- predicted: utter_not_sure -->
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* enter_data
    - action_greet_user   <!-- predicted: action_store_bot_language -->
    - utter_stack_details   <!-- predicted: action_listen -->
    - utter_anything_else   <!-- predicted: utter_built_bot_before -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: utter_ask_migration -->
    - utter_first_bot_with_rasa   <!-- predicted: utter_built_bot_before -->
* handleinsult
    - chitchat: action_chitchat
    - onboarding: utter_first_bot_with_rasa
* affirm
    - action_set_onboarding   <!-- predicted: utter_ask_migration -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: utter_ask_migration -->
* bye
    - utter_bye   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_built_bot_before -->


## Generated Story goal:1 step, id:84082ae966d64d0ca415b276c3635916, 12/15/18 -5644677460292251299
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->


## Generated Story goal:1 step, id:79e8dd05329946a8963c170d920e0144, 05/01/19 -5283482436135596936
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - getstarted_1: utter_built_bot_before
* enter_data
    - utter_ask_migration   <!-- predicted: action_get_community_events -->
* enter_data
    - utter_contact_email   <!-- predicted: action_get_community_events -->
* telljoke
    - chitchat: action_chitchat
* telljoke
    - chitchat: action_chitchat
* ask_faq_channels
    - faq: action_faqs
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - slot{"product": "core"}
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_also_explain_nlu
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_tryout
* ask_whatspossible
    - chitchat: action_chitchat
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->


## Generated Story goal:1 step, id:5b7be2c22b874342aeca4216cfd5d35a, 12/15/18 1624335723075150223
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* out_of_scope
    - oos: utter_out_of_scope
    - utter_possibilities   <!-- predicted: action_listen -->
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->


## Generated Story goal:1 step, id:cfa8bb9deaf0427498c662745431a282, 12/15/18 -56217783078242536
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatisrasa
    - chitchat: action_chitchat
* enter_data
    - action_greet_user   <!-- predicted: utter_not_sure -->
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: utter_explain_nlu -->
* deny
    - utter_nohelp   <!-- predicted: utter_direct_install -->
* thank
    - utter_noworries   <!-- predicted: utter_not_sure -->
    - utter_anything_else   <!-- predicted: utter_possibilities -->
* deny
    - utter_nohelp   <!-- predicted: utter_thumbsup -->


## Generated Story goal:1 step, id:16439d767388463d93e9c827767bca96, 05/01/19 -5426994757726665781
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* greet
    - action_greet_user   <!-- predicted: utter_getstarted -->


## Generated Story goal:chitchat, id:9e785c9f586b48b7affc592dd2d499fb, 12/17/18 8538685554217994801
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->


## Generated Story goal:oos , id:5a1c8e47b3ba4dc38b2a3de3ffedee30, 12/17/18 4221492392327213787
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* ask_whoisit
    - chitchat: action_chitchat
    - onboarding: utter_first_bot_with_rasa
* deny
    - rasa_help: action_set_onboarding
    - slot{"onboarding": false}
    - rasa_help: utter_ask_which_product
* deny
    - chitchat: utter_thumbsup -> fail
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_ask_which_product -->


## Generated Story goal:1 step, id:fe9205767e5540319511248ba2d7aa7d, 12/15/18 -1169614020695031757
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - utter_tryout   <!-- predicted: utter_built_bot_before -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* thank
    - utter_noworries   <!-- predicted: utter_not_sure -->
    - utter_anything_else   <!-- predicted: action_listen -->
* enter_data
    - action_greet_user   <!-- predicted: utter_not_sure -->


## Generated Story goal:1 step, id:de903a69d7524115a8affa517ba1df0c, 12/15/18 4546830120439352871
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatisrasa
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started
    - action_chitchat   <!-- predicted: utter_explain_nlu -->
    - utter_explain_nlucore   <!-- predicted: utter_explain_core -->
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_nlu   <!-- predicted: utter_explain_core -->
    - utter_explain_core   <!-- predicted: utter_also_explain_nlu -->
    - utter_tryout   <!-- predicted: utter_also_explain_nlu -->


## Generated Story goal:1 step, id:f425b3ba996e4eaeacbc82becd473dbf, 12/17/18 4246660389998784195
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* ask_whoisit
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* ask_howdoing
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_tryout -->
* enter_data
    - utter_possibilities   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->


## Generated Story goal:chitchat, id:9a569475596347ad9d181b33f887a87f, 12/15/18 2802758851923456977
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whoisit
    - chitchat: action_chitchat
* ask_howold
    - chitchat: action_chitchat
* enter_data{"email": "tens@da.ok"}
    - slot{"email": "tens@da.ok"}
    - slot{"email": "tens@da.ok"}
    - action_store_email   <!-- predicted: utter_not_sure -->
    - slot{"email": "tens@da.ok"}
    - subscribe: action_subscribe_newsletter -> fail
    - slot{"subscribed": true}
    - subscribe: utter_awesome -> fail
    - subscribe_success: utter_confirmationemail -> fail
    - subscribe: utter_docu -> fail
    - feedback: utter_ask_feedback -> fail
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* enter_data
    - utter_great   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* affirm
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* affirm
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* deny
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* ask_wherefrom
    - action_chitchat   <!-- predicted: utter_great -->
* affirm
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* enter_data
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* handleinsult
    - action_chitchat   <!-- predicted: utter_great -->
* enter_data
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* affirm
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail


## Generated Story goal:oos, id:174129b4be704f47b76aa8dc5b2f3ab6, 12/15/18 -5421971901023397932
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* out_of_scope
    - oos: utter_out_of_scope
* enter_data{"email": "lavi@email.com"}
    - slot{"email": "lavi@email.com"}
    - slot{"email": "lavi@email.com"}
    - action_greet_user   <!-- predicted: utter_not_sure -->
* greet
    - greet_success: action_greet_user


## Generated Story goal:1 step, id:c1712b9b83444c4d950fb1d0c06ee81e, 05/01/19 -4543793503788733794
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->


## Generated Story goal:1 step, id:9e28b5d02f08459b9cb19e2888976813, 12/15/18 523765784065373811
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_python_installed -->
* ask_howdoing
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: action_set_onboarding -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* ask_whatspossible
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: action_greet_user -->
* signup_newsletter
    - utter_great   <!-- predicted: utter_tryout -->
    - utter_ask_email   <!-- predicted: utter_tryout -->
* enter_data{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - slot{"email": "arvindk@yopmail.com"}
    - action_store_email   <!-- predicted: utter_tryout -->
    - slot{"email": "arvindk@yopmail.com"}
    - subscribe: action_subscribe_newsletter
    - slot{"subscribed": false}
    - utter_already_subscribed   <!-- predicted: action_store_email -->
    - utter_docu   <!-- predicted: utter_tryout -->
    - utter_ask_feedback   <!-- predicted: utter_tryout -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great
    - chitchat: utter_anything_else
* ask_restaurant
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_anything_else -->
* signup_newsletter
    - subscribe: utter_great
    - action_listen   <!-- predicted: utter_anything_else -->
* out_of_scope
    - utter_great   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - utter_ask_name   <!-- predicted: utter_great -->
    - utter_anything_else   <!-- predicted: action_listen -->
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* deny
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* enter_data
    - utter_spacy_or_tensorflow   <!-- predicted: utter_great -->
    - chitchat: utter_anything_else -> fail
* canthelp
    - utter_canthelp   <!-- predicted: utter_great -->
* greet
    - action_greet_user   <!-- predicted: utter_great -->
* bye
    - utter_ask_company   <!-- predicted: utter_great -->
* enter_data{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - action_store_company   <!-- predicted: utter_anything_else -->
    - slot{"company_name": "google"}
    - utter_ask_businessmail   <!-- predicted: utter_anything_else -->
* enter_data{"email": "arvind@google.com"}
    - slot{"email": "arvind@google.com"}
    - slot{"email": "arvind@google.com"}
    - action_store_email   <!-- predicted: utter_great -->
    - slot{"email": "arvind@google.com"}
    - action_subscribe_newsletter   <!-- predicted: action_listen -->
    - slot{"subscribed": true}
    - utter_awesome   <!-- predicted: action_listen -->
    - utter_confirmationemail   <!-- predicted: action_listen -->
    - utter_docu   <!-- predicted: action_listen -->
    - utter_ask_feedback   <!-- predicted: action_listen -->
* feedback{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - slot{"feedback_value": "negative"}
    - utter_thumbsup   <!-- predicted: utter_switch_dialogflow -->
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_thumbsup   <!-- predicted: utter_anything_else -->
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_thumbsup   <!-- predicted: utter_anything_else -->
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - chitchat: utter_anything_else -> fail
* thank
    - utter_anything_else   <!-- predicted: utter_moreinformation -->
* bye
    - utter_bye   <!-- predicted: action_store_email -->
* greet
    - action_get_community_events   <!-- predicted: action_store_email -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_whoisit
    - action_chitchat   <!-- predicted: utter_not_sure -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_howold
    - action_chitchat   <!-- predicted: utter_not_sure -->
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_howold
    - action_faqs   <!-- predicted: utter_not_sure -->
    - action_listen   <!-- predicted: utter_anything_else -->
* enter_data
    - action_store_unknown_nlu_part   <!-- predicted: utter_not_sure -->
    - slot{"unknown_nlu_part": "nopes"}
    - action_store_unknown_nlu_part   <!-- predicted: utter_anything_else -->
    - slot{"unknown_nlu_part": "nopes"}
    - utter_dont_know_nlu_part   <!-- predicted: utter_moreinformation -->
    - utter_duckling   <!-- predicted: utter_moreinformation -->
    - utter_anything_else   <!-- predicted: utter_moreinformation -->
* enter_data
    - utter_switch_dialogflow   <!-- predicted: utter_not_sure -->
    - chitchat: utter_anything_else -> fail
* ask_languagesbot
    - utter_switch_dialogflow   <!-- predicted: utter_not_sure -->
    - chitchat: utter_anything_else -> fail


## Generated Story goal:1 step, id:c1413213af684cbd952299e5b640a174, 12/15/18 5367922669514830768
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whatisrasa
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->
* thank
    - utter_noworries   <!-- predicted: action_chitchat -->
    - chitchat: utter_anything_else
* deny
    - utter_nohelp   <!-- predicted: utter_thumbsup -->


## Generated Story goal:1 step, id:3b58d04997b343dca11db2d8b09d5f56, 12/17/18 -5919216385967754526
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_getstarted   <!-- predicted: utter_not_sure -->
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* affirm
    - action_faqs   <!-- predicted: action_set_onboarding -->
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* affirm
    - action_set_onboarding   <!-- predicted: utter_ask_entities -->
    - utter_ask_which_product   <!-- predicted: action_set_onboarding -->
    - action_listen   <!-- predicted: utter_built_bot_before -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_ask_for_nlu_specifics   <!-- predicted: action_set_onboarding -->
* nlu_info
    - action_store_unknown_nlu_part   <!-- predicted: utter_duckling_info -->
    - slot{"unknown_nlu_part": "classification"}
    - utter_dont_know_nlu_part   <!-- predicted: utter_tryout -->
    - utter_search_bar   <!-- predicted: utter_direct_step3 -->
    - utter_anything_else   <!-- predicted: action_store_unknown_nlu_part -->


## Generated Story goal:FAQ, id:3ae94172c7864fb59ab78db2334db86c, 05/01/19 2833611311799497832
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* nlu_info{"nlu_part": "duckling"}
    - slot{"nlu_part": "duckling"}
    - slot{"nlu_part": "duckling"}
    - rasa_help_success: utter_duckling_info
    - chitchat: utter_anything_else
* affirm
    - chitchat: utter_what_help
* nlu_info{"nlu_part": "duckling"}
    - slot{"nlu_part": "duckling"}
    - slot{"nlu_part": "duckling"}
    - rasa_help_success: utter_duckling_info
    - chitchat: utter_anything_else
* deny
    - utter_core_tutorial   <!-- predicted: utter_explain_nlucore -->
    - chitchat: utter_anything_else -> fail
* bye
    - utter_bye   <!-- predicted: utter_what_help -->
* greet
    - action_greet_user   <!-- predicted: action_listen -->
* greet
    - action_greet_user   <!-- predicted: utter_explain_nlucore -->


## Generated Story goal:1 step, id:7c9b8897dcbe4b46af67aa5b2290dc4f, 12/17/18 -1844283597923529811
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
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
* enter_data
    - getstarted_1: action_store_unknown_product
    - slot{"unknown_product": "hubot"}
    - getstarted_1_success: utter_no_guide_for_switch
    - chitchat: utter_anything_else
* ask_whoisit
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_anything_else -->
* ask_time
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_built_bot_before -->
* telljoke{"user_type": "new"}
    - chitchat: action_chitchat
    - action_listen   <!-- predicted: utter_built_bot_before -->
* enter_data
    - utter_possibilities   <!-- predicted: action_get_community_events -->
    - action_listen   <!-- predicted: action_chitchat -->


## Generated Story goal:1 step, id:3a1c70eaf9234bb6b27160abfb6d1f88, 12/15/18 3863097957169160390
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - getstarted_1_success: utter_quickstart_nlu_only
    - chitchat: utter_anything_else
* deny
    - utter_nohelp   <!-- predicted: utter_tryout -->
* affirm
    - utter_thumbsup   <!-- predicted: utter_explain_core -->


## Generated Story goal:1 step, id:321d95bf0cb14dc8b09f3f9a62827081, 12/15/18 6069986032596098095
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatspossible
    - chitchat: action_chitchat
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
* enter_data
    - utter_explain_stack   <!-- predicted: action_store_unknown_product -->
    - utter_stack_details   <!-- predicted: utter_built_bot_before -->
    - utter_explain_nlucore   <!-- predicted: utter_built_bot_before -->
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - slot{"product": "core"}
    - utter_core_tutorial   <!-- predicted: utter_explain_core -->
    - utter_anything_else   <!-- predicted: utter_also_explain_nlu -->
* deny
    - utter_thumbsup   <!-- predicted: utter_tryout -->
    - utter_anything_else   <!-- predicted: utter_tryout -->


## Generated Story goal:1 step, id:618cb7db283a4c0ea000cd60e198e6b0, 05/01/19 -391894298907133881
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - utter_explain_stack   <!-- predicted: utter_tryout -->
    - utter_stack_details   <!-- predicted: utter_tryout -->
    - utter_explain_nlucore   <!-- predicted: utter_explain_stack -->
* affirm
    - utter_explain_nlu   <!-- predicted: utter_explain_core -->
    - utter_explain_core   <!-- predicted: utter_tryout -->
    - getstarted_1: utter_tryout


## Generated Story goal:chitchat, id:39d029c35a994bf4bffc36e2a9a4c6de, 12/17/18 7695879941084586485
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* thank
    - utter_noworries   <!-- predicted: utter_canthelp -->
    - utter_anything_else   <!-- predicted: utter_possibilities -->
* affirm
    - utter_what_help   <!-- predicted: utter_thumbsup -->
* enter_data
    - action_select_installation_command   <!-- predicted: utter_not_sure -->
    - utter_ask_ready_to_build   <!-- predicted: utter_possibilities -->
* deny
    - utter_ask_if_problem   <!-- predicted: utter_canthelp -->
* deny
    - utter_anything_else   <!-- predicted: utter_canthelp -->
* affirm
    - utter_ask_describe_problem   <!-- predicted: utter_thumbsup -->
* affirm
    - action_store_problem_description   <!-- predicted: utter_thumbsup -->
    - slot{"problem_description": "yes"}
    - action_faqs   <!-- predicted: action_listen -->
* greet
    - action_greet_user   <!-- predicted: action_listen -->
* ask_howdoing
    - action_chitchat   <!-- predicted: utter_canthelp -->
* ask_whatspossible
    - action_chitchat   <!-- predicted: action_listen -->
* telljoke
    - action_chitchat   <!-- predicted: action_listen -->
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* greet
    - action_greet_user   <!-- predicted: action_listen -->


## Generated Story goal:1 step, id:c96f626b26e444c2ba743af283e3e5b5, 12/17/18 8581107588372252626
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_faq_slots
    - faq: action_faqs
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - utter_explain_stack   <!-- predicted: utter_tryout -->
    - utter_stack_details   <!-- predicted: utter_tryout -->
    - utter_explain_nlucore   <!-- predicted: utter_explain_stack -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_explain_nlu   <!-- predicted: utter_anything_else -->
    - utter_also_explain_core   <!-- predicted: utter_tryout -->
* affirm
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* affirm
    - utter_what_help   <!-- predicted: action_listen -->
* enter_data
    - action_select_installation_command   <!-- predicted: utter_not_sure -->
    - utter_ask_ready_to_build   <!-- predicted: utter_tryout -->
* nlu_generation_tool_recommendation
    - utter_already_subscribed   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* greet
    - action_store_problem_description   <!-- predicted: utter_explain_nlu -->
    - slot{"problem_description": "Hello"}
    - action_faqs   <!-- predicted: action_store_budget -->
* ask_whoisit
    - action_chitchat   <!-- predicted: utter_not_sure -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: action_listen -->
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* affirm
    - action_set_onboarding   <!-- predicted: action_listen -->
    - utter_built_bot_before   <!-- predicted: action_listen -->
* affirm
    - action_faqs   <!-- predicted: action_listen -->
    - utter_built_bot_before   <!-- predicted: action_listen -->
* affirm
    - utter_ask_migration   <!-- predicted: action_listen -->
* how_to_get_started
    - utter_ask_which_tool   <!-- predicted: action_listen -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: action_listen -->
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* deny
    - action_set_onboarding   <!-- predicted: action_listen -->
    - slot{"onboarding": false}
    - utter_ask_which_product   <!-- predicted: action_listen -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_ask_for_nlu_specifics   <!-- predicted: action_listen -->
* nlu_info{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - slot{"nlu_part": "intent classification"}
    - utter_nlu_intent_tutorial   <!-- predicted: action_listen -->
    - utter_offer_recommendation   <!-- predicted: utter_anything_else -->
* nlu_generation_tool_recommendation
    - utter_nlu_tools   <!-- predicted: action_listen -->


## Generated Story goal:1 step, id:cdd14d763a664a5b95e998ce165bd86f, 12/15/18 5883009647019170057
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* enter_data
    - action_greet_user   <!-- predicted: utter_not_sure -->


## Generated Story goal:subscribe, id:ee59175ac0a64f468b1b4559296f359a, 12/17/18 7101882852510041551
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_whoisit
    - chitchat: action_chitchat
* affirm
    - chitchat: utter_thumbsup
* ask_howdoing
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_chitchat
* contact_sales
    - sales: utter_moreinformation
    - sales: utter_ask_jobfunction
* enter_data
    - sales: action_store_job
    - slot{"job_function": "blah"}
    - sales: utter_ask_usecase
* enter_data
    - sales: action_store_usecase
    - slot{"use_case": "chat "}
    - sales: utter_thank_usecase
    - sales: utter_ask_budget
* enter_data{"number": 1}
    - sales: action_store_budget
    - slot{"budget": 1}
    - sales: utter_sales_contact
    - sales: utter_ask_name
* enter_data
    - sales: action_store_name
    - slot{"person_name": "bi"}
    - sales: utter_ask_company
* enter_data
    - sales: action_store_company
    - slot{"company_name": "q"}
    - sales: utter_ask_businessmail
* bye
    - utter_bye   <!-- predicted: utter_not_sure -->


## Generated Story goal:1 step, id:dab1fc88af214c1abb57334f72b8cfb2, 12/17/18 1502159966905958231
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatspossible
    - chitchat: action_chitchat
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
* switch{"current_api": "dialogflow"}
    - slot{"current_api": "dialogflow"}
    - getstarted_1_success: utter_switch_dialogflow
    - chitchat: utter_anything_else
* how_to_get_started
    - utter_getstarted   <!-- predicted: utter_switch_dialogflow -->
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* affirm
    - action_set_onboarding   <!-- predicted: utter_switch_dialogflow -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: action_listen -->
* affirm
    - utter_ask_migration   <!-- predicted: utter_switch_dialogflow -->
* deny
    - utter_explain_stack   <!-- predicted: utter_anything_else -->
    - utter_stack_details   <!-- predicted: utter_switch_dialogflow -->
    - utter_explain_nlucore   <!-- predicted: action_listen -->
* affirm
    - utter_explain_nlu   <!-- predicted: utter_switch_dialogflow -->
    - utter_explain_core   <!-- predicted: utter_anything_else -->
    - utter_tryout   <!-- predicted: utter_anything_else -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart   <!-- predicted: utter_switch_dialogflow -->
    - utter_anything_else   <!-- predicted: action_listen -->


## Generated Story goal:3 step, id:49e29935e38740429d10ae50045b11a6, 12/15/18 -1571430978479800820
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* install_rasa{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - utter_ask_python_installed   <!-- predicted: action_get_community_events -->
* deny
    - getstarted_3: utter_get_python
    - utter_ask_pip_or_conda   <!-- predicted: utter_ask_python_installed -->
* ask_faq_differencecorenlu
    - action_select_installation_command   <!-- predicted: action_faqs -->
    - utter_ask_ready_to_build   <!-- predicted: utter_ask_python_installed -->
* deny
    - utter_ask_if_problem   <!-- predicted: action_store_job -->
* enter_data
    - action_store_problem_description   <!-- predicted: utter_ask_python_installed -->
    - slot{"problem_description": "i'm sad"}
    - utter_direct_to_forum_for_help   <!-- predicted: action_greet_user -->
    - action_listen   <!-- predicted: utter_anything_else -->


## Generated Story goal:1 step, id:2de75b1f7d17449a8e8a6e481f6d14bd, 05/01/19 8262034575362695580
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* greet
    - action_greet_user   <!-- predicted: utter_anything_else -->
* greet
    - action_greet_user   <!-- predicted: action_chitchat -->
* enter_data
    - chitchat: utter_not_sure
    - utter_possibilities   <!-- predicted: action_greet_user -->
* deny
    - action_default_ask_affirmation   <!-- predicted: action_listen -->


## Generated Story goal:1 step, id:ef54f3457dd947be9f7ccdfa66d146ce, 12/17/18 -4040032104474387651
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* affirm
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* affirm
    - getstarted_1: utter_ask_migration
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* ask_whatisrasa{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - chitchat: action_chitchat
    - getstarted_1: utter_explain_nlucore
* out_of_scope{"product": "core", "number": 1}
    - slot{"product": "core"}
    - slot{"product": "core"}
    - utter_out_of_scope   <!-- predicted: utter_explain_core -->
    - utter_possibilities   <!-- predicted: utter_anything_else -->
    - action_listen   <!-- predicted: utter_also_explain_nlu -->
* affirm
    - utter_thumbsup   <!-- predicted: utter_explain_nlu -->


## Generated Story goal:1 step, id:318f6636b6c842f6a330b015599e8f7d, 05/01/19 -2612547548431379099
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* enter_data
    - action_faqs   <!-- predicted: utter_explain_nlucore -->
    - utter_explain_nlucore   <!-- predicted: utter_built_bot_before -->
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - slot{"product": "core"}
    - utter_explain_nlu   <!-- predicted: utter_explain_core -->
    - utter_explain_core   <!-- predicted: utter_also_explain_nlu -->
    - utter_tryout   <!-- predicted: utter_also_explain_nlu -->
* ask_faq_differencecorenlu
    - faq: action_faqs
    - utter_tryout   <!-- predicted: utter_also_explain_nlu -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* ask_howdoing
    - action_default_ask_affirmation   <!-- predicted: action_chitchat -->
    - action_listen   <!-- predicted: utter_tryout -->


## Generated Story goal:1 step, id:92128e5e2ea74967876544a30c37b41a, 12/15/18 7589135915048511041
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->


## Generated Story goal:1 step, id:33a2877c49944765a102c0a215632b8a, 12/15/18 3487883399882115987
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_howdoing
    - chitchat: action_chitchat
* ask_builder
    - chitchat: action_chitchat
* ask_whatspossible
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->


## Generated Story goal:1 step, id:dbb64f3d387441949443e4e6a7c83520, 05/01/19 982787949487219313
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatisrasa
    - chitchat: action_chitchat
* technical_question
    - utter_not_sure   <!-- predicted: utter_canthelp -->
    - chitchat: utter_possibilities -> fail
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout


## Generated Story goal:chitchat, id:1277dc2ceae04fe0b963c7786a41f750, 05/01/19 806262383242887293
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_time
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat
* ask_weather
    - chitchat: action_chitchat


## Generated Story goal:1 step , id:7146d879adc44cf5947ffe723015f02a, 12/15/18 7977723706233268217
* get_started_step3
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_howdoing
    - chitchat: action_chitchat
* install_rasa
    - getstarted_3: utter_ask_python_installed
* affirm
    - utter_ask_pip_or_conda   <!-- predicted: utter_ask_python_installed -->
* enter_data{"package_manager": "conda"}
    - slot{"package_manager": "conda"}
    - slot{"package_manager": "conda"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build
* enter_data
    - getstarted_3: action_store_problem_description
    - slot{"problem_description": "done"}
    - utter_direct_to_forum_for_help   <!-- predicted: utter_direct_to_step4 -->
    - action_listen   <!-- predicted: utter_direct_to_step4 -->
* affirm
    - utter_anything_else   <!-- predicted: utter_direct_to_forum_for_help -->
* how_to_get_started
    - onboarding: utter_getstarted
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* affirm
    - action_set_onboarding   <!-- predicted: utter_getstarted -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: action_listen -->
* deny
    - utter_explain_stack   <!-- predicted: utter_direct_to_step4 -->
    - utter_stack_details   <!-- predicted: action_listen -->
    - utter_explain_nlucore   <!-- predicted: action_listen -->
* affirm
    - utter_explain_nlu   <!-- predicted: action_listen -->
    - utter_explain_core   <!-- predicted: action_listen -->
    - utter_tryout   <!-- predicted: action_listen -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart_nlu_only   <!-- predicted: action_listen -->
    - utter_anything_else   <!-- predicted: utter_tryout -->
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - slot{"product": "core"}
    - utter_core_tutorial   <!-- predicted: action_listen -->
    - utter_anything_else   <!-- predicted: action_listen -->
* signup_newsletter
    - utter_great   <!-- predicted: action_listen -->
    - utter_ask_email   <!-- predicted: utter_getstarted -->
* ask_whatspossible
    - action_chitchat   <!-- predicted: utter_getstarted -->
    - utter_ask_email   <!-- predicted: action_listen -->
* signup_newsletter
    - utter_already_subscribed   <!-- predicted: action_listen -->
    - utter_docu   <!-- predicted: action_listen -->
    - utter_ask_feedback   <!-- predicted: action_listen -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* thank
    - utter_noworries   <!-- predicted: utter_getstarted -->
    - utter_anything_else   <!-- predicted: action_listen -->


## Generated Story goal:1 step, id:9978f875abec4c3c9955ec3d5dae51b1, 12/15/18 1526679696595893973
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
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
* enter_data
    - utter_explain_stack   <!-- predicted: action_store_unknown_product -->
    - utter_stack_details   <!-- predicted: utter_built_bot_before -->
    - utter_explain_nlucore   <!-- predicted: utter_built_bot_before -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_explain_nlu   <!-- predicted: utter_ask_budget -->
    - getstarted_1: utter_also_explain_core
* enter_data{"email": "amy@example.com"}
    - slot{"email": "amy@example.com"}
    - slot{"email": "amy@example.com"}
    - utter_tryout   <!-- predicted: action_store_bot_language -->
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_quickstart   <!-- predicted: utter_quickstart_nlu_only -->
    - utter_anything_else   <!-- predicted: action_listen -->


## Generated Story goal:1 step, id:19722107f07a4120bef398ea514e00de, 12/15/18 3342731703903234413
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"language": "chinese"}
    - slot{"language": "chinese"}
    - slot{"language": "chinese"}
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_tryout
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: action_listen -->


## Generated Story goal:1 step, id:decd65b902e148baac9a1e373c056474, 12/17/18 2076418664202927492
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_getstarted   <!-- predicted: utter_not_sure -->
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* affirm
    - getstarted_1: action_set_onboarding -> fail
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before -> fail
* deny
    - getstarted_1: utter_explain_stack -> fail
    - getstarted_1: utter_stack_details -> fail
    - getstarted_1: utter_explain_nlucore -> fail
* deny
    - getstarted_1: utter_tryout -> fail
* how_to_get_started{"product": "nlu"}
    - slot{"product": "nlu"}
    - slot{"product": "nlu"}
    - utter_quickstart   <!-- predicted: utter_quickstart_nlu_only -->
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - utter_nohelp   <!-- predicted: utter_tryout -->


## Generated Story goal:chitchat, id:bc6723f023be41cb9516b53781448272, 12/15/18 6369486256094570096
* get_started_step2
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
    - action_listen   <!-- predicted: utter_direct_step3 -->
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* greet
    - greet_success: action_greet_user
* ask_whoisit
    - chitchat: action_chitchat


## Generated Story goal:1 step, id:ad02fffc3bd841788f5b10e283fe2ab8, 12/17/18 7345417199532554495
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_getstarted   <!-- predicted: utter_not_sure -->
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* affirm
    - action_faqs   <!-- predicted: action_set_onboarding -->
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* affirm
    - action_set_onboarding   <!-- predicted: utter_ask_entities -->
    - utter_ask_which_product   <!-- predicted: action_set_onboarding -->
    - action_listen   <!-- predicted: utter_built_bot_before -->
* affirm
    - utter_ask_migration   <!-- predicted: action_set_onboarding -->
* deny
    - rasa_help: utter_explain_stack -> fail
    - rasa_help: utter_stack_details -> fail
    - rasa_help: utter_explain_nlucore -> fail
* affirm
    - rasa_help: utter_explain_nlu -> fail
    - utter_also_explain_core   <!-- predicted: utter_explain_core -->
* affirm
    - utter_tryout   <!-- predicted: action_set_onboarding -->
* affirm
    - action_faqs   <!-- predicted: utter_quickstart -->
    - utter_tryout   <!-- predicted: utter_first_bot_with_rasa -->
* enter_data{"email": "urandombg@abv.bg"}
    - slot{"email": "urandombg@abv.bg"}
    - slot{"email": "urandombg@abv.bg"}
    - action_store_email   <!-- predicted: utter_quickstart -->
    - slot{"email": "urandombg@abv.bg"}
    - action_subscribe_newsletter   <!-- predicted: utter_anything_else -->
    - slot{"subscribed": true}
    - subscribe: utter_awesome -> fail
    - subscribe_success: utter_confirmationemail -> fail
    - subscribe: utter_docu -> fail
    - feedback: utter_ask_feedback -> fail
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - feedback_success: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* affirm
    - utter_spacy_or_tensorflow   <!-- predicted: utter_great -->
    - chitchat: utter_anything_else -> fail
* affirm
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* affirm
    - chitchat: utter_great -> fail
    - chitchat: utter_anything_else -> fail
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* enter_data
    - chitchat: utter_great -> fail
    - utter_spacy_or_tensorflow   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail


## Generated Story goal:1 step, id:5458e9cbe0be44a589ad3c8b89d77642, 12/17/18 -981377364561820576
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whatisrasa
    - chitchat: action_chitchat
* ask_whatisrasa
    - chitchat: action_chitchat
* technical_question
    - action_store_problem_description   <!-- predicted: utter_canthelp -->
    - slot{"problem_description": "How Rasa works?"}
    - utter_direct_to_forum_for_help   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: utter_possibilities -->
* ask_whatspossible
    - action_chitchat   <!-- predicted: utter_not_sure -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: action_listen -->
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* affirm
    - action_set_onboarding   <!-- predicted: action_listen -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: action_listen -->
* enter_data
    - action_greet_user   <!-- predicted: utter_possibilities -->
    - utter_stack_details   <!-- predicted: action_listen -->
    - utter_explain_nlucore   <!-- predicted: action_listen -->
* deny
    - utter_tryout   <!-- predicted: action_listen -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - utter_quickstart   <!-- predicted: utter_not_sure -->
    - utter_anything_else   <!-- predicted: action_listen -->
* enter_data{"number": 9}
    - action_select_installation_command   <!-- predicted: utter_possibilities -->
    - utter_ask_ready_to_build   <!-- predicted: utter_anything_else -->
* greet
    - action_store_problem_description   <!-- predicted: action_listen -->
    - slot{"problem_description": "hello"}
    - action_faqs   <!-- predicted: action_listen -->
* affirm
    - action_greet_user   <!-- predicted: action_listen -->
* greet
    - action_greet_user   <!-- predicted: action_listen -->
* greet
    - action_greet_user   <!-- predicted: action_listen -->
* greet
    - action_greet_user   <!-- predicted: action_listen -->
* greet
    - action_greet_user   <!-- predicted: action_listen -->
* greet
    - action_greet_user   <!-- predicted: action_listen -->
* greet
    - action_greet_user   <!-- predicted: action_listen -->
* greet
    - action_greet_user   <!-- predicted: action_listen -->
* greet
    - action_greet_user   <!-- predicted: action_listen -->
* greet
    - action_greet_user   <!-- predicted: action_listen -->
* ask_whatspossible
    - action_chitchat   <!-- predicted: action_greet_user -->
* signup_newsletter
    - utter_great   <!-- predicted: action_listen -->
    - utter_ask_email   <!-- predicted: utter_possibilities -->
* deny{"email": "no@nonono.no"}
    - slot{"email": "no@nonono.no"}
    - slot{"email": "no@nonono.no"}
    - subscribe: action_store_email
    - slot{"email": "no@nonono.no"}
    - action_subscribe_newsletter   <!-- predicted: action_listen -->
    - slot{"subscribed": true}
    - utter_awesome   <!-- predicted: action_listen -->
    - utter_confirmationemail   <!-- predicted: action_listen -->
    - utter_docu   <!-- predicted: action_listen -->
    - utter_ask_feedback   <!-- predicted: action_listen -->
* greet
    - action_greet_user   <!-- predicted: utter_ask_feedback -->


## Generated Story goal:chitchat, id:7280484f234c47c98952837077cff3fc, 12/15/18 1673539480913407606
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_wherefrom
    - chitchat: action_chitchat


## Generated Story goal:1 step, id:2a075ca47bd942e29e99c10ef9b2533a, 12/17/18 -6381151701767496471
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* how_to_get_started{"product": "core"}
    - slot{"product": "core"}
    - slot{"product": "core"}
    - getstarted_1: utter_explain_core
    - getstarted_1: utter_also_explain_nlu
* affirm
    - getstarted_1: utter_explain_nlu
    - utter_tryout   <!-- predicted: utter_built_bot_before -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* deny
    - chitchat: utter_nohelp
* source_code
    - utter_source_code   <!-- predicted: utter_get_python -->
    - chitchat: utter_anything_else


## Generated Story goal:1 step, id:320e02b044fe472389b0e486833aab2c, 12/17/18 5108855124096892797
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_getstarted   <!-- predicted: utter_not_sure -->
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* affirm
    - getstarted_1: action_set_onboarding -> fail
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before -> fail
* out_of_scope
    - action_default_ask_affirmation   <!-- predicted: utter_not_sure -->
    - action_listen   <!-- predicted: utter_possibilities -->
* deny
    - action_default_ask_rephrase   <!-- predicted: utter_explain_stack -->
    - action_listen   <!-- predicted: utter_stack_details -->


## Generated Story goal:3 step, id:424bba9c6020412c920724ae7c0444ad, 05/01/19 -2955948574844971987
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* install_rasa
    - action_faqs   <!-- predicted: utter_explain_nlu -->
    - utter_explain_nlucore   <!-- predicted: utter_explain_core -->
* greet
    - action_greet_user   <!-- predicted: utter_getstarted -->
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding   <!-- predicted: utter_tryout -->
    - utter_ask_which_product   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* technical_question
    - action_greet_user   <!-- predicted: action_store_sales_info -->
* greet
    - action_greet_user   <!-- predicted: utter_getstarted -->
* how_to_get_started
    - action_default_ask_affirmation   <!-- predicted: utter_ask_migration -->
    - action_listen   <!-- predicted: utter_built_bot_before -->
* enter_data
    - action_default_fallback   <!-- predicted: action_store_unknown_product -->
    - slot{"feedback_value": "negative"}
    - form{"name": "feedback_form"}
    - slot{"requested_slot": "feedback_message"}
    - slot{"feedback_message": "hi"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_listen   <!-- predicted: utter_tryout -->
* how_to_get_started{"user_type": "new"}
    - action_set_onboarding   <!-- predicted: utter_ask_migration -->
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - utter_built_bot_before   <!-- predicted: action_set_onboarding -->
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - utter_explain_nlucore   <!-- predicted: action_store_email -->
* affirm
    - getstarted_1: utter_explain_nlu
    - utter_explain_core   <!-- predicted: utter_tryout -->
    - getstarted_1: utter_tryout
* affirm
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* affirm
    - utter_thumbsup   <!-- predicted: utter_ask_migration -->
* install_rasa
    - utter_ask_python_installed   <!-- predicted: utter_tryout -->
    - action_listen   <!-- predicted: utter_tryout -->
* deny
    - utter_get_python   <!-- predicted: utter_tryout -->
    - utter_ask_pip_or_conda   <!-- predicted: utter_anything_else -->
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - action_select_installation_command   <!-- predicted: action_listen -->
    - utter_ask_ready_to_build   <!-- predicted: utter_explain_stack -->
* technical_question
    - action_store_problem_description   <!-- predicted: utter_direct_install -->
    - slot{"problem_description": "error syntax"}
    - utter_direct_to_forum_for_help   <!-- predicted: utter_great -->
    - action_listen   <!-- predicted: utter_anything_else -->
* enter_data{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - slot{"package_manager": "pip"}
    - action_store_entity_extractor   <!-- predicted: utter_not_sure -->
    - slot{"entity_extractor": "ner_crf"}
    - utter_duckling   <!-- predicted: utter_anything_else -->
    - chitchat: utter_anything_else -> fail
* install_rasa
    - action_store_budget   <!-- predicted: utter_moreinformation -->
    - slot{"budget": "i need to install in my computer"}
    - utter_sales_contact   <!-- predicted: utter_anything_else -->
    - action_listen   <!-- predicted: utter_moreinformation -->
* install_rasa
    - action_faqs   <!-- predicted: action_listen -->
* greet
    - action_store_budget   <!-- predicted: utter_confirmationemail -->
    - slot{"budget": "hello"}
    - utter_quickstart_nlu_only   <!-- predicted: utter_confirmationemail -->
    - utter_quickstart   <!-- predicted: utter_anything_else -->
    - utter_direct_install   <!-- predicted: action_listen -->
    - utter_anything_else   <!-- predicted: utter_confirmationemail -->
* greet
    - action_greet_user   <!-- predicted: utter_moreinformation -->
* install_rasa
    - utter_quickstart_nlu_only   <!-- predicted: action_listen -->
    - utter_anything_else   <!-- predicted: action_greet_user -->
* greet
    - action_greet_user   <!-- predicted: action_store_sales_info -->
* how_to_get_started
    - utter_thumbsup   <!-- predicted: action_greet_user -->
* ask_howdoing
    - action_chitchat   <!-- predicted: utter_confirmationemail -->
    - action_listen   <!-- predicted: utter_confirmationemail -->
* ask_how_contribute
    - utter_not_sure   <!-- predicted: utter_confirmationemail -->
    - utter_possibilities   <!-- predicted: utter_confirmationemail -->
    - action_listen   <!-- predicted: utter_confirmationemail -->
* how_to_get_started
    - utter_getstarted   <!-- predicted: utter_confirmationemail -->
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* affirm
    - action_set_onboarding   <!-- predicted: action_store_sales_info -->
    - slot{"onboarding": true}
    - utter_built_bot_before   <!-- predicted: utter_confirmationemail -->
* affirm
    - utter_ask_migration   <!-- predicted: utter_confirmationemail -->
* affirm
    - utter_ask_which_tool   <!-- predicted: action_store_sales_info -->
* enter_data
    - utter_quickstart_nlu_only   <!-- predicted: utter_ask_feedback -->
    - utter_anything_else   <!-- predicted: utter_confirmationemail -->
* ask_whatisrasa
    - action_chitchat   <!-- predicted: utter_confirmationemail -->
    - action_listen   <!-- predicted: utter_confirmationemail -->


## Generated Story goal:3 step, id:6ce300612cda42c1a084c292455056f7, 12/15/18 3997558787082995527
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* install_rasa
    - getstarted_3: utter_ask_python_installed
* affirm
    - utter_ask_pip_or_conda   <!-- predicted: utter_ask_python_installed -->
* enter_data{"package_manager": "conda"}
    - slot{"package_manager": "conda"}
    - slot{"package_manager": "conda"}
    - getstarted_3: action_select_installation_command
    - getstarted_3: utter_ask_ready_to_build


## Generated Story goal:1 step, id:1bc7a86220da42588b30b2a5566b00dc, 12/17/18 940448344067621014
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* enter_data
    - utter_getstarted   <!-- predicted: utter_not_sure -->
    - utter_first_bot_with_rasa   <!-- predicted: action_listen -->
* affirm
    - getstarted_1: action_set_onboarding -> fail
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before -> fail
* deny
    - getstarted_1: utter_explain_stack -> fail
    - getstarted_1: utter_stack_details -> fail
    - getstarted_1: utter_explain_nlucore -> fail
* enter_data
    - utter_great   <!-- predicted: utter_explain_nlucore -->
    - utter_ask_email   <!-- predicted: utter_built_bot_before -->
* enter_data{"email": "f.madureira@gmail.com"}
    - slot{"email": "f.madureira@gmail.com"}
    - slot{"email": "f.madureira@gmail.com"}
    - subscribe: action_store_email -> fail
    - slot{"email": "f.madureira@gmail.com"}
    - subscribe: action_subscribe_newsletter -> fail
    - slot{"subscribed": true}
    - utter_awesome   <!-- predicted: utter_tryout -->
    - utter_confirmationemail   <!-- predicted: utter_tryout -->
    - utter_docu   <!-- predicted: utter_tryout -->
    - utter_ask_feedback   <!-- predicted: utter_tryout -->
* feedback{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - slot{"feedback_value": "positive"}
    - utter_great   <!-- predicted: utter_tryout -->
    - chitchat: utter_anything_else -> fail
* affirm
    - utter_great   <!-- predicted: utter_tryout -->
    - utter_anything_else   <!-- predicted: utter_tryout -->
* enter_data
    - utter_great   <!-- predicted: utter_anything_else -->
    - utter_spacy_or_tensorflow   <!-- predicted: utter_tryout -->
    - chitchat: utter_anything_else -> fail


## Generated Story goal:1 step, id:8d69c4b1d6db489789fe20e2bbeec153, 12/15/18 -7810778017142759063
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started{"user_type": "new"}
    - getstarted_1: action_set_onboarding
    - utter_getstarted_new   <!-- predicted: utter_built_bot_before -->
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* affirm
    - getstarted_1: utter_explain_nlu
    - getstarted_1: utter_explain_core
    - utter_tryout   <!-- predicted: utter_built_bot_before -->
* how_to_get_started
    - utter_quickstart_nlu_only   <!-- predicted: utter_getstarted -->
    - utter_anything_else   <!-- predicted: utter_first_bot_with_rasa -->
* deny
    - utter_nohelp   <!-- predicted: utter_explain_stack -->


## Generated Story goal:1 step, id:35dc087ff6084dc087a9b5d1fda96d60, 12/17/18 5905188858882087469
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - utter_ask_which_product   <!-- predicted: utter_built_bot_before -->
* affirm
    - utter_thumbsup   <!-- predicted: action_set_onboarding -->
    - action_listen   <!-- predicted: utter_built_bot_before -->


## Generated Story goal:oos, id:ee962c4c1af542f8952d6082ceb9c208, 05/01/19 1544238638038077071
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_whoisit
    - chitchat: action_chitchat
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities
* canthelp
    - chitchat: utter_canthelp


## Generated Story goal:faq, id:b7c01a1b3b034a59b74a25e4ffd94b12, 12/15/18 1531624798006099569
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* ask_faq_languages
    - faq: action_faqs


## Generated Story goal:1 step, id:8bfddbb9e63f47a5b1da9fd4f46a521e, 05/01/19 4337175060932118406
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_weather
    - chitchat: action_chitchat
* enter_data{"name": "Hanoi Vietnam"}
    - slot{"name": "Hanoi Vietnam"}
    - slot{"name": "Hanoi Vietnam"}
    - utter_not_sure   <!-- predicted: action_greet_user -->
    - utter_possibilities   <!-- predicted: action_greet_user -->
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - utter_explain_nlucore   <!-- predicted: utter_ask_name -->
* affirm
    - utter_explain_nlu   <!-- predicted: utter_great -->
    - utter_explain_core   <!-- predicted: utter_great -->
    - utter_tryout   <!-- predicted: utter_great -->


## Generated Story goal:chitchat, id:2721ae89d30d4c28964ac367c2e553ed, 12/15/18 -3646576092582365265
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_time
    - chitchat: action_chitchat
* ask_time
    - chitchat: action_chitchat
* source_code
    - utter_source_code   <!-- predicted: action_faqs -->
    - chitchat: utter_anything_else


## Generated Story goal:chitchat, id:912897e570334aa0bf5360977052e95b, 12/17/18 -1934419123625089053
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* greet
    - greet_success: action_greet_user
* ask_howdoing
    - chitchat: action_chitchat
* ask_whoisit
    - chitchat: action_chitchat
* enter_data
    - utter_possibilities   <!-- predicted: utter_not_sure -->
* deny
    - chitchat: utter_nohelp
* human_handoff
    - sales: utter_contact_email
* deny
    - utter_nohelp   <!-- predicted: utter_contact_email -->
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities


## Generated Story goal:1 step, id:e8fc2e0b2c374353a63da30fb64748f3, 05/01/19 -1435447685661180167
* get_started_step1
    - greet_success: action_greet_user
    - slot{"shown_privacy": true}
* nicetomeeyou
    - chitchat: action_chitchat
* how_to_get_started
    - onboarding: utter_getstarted
    - onboarding: utter_first_bot_with_rasa
* affirm
    - getstarted_1: action_set_onboarding
    - slot{"onboarding": true}
    - getstarted_1: utter_built_bot_before
* deny
    - getstarted_1: utter_explain_stack
    - getstarted_1: utter_stack_details
    - getstarted_1: utter_explain_nlucore
* ask_faq_differencecorenlu
    - faq: action_faqs
    - getstarted_1: utter_explain_nlucore
* enter_data
    - utter_tryout   <!-- predicted: utter_explain_nlu -->
* how_to_get_started{"product": "stack"}
    - slot{"product": "stack"}
    - slot{"product": "stack"}
    - getstarted_1_success: utter_quickstart
    - utter_anything_else   <!-- predicted: action_listen -->
* enter_data
    - chitchat: utter_not_sure
    - chitchat: utter_possibilities


