class KthLargest:
    def __init__(self, k, streamNum):
        self.k = k
        self.streamNum = streamNum
    
    def findKLargest(self):
        self.streamNum.sort()
        print(self.streamNum[-self.k])
        

kthLargest = KthLargest(3, [1,5,3,1,4])
kthLargest.findKLargest()