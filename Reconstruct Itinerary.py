class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        destinations = {}
        n = len(tickets)

        def exploreNode(airport, visited, path):
            for destination in destinations[airport]:
                dest, ticket_id = destination
                if ticket_id not in visited:
                    visited.add(ticket_id)
                    path.append(dest)

                    if len(path) - 1 == n:
                        return path

                    childPath = exploreNode(dest, visited, path)
                    if childPath is not None:
                        return childPath

                    visited.remove(ticket_id)
                    path.pop()

            return None

        for i, ticket in enumerate(tickets):
            fro, to = ticket
            if fro not in destinations:
                destinations[fro] = [(to, i)]
            else:
                destinations[fro].append((to, i))

            if to not in destinations:
                destinations[to] = []

        for k in destinations.keys():
            destinations[k].sort()

        return exploreNode("JFK", set(), ["JFK"])
