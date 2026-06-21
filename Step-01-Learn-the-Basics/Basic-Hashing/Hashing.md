# Hashing — Complete Notes
### (Maps | Time Complexity | Collisions | Division Rule of Hashing)

---

## What is Hashing?

- Hashing is a technique used to uniquely identify a specific element from a group of elements.
- The idea is to map data of arbitrary size to data of a **fixed size** using a **hash function**.
- It allows us to perform **insert, delete, and search operations in O(1) average time** — much
  faster than arrays (O(n) for search) or BSTs (O(log n) for search).

- **Real-life analogy:** Imagine a library where each book is assigned a unique code and placed
  on a shelf corresponding to that code. Instead of searching every shelf, you directly go to
  the right shelf using the code. That code is the **hash** and the shelf is the **bucket**.

- Hashing is one of the most important concepts in DSA, used extensively in:
  - Frequency counting
  - Searching in O(1)
  - Detecting duplicates
  - Implementing Maps and Sets

---

## The Core Problem Hashing Solves

- **Problem:** Given an array, answer multiple queries of the type "how many times does element
  `x` appear in the array?" efficiently.

- **Brute Force approach:** For every query, traverse the entire array and count. 
  Time Complexity: **O(n)** per query → **O(n × q)** for q queries. Too slow.

- **Better approach using Hashing:** Pre-process the array once and store the frequency of each
  element. Then answer every query in **O(1)**.

---

## Hashing with Numbers (Array-based hashing)

- If the elements of the array are small non-negative integers (say 0 to 10^6), we can use a
  **hash array** (frequency array) to store counts.

**Steps:**
1. Create a `hash[]` array of size (max_element + 1), initialized to 0.
2. **Pre-computation (hashing step):** Traverse the input array, for each element `a[i]`
   do `hash[a[i]]++`.
3. **Fetching (query step):** For a query `x`, return `hash[x]` directly in O(1).

**Example in C++:**
```cpp
int arr[] = {1, 3, 2, 1, 3, 1};
int n = 6;

int hash[10] = {0};  // assuming elements < 10

// Pre-computation
for (int i = 0; i < n; i++) {
    hash[arr[i]]++;
}

// Query
int q;
cin >> q;
while (q--) {
    int x;
    cin >> x;
    cout << hash[x] << "\n";  // O(1)
}
```

**Example in Java:**
```java
int[] arr = {1, 3, 2, 1, 3, 1};
int n = arr.length;

int[] hash = new int[10];  // assuming elements < 10

// Pre-computation
for (int i = 0; i < n; i++) {
    hash[arr[i]]++;
}

// Query
Scanner sc = new Scanner(System.in);
int q = sc.nextInt();
while (q-- > 0) {
    int x = sc.nextInt();
    System.out.println(hash[x]);  // O(1)
}
```

### Limitations of Array-based Hashing:
- Works only when elements are **small non-negative integers**.
- If elements are very large (e.g., 10^9), we cannot create an array of that size → **Memory
  Limit Exceeded (MLE)**.
- If elements are **negative** or **strings**, array indexing doesn't directly apply.
- This is where **Maps** come in.

---

## Hashing with Characters (Character Hashing)

- If the input contains only **lowercase English letters** (a to z), we can use a hash array of
  size 26.
- Map each character to an index: `'a' → 0`, `'b' → 1`, ..., `'z' → 25`.
- Use `ch - 'a'` to get the index.

**Example in C++:**
```cpp
string s = "abcdabefc";

int hash[26] = {0};

// Pre-computation
for (char ch : s) {
    hash[ch - 'a']++;
}

// Query: how many times does 'c' appear?
cout << hash['c' - 'a'] << "\n";  // O(1)
```

**Example in Java:**
```java
String s = "abcdabefc";

int[] hash = new int[26];

// Pre-computation
for (char ch : s.toCharArray()) {
    hash[ch - 'a']++;
}

// Query: how many times does 'c' appear?
System.out.println(hash['c' - 'a']);  // O(1)
```

- If the string contains both **uppercase and lowercase** letters, use a hash array of size **52**.
  - Lowercase: `ch - 'a'` → index 0 to 25
  - Uppercase: `ch - 'A' + 26` → index 26 to 51

- If the string contains **any ASCII character**, use a hash array of size **256** (total ASCII
  characters).

```cpp
int hash[256] = {0};
for (char ch : s) {
    hash[(int)ch]++;
}
```

---

## Hashing with Maps

- When elements can be **large integers**, **negative numbers**, or **strings**, we use **Maps**
  instead of arrays.
- Maps internally use hashing to give **O(1) average** time for insert, delete, and search.

### In C++ — `unordered_map`

```cpp
#include <unordered_map>
using namespace std;

int arr[] = {1, 3, 2, 1, 3, 1, 1000000000};
int n = 7;

unordered_map<int, int> mp;

// Pre-computation (hashing step)
for (int i = 0; i < n; i++) {
    mp[arr[i]]++;
}

// Query
int q;
cin >> q;
while (q--) {
    int x;
    cin >> x;
    if (mp.find(x) != mp.end())
        cout << mp[x] << "\n";
    else
        cout << 0 << "\n";
}
```

### In Java — `HashMap`

```java
import java.util.*;

int[] arr = {1, 3, 2, 1, 3, 1, 1000000000};
HashMap<Integer, Integer> map = new HashMap<>();

// Pre-computation
for (int x : arr) {
    map.put(x, map.getOrDefault(x, 0) + 1);
}

// Query
Scanner sc = new Scanner(System.in);
int q = sc.nextInt();
while (q-- > 0) {
    int x = sc.nextInt();
    System.out.println(map.getOrDefault(x, 0));
}
```

### Hashing Strings with Map (C++)

```cpp
unordered_map<string, int> mp;
string arr[] = {"apple", "banana", "apple", "cherry"};

for (string s : arr) {
    mp[s]++;
}

cout << mp["apple"];  // 2
```

### Hashing Strings with Map (Java)

```java
HashMap<String, Integer> map = new HashMap<>();
String[] arr = {"apple", "banana", "apple", "cherry"};

for (String s : arr) {
    map.put(s, map.getOrDefault(s, 0) + 1);
}

System.out.println(map.get("apple"));  // 2
```

---

## How Does Hashing Work Internally?

- Internally, a hash map (or hash table) is basically an **array of buckets**.
- When we insert a key, a **hash function** is applied to the key to compute an index (bucket
  number) where that key-value pair will be stored.
- When we search for a key, the same hash function is applied to find the bucket directly.

### Hash Function

- A hash function maps a key to a number (called hash code) which is then used as an index
  into the internal array.

**Ideal properties of a good hash function:**
  1. **Deterministic** — same key always produces same hash
  2. **Fast to compute** — should be O(1)
  3. **Uniform distribution** — distributes keys uniformly across buckets (avoids clustering)
  4. **Minimizes collisions**

---

## Division Rule of Hashing

- The most common and simple hash function is the **division method**.
- Formula: `hash(key) = key % tableSize`
- The key is divided by the size of the hash table and the remainder is used as the index.

**Example:**
```
Table Size = 10
Key = 37  →  hash(37) = 37 % 10 = 7  →  store at index 7
Key = 23  →  hash(23) = 23 % 10 = 3  →  store at index 3
Key = 57  →  hash(57) = 57 % 10 = 7  →  COLLISION! (index 7 already occupied)
```

- **Choosing a good table size:**
  - Table size should ideally be a **prime number** to minimize collisions.
  - Avoid powers of 2 — they tend to cause clustering with many real-world keys.
  - A prime number distributes keys more uniformly.

**Example:**
  - Bad table size: 10 (many keys end with same digit → clustering)
  - Good table size: 11 or 13 (prime, distributes better)

---

## What is a Collision?

- A **collision** occurs when two different keys produce the **same hash value** (i.e., they
  map to the same bucket).
- Since the number of possible keys is much larger than the number of buckets, collisions are
  **inevitable**.
- The quality of the hash function determines how frequently collisions occur.
- A good hash function minimizes collisions by distributing keys uniformly.

**Example of collision:**
```
hash(7)  = 7 % 10 = 7
hash(17) = 17 % 10 = 7   ← collision with 7
hash(27) = 27 % 10 = 7   ← collision again
```

---

## Collision Handling Techniques

### 1. Chaining (Separate Chaining)

- Each bucket in the hash table stores a **linked list** (or any other data structure) of all
  keys that hash to that bucket.
- When a collision occurs, the new key is simply **appended to the linked list** at that bucket.
- On search, we go to the bucket and traverse the linked list to find the key.

```
Index  Bucket (Linked List)
  0  →  []
  1  →  []
  2  →  []
  3  →  [23]
  4  →  []
  5  →  []
  6  →  []
  7  →  [7] → [17] → [27]   ← all three chained here
  8  →  []
  9  →  []
```

- **Time Complexity:**
  - Best case (no collision): O(1)
  - Average case: O(1) (if hash function distributes well)
  - Worst case: O(n) (all keys map to the same bucket → one long linked list)

- **Load Factor (λ):**
  - λ = n / m  where n = number of keys, m = number of buckets
  - When λ is low, fewer collisions occur and performance stays near O(1).
  - When λ is high, more collisions → performance degrades.
  - Most implementations **rehash** (resize the table) when λ exceeds a threshold (e.g., 0.75).

### 2. Open Addressing (Linear Probing)

- Instead of using a linked list, all keys are stored **inside the hash table itself**.
- When a collision occurs, we **probe** (look for) the next available empty slot.

**Linear Probing:**
  - If `hash(key) = h` is occupied, try `h+1`, `h+2`, `h+3`, ... (wrapping around if needed)

```
Insert 7:  hash(7) = 7  → slot 7 is empty → place at 7
Insert 17: hash(17) = 7 → slot 7 is occupied → try slot 8 → empty → place at 8
Insert 27: hash(27) = 7 → slot 7 occupied → slot 8 occupied → try slot 9 → place at 9
```

- **Problem with linear probing:** **Primary clustering** — consecutive occupied slots form
  clusters, slowing down future insertions and searches.

**Quadratic Probing:**
  - If `hash(key) = h` is occupied, try `h + 1²`, `h + 2²`, `h + 3²`, ...
  - Reduces primary clustering.

**Double Hashing:**
  - Use a second hash function to determine the step size.
  - `next_slot = (hash1(key) + i * hash2(key)) % tableSize`
  - Provides better distribution than linear or quadratic probing.

---

## Time Complexity of Hashing

| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Insert    | O(1)         | O(n)       |
| Search    | O(1)         | O(n)       |
| Delete    | O(1)         | O(n)       |

- **Average O(1):** Happens when the hash function distributes keys uniformly with few
  collisions. This is the expected behavior in practice.

- **Worst O(n):** Happens when all keys hash to the same bucket (all collide). This is
  extremely rare with a good hash function and rarely happens in practice.

- For competitive programming, this worst case can be **deliberately triggered** by an
  adversary who knows the hash function (called anti-hash attacks). To avoid this:
  - Use a **custom hash function** with randomization.
  - Or use ordered maps (`map` in C++ / `TreeMap` in Java) which give O(log n) guaranteed.

---

## map vs unordered_map (C++) — When to use which?

| Feature              | `map`                  | `unordered_map`        |
|----------------------|------------------------|------------------------|
| Internal structure   | Red-Black Tree (BST)   | Hash Table             |
| Ordering             | Keys sorted            | No ordering            |
| Insert/Search/Delete | O(log n)               | O(1) average, O(n) worst |
| lower_bound / upper_bound | Supported         | Not supported          |
| Memory usage         | Less                   | More (due to hash table) |
| Safe in CP           | Yes (no anti-hash)     | Can be hacked          |
| Use when             | Need sorted order or range queries | Need fast O(1) lookups |

```cpp
// When to use map
map<int,int> mp;  // when you need sorted keys or lower_bound/upper_bound

// When to use unordered_map
unordered_map<int,int> mp;  // when you just need fast frequency counting
```

## TreeMap vs HashMap (Java) — When to use which?

| Feature              | `TreeMap`              | `HashMap`              |
|----------------------|------------------------|------------------------|
| Internal structure   | Red-Black Tree         | Hash Table             |
| Ordering             | Keys sorted            | No ordering            |
| Insert/Search/Delete | O(log n)               | O(1) average, O(n) worst |
| floorKey/ceilingKey  | Supported              | Not supported          |
| Null keys            | Not allowed            | One null key allowed   |
| Use when             | Need sorted order or range queries | Need fast lookups |

---

## Practical Hashing Patterns in Competitive Programming

### Pattern 1 — Frequency Count
```cpp
// C++
unordered_map<int, int> freq;
for (int x : arr) freq[x]++;
```
```java
// Java
HashMap<Integer, Integer> freq = new HashMap<>();
for (int x : arr) freq.put(x, freq.getOrDefault(x, 0) + 1);
```

### Pattern 2 — Check if element exists
```cpp
// C++
if (mp.count(x)) { /* exists */ }
if (mp.find(x) != mp.end()) { /* exists */ }
```
```java
// Java
if (map.containsKey(x)) { /* exists */ }
```

### Pattern 3 — First non-repeating element
```cpp
// C++
string s = "aabbcddce";
unordered_map<char, int> freq;
for (char c : s) freq[c]++;
for (char c : s) {
    if (freq[c] == 1) {
        cout << c;  // 'e' — first non-repeating
        break;
    }
}
```
```java
// Java
String s = "aabbcddce";
LinkedHashMap<Character, Integer> freq = new LinkedHashMap<>();
for (char c : s.toCharArray())
    freq.put(c, freq.getOrDefault(c, 0) + 1);
for (Map.Entry<Character, Integer> e : freq.entrySet()) {
    if (e.getValue() == 1) {
        System.out.println(e.getKey());  // 'e'
        break;
    }
}
// Note: LinkedHashMap is used here to preserve insertion order
```

### Pattern 4 — Two Sum (check if complement exists)
```cpp
// C++
unordered_set<int> seen;
for (int x : arr) {
    if (seen.count(target - x)) {
        cout << "Pair found";
        break;
    }
    seen.insert(x);
}
```
```java
// Java
HashSet<Integer> seen = new HashSet<>();
for (int x : arr) {
    if (seen.contains(target - x)) {
        System.out.println("Pair found");
        break;
    }
    seen.add(x);
}
```

### Pattern 5 — Subarray with zero sum (prefix sum + hashing)
```cpp
// C++: check if subarray with sum 0 exists
unordered_set<int> prefixSums;
prefixSums.insert(0);
int prefixSum = 0;
for (int x : arr) {
    prefixSum += x;
    if (prefixSums.count(prefixSum)) {
        cout << "Zero sum subarray exists";
        break;
    }
    prefixSums.insert(prefixSum);
}
```

---

## Summary — Key Takeaways

- **Hashing** maps keys to fixed-size indices using a hash function to achieve O(1) average
  time for insert, search, and delete.

- **Array-based hashing** works for small non-negative integers or characters. Use `hash[key]++`
  for frequency counting.

- **Map-based hashing** works for large integers, negative numbers, and strings. Use
  `unordered_map` in C++ and `HashMap` in Java.

- **Division rule:** `hash(key) = key % tableSize`. Use a **prime number** as table size for
  better distribution.

- **Collision:** When two keys produce the same hash value. Handled by:
  - **Chaining** — linked list at each bucket (used in Java HashMap and C++ unordered_map)
  - **Open Addressing** — linear probing, quadratic probing, double hashing

- **Time Complexity:** O(1) average, O(n) worst case. Worst case is rare in practice but
  can be triggered by anti-hash attacks in CP — use `map`/`TreeMap` (O(log n)) when safety
  is needed.

- **Load Factor** determines when rehashing occurs. Java HashMap rehashes at load factor 0.75.

- Use **unordered_map / HashMap** when you need fast O(1) lookups without caring about order.
- Use **map / TreeMap** when you need sorted order or range queries (lower_bound, upper_bound,
  floorKey, ceilingKey).

---

*Notes based on: Hashing | Maps | Time Complexity | Collisions | Division Rule of Hashing | Striver's A2Z DSA Course*