Approach #1: Brute Force [Accepted]

Intuition

    When booking a new event [start, end), check if every current event conflicts with the new event. If none of them do, we can book the event.

Algorithm

    We will maintain a list of interval events (not necessarily sorted). Evidently, two events [s1, e1) and [s2, e2) do not conflict if and only if one of them starts after the other one ends: either e1 <= s2 OR e2 <= s1. By De Morgan's laws, this means the events conflict when s1 < e2 AND s2 < e1.

