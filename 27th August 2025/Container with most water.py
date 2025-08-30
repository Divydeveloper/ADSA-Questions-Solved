h=eval(input("Enter Height"))
n=len(h)
left=0
right=n-1
max_area=0
while left <right:
    width=right-left
    min_height=min(h[left], h[right])
    max_area= max(max_area, width*min_height)
    if h[left]<h[right]:
        left+=1
    else:
        right-=1
print(max_area)
