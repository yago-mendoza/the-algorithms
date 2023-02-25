def check_near_array_convergence_v1 (arr):
    if len(set(arr)) == 1:
        return arr.pop()
    set_a = set([(arr[0]+1)%10, arr[0], (arr[0]-1)%10])
    set_b = set()
    for x in arr[1:] :
        set_b.update({(x+1)%10,x,(x-1)%10})
        if len(set_a & set_b)==0:
            return -1
        else:
            set_a = set_a & set_b
            set_b = set()
    return set_a.pop()

def check_near_array_convergence_v2 (arr, pick_max_when_only_two = False):
    clock_down = [(x - 1) % 10 for x in arr]
    shortest_path = abs(max(clock_down)-min(clock_down))
    if min(shortest_path, 10-shortest_path) <= 3:
        if len(set(clock_down)) in (1,2):
            return (max(arr) if pick_max_when_only_two else min(arr)) % 10
        elif len(set(clock_down)) == 3:
            clock_up = [(x + 1) % 10 for x in arr]
            intersect = set(clock_up) & set(clock_down)
            if len(intersect) == 1:
                return intersect.pop()
            return -1
    return -1

########################################################################################################

arrs = [[7,5,5,0,5],[6,5,7,6,5],[1,0,2,0,1,9],[0,9,8,9,0],[0,9,0,0],[0,1,2],[0],[9],[9,9,9,9,9],[7,6,7,6],[6,7,6,7]]

