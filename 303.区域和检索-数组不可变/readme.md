# 303. 区域和检索-数组不可变
难度 简单 

完成日期 2021.3.1

## 1.题干
给定一个整数数组  nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点。

实现 NumArray 类：

NumArray(int[] nums) 使用数组 nums 初始化对象

int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）

## 2.示例

NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);

numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)

numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1)) 

numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))

## 3.提示

0 <= nums.length <= 104

-105 <= nums[i] <= 105

0 <= i <= j < nums.length

最多调用 104 次 sumRange 方法

## 4.解题思路 
### 方法名 前缀和

最朴素的想法是存储数组 nums 的值，每次调用 sumRange 时，通过循环的方法计算数组 nums 从下标 i 到下标 j 范围内的元素和，需要计算 j−i+1 个元素的和。由于每次检索的时间和检索的下标范围有关，因此检索的时间复杂度较高，如果检索次数较多，则会超出时间限制。

由于会进行多次检索，即多次调用 sumRange，因此为了降低检索的总时间，应该降低 sumRange 的时间复杂度，最理想的情况是时间复杂度 O(1)。为了将检索的时间复杂度降到 O(1)，需要在初始化的时候进行预处理。

要计算 sumRange(i,j)，则需要计算数组 nums 在下标 j 和下标 i−1 的前缀和，然后计算两个前缀和的差。

如果可以在初始化的时候计算出数组 nums 在每个下标处的前缀和，即可满足每次调用 sumRange 的时间复杂度都是 O(1)。

具体实现方面，假设数组 nums 的长度为 n，创建长度为 n+1 的前缀和数组 sums，对于 0≤i<n 都有 sums[i+1]=sums[i]+nums[i]，则当0<i≤n 时，sums[i] 表示数组 nums 从下标 0 到下标 i-1 的前缀和。

将前缀和数组 sums 的长度设为 n+1 的目的是为了方便计算 sumRange(i,j)，不需要对 i=0 的情况特殊处理。此时有：

sumRange(i,j)=sums[j+1]−sums[i]

### 复杂度分析 
时间复杂度：初始化 O(n)，每次检索 O(1)，其中 n 是数组 nums 的长度。
初始化需要遍历数组 nums 计算前缀和，时间复杂度是 O(n)。
每次检索只需要得到两个下标处的前缀和，然后计算差值，时间复杂度是 O(1)。

空间复杂度：O(n)，其中 n 是数组 nums 的长度。需要创建一个长度为 n+1 的前缀和数组。



