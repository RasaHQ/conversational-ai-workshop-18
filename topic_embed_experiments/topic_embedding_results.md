## Results

### Merged topics (for all unhappy paths)
For the paperbot we merged the chitchat, explain, correct and didthatwork topics into one topic.
Topic prediction accuracy is 1.0 for this task on training and held out testing data. 

Action prediction evaluation for topic embedding model on paperbot stories with merged topics:
![Pic1](merged_topics.png?raw=true "Merged topics prediction performance")

Action prediction evaluation for topic embedding model on paperbot stories with distinct topics:
![Pic2](model_comparison_topic_switch.png?raw=true  "Seperate topics prediction performance")

Results are similar and we can conclude that for the paperbot it does not matter 
too much if we treat all unhappy paths with the same or seperate topics. 

### Train topic embedding policy on demo-bot stories

Evaluation of topic prediction on training data:
    
    Evaluation Results on CONVERSATION level:
        Correct:          4601 / 4636
        F1-Score:         0.996
        Precision:        1.000
        Accuracy:         0.992
        In-data fraction: 0
    Evaluation Results on ACTION level:
        Correct:          89529 / 89578
        F1-Score:         0.999
        Precision:        0.999
        Accuracy:         0.999
        In-data fraction: 0
    Comments: better than expected for those stories, need carelfully designed topic assignemnts
Evaluation of topic prediction on testing data:
   
    Evaluation Results on CONVERSATION level:
        Correct:          64 / 313
        F1-Score:         0.340
        Precision:        1.000
        Accuracy:         0.204
        In-data fraction: 0
    Evaluation Results on ACTION level:
        Correct:          6648 / 9947
        F1-Score:         0.619
        Precision:        0.612
        Accuracy:         0.668
        In-data fraction: 0
    Comments: results are not conclusive since train and test data are differently generated;
            Mistakes in topic prediction can be devided into three bins: 
            1. fail flag didn't exist in training data
            2. understandable mistakes
            3. messy mistakes
            Accuracy is not good, but still better than excpected on those stories

Evaluation of action prediction on training data:

    Evaluation Results on CONVERSATION level:
        Correct:          4369 / 4636
        F1-Score:         0.970
        Precision:        1.000
        Accuracy:         0.942
        In-data fraction: 0
    Evaluation Results on ACTION level:
        Correct:          89307 / 89578
        F1-Score:         0.996
        Precision:        0.995
        Accuracy:         0.997
        In-data fraction: 0
    Comments: common mistakes are: utter_tensorflow for utter_spacy_or_tensorflow, not predicting fallback,
            utter_nlu_intent_tutorial for utter_nlu_entity_tutorial
            (see failed_stories for more insight)
            
Evaluation of action prediction on testing data:

    Evaluation Results on CONVERSATION level:
        Correct:          18 / 313
        F1-Score:         0.109
        Precision:        1.000
        Accuracy:         0.058
        In-data fraction: 0
    Evaluation Results on ACTION level:
        Correct:          6101 / 9947
        F1-Score:         0.593
        Precision:        0.617
        Accuracy:         0.613
        In-data fraction: 0
    Comments: does not predict fallback, good on predicting correct actions after fail, 
            results are in fact much better than numbers suggest; 
            (see failed_stories for more insight)
            most mistakes are due to incompatibility of training and test data
            