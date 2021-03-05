# 232.用栈实现队列
难度 简单 

完成日期 2021.3.5


## 1.题干
请你仅使用两个栈实现先入先出队列。队列应当支持一般队列的支持的所有操作（push、pop、peek、empty）：

实现 MyQueue 类：

void push(int x) 将元素 x 推到队列的末尾

int pop() 从队列的开头移除并返回元素

int peek() 返回队列开头的元素

boolean empty() 如果队列为空，返回 true ；否则，返回 false
 
## 2.说明
你只能使用标准的栈操作 —— 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。

你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。

## 3.进阶
你能否实现每个操作均摊时间复杂度为 O(1) 的队列？换句话说，执行 n 个操作的总时间复杂度为 O(n) ，即使其中一个操作可能花费较长时间。

## 4.示例
输入：

["MyQueue", "push", "push", "peek", "pop", "empty"]

[[], [1], [2], [], [], []]

输出：

[null, null, null, 1, 1, false]

解释：

MyQueue myQueue = new MyQueue();

myQueue.push(1); // queue is: [1]

myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)

myQueue.peek(); // return 1

myQueue.pop(); // return 1, queue is [2]

myQueue.empty(); // return false

## 5.提示
1 <= x <= 9

最多调用 100 次 push、pop、peek 和 empty

假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）

## 6.解题思路
将一个栈当作输入栈，用于压入push传入的数据；另一个栈当作输出栈，用于pop和peek操作。

每次pop或peek时，若输出栈为空则将输入栈的全部数据依次弹出并压入输出栈，这样输出栈从栈顶往栈底的顺序就是队列从队首往队尾的顺序。

### 复杂度分析
时间复杂度：push和empty为O(1)，pop和peek为均摊O(1)。对于每个元素，至多入栈和出栈各两次，故均摊复杂度为O(1)。

空间复杂度：O(n)。其中n是操作总数。对于有n次push操作的情况，队列中会有n个元素，故空间复杂度为O(n)。

