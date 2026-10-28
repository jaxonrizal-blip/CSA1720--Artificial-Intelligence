% Facts
fact(sunshine).
fact(warm_weather).

% Rules
good_day :-
    sunshine,
    warm_weather.

go_outside :-
    good_day.

sunshine :-
    fact(sunshine).

warm_weather :-
    fact(warm_weather).