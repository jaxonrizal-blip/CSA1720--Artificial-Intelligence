:- dynamic fact/1.

% Facts
fact(sunshine).
fact(warm_weather).

% Rules
rule(go_outside) :-
    fact(sunshine),
    fact(warm_weather).

rule(good_day) :-
    fact(go_outside).

% Forward Chaining
forward :-
    rule(X),
    \+ fact(X),
    assertz(fact(X)),
    write('New fact: '), write(X), nl,
    forward.
forward :-
    write('Forward chaining completed.'), nl.