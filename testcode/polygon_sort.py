'''
多边形点集排序
    已知多边形点集C={P1,P2,...,PN}，其排列顺序是杂乱，依次连接这N个点
    无法形成确定的多边形，需要对点集C进行排序后，再绘制多边形。
    定义：点A在点B的逆时针方向，则点A大于点B
        1.计算点集的重心O，以重心作为逆时针旋转的中心点。
        2.计算点之间的大小关系。

'''
from typing import List
class Solution:
    def polygon_sort(self, points: List[int]) -> List[int]:
        #求多边形重心
        x = 0
        y = 0
        for each in points:
            x += each[0]
            y += each[1]
        x /= len(points)
        y /= len(points)
        
        #向量积比较 插入排序：
        #lambda x1,y1,x2,y2 : x1*y2 - x2*y1
        for i in range(1,len(points)):
            tmp = points[i]
            j = i-1
            while(  j>=0 and ((points[j][0]-x)*(tmp[1]-y)- (tmp[0]-x)*(points[j][1]-y)) <0  ):
                points[j+1] = points[j]
                j -= 1 
            points[j+1] = tmp
        return points

C = [[1,2], [8,6], [2,7], [5,1]] 
sol = Solution()
print(sol.polygon_sort(C))