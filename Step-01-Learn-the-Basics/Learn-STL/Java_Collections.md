# Java Collections Framework - Complete Notes

---

## What is Java Collections Framework?

- Java is one of the most widely used programming languages, especially for backend development,
  competitive programming, and enterprise applications.

- The **Java Collections Framework (JCF)** is a set of classes and interfaces that provide
  ready-made data structures to store and manipulate groups of objects efficiently.

- Just like C++ has STL (Standard Template Library), Java has the **Collections Framework**
  which provides pre-built implementations of common data structures like List, Set, Map, Queue etc.

- It saves developers from writing data-handling code from scratch and improves code
  reusability, maintainability, and performance.

- To use Java Collections, import:
```java
import java.util.*;
```

- Java Collections Framework is divided into:
  1. **Interfaces** — define the behavior (Collection, List, Set, Map, Queue, Deque)
  2. **Implementations** — actual classes (ArrayList, HashSet, HashMap etc.)
  3. **Algorithms** — utility methods via the `Collections` class (sort, reverse, shuffle etc.)
  4. **Iterators** — used to traverse collections

---

## Hierarchy of Java Collections Framework

```
Iterable
  └── Collection
        ├── List
        │     ├── ArrayList
        │     ├── LinkedList
        │     ├── Vector
        │     └── Stack
        ├── Set
        │     ├── HashSet
        │     ├── LinkedHashSet
        │     └── TreeSet
        └── Queue
              ├── PriorityQueue
              ├── LinkedList (also implements Deque)
              └── Deque
                    └── ArrayDeque

Map (separate hierarchy — does NOT extend Collection)
  ├── HashMap
  ├── LinkedHashMap
  ├── TreeMap
  └── Hashtable
```

> Note: **Map** is NOT a part of the Collection interface hierarchy. It is a separate interface.

---

## Pairs (using AbstractMap.SimpleEntry or Map.Entry)

- Java does not have a built-in `pair` type like C++.
- We can use `Map.Entry`, `AbstractMap.SimpleEntry`, or create a custom class.
- For competitive programming, a common approach is to use `int[]` arrays of size 2 or
  `AbstractMap.SimpleEntry`.

**Using AbstractMap.SimpleEntry:**
```java
import java.util.AbstractMap;

AbstractMap.SimpleEntry<Integer, Integer> pair = new AbstractMap.SimpleEntry<>(1, 2);
System.out.println(pair.getKey());    // 1
System.out.println(pair.getValue());  // 2
```

**Common competitive programming approach (using int array):**
```java
int[] pair = {1, 2};
System.out.println(pair[0]);  // first value
System.out.println(pair[1]);  // second value
```

**Array of pairs:**
```java
int[][] pairs = {{1, 2}, {3, 4}, {5, 6}};
System.out.println(pairs[0][0]);  // 1
System.out.println(pairs[0][1]);  // 2
```

---

## Core Interfaces

### Collection Interface
- The **root interface** of the Java Collections Framework.
- All collection classes implement this interface (except Map).
- It extends the `Iterable` interface (so all collections can be iterated using for-each).
- Provides basic operations: `add()`, `remove()`, `size()`, `contains()`, `clear()`, `isEmpty()` etc.

### List Interface
- Ordered collection (maintains insertion order).
- Allows **duplicate elements**.
- Supports **positional access** (by index).
- Implementations: `ArrayList`, `LinkedList`, `Vector`, `Stack`.

### Set Interface
- Collection of **unique elements** (no duplicates allowed).
- May or may not maintain order depending on implementation.
- Implementations: `HashSet`, `LinkedHashSet`, `TreeSet`.

### Queue Interface
- Follows **FIFO (First In First Out)** order.
- Elements are inserted at the rear and removed from the front.
- Implementations: `PriorityQueue`, `LinkedList`, `ArrayDeque`.

### Deque Interface
- **Double-Ended Queue** — allows insertion and removal from both ends.
- Extends the `Queue` interface.
- Implementations: `ArrayDeque`, `LinkedList`.

### Map Interface
- Stores data as **key-value pairs**.
- Keys are **unique**; values can be duplicated.
- Does **NOT** extend Collection interface.
- Implementations: `HashMap`, `LinkedHashMap`, `TreeMap`, `Hashtable`.

---

## Containers (Implementations)

---

### 1. ArrayList

- It is a **dynamic array** — resizes automatically when elements are added.
- Maintains **insertion order**.
- Allows **duplicate elements**.
- Supports **random access** (O(1) by index).
- Not thread-safe (use `Vector` or `Collections.synchronizedList()` for thread safety).

**Syntax:**
```java
ArrayList<datatype> variable_name = new ArrayList<>();
// OR using List interface reference (recommended)
List<datatype> variable_name = new ArrayList<>();
```

**Example:**
```java
ArrayList<Integer> list = new ArrayList<>();
```

#### Functions in ArrayList:

**1. add(value)** — adds element at the end, O(1) amortized
```java
list.add(1);
list.add(2);
list.add(3);
// list = [1, 2, 3]
```

**2. add(index, value)** — inserts at a specific index, O(n)
```java
list.add(1, 10);  // inserts 10 at index 1
// list = [1, 10, 2, 3]
```

**3. get(index)** — returns element at index, O(1)
```java
list.get(0);  // returns 1
list.get(2);  // returns 2
```

**4. set(index, value)** — replaces element at index, O(1)
```java
list.set(0, 99);
// list = [99, 10, 2, 3]
```

**5. remove(index)** — removes element at index, O(n)
```java
list.remove(0);  // removes element at index 0
```

**6. remove(Object o)** — removes first occurrence of the value, O(n)
```java
list.remove(Integer.valueOf(10));  // removes the value 10 (not index 10)
```

> ⚠️ Important: `list.remove(1)` removes by **index**, but `list.remove(Integer.valueOf(1))` removes by **value**.

**7. size()** — returns number of elements, O(1)
```java
list.size();
```

**8. isEmpty()** — returns true if empty, O(1)
```java
list.isEmpty();
```

**9. contains(value)** — returns true if value exists, O(n)
```java
list.contains(2);  // true
list.contains(99); // false
```

**10. indexOf(value)** — returns first index of value, -1 if not found, O(n)
```java
list.indexOf(2);  // returns index
```

**11. clear()** — removes all elements, O(n)
```java
list.clear();
```

**12. Iterating through ArrayList:**
```java
// Using index
for (int i = 0; i < list.size(); i++) {
    System.out.println(list.get(i));
}

// Using enhanced for-each loop
for (int x : list) {
    System.out.println(x);
}

// Using Iterator
Iterator<Integer> it = list.iterator();
while (it.hasNext()) {
    System.out.println(it.next());
}
```

**13. Sorting an ArrayList:**
```java
Collections.sort(list);                        // ascending
Collections.sort(list, Collections.reverseOrder());  // descending
```

**14. Converting array to ArrayList:**
```java
Integer[] arr = {1, 2, 3};
List<Integer> list = new ArrayList<>(Arrays.asList(arr));
```

**Time Complexity Summary for ArrayList:**

| Operation              | Time Complexity |
|------------------------|-----------------|
| get(index)             | O(1)            |
| add(value) at end      | O(1) amortized  |
| add(index, value)      | O(n)            |
| remove(index)          | O(n)            |
| contains(value)        | O(n)            |
| size()                 | O(1)            |

---

### 2. LinkedList

- Internally implemented as a **doubly linked list**.
- Implements both **List** and **Deque** interfaces.
- Maintains **insertion order**.
- Allows **duplicate elements**.
- Supports fast insertion/deletion at both ends — O(1).
- **No random access** support (getting by index is O(n)).

**Syntax:**
```java
LinkedList<datatype> variable_name = new LinkedList<>();
```

**Example:**
```java
LinkedList<Integer> ll = new LinkedList<>();
```

#### Functions in LinkedList:

**1. add(value) / addLast(value)** — adds at end, O(1)
```java
ll.add(2);
ll.addLast(3);
```

**2. addFirst(value)** — adds at front, O(1)
```java
ll.addFirst(1);
// ll = [1, 2, 3]
```

**3. getFirst() / peekFirst()** — returns first element, O(1)
```java
ll.getFirst();   // throws exception if empty
ll.peekFirst();  // returns null if empty
```

**4. getLast() / peekLast()** — returns last element, O(1)
```java
ll.getLast();
ll.peekLast();
```

**5. removeFirst() / pollFirst()** — removes first element, O(1)
```java
ll.removeFirst();   // throws exception if empty
ll.pollFirst();     // returns null if empty
```

**6. removeLast() / pollLast()** — removes last element, O(1)
```java
ll.removeLast();
ll.pollLast();
```

**7. get(index)** — returns element at index, O(n)
```java
ll.get(1);  // second element
```

**8. size(), isEmpty(), contains(), clear()** — same as ArrayList

**9. Iterating:**
```java
for (int x : ll) {
    System.out.println(x);
}
```

**Time Complexity Summary for LinkedList:**

| Operation                    | Time Complexity |
|------------------------------|-----------------|
| addFirst / addLast           | O(1)            |
| removeFirst / removeLast     | O(1)            |
| get(index)                   | O(n)            |
| contains(value)              | O(n)            |
| add(index, value)            | O(n)            |

---

### 3. Stack

- Stack follows the **LIFO (Last In First Out)** principle.
- Extends the `Vector` class.
- In competitive programming, `Deque` (specifically `ArrayDeque`) is preferred over `Stack`
  for better performance.

**Syntax:**
```java
Stack<datatype> variable_name = new Stack<>();
```

**Example:**
```java
Stack<Integer> st = new Stack<>();
```

#### Functions in Stack:

**1. push(value)** — adds element on top, O(1)
```java
st.push(1);
st.push(2);
st.push(3);
// top → 3, 2, 1
```

**2. peek()** — returns top element without removing, O(1)
```java
st.peek();  // 3
```

**3. pop()** — removes and returns top element, O(1)
```java
st.pop();  // removes 3, top → 2, 1
```

**4. isEmpty()** — returns true if stack is empty, O(1)
```java
st.isEmpty();
```

**5. size()** — returns number of elements, O(1)
```java
st.size();
```

**6. search(value)** — returns 1-based position from top, -1 if not found, O(n)
```java
st.search(2);  // returns 1 (it's at the top)
```

> ⚠️ Preferred alternative in competitive programming:
```java
Deque<Integer> st = new ArrayDeque<>();
st.push(1);    // addFirst
st.peek();     // peekFirst
st.pop();      // removeFirst
```

**Time Complexity Summary for Stack:**

| Operation | Time Complexity |
|-----------|-----------------|
| push      | O(1)            |
| pop       | O(1)            |
| peek      | O(1)            |
| search    | O(n)            |

---

### 4. Queue

- Queue follows the **FIFO (First In First Out)** principle.
- `Queue` is an interface. Common implementations: `LinkedList`, `ArrayDeque`.
- In competitive programming, `ArrayDeque` is preferred over `LinkedList` for Queue.

**Syntax:**
```java
Queue<datatype> variable_name = new LinkedList<>();
// OR (preferred)
Queue<datatype> variable_name = new ArrayDeque<>();
```

**Example:**
```java
Queue<Integer> q = new LinkedList<>();
```

#### Functions in Queue:

**1. add(value) / offer(value)** — adds element at rear, O(1)
```java
q.add(1);
q.offer(2);
q.offer(3);
// front → 1, 2, 3 ← rear
```

> `add()` throws exception if fails; `offer()` returns false if fails. Prefer `offer()`.

**2. peek() / element()** — returns front element without removing, O(1)
```java
q.peek();     // returns null if empty
q.element();  // throws exception if empty
```

**3. poll() / remove()** — removes and returns front element, O(1)
```java
q.poll();    // returns null if empty
q.remove();  // throws exception if empty
```

**4. size() and isEmpty():**
```java
q.size();
q.isEmpty();
```

**5. Iterating through Queue:**
```java
for (int x : q) {
    System.out.println(x);
}
```

**Time Complexity Summary for Queue (ArrayDeque):**

| Operation          | Time Complexity |
|--------------------|-----------------|
| offer (add rear)   | O(1)            |
| poll (remove front)| O(1)            |
| peek               | O(1)            |

---

### 5. Deque (ArrayDeque)

- **Double-Ended Queue** — allows insertion and removal from both front and rear.
- `ArrayDeque` is the most commonly used implementation.
- It is faster than `Stack` for stack operations and faster than `LinkedList` for queue operations.
- Does **NOT** allow null elements.

**Syntax:**
```java
Deque<datatype> variable_name = new ArrayDeque<>();
```

**Example:**
```java
Deque<Integer> dq = new ArrayDeque<>();
```

#### Functions in Deque (ArrayDeque):

**1. addFirst(value) / offerFirst(value)** — adds at front, O(1)
```java
dq.addFirst(1);
```

**2. addLast(value) / offerLast(value)** — adds at rear, O(1)
```java
dq.addLast(2);
dq.addLast(3);
// dq = [1, 2, 3]
```

**3. peekFirst() / getFirst()** — returns front element, O(1)
```java
dq.peekFirst();  // 1
```

**4. peekLast() / getLast()** — returns rear element, O(1)
```java
dq.peekLast();  // 3
```

**5. pollFirst() / removeFirst()** — removes from front, O(1)
```java
dq.pollFirst();  // removes 1
```

**6. pollLast() / removeLast()** — removes from rear, O(1)
```java
dq.pollLast();  // removes 3
```

**Using ArrayDeque as Stack:**
```java
Deque<Integer> stack = new ArrayDeque<>();
stack.push(1);   // same as addFirst
stack.peek();    // same as peekFirst
stack.pop();     // same as removeFirst
```

**Using ArrayDeque as Queue:**
```java
Deque<Integer> queue = new ArrayDeque<>();
queue.offer(1);  // same as addLast
queue.peek();    // same as peekFirst
queue.poll();    // same as pollFirst
```

**Time Complexity Summary for ArrayDeque:**

| Operation                   | Time Complexity |
|-----------------------------|-----------------|
| addFirst / addLast           | O(1)            |
| pollFirst / pollLast         | O(1)            |
| peekFirst / peekLast         | O(1)            |

---

### 6. PriorityQueue

- PriorityQueue is a **Min-Heap by default** (smallest element is at the top).
  > Note: This is the **opposite** of C++ where priority_queue is max-heap by default.
- Elements are **ordered by natural ordering** or by a custom `Comparator`.
- Does **NOT** allow null elements.
- Not thread-safe.

**Syntax (Min-Heap — default):**
```java
PriorityQueue<datatype> variable_name = new PriorityQueue<>();
```

**Syntax (Max-Heap):**
```java
PriorityQueue<datatype> variable_name = new PriorityQueue<>(Collections.reverseOrder());
```

**Example (Min-Heap):**
```java
PriorityQueue<Integer> pq = new PriorityQueue<>();
pq.add(3);
pq.add(1);
pq.add(5);
pq.add(2);
// internally min-heap: top = 1
```

#### Functions in PriorityQueue:

**1. add(value) / offer(value)** — inserts element, O(log n)
```java
pq.add(4);
pq.offer(6);
```

**2. peek()** — returns top (minimum in min-heap) element without removing, O(1)
```java
pq.peek();  // 1
```

**3. poll()** — removes and returns the top element, O(log n)
```java
pq.poll();  // removes 1, now top = 2
```

**4. size() and isEmpty():**
```java
pq.size();
pq.isEmpty();
```

**5. contains(value)** — O(n)
```java
pq.contains(3);  // true
```

**6. Max-Heap Example:**
```java
PriorityQueue<Integer> maxPQ = new PriorityQueue<>(Collections.reverseOrder());
maxPQ.add(3);
maxPQ.add(1);
maxPQ.add(5);
System.out.println(maxPQ.peek());  // 5 (maximum element)
```

**7. Custom Comparator PriorityQueue:**
```java
// Min-heap based on absolute value
PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> Math.abs(a) - Math.abs(b));

// PriorityQueue of int arrays sorted by second element
PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
```

**Time Complexity Summary for PriorityQueue:**

| Operation | Time Complexity |
|-----------|-----------------|
| add/offer | O(log n)        |
| poll      | O(log n)        |
| peek      | O(1)            |
| contains  | O(n)            |

---

### 7. HashSet

- Stores **unique elements only** (no duplicates).
- Does **NOT** maintain any order (insertion order is not preserved).
- Uses **hashing** internally (backed by a HashMap).
- Allows **one null** element.

**Syntax:**
```java
HashSet<datatype> variable_name = new HashSet<>();
// OR using Set interface reference (recommended)
Set<datatype> variable_name = new HashSet<>();
```

**Example:**
```java
HashSet<Integer> hs = new HashSet<>();
hs.add(3);
hs.add(1);
hs.add(2);
hs.add(1);  // duplicate, will be ignored
// hs = {1, 2, 3} — order NOT guaranteed
```

#### Functions in HashSet:

**1. add(value)** — adds element (ignored if already present), O(1) average
```java
hs.add(5);
```

**2. contains(value)** — returns true if value exists, O(1) average
```java
hs.contains(3);  // true
hs.contains(7);  // false
```

**3. remove(value)** — removes element, O(1) average
```java
hs.remove(3);
```

**4. size() and isEmpty():**
```java
hs.size();
hs.isEmpty();
```

**5. Iterating through HashSet:**
```java
for (int x : hs) {
    System.out.println(x);
}

// Using Iterator
Iterator<Integer> it = hs.iterator();
while (it.hasNext()) {
    System.out.println(it.next());
}
```

**Time Complexity Summary for HashSet:**

| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| add       | O(1)         | O(n)       |
| contains  | O(1)         | O(n)       |
| remove    | O(1)         | O(n)       |

---

### 8. LinkedHashSet

- Same as HashSet but **maintains insertion order**.
- Uses a **doubly linked list + hash table** internally.
- Slightly slower than HashSet due to maintaining order.
- Allows **one null** element.

**Syntax:**
```java
LinkedHashSet<datatype> variable_name = new LinkedHashSet<>();
```

**Example:**
```java
LinkedHashSet<Integer> lhs = new LinkedHashSet<>();
lhs.add(3);
lhs.add(1);
lhs.add(2);
lhs.add(1);  // duplicate ignored
// lhs = [3, 1, 2] — insertion order preserved
```

- All functions are the same as HashSet.
- Time complexity is the same as HashSet: O(1) average for add, remove, contains.

---

### 9. TreeSet

- Stores **unique elements in sorted (ascending) order**.
- Internally implemented as a **Red-Black Tree**.
- Does **NOT** allow null elements (throws NullPointerException).
- Equivalent of C++'s `set`.

**Syntax:**
```java
TreeSet<datatype> variable_name = new TreeSet<>();
```

**Example:**
```java
TreeSet<Integer> ts = new TreeSet<>();
ts.add(3);
ts.add(1);
ts.add(2);
ts.add(1);  // duplicate ignored
// ts = [1, 2, 3]  — sorted order
```

#### Functions in TreeSet:

**1. add(value)** — O(log n)
```java
ts.add(5);
```

**2. contains(value)** — O(log n)
```java
ts.contains(3);  // true
```

**3. remove(value)** — O(log n)
```java
ts.remove(2);
```

**4. first()** — returns smallest element, O(log n)
```java
ts.first();  // 1
```

**5. last()** — returns largest element, O(log n)
```java
ts.last();  // 5
```

**6. floor(value)** — returns largest element **<= value**, O(log n)
  - Equivalent of C++'s `lower_bound` (but returns value, not iterator)
```java
ts.floor(3);  // 3 (or the largest element <= 3)
```

**7. ceiling(value)** — returns smallest element **>= value**, O(log n)
  - Equivalent of C++'s `lower_bound`
```java
ts.ceiling(2);  // 2 (or the smallest element >= 2)
```

**8. lower(value)** — returns largest element **< value** (strictly less), O(log n)
```java
ts.lower(3);  // 2
```

**9. higher(value)** — returns smallest element **> value** (strictly greater), O(log n)
```java
ts.higher(3);  // 5
```

**10. headSet(value)** — returns all elements **< value**
```java
ts.headSet(3);  // [1, 2]
```

**11. tailSet(value)** — returns all elements **>= value**
```java
ts.tailSet(3);  // [3, 5]
```

**12. subSet(from, to)** — returns elements from `from` (inclusive) to `to` (exclusive)
```java
ts.subSet(2, 5);  // [2, 3]
```

**13. Iterating through TreeSet:**
```java
for (int x : ts) {
    System.out.println(x);  // prints in ascending order
}

// Descending order
for (int x : ts.descendingSet()) {
    System.out.println(x);
}
```

**Time Complexity Summary for TreeSet:**

| Operation           | Time Complexity |
|---------------------|-----------------|
| add                 | O(log n)        |
| contains            | O(log n)        |
| remove              | O(log n)        |
| first / last        | O(log n)        |
| floor / ceiling     | O(log n)        |
| lower / higher      | O(log n)        |

---

### 10. HashMap

- Stores data as **key-value pairs**.
- Keys are **unique**; values can be duplicated.
- Does **NOT** maintain any order.
- Uses **hashing** internally.
- Allows **one null key** and **multiple null values**.
- Equivalent of C++'s `unordered_map`.

**Syntax:**
```java
HashMap<key_datatype, value_datatype> variable_name = new HashMap<>();
// OR using Map interface reference (recommended)
Map<key_datatype, value_datatype> variable_name = new HashMap<>();
```

**Example:**
```java
HashMap<Integer, Integer> hm = new HashMap<>();
HashMap<String, Integer> hm2 = new HashMap<>();
```

#### Functions in HashMap:

**1. put(key, value)** — inserts or updates a key-value pair, O(1) average
```java
hm.put(1, 10);
hm.put(2, 20);
hm.put(1, 30);  // updates key 1's value to 30
// hm = {1:30, 2:20}
```

**2. get(key)** — returns value for key, null if not found, O(1) average
```java
hm.get(1);  // 30
hm.get(5);  // null
```

**3. getOrDefault(key, defaultValue)** — returns value or default if key not found, O(1) average
```java
hm.getOrDefault(1, 0);   // 30
hm.getOrDefault(99, 0);  // 0 (default)
```

**4. containsKey(key)** — returns true if key exists, O(1) average
```java
hm.containsKey(1);  // true
hm.containsKey(5);  // false
```

**5. containsValue(value)** — returns true if value exists, O(n)
```java
hm.containsValue(20);  // true
```

**6. remove(key)** — removes key-value pair, O(1) average
```java
hm.remove(2);
```

**7. size() and isEmpty():**
```java
hm.size();
hm.isEmpty();
```

**8. keySet()** — returns a Set of all keys
```java
Set<Integer> keys = hm.keySet();
for (int key : hm.keySet()) {
    System.out.println(key);
}
```

**9. values()** — returns a Collection of all values
```java
for (int val : hm.values()) {
    System.out.println(val);
}
```

**10. entrySet()** — returns a Set of all key-value pairs (Map.Entry objects)
```java
for (Map.Entry<Integer, Integer> entry : hm.entrySet()) {
    System.out.println(entry.getKey() + " " + entry.getValue());
}
```

**11. putIfAbsent(key, value)** — inserts only if key not already present, O(1) average
```java
hm.putIfAbsent(3, 50);
```

**12. Frequency counting pattern (very common in CP):**
```java
int[] arr = {1, 2, 2, 3, 1, 4};
HashMap<Integer, Integer> freq = new HashMap<>();
for (int x : arr) {
    freq.put(x, freq.getOrDefault(x, 0) + 1);
}
// freq = {1:2, 2:2, 3:1, 4:1}
```

**Time Complexity Summary for HashMap:**

| Operation      | Average Case | Worst Case |
|----------------|--------------|------------|
| put            | O(1)         | O(n)       |
| get            | O(1)         | O(n)       |
| containsKey    | O(1)         | O(n)       |
| remove         | O(1)         | O(n)       |

---

### 11. LinkedHashMap

- Same as HashMap but **maintains insertion order**.
- Uses a **doubly linked list + hash table** internally.
- Allows **one null key** and **multiple null values**.

**Syntax:**
```java
LinkedHashMap<key_datatype, value_datatype> variable_name = new LinkedHashMap<>();
```

**Example:**
```java
LinkedHashMap<Integer, Integer> lhm = new LinkedHashMap<>();
lhm.put(3, 30);
lhm.put(1, 10);
lhm.put(2, 20);
// lhm = {3:30, 1:10, 2:20} — insertion order preserved
```

- All functions are the same as HashMap.
- Time complexity is also the same as HashMap: O(1) average.

---

### 12. TreeMap

- Stores key-value pairs where keys are in **sorted (ascending) order**.
- Internally implemented as a **Red-Black Tree**.
- Does **NOT** allow null keys (throws NullPointerException).
- Equivalent of C++'s `map`.

**Syntax:**
```java
TreeMap<key_datatype, value_datatype> variable_name = new TreeMap<>();
```

**Example:**
```java
TreeMap<Integer, Integer> tm = new TreeMap<>();
tm.put(3, 30);
tm.put(1, 10);
tm.put(2, 20);
// tm = {1:10, 2:20, 3:30} — sorted by key
```

#### Functions in TreeMap:

All HashMap functions work + these additional ones:

**1. firstKey()** — returns smallest key, O(log n)
```java
tm.firstKey();  // 1
```

**2. lastKey()** — returns largest key, O(log n)
```java
tm.lastKey();  // 3
```

**3. floorKey(key)** — returns largest key **<= given key**, O(log n)
```java
tm.floorKey(2);  // 2
```

**4. ceilingKey(key)** — returns smallest key **>= given key**, O(log n)
```java
tm.ceilingKey(2);  // 2
```

**5. lowerKey(key)** — returns largest key **< given key** (strictly less), O(log n)
```java
tm.lowerKey(3);  // 2
```

**6. higherKey(key)** — returns smallest key **> given key** (strictly greater), O(log n)
```java
tm.higherKey(1);  // 2
```

**7. headMap(key)** — returns map with keys **< key**
```java
tm.headMap(3);  // {1:10, 2:20}
```

**8. tailMap(key)** — returns map with keys **>= key**
```java
tm.tailMap(2);  // {2:20, 3:30}
```

**9. Iterating through TreeMap:**
```java
for (Map.Entry<Integer, Integer> entry : tm.entrySet()) {
    System.out.println(entry.getKey() + " " + entry.getValue());
    // prints in ascending key order
}

// Descending key order
for (Map.Entry<Integer, Integer> entry : tm.descendingMap().entrySet()) {
    System.out.println(entry.getKey() + " " + entry.getValue());
}
```

**Time Complexity Summary for TreeMap:**

| Operation         | Time Complexity |
|-------------------|-----------------|
| put               | O(log n)        |
| get               | O(log n)        |
| remove            | O(log n)        |
| firstKey/lastKey  | O(log n)        |
| floorKey/ceilingKey | O(log n)      |

---

## Iterators

- Iterators are used to **traverse elements** of a collection without exposing its underlying structure.
- Every collection class provides an `iterator()` method.

**Types:**
1. **Iterator** — can traverse forward only
2. **ListIterator** — can traverse both forward and backward (only for List)

**Iterator Syntax:**
```java
Iterator<datatype> it = collection.iterator();
while (it.hasNext()) {
    datatype element = it.next();
    System.out.println(element);
}
```

**Iterator methods:**
- `hasNext()` — returns true if more elements exist
- `next()` — returns next element and moves iterator forward
- `remove()` — removes current element (safe removal during iteration)

**ListIterator Syntax (for List):**
```java
List<Integer> list = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
ListIterator<Integer> lit = list.listIterator();

// Forward traversal
while (lit.hasNext()) {
    System.out.println(lit.next());
}

// Backward traversal
while (lit.hasPrevious()) {
    System.out.println(lit.previous());
}
```

> ⚠️ Never modify a collection directly while iterating (throws `ConcurrentModificationException`).
> Use `iterator.remove()` instead for safe removal during iteration.

---

## Algorithms — Collections Utility Class

- `Collections` (with an 's') is a **utility class** in `java.util` that provides static methods
  for common operations on collections.
- It is different from the `Collection` (without 's') interface.

```java
import java.util.Collections;
```

---

### 1. sort()

- Sorts a List in **ascending order** (natural ordering).
- Time Complexity: **O(n log n)**

```java
List<Integer> list = new ArrayList<>(Arrays.asList(5, 3, 1, 4, 2));

Collections.sort(list);
// list = [1, 2, 3, 4, 5]

// Descending order
Collections.sort(list, Collections.reverseOrder());
// list = [5, 4, 3, 2, 1]

// Custom comparator
Collections.sort(list, (a, b) -> b - a);  // descending
```

---

### 2. binarySearch()

- Returns the **index** of the element if found, otherwise returns a negative value.
- The list must be **sorted** before using binary search.
- Time Complexity: **O(log n)**

```java
List<Integer> list = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
int idx = Collections.binarySearch(list, 3);  // returns 2 (index of 3)
int idx2 = Collections.binarySearch(list, 7); // returns negative (not found)
```

---

### 3. reverse()

- Reverses the order of elements in a List.
- Time Complexity: **O(n)**

```java
List<Integer> list = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
Collections.reverse(list);
// list = [5, 4, 3, 2, 1]
```

---

### 4. shuffle()

- Randomly shuffles elements in a List.
- Time Complexity: **O(n)**

```java
Collections.shuffle(list);
```

---

### 5. max() and min()

- Returns the maximum/minimum element in a Collection.
- Time Complexity: **O(n)**

```java
List<Integer> list = new ArrayList<>(Arrays.asList(3, 1, 4, 1, 5, 9));
System.out.println(Collections.max(list));  // 9
System.out.println(Collections.min(list));  // 1
```

---

### 6. frequency()

- Returns the count of a specific element in a Collection.
- Time Complexity: **O(n)**

```java
List<Integer> list = new ArrayList<>(Arrays.asList(1, 2, 2, 3, 2));
Collections.frequency(list, 2);  // 3
```

---

### 7. fill()

- Replaces all elements in a List with the specified value.
- Time Complexity: **O(n)**

```java
List<Integer> list = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
Collections.fill(list, 0);
// list = [0, 0, 0, 0, 0]
```

---

### 8. nCopies()

- Returns an immutable List with n copies of a value.
- Time Complexity: **O(1)**

```java
List<Integer> list = Collections.nCopies(5, 7);
// list = [7, 7, 7, 7, 7]
```

---

### 9. swap()

- Swaps elements at two positions in a List.
- Time Complexity: **O(1)**

```java
List<Integer> list = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
Collections.swap(list, 0, 4);
// list = [5, 2, 3, 4, 1]
```

---

### 10. disjoint()

- Returns true if two collections have **no elements in common**.
- Time Complexity: **O(n)**

```java
List<Integer> a = Arrays.asList(1, 2, 3);
List<Integer> b = Arrays.asList(4, 5, 6);
Collections.disjoint(a, b);  // true

List<Integer> c = Arrays.asList(3, 4, 5);
Collections.disjoint(a, c);  // false (both have 3)
```

---

### 11. unmodifiableList() / unmodifiableMap() / unmodifiableSet()

- Returns a **read-only view** of the collection.
- Any attempt to modify it throws `UnsupportedOperationException`.

```java
List<Integer> list = new ArrayList<>(Arrays.asList(1, 2, 3));
List<Integer> readOnly = Collections.unmodifiableList(list);
// readOnly.add(4);  // throws UnsupportedOperationException
```

---

## C++ STL vs Java Collections — Quick Comparison

| C++ STL              | Java Equivalent         | Notes                          |
|----------------------|-------------------------|--------------------------------|
| `vector<int>`        | `ArrayList<Integer>`    | Dynamic array                  |
| `list<int>`          | `LinkedList<Integer>`   | Doubly linked list             |
| `stack<int>`         | `Stack<Integer>` / `Deque<Integer>` | LIFO                |
| `queue<int>`         | `Queue<Integer>` (LinkedList/ArrayDeque) | FIFO          |
| `deque<int>`         | `Deque<Integer>` (ArrayDeque) | Double-ended queue        |
| `priority_queue<int>` (max) | `PriorityQueue<Integer>(reverseOrder())` | Max-heap |
| `priority_queue<int, vector<int>, greater<int>>` | `PriorityQueue<Integer>()` | Min-heap |
| `set<int>`           | `TreeSet<Integer>`      | Sorted unique elements         |
| `unordered_set<int>` | `HashSet<Integer>`      | Unique elements, no order      |
| `multiset<int>`      | No direct equivalent    | Use TreeMap with count         |
| `map<int,int>`       | `TreeMap<Integer,Integer>` | Sorted key-value pairs      |
| `unordered_map<int,int>` | `HashMap<Integer,Integer>` | Key-value, no order      |
| `lower_bound()`      | `TreeSet.ceiling()` / `TreeMap.ceilingKey()` | First >= value |
| `upper_bound()`      | `TreeSet.higher()` / `TreeMap.higherKey()` | First > value   |
| `sort()`             | `Collections.sort()`    | O(n log n)                     |
| `binary_search()`    | `Collections.binarySearch()` | Returns index (not bool) |
| `reverse()`          | `Collections.reverse()` | O(n)                           |

---

## Overall Time Complexity Cheat Sheet

| Container         | Insert      | Delete      | Search      | Access    |
|-------------------|-------------|-------------|-------------|-----------|
| ArrayList         | O(1)* / O(n)| O(n)        | O(n)        | O(1)      |
| LinkedList        | O(1) ends   | O(1) ends   | O(n)        | O(n)      |
| Stack (ArrayDeque)| O(1)        | O(1)        | O(n)        | O(1) top  |
| Queue (ArrayDeque)| O(1)        | O(1)        | O(n)        | O(1) front|
| ArrayDeque        | O(1)        | O(1)        | O(n)        | O(1) ends |
| PriorityQueue     | O(log n)    | O(log n)    | O(n)        | O(1) top  |
| HashSet           | O(1) avg    | O(1) avg    | O(1) avg    | —         |
| LinkedHashSet     | O(1) avg    | O(1) avg    | O(1) avg    | —         |
| TreeSet           | O(log n)    | O(log n)    | O(log n)    | —         |
| HashMap           | O(1) avg    | O(1) avg    | O(1) avg    | —         |
| LinkedHashMap     | O(1) avg    | O(1) avg    | O(1) avg    | —         |
| TreeMap           | O(log n)    | O(log n)    | O(log n)    | —         |

*O(1) amortized at end; O(n) for insert/delete in the middle

---

## Key Tips & Takeaways

- In Java, **PriorityQueue is min-heap by default** — opposite of C++ where it is max-heap.
  Use `Collections.reverseOrder()` for max-heap in Java.

- **Prefer `ArrayDeque` over `Stack`** for stack operations — it is faster and more efficient.

- **Prefer `ArrayDeque` over `LinkedList`** for queue operations — better cache performance.

- Use `list.remove(Integer.valueOf(x))` to remove by **value**; `list.remove(x)` removes by **index**.

- **`TreeSet` / `TreeMap`** are equivalent to C++'s `set` / `map` — sorted, O(log n).

- **`HashSet` / `HashMap`** are equivalent to C++'s `unordered_set` / `unordered_map` — O(1) average.

- For **frequency counting**, use `HashMap` with `getOrDefault(key, 0) + 1` pattern.

- **`entrySet()`** is the most efficient way to iterate over a Map (avoids double lookups).

- `TreeSet.ceiling(x)` → first element **>= x** (like C++'s `lower_bound`)
  `TreeSet.higher(x)` → first element **> x** (like C++'s `upper_bound`)
  `TreeSet.floor(x)` → largest element **<= x**
  `TreeSet.lower(x)` → largest element **< x**

- Java does **NOT have a built-in pair** type. Use `int[]`, `long[]`, custom class, or `Map.Entry`.

- **`Collections`** (with 's') is the utility class with static methods like `sort()`, `reverse()`, `max()`.
  **`Collection`** (without 's') is the root interface.

---

*Notes based on: Java Collections Tutorial | take U forward (Striver)*