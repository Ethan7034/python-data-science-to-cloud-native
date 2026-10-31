# CPU ICPC Workshop — Python Prerequisite Check
# Python 基础能力检查

This check covers basic Python programming only. No C++, algorithms, data structures course, or competitive programming experience is required.

本练习只检查基础 Python 编程能力，不要求 C++、算法、数据结构课程或算法竞赛经验。

## Before you start / 开始前

- Suggested time: **30–45 minutes**. This is a suggestion, not a time limit.
  建议用时 **30–45 分钟**，不是强制计时限制。
- Write and debug the programs independently. You may consult Python documentation and your own notes. Do not copy another person's solution or use AI to generate or repair the solution.
  请独立编写和调试；可以查阅 Python 文档和自己的笔记，请勿复制他人答案或使用 AI 生成、修复答案。
- Use **Python 3.10**, the standard library, `input()` and `print()`. No third-party packages are needed. Functions and classes are not required.
  使用 **Python 3.10**、标准库、`input()` 和 `print()`，无需第三方包、函数或类。
- Upload **three files together**, with these exact names, at the top level of your submission:
  请一次提交以下三个文件，文件名须完全一致，放在提交的最外层：
  `q1_target.py`, `q2_practice.py`, `q3_supplies.py`.
- Each file is a separate program. The grader runs it afresh for every test case. Read one input instance, print its result, and exit. Do not ask for a file name or read from a file.
  每个文件都是独立程序，每个测试点会重新运行。只需读取一组输入、输出结果并结束，不要读取文件。
- Do not print input prompts, explanations, or debugging messages. For example, use `input()` rather than `input("Enter a number: ")`.
  不要输出输入提示、解释或调试信息，例如使用 `input()`，而不是带提示文字的 `input(...)`。
- All inputs satisfy the constraints below; you do not need to handle invalid input. Output is case-sensitive. The grader ignores differences in spaces, blank lines, and final newlines.
  输入保证符合约束，无需处理非法输入。输出区分大小写；评测忽略空格、空行和末尾换行差异。
- Partial credit is awarded per test. Feedback includes input, expected output, your output, and syntax/runtime errors. You may fix your code and resubmit before the deadline shown in Gradescope.
  每个测试点独立给分；反馈包含输入、预期输出、实际输出及语法或运行错误。可在 Gradescope 显示的截止时间前修改并重新提交。
- Per run: 3 seconds wall time and 256 MiB memory on Gradescope. Small, straightforward loops are sufficient.
  Gradescope 每次运行限制为 3 秒、256 MiB；直接使用简单循环即可完成。

## Q1. Practice Target / 练习目标（30 points）

Read a participant's display name, target number of practice minutes, and completed minutes. Print the name, the remaining minutes (never negative), and a status. If completed minutes are at least the target, print `DONE`; otherwise, print `KEEP GOING`.

读取参与者昵称、目标练习分钟数、已完成分钟数。输出昵称、还需练习的分钟数（不能为负数）及状态：已完成分钟数大于或等于目标时输出 `DONE`，否则输出 `KEEP GOING`。

**Input / 输入**

1. A display name, 1–40 characters, containing English letters and spaces. There are no leading or trailing spaces. Use the whole line as the name.
   昵称，1–40 个字符，仅包含英文字母和空格，无首尾空格，整行都是昵称。
2. An integer `target`, `1 <= target <= 180`.
3. An integer `completed`, `0 <= completed <= 240`.

**Output / 输出**

Print the name on the first line, remaining minutes on the second, and status on the third.
第一行输出昵称，第二行输出剩余分钟数，第三行输出状态。

**Example 1 / 示例 1**

Input:
```text
Alex Chen
60
25
```

Output:
```text
Alex Chen
35
KEEP GOING
```

**Example 2 / 示例 2**

Input:
```text
Bo
30
40
```

Output:
```text
Bo
0
DONE
```

**Use variables, integers, a string and an `if`/`else` statement.**
请使用变量、整数、字符串和 `if`/`else` 条件判断。

## Q2. Practice Log / 练习记录（35 points）

A participant records practice minutes for `n` days. The daily target is **30 minutes**. Store the minutes in a **list**. Use a loop to calculate the total practice time, the number of days meeting the target, and the additional minutes needed for each day. A day meeting or exceeding the target needs `0` additional minutes.

参与者记录了 `n` 天的练习时长，每天目标为 **30 分钟**。将时长存入**列表**，使用循环计算总时长、达标天数，以及每天还差多少分钟；达到或超过目标的天数记为 `0`。

**Input / 输入**

1. An integer `n`, `1 <= n <= 20`.
2. Exactly `n` space-separated integers, each between `0` and `180`, in day order.
   恰好 `n` 个空格分隔的整数，每个数在 `0` 到 `180` 之间，按天数顺序给出。

**Output / 输出**

1. Total practice minutes / 总练习分钟数。
2. Number of days with at least 30 minutes / 大于或等于 30 分钟的天数。
3. `n` space-separated remaining-minute values, in the original day order / 按原顺序输出每天还差的分钟数，以空格分隔。

**Example / 示例**

Input:
```text
5
0 15 30 45 29
```

Output:
```text
119
2
30 15 0 0 1
```

**Use a list and a loop. You do not need sorting, recursion or an algorithm library.**
请使用列表和循环，无需排序、递归或算法库。

## Q3. Supplies Counter / 物资汇总（35 points）

Read `n` delivery records. Each record contains an item name and a quantity. Use a **dictionary** to accumulate the total quantity of each item. Then answer `q` queries. Repeated records for the same item must be added together. For an item never delivered, output `0`. Answer queries in their input order, including repeated queries.

读取 `n` 条到货记录，每条记录包含物品名和数量。使用**字典**累计每种物品的总数量，然后回答 `q` 次查询。同名物品需要累加；从未到货的物品输出 `0`。按查询输入顺序回答，包括重复查询。

**Input / 输入**

1. An integer `n`, `1 <= n <= 20`.
2. The next `n` lines each contain `item quantity`. Item names contain 1–12 lowercase English letters with no spaces; quantities are integers between `1` and `20`.
   接下来 `n` 行，每行是 `物品名 数量`；物品名为 1–12 个小写英文字母，不含空格；数量为 `1` 到 `20` 的整数。
3. An integer `q`, `1 <= q <= 20`.
4. The next `q` lines each contain one item name under the same naming rules.
   接下来 `q` 行，每行一个物品名，规则同上。

**Output / 输出**

For each query, print the item's total quantity on its own line.
每个查询输出一行，为对应物品的累计数量。

**Example / 示例**

Input:
```text
4
pen 3
notebook 2
pen 4
cable 1
4
pen
sticker
notebook
pen
```

Output:
```text
7
0
2
7
```

**Use a dictionary and loops. You do not need sorting or advanced data structures.**
请使用字典和循环，无需排序或进阶数据结构。

## Submission checklist / 提交前检查

- All three files run with Python 3.10 and use the exact file names above.
  三个文件均可用 Python 3.10 运行，文件名正确。
- The examples match. Also try an exact target, a single day, and repeated/missing items.
  示例结果一致，并尝试目标恰好完成、只有一天、物品重复和不存在等情况。
- Q2 uses a list; Q3 uses a dictionary; both use loops.
  Q2 使用列表，Q3 使用字典，两题均使用循环。
- The programs contain your own work and no extra printed prompts.
  代码由本人完成，输出中没有多余提示信息。

The automatic score checks program behaviour. Staff may briefly inspect the code or ask you to explain a change to confirm the stated skills and independent work.
自动分数检查程序行为；工作人员可能简短查看代码或请你解释一个修改，以确认所列技能及独立完成情况。
