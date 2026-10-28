% Facts about birds

bird(sparrow).
bird(parrot).
bird(pigeon).
bird(ostrich).
bird(penguin).

% Birds that can fly

can_fly(sparrow).
can_fly(parrot).
can_fly(pigeon).

% Rule to check whether a bird can fly

cannot_fly(Bird) :-
    bird(Bird),
    \+ can_fly(Bird).