class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        departures = set()
        arrivals = set()

        for path in paths:
            departures.add(path[0])
            arrivals.add(path[1])

        return arrivals.difference(departures).pop()

        