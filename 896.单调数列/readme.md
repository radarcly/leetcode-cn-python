# 896. 单调数列
难度 简单

完成日期 2021.2.28

## 1.题干
如果数组是单调递增或单调递减的，那么它是单调的。

如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。

当给定的数组 A 是单调数组时返回 true，否则返回 false。

## 2.示例
### 示例1
输入：[1,2,2,3]

输出：true

### 示例2

输入：[6,5,4,4]

输出：true

### 示例3

输入：[1,3,2]

输出：false

### 示例4

输入：[1,2,4,5]

输出：true

### 示例5

输入：[1,1,1]

输出：true

## 3.提示
1 <= A.length <= 50000

-100000 <= A[i] <= 100000

## 4.解题思路
遍历数组 A，若既遇到了A[i]>A[i+1] 又遇到了 A[i']<A[i'+1]，则说明 A 既不是单调递增的，也不是单调递减的。

### 思路一
具体代码实现时设定一个数组递增的标识和数组递减的标识，一旦出现递增则说明递减标识为False，
反之出现递减则代表递增标识为False，最终返回 递增标识 || 递减

### 思路二
根据头尾判定是递增还是递减（尾比头大为递增，反之相反） 然后开启遍历，遇到不满足条件直接return

