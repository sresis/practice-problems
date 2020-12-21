def Helper(start, end, connections, routes, curr, weight):  """Get possible routes and add to routes dict."""
  # if start and end are the same, add to routes
  if start == end:
    routes[curr+start] = weight
  # otherwise, iterate through possible connections
  else:
    for connection in connections:
      if start in connection:
        temp = connection[:]
        temp.remove(start)
        curr_weight = weight + int(temp[1])
        # remove this connection from considered list
        new_connections = connections[:]
        new_connections.remove(connection)
        # use updated vals in recursive call
        Helper(temp[0], end, new_connections, routes, curr+start+'-', curr_weight)

  return 

def WeightedPath(strArr):

  node_count = int(strArr[0])
  
  # get the nodes
  all_nodes = strArr[1:node_count+1]
  start = all_nodes[0]
  end = all_nodes[-1]
  # seperate the weighted strings into relevant components
  connections = [item.split('|') for item in strArr[node_count+1:]]
  # store possible routes 
  routes = {}
  # helper function to get all of the possible routes
  Helper(start, end, connections, routes, curr='', weight=0)
  if routes:
    # get the min value from routes
    val = list(routes.values())
    key = list(routes.keys())
    return key[val.index(min(val))]
  else:
    return -1


# keep this function call here 
print(WeightedPath(input()))