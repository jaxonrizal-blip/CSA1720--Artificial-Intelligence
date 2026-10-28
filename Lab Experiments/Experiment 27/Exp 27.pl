% Graph connections
edge(a, b, 4).
edge(a, c, 2).
edge(b, d, 5).
edge(b, e, 1).
edge(c, f, 3).
edge(c, g, 6).

% Heuristic values
h(a, 7).
h(b, 4).
h(c, 2).
h(d, 5).
h(e, 1).
h(f, 3).
h(g, 0).

% Best First Search
bestfirst(Start, Goal, Path) :-
    search([[Start]], Goal, RevPath),
    reverse(RevPath, Path).

search([[Goal|Path]|_], Goal, [Goal|Path]).

search([[Node|Path]|Rest], Goal, Solution) :-
    findall([Next,Node|Path],
            (edge(Node, Next, _),
             \+ member(Next, [Node|Path])),
            Children),
    append(Rest, Children, NewQueue),
    sort_queue(NewQueue, SortedQueue),
    search(SortedQueue, Goal, Solution).

sort_queue([], []).
sort_queue(Paths, Sorted) :-
    predsort(compare_paths, Paths, Sorted).

compare_paths(Order, [A|_], [B|_]) :-
    h(A, HA),
    h(B, HB),
    compare(Order, HA, HB).