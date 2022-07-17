import heapq

H = [21, 1, 45, 78, 3, 5]

# Use heapify to rearrange the elements
heapq.heapify(H)
print(H)

# tambah element
heapq.heappush(H, 99)
print(H)

# kurangi element
heapq.heappop(H)
heapq.heappop(H)
heapq.heapreplace(H, 1009)
print(H)
