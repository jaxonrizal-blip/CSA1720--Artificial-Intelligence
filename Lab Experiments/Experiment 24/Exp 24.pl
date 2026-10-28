% Diet Suggestion System Based on Disease

diet(diabetes, 'Low sugar and high fiber foods').
diet(obesity, 'Low calorie foods and vegetables').
diet(anemia, 'Iron-rich foods like spinach and beans').
diet(hypertension, 'Low salt foods and fruits').
diet(heart_disease, 'Low fat foods and whole grains').

% Rule to suggest diet
suggest_diet(Disease, Diet) :-
    diet(Disease, Diet).