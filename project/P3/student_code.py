import math

def euclid_dist(p1, p2):
    """
    Calculate euclidean distance between 2 points
    """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def print_vars(frontier,travelled,routes,f,g,h):
    """
    Helper function to print out all variables
    """
    print('frontier:',frontier)
    print('travelled:',travelled)
    print('routes:',routes)
    print('Cost f:',f)
    print('Cost g:',g)
    print('Cost h:',h)
    return 0

def shortest_path(M, start, end):
    """
    ## Input
        M : the map
        start : node where we start
        end : node where we want to go
    ## Output
        route : array of traversed nodes

    ## A* algorithm in a nutshell -> minimize f(x)
        f = g + h
        g : distance to next point
        h : distance from next point to destination    
    """
    
    # initialize variables for nodes
    frontier = [] # nodes we can go to
    travelled = [] # nodes we've covered
    routes = {} # maintain routes
    
    # initialize variables for cost
    f = {}
    g = {}
    h = {}
 
    frontier.append(start)
    g[start] = 0
    h[start] = euclid_dist(M.intersections[start], M.intersections[end])
    f[start] = g[start] + h[start]
    
    while len(frontier) > 0: # we loop until a solution is found
#         print_vars(frontier,travelled,routes,f,g,h)
        # derive a subset of node from f-cost dictionary, and find lowest cost to determine next node
        tmp_dict = dict((node, f[node]) for node in frontier if node in f)
        curr_node = min(tmp_dict, key=tmp_dict.get)
        
        # when arrived, backtrace the path
        if curr_node == end:
            route_taken = []
            route_taken.append(end)
            next = end
            while next != start:
                next = routes[next]
                route_taken.append(next)
            route_taken.reverse()
            return route_taken
        
        # move current to visited list
        frontier.remove(curr_node)
        travelled.append(curr_node)
        
        # evaluate next nodes in the frontier, excluding ones that we've already covered
        for node in list(set(M.roads[curr_node]) - set(travelled)):
            curr_node_coor = M.intersections[curr_node]
            next_node_coor = M.intersections[node]
            
            # check if this city would be an improvement (curr_node cost + cost to get to next node)
            next_node_cost = g[curr_node] + euclid_dist(curr_node_coor, next_node_coor)
            
            # if cost of going to node against other routes to the same node.
            if node in g:
                if (next_node_cost >= g[node]):
                    continue
                    
            # add node to frontier list
            frontier.append(node)
                
            # since node is not in frontier list
            g[node] = next_node_cost
            h[node] = euclid_dist(M.intersections[node], M.intersections[end]) 
            f[node] = g[node] + h[node] 
            routes[node] = curr_node
            
    return 0
