 **0/1 Knapsack using Dynamic Programming**

**1. Objective**

To develop a Python-based 0/1 Knapsack program using the Dynamic Programming technique and analyze its time and space complexity.

**2. Input**

The program accepts:

Number of items

Weight of each item

Value of each item

Maximum capacity of the knapsack

**3. Output**

The program displays:

Weights of the items

Values of the items

Maximum capacity of the knapsack

Maximum value that can be obtained

Selected items

Time complexity

Space complexity

**4. Algorithm**

Start.

Read the number of items.

Read the weight of each item.

Read the value of each item.

Read the maximum capacity of the knapsack.

Create a Dynamic Programming table dp.

Initialize the table with 0.

For each item:


Check whether the item can be included in the knapsack.

If the item weight is less than or equal to the current capacity:

Calculate the maximum of:

Including the current item

Excluding the current item

Otherwise, do not include the item.

The recurrence relation is:

dp[i][w] = max(dp[i-1][w], value[i-1] + dp[i-1][w-weight[i-1]])

The last cell of the DP table gives the maximum value that can be obtained.

Display the maximum value.

**5.Time Complexity:**

O(n × W)

Where n is the number of items and W is the maximum capacity of the knapsack.

**Space Complexity:**

O(n × W)

Stop.
