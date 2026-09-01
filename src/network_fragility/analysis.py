"""Dependency-light graph robustness functions for portfolio reproduction."""

from __future__ import annotations

from collections import deque

Graph = dict[str, dict[str, float]]


def largest_component_fraction(graph: Graph, removed: set[str] | None = None) -> float:
    removed = removed or set()
    active = set(graph) - removed
    if not active:
        return 0.0
    largest = 0
    unseen = set(active)
    while unseen:
        root = unseen.pop()
        queue = deque([root])
        size = 0
        while queue:
            node = queue.popleft()
            size += 1
            neighbours = set(graph[node]) & unseen & active
            unseen -= neighbours
            queue.extend(neighbours)
        largest = max(largest, size)
    return largest / len(active)


def participation_coefficient(graph: Graph, communities: dict[str, int], node: str) -> float:
    neighbours = graph[node]
    strength = sum(neighbours.values())
    if not strength:
        return 0.0
    by_community: dict[int, float] = {}
    for other, weight in neighbours.items():
        cid = communities[other]
        by_community[cid] = by_community.get(cid, 0.0) + weight
    return 1.0 - sum((value / strength) ** 2 for value in by_community.values())
