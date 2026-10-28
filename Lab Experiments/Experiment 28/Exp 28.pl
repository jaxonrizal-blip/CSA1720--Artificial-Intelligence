% Symptoms
symptom(john, fever).
symptom(john, cough).
symptom(john, headache).

symptom(alice, sneezing).
symptom(alice, runny_nose).

% Diagnosis rules
disease(Person, flu) :-
    symptom(Person, fever),
    symptom(Person, cough),
    symptom(Person, headache).

disease(Person, common_cold) :-
    symptom(Person, sneezing),
    symptom(Person, runny_nose).
