# C++ STL (Standard Template Library) - Complete Notes

---

## What is C++ STL?

- C++ is one of the most popular high-level programming languages which is used extensively for a long time by developers
  and has always been loved by all programmers, especially competitive programmers because of its faster execution time.

- STL is one of the unique abilities of C++ which makes it stand out from every other programming language.
  STL stands for **Standard Template Library** which contains a lot of pre-defined templates in terms of containers and
  classes which makes it very easy for developers or programmers to implement different data structures easily without
  having to write complete code and worry about space-time complexities.

- STL is divided into 4 parts:
  1. Algorithms
  2. Containers
  3. Functions
  4. Iterators

- To learn containers, first we need to learn **Pairs**.

---

## What is Pair?

- Pair is a part of the **utility library**.
- It is used when we have to store a couple of values in 1 variable.
- The indexing in pair starts from **first** (not 0).
- Pair can be treated as a datatype but it generally lies inside the utility library.

**Syntax:**
```cpp
pair<datatype, datatype> variable_name = {value, value};
```

**Example:**
```cpp
pair<int, int> p = {1, 3};
cout << p.first << " " << p.second;  // Output: 1 3
```

**Accessing values in pair:**
```cpp
variable_name.first   // accesses first element
variable_name.second  // accesses second element
```

- We can use the **nested property** of pair to store more than 2 values in a single variable.

**Syntax for nested pair:**
```cpp
pair<datatype, pair<datatype, datatype>> variable_name = {value, {value, value}};
```

**Example:**
```cpp
pair<int, pair<int, int>> p = {1, {2, 3}};
cout << p.first << " " << p.second.first << " " << p.second.second;
// Output: 1 2 3
```

**Accessing values in nested pair:**
```cpp
variable_name.first              // first value
variable_name.second.first       // second value
variable_name.second.second      // third value
```

- We can also declare an **array of pairs**.

**Syntax:**
```cpp
pair<datatype, datatype> arr[] = {{value, value}, {value, value}};
```

**Example:**
```cpp
pair<int, int> arr[] = {{1, 2}, {3, 4}, {5, 6}};
cout << arr[0].first << " " << arr[0].second;  // Output: 1 2
cout << arr[1].first << " " << arr[1].second;  // Output: 3 4
```

- The indexing is the same as for arrays. To access values: `arr[index].first` or `arr[index].second`.

---

## Containers

Containers are data structures provided by STL to store and organize data.

---

### 1. Vectors

- Vectors are **dynamic arrays** — they can resize themselves automatically when elements are inserted or deleted.
- They are the most commonly used container in STL.

**Syntax to declare a vector:**
```cpp
vector<datatype> variable_name;
```

**Example:**
```cpp
vector<int> v;
```

- We can also define a **vector of pairs**:
```cpp
vector<pair<datatype, datatype>> variable_name;
```

**Example:**
```cpp
vector<pair<int, int>> vp;
```

#### Functions in Vector:

**1. push_back(value)**
- Adds an element at the end of the vector.
- Time Complexity: **O(1)** amortized
```cpp
v.push_back(1);
v.push_back(2);
// v = {1, 2}
```

**2. emplace_back(value)**
- Similar to push_back but **faster** because it constructs the element in-place (avoids extra copy).
- Preferred over push_back for performance.
- Time Complexity: **O(1)** amortized
```cpp
v.emplace_back(4);
// v = {1, 2, 4}
```

**3. Initializing a vector with a size and default value:**
```cpp
vector<int> v(5, 100);
// v = {100, 100, 100, 100, 100}
```

**4. Copying a vector:**
```cpp
vector<int> v1(5, 20);
vector<int> v2(v1);   // v2 is a copy of v1
```

**5. Iterating through a vector:**
```cpp
// Using index
for (int i = 0; i < v.size(); i++) {
    cout << v[i] << " ";
}

// Using iterator
for (vector<int>::iterator it = v.begin(); it != v.end(); it++) {
    cout << *it << " ";
}

// Using auto (shorthand for iterator)
for (auto it = v.begin(); it != v.end(); it++) {
    cout << *it << " ";
}

// Range-based for loop (simplest)
for (auto x : v) {
    cout << x << " ";
}
```

**6. begin() and end():**
- `v.begin()` → returns iterator pointing to the **first element**
- `v.end()` → returns iterator pointing to **one position after the last element**

**7. rbegin() and rend():**
- `v.rbegin()` → iterator pointing to the **last element** (reverse begin)
- `v.rend()` → iterator pointing to **one before the first element** (reverse end)

**8. back() and front():**
```cpp
v.front();  // returns first element,  O(1)
v.back();   // returns last element,   O(1)
```

**9. pop_back():**
- Removes the last element.
- Time Complexity: **O(1)**
```cpp
v.pop_back();
```

**10. size():**
- Returns the number of elements in the vector.
```cpp
v.size();  // O(1)
```

**11. empty():**
- Returns `true` if the vector is empty, `false` otherwise.
```cpp
v.empty();  // O(1)
```

**12. clear():**
- Removes all elements from the vector.
```cpp
v.clear();  // O(n)
```

**13. insert(position, value):**
- Inserts an element at a given position.
- Time Complexity: **O(n)** (because elements need to be shifted)
```cpp
v.insert(v.begin(), 10);       // insert 10 at beginning
v.insert(v.begin() + 1, 20);  // insert 20 at index 1
```

**14. erase(position):**
- Removes an element at a given position.
- Time Complexity: **O(n)**
```cpp
v.erase(v.begin());        // removes first element
v.erase(v.begin() + 1);   // removes element at index 1
```

- We can also erase a **range** of elements:
```cpp
v.erase(v.begin(), v.begin() + 3);  // removes first 3 elements
```

**Time Complexity Summary for Vector:**

| Operation            | Time Complexity |
|----------------------|-----------------|
| Access by index      | O(1)            |
| push_back / emplace_back | O(1) amortized |
| pop_back             | O(1)            |
| insert (middle)      | O(n)            |
| erase (middle)       | O(n)            |
| size / empty         | O(1)            |

---

### 2. List (Doubly Linked List)

- Internally implemented as a **doubly linked list**.
- Allows fast insertions and deletions at both ends and even in the middle (if you have an iterator).
- Does **not** support random access (no `[]` operator).

**Syntax:**
```cpp
list<datatype> variable_name;
```

**Example:**
```cpp
list<int> ls;
```

#### Functions in List:

**1. push_back(value)** — adds at end
```cpp
ls.push_back(2);
ls.push_back(3);
```

**2. push_front(value)** — adds at front
```cpp
ls.push_front(1);
// ls = {1, 2, 3}
```

**3. pop_back()** — removes from end, O(1)
```cpp
ls.pop_back();
```

**4. pop_front()** — removes from front, O(1)
```cpp
ls.pop_front();
```

**5. front() and back():**
```cpp
ls.front();  // first element
ls.back();   // last element
```

**6. Iterating through a list:**
```cpp
for (auto x : ls) {
    cout << x << " ";
}
```

**7. insert(position, value):**
- Insert at a specific iterator position, O(1) if iterator is known.
```cpp
auto it = ls.begin();
it++;
ls.insert(it, 10);  // insert 10 at second position
```

**8. erase(position):**
```cpp
auto it = ls.begin();
ls.erase(it);  // erase first element
```

**9. size() and empty():**
```cpp
ls.size();
ls.empty();
```

**Time Complexity Summary for List:**

| Operation              | Time Complexity |
|------------------------|-----------------|
| push_front / push_back | O(1)            |
| pop_front / pop_back   | O(1)            |
| insert (at iterator)   | O(1)            |
| erase (at iterator)    | O(1)            |
| Search                 | O(n)            |
| Random access          | ❌ Not supported |

---

### 3. Deque (Double-Ended Queue)

- Deque stands for **Double-Ended Queue**.
- Similar to vector but supports **fast insert and delete at both front and back**.
- Supports **random access** (like vector).

**Syntax:**
```cpp
deque<datatype> variable_name;
```

**Example:**
```cpp
deque<int> dq;
```

#### Functions in Deque:

**1. push_back(value)** — adds at end, O(1)
```cpp
dq.push_back(1);
```

**2. push_front(value)** — adds at front, O(1)
```cpp
dq.push_front(0);
// dq = {0, 1}
```

**3. pop_back()** — removes from end, O(1)
```cpp
dq.pop_back();
```

**4. pop_front()** — removes from front, O(1)
```cpp
dq.pop_front();
```

**5. Random access:**
```cpp
dq[0];   // first element, O(1)
dq[1];   // second element, O(1)
```

**6. front() and back():**
```cpp
dq.front();
dq.back();
```

**Time Complexity Summary for Deque:**

| Operation              | Time Complexity |
|------------------------|-----------------|
| push_front / push_back | O(1)            |
| pop_front / pop_back   | O(1)            |
| Random access []       | O(1)            |
| Insert (middle)        | O(n)            |

---

### 4. Stack

- Stack follows the **LIFO (Last In First Out)** principle.
- Internally uses **deque** by default.
- Think of it like a stack of plates — you add and remove from the top only.

**Syntax:**
```cpp
stack<datatype> variable_name;
```

**Example:**
```cpp
stack<int> st;
```

#### Functions in Stack:

**1. push(value)** — adds element on top, O(1)
```cpp
st.push(1);
st.push(2);
st.push(3);
// top → 3, 2, 1
```

**2. top()** — returns the top element without removing, O(1)
```cpp
cout << st.top();  // Output: 3
```

**3. pop()** — removes the top element, O(1)
```cpp
st.pop();
// top → 2, 1
```

**4. size()** — returns number of elements, O(1)
```cpp
st.size();
```

**5. empty()** — returns true if stack is empty, O(1)
```cpp
st.empty();
```

> ⚠️ Note: Stack does **not** support iteration or random access. You can only access the top element.

**Time Complexity Summary for Stack:**

| Operation | Time Complexity |
|-----------|-----------------|
| push      | O(1)            |
| pop       | O(1)            |
| top       | O(1)            |
| size      | O(1)            |
| empty     | O(1)            |

---

### 5. Queue

- Queue follows the **FIFO (First In First Out)** principle.
- Internally uses **deque** by default.
- Think of it like a line at a ticket counter — first person in is first to be served.

**Syntax:**
```cpp
queue<datatype> variable_name;
```

**Example:**
```cpp
queue<int> q;
```

#### Functions in Queue:

**1. push(value)** — adds element at the back (rear), O(1)
```cpp
q.push(1);
q.push(2);
q.push(3);
// front → 1, 2, 3 ← back
```

**2. front()** — returns the front element without removing, O(1)
```cpp
cout << q.front();  // Output: 1
```

**3. back()** — returns the rear element without removing, O(1)
```cpp
cout << q.back();  // Output: 3
```

**4. pop()** — removes the front element, O(1)
```cpp
q.pop();
// front → 2, 3 ← back
```

**5. size() and empty():**
```cpp
q.size();
q.empty();
```

**Time Complexity Summary for Queue:**

| Operation | Time Complexity |
|-----------|-----------------|
| push      | O(1)            |
| pop       | O(1)            |
| front     | O(1)            |
| back      | O(1)            |

---

### 6. Priority Queue

- Priority Queue is a container where the **element with highest priority is served first**.
- By default, it is a **Max-Heap** (largest element is at the top).
- Internally implemented using a **heap** data structure.

**Syntax (Max-Heap — default):**
```cpp
priority_queue<datatype> variable_name;
```

**Syntax (Min-Heap):**
```cpp
priority_queue<datatype, vector<datatype>, greater<datatype>> variable_name;
```

**Example (Max-Heap):**
```cpp
priority_queue<int> pq;
pq.push(3);
pq.push(1);
pq.push(5);
pq.push(2);
// internal order (max-heap): top = 5
```

#### Functions in Priority Queue:

**1. push(value)** — adds element and maintains heap order, O(log n)
```cpp
pq.push(5);
```

**2. top()** — returns the highest priority (largest in max-heap) element, O(1)
```cpp
cout << pq.top();  // Output: 5
```

**3. pop()** — removes the top element, O(log n)
```cpp
pq.pop();
// now top = 3
```

**4. size() and empty():**
```cpp
pq.size();
pq.empty();
```

**Example (Min-Heap):**
```cpp
priority_queue<int, vector<int>, greater<int>> minpq;
minpq.push(3);
minpq.push(1);
minpq.push(5);
cout << minpq.top();  // Output: 1 (minimum element)
```

**Time Complexity Summary for Priority Queue:**

| Operation | Time Complexity |
|-----------|-----------------|
| push      | O(log n)        |
| pop       | O(log n)        |
| top       | O(1)            |

---

### 7. Set

- Set stores **unique elements only** (no duplicates allowed).
- Elements are stored in **sorted order** (ascending by default).
- Internally implemented as a **Red-Black Tree (BST)**.

**Syntax:**
```cpp
set<datatype> variable_name;
```

**Example:**
```cpp
set<int> s;
s.insert(3);
s.insert(1);
s.insert(2);
s.insert(1);  // duplicate, will be ignored
// s = {1, 2, 3}  (sorted, unique)
```

#### Functions in Set:

**1. insert(value)** — inserts element (ignored if already present), O(log n)
```cpp
s.insert(5);
```

**2. find(value)** — returns iterator to the element if found, else returns `s.end()`, O(log n)
```cpp
auto it = s.find(3);
if (it != s.end()) {
    cout << "Found: " << *it;
}
```

**3. count(value)** — returns 1 if element exists, 0 otherwise, O(log n)
```cpp
s.count(3);  // returns 1 (exists)
s.count(7);  // returns 0 (not found)
```

**4. erase(value)** — removes element, O(log n)
```cpp
s.erase(3);
```

**5. size() and empty():**
```cpp
s.size();
s.empty();
```

**6. begin() and end():**
```cpp
// s.begin() → smallest element
// s.end()   → one past largest
```

**7. lower_bound(value)** — returns iterator to first element **>= value**, O(log n)
```cpp
auto it = s.lower_bound(2);  // points to first element >= 2
```

**8. upper_bound(value)** — returns iterator to first element **> value**, O(log n)
```cpp
auto it = s.upper_bound(2);  // points to first element > 2
```

**9. Iterating through a set:**
```cpp
for (auto x : s) {
    cout << x << " ";  // prints in sorted order
}
```

**Time Complexity Summary for Set:**

| Operation    | Time Complexity |
|--------------|-----------------|
| insert       | O(log n)        |
| find         | O(log n)        |
| erase        | O(log n)        |
| lower_bound  | O(log n)        |
| upper_bound  | O(log n)        |

---

### 8. Multiset

- Similar to set, but **allows duplicate elements**.
- Elements are still stored in **sorted order**.
- Internally implemented as a **Red-Black Tree**.

**Syntax:**
```cpp
multiset<datatype> variable_name;
```

**Example:**
```cpp
multiset<int> ms;
ms.insert(1);
ms.insert(1);
ms.insert(2);
ms.insert(3);
// ms = {1, 1, 2, 3}
```

#### Functions in Multiset:

All functions are the same as set. Key difference is in **erase**:

**Erasing ONE occurrence of a value:**
```cpp
ms.erase(ms.find(1));  // removes only the first occurrence of 1
// ms = {1, 2, 3}
```

**Erasing ALL occurrences of a value:**
```cpp
ms.erase(1);  // removes ALL occurrences of 1
// ms = {2, 3}
```

> ⚠️ Important: `ms.erase(value)` removes **all** occurrences.
> Use `ms.erase(ms.find(value))` to remove only **one** occurrence.

**count(value)** — returns the number of times value appears, O(log n + count)
```cpp
ms.count(1);  // returns 2 (if 1 appears twice)
```

---

### 9. Unordered Set

- Similar to set but elements are **not stored in sorted order**.
- Uses **hashing** internally.
- Average case operations are **O(1)** but worst case can be **O(n)** due to hash collisions.
- Does **not** support lower_bound and upper_bound.

**Syntax:**
```cpp
unordered_set<datatype> variable_name;
```

**Example:**
```cpp
unordered_set<int> us;
us.insert(1);
us.insert(3);
us.insert(2);
// stored in any order (hash-based), elements are unique
```

#### Functions in Unordered Set:

Same as set: `insert`, `find`, `count`, `erase`, `size`, `empty`.

**Time Complexity Summary for Unordered Set:**

| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| insert    | O(1)         | O(n)       |
| find      | O(1)         | O(n)       |
| erase     | O(1)         | O(n)       |

> Use unordered_set when you need fast lookups and don't care about order.
> Use set when you need sorted order or lower_bound/upper_bound.

---

### 10. Map

- Map stores data as **key-value pairs**.
- Keys are **unique** (no duplicate keys).
- Stored in **sorted order by key** (ascending by default).
- Internally implemented as a **Red-Black Tree**.

**Syntax:**
```cpp
map<key_datatype, value_datatype> variable_name;
```

**Example:**
```cpp
map<int, int> mp;
map<int, string> mp2;
map<string, int> mp3;
```

#### Functions in Map:

**1. Inserting elements:**
```cpp
mp[1] = 10;        // using [] operator
mp[2] = 20;
mp.insert({3, 30});  // using insert
// mp = {1:10, 2:20, 3:30}
```

> ⚠️ Note: If you use `mp[key]` for a key that doesn't exist, it will **create** that key with default value (0 for int).

**2. Accessing values:**
```cpp
mp[1];          // returns 10
mp.at(1);       // returns 10 (throws exception if key not found)
```

**3. find(key)** — returns iterator to {key, value} pair, O(log n)
```cpp
auto it = mp.find(1);
if (it != mp.end()) {
    cout << it->first << " " << it->second;  // 1 10
}
```

**4. count(key)** — returns 1 if key exists, 0 otherwise, O(log n)
```cpp
mp.count(1);  // 1
mp.count(5);  // 0
```

**5. erase(key)** — removes the key-value pair, O(log n)
```cpp
mp.erase(1);
```

**6. size() and empty():**
```cpp
mp.size();
mp.empty();
```

**7. lower_bound(key) and upper_bound(key):**
```cpp
auto it = mp.lower_bound(2);  // iterator to first key >= 2
auto it = mp.upper_bound(2);  // iterator to first key > 2
```

**8. Iterating through a map:**
```cpp
// Using range-based for loop
for (auto x : mp) {
    cout << x.first << " " << x.second << "\n";
}

// Using structured bindings (C++17)
for (auto& [key, value] : mp) {
    cout << key << " " << value << "\n";
}

// Using iterator
for (auto it = mp.begin(); it != mp.end(); it++) {
    cout << it->first << " " << it->second << "\n";
}
```

**Time Complexity Summary for Map:**

| Operation | Time Complexity |
|-----------|-----------------|
| insert    | O(log n)        |
| find      | O(log n)        |
| erase     | O(log n)        |
| []        | O(log n)        |

---

### 11. Multimap

- Similar to map but allows **duplicate keys**.
- Keys are stored in **sorted order**.
- Internally implemented as a **Red-Black Tree**.

**Syntax:**
```cpp
multimap<key_datatype, value_datatype> variable_name;
```

**Example:**
```cpp
multimap<int, int> mm;
mm.insert({1, 10});
mm.insert({1, 20});  // duplicate key allowed
mm.insert({2, 30});
// mm = {1:10, 1:20, 2:30}
```

> ⚠️ Note: `mm[key]` is **NOT** supported in multimap (because multiple values for same key would be ambiguous).
> Always use `mm.insert({key, value})`.

**Finding all values for a key:**
```cpp
auto range = mm.equal_range(1);
for (auto it = range.first; it != range.second; it++) {
    cout << it->first << " " << it->second << "\n";
}
// Output: 1 10
//         1 20
```

---

### 12. Unordered Map

- Similar to map but elements are **not stored in sorted order**.
- Uses **hashing** internally.
- Average case operations are **O(1)** but worst case can be **O(n)**.
- Most commonly used for frequency counting problems.

**Syntax:**
```cpp
unordered_map<key_datatype, value_datatype> variable_name;
```

**Example:**
```cpp
unordered_map<int, int> um;
um[1] = 10;
um[2] = 20;
um[3] = 30;
```

#### Functions in Unordered Map:

Same as map: `insert`, `find`, `count`, `erase`, `[]`, `size`, `empty`.

**Time Complexity Summary for Unordered Map:**

| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| insert    | O(1)         | O(n)       |
| find      | O(1)         | O(n)       |
| erase     | O(1)         | O(n)       |
| []        | O(1)         | O(n)       |

> Use unordered_map when you need fast lookups and don't care about sorted order.
> Use map when you need sorted keys or range queries (lower_bound/upper_bound).

---

## Iterators

- Iterators are used to **point to elements** inside containers and traverse them.
- They work like pointers.

**Types of Iterators:**
1. `begin()` — points to the first element
2. `end()` — points to one position past the last element
3. `rbegin()` — points to the last element (reverse iterator)
4. `rend()` — points to one before the first element (reverse iterator)

**Syntax:**
```cpp
container<datatype>::iterator variable_name = container.begin();
// OR using auto (recommended)
auto it = container.begin();
```

**Dereferencing an iterator:**
```cpp
*it  // gives the value at the iterator
```

**Incrementing/Decrementing:**
```cpp
it++;   // move to next element
it--;   // move to previous element
it + 2; // move 2 positions forward (only for random-access iterators like vector)
```

**Example:**
```cpp
vector<int> v = {1, 2, 3, 4, 5};

for (auto it = v.begin(); it != v.end(); it++) {
    cout << *it << " ";
}
// Output: 1 2 3 4 5

for (auto it = v.rbegin(); it != v.rend(); it++) {
    cout << *it << " ";
}
// Output: 5 4 3 2 1
```

---

## Algorithms (`#include <algorithm>`)

STL provides many useful built-in algorithms that work with iterators.

---

### 1. sort()

- Sorts elements in a range.
- Default: **ascending order**.
- Uses **introsort** (hybrid of quicksort + heapsort + insertion sort).
- Time Complexity: **O(n log n)**

```cpp
vector<int> v = {5, 3, 1, 4, 2};

// Ascending order (default)
sort(v.begin(), v.end());
// v = {1, 2, 3, 4, 5}

// Descending order
sort(v.begin(), v.end(), greater<int>());
// v = {5, 4, 3, 2, 1}

// Sort with custom comparator
sort(v.begin(), v.end(), [](int a, int b) {
    return a > b;  // descending
});

// Sort only part of the array
sort(v.begin(), v.begin() + 3);  // sorts first 3 elements
```

---

### 2. binary_search()

- Returns **true** if the element is found, **false** otherwise.
- The array/vector must be **sorted** before using binary search.
- Time Complexity: **O(log n)**

```cpp
vector<int> v = {1, 2, 3, 4, 5};
binary_search(v.begin(), v.end(), 3);  // true
binary_search(v.begin(), v.end(), 7);  // false
```

---

### 3. lower_bound()

- Returns an iterator to the **first element >= value**.
- The range must be **sorted**.
- Time Complexity: **O(log n)**

```cpp
vector<int> v = {1, 2, 4, 5, 6};
auto it = lower_bound(v.begin(), v.end(), 4);
cout << *it;  // Output: 4 (first element >= 4)

// To find the index
int idx = it - v.begin();  // idx = 2
```

> If no such element exists, returns `v.end()`.

---

### 4. upper_bound()

- Returns an iterator to the **first element > value**.
- The range must be **sorted**.
- Time Complexity: **O(log n)**

```cpp
vector<int> v = {1, 2, 4, 4, 6};
auto it = upper_bound(v.begin(), v.end(), 4);
cout << *it;  // Output: 6 (first element > 4)

// To find the index
int idx = it - v.begin();  // idx = 4
```

---

### 5. max_element() and min_element()

- Returns an iterator to the **maximum/minimum** element in a range.
- Time Complexity: **O(n)**

```cpp
vector<int> v = {3, 1, 4, 1, 5, 9, 2, 6};
auto maxIt = max_element(v.begin(), v.end());
auto minIt = min_element(v.begin(), v.end());

cout << *maxIt;  // 9
cout << *minIt;  // 1

// To get the index
int maxIdx = maxIt - v.begin();
```

---

### 6. accumulate() — `#include <numeric>`

- Returns the **sum** of all elements in a range.
- Time Complexity: **O(n)**

```cpp
#include <numeric>
vector<int> v = {1, 2, 3, 4, 5};
int total = accumulate(v.begin(), v.end(), 0);  // 0 is initial value
cout << total;  // Output: 15
```

---

### 7. count()

- Returns the **count** of a specific value in a range.
- Time Complexity: **O(n)**

```cpp
vector<int> v = {1, 2, 2, 3, 2, 4};
cout << count(v.begin(), v.end(), 2);  // Output: 3
```

---

### 8. find()

- Returns an iterator to the **first occurrence** of a value.
- Returns `v.end()` if not found.
- Time Complexity: **O(n)**

```cpp
vector<int> v = {1, 2, 3, 4, 5};
auto it = find(v.begin(), v.end(), 3);
if (it != v.end()) {
    cout << "Found at index: " << it - v.begin();  // 2
}
```

---

### 9. reverse()

- Reverses the elements in a range.
- Time Complexity: **O(n)**

```cpp
vector<int> v = {1, 2, 3, 4, 5};
reverse(v.begin(), v.end());
// v = {5, 4, 3, 2, 1}
```

---

### 10. next_permutation() and prev_permutation()

- Rearranges elements into the **next/previous lexicographic permutation**.
- Returns `true` if next permutation exists, `false` if it wrapped around.
- Time Complexity: **O(n)**

```cpp
vector<int> v = {1, 2, 3};
next_permutation(v.begin(), v.end());
// v = {1, 3, 2}

// To generate all permutations
sort(v.begin(), v.end());  // start from smallest permutation
do {
    for (int x : v) cout << x << " ";
    cout << "\n";
} while (next_permutation(v.begin(), v.end()));
```

---

### 11. fill()

- Fills a range with a specific value.
- Time Complexity: **O(n)**

```cpp
vector<int> v(5);
fill(v.begin(), v.end(), 7);
// v = {7, 7, 7, 7, 7}
```

---

### 12. rotate()

- Rotates elements so that the element at a given position becomes the first element.
- Time Complexity: **O(n)**

```cpp
vector<int> v = {1, 2, 3, 4, 5};
rotate(v.begin(), v.begin() + 2, v.end());
// v = {3, 4, 5, 1, 2}
```

---

## Overall Time Complexity Cheat Sheet

| Container          | Insert      | Delete      | Search      | Access   |
|--------------------|-------------|-------------|-------------|----------|
| Vector             | O(1)* / O(n)| O(n)        | O(n)        | O(1)     |
| List               | O(1)        | O(1)        | O(n)        | O(n)     |
| Deque              | O(1)        | O(1)        | O(n)        | O(1)     |
| Stack              | O(1)        | O(1)        | —           | O(1) top |
| Queue              | O(1)        | O(1)        | —           | O(1) front/back |
| Priority Queue     | O(log n)    | O(log n)    | —           | O(1) top |
| Set                | O(log n)    | O(log n)    | O(log n)    | —        |
| Multiset           | O(log n)    | O(log n)    | O(log n)    | —        |
| Unordered Set      | O(1) avg    | O(1) avg    | O(1) avg    | —        |
| Map                | O(log n)    | O(log n)    | O(log n)    | —        |
| Multimap           | O(log n)    | O(log n)    | O(log n)    | —        |
| Unordered Map      | O(1) avg    | O(1) avg    | O(1) avg    | —        |

*O(1) amortized at end; O(n) for insert/delete in the middle

---

## Key Tips & Takeaways

- **emplace_back** is faster than **push_back** (avoids an extra copy).
- Use **unordered_map/unordered_set** for O(1) average lookups; use **map/set** when sorted order or range queries (lower_bound/upper_bound) are needed.
- In **multiset**, to erase only ONE occurrence: use `ms.erase(ms.find(val))`. Using `ms.erase(val)` removes ALL occurrences.
- `lower_bound` and `upper_bound` work in **O(log n)** on **sorted vectors** and directly on **set/map**.
- On an **unsorted vector**, `lower_bound` still runs but gives incorrect results — always sort first.
- `map[key]` creates the key with a default value (0 for int) if it doesn't exist — use `map.find(key)` to check first.
- **Stack and Queue** don't support iteration — use deque if you need both.
- When in doubt between vector and list: prefer **vector** (better cache performance) unless you need frequent insertions/deletions at the front.

---

*Notes based on: Complete C++ STL in 1 Video | take U forward (Striver)*