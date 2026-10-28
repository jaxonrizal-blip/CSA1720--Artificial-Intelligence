% Facts
parent(john, david).
parent(john, mary).
parent(mary, alice).
parent(david, peter).
parent(susan, david).
parent(susan, mary).

% Rules
father(X, Y) :-
    parent(X, Y),
    male(X).

mother(X, Y) :-
    parent(X, Y),
    female(X).

% Gender facts
male(john).
male(david).
male(peter).

female(susan).
female(mary).
female(alice).

% Grandparent rule
grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

% Sibling rule
sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.