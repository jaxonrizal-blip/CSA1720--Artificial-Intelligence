% Initial state: monkey at door, box at window, monkey on floor
initial_state(at(door), at(window), on_floor, has_not).

% Monkey moves to the box
move(state(at(X), at(X), on_floor, has_not),
     state(at(X), at(X), on_box, has_not),
     climb).

% Monkey pushes the box
move(state(at(_), at(Y), on_floor, has_not),
     state(at(Y), at(Y), on_floor, has_not),
     push_box).

% Monkey climbs down
move(state(at(X), at(X), on_box, has_not),
     state(at(X), at(X), on_floor, has_not),
     climb_down).

% Monkey gets the banana
move(state(at(middle), at(middle), on_box, has_not),
     state(at(middle), at(middle), on_box, has),
     grasp).

% Goal state
goal(state(_, _, _, has)).