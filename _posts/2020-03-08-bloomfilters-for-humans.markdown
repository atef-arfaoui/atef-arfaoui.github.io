---
title:  "Bloom filters for Humans"
date:   2020-04-10 23:04:23
categories: 
tags: [data_structure]
---

![Bloom filter](/images/bloom_intro.jpg)
My story with Bloom filters started back in 2018, when our CTO reached out and pointed to this data structure that could be used for anonymizing stored PII data in our servers (preparing for GDPR migration). To fully understand, I decided to write from scratch. If you are planning to google "bloom filter" just hold a second and follow me along. 
But in first place, **_what is a Bloom filter ?_**


A Bloom Filer is a **probablistic** data structure which is used to check the existance of an element in set. 
It mainly used for its **space effeciancy** and the price paid for that is **accucrancy** -> that's why it's called probablictic data structure.
In other words, there is the possibility for false positive values (BF claims that the element exists in the set but it's not). 

To resume that, there are two cases when checking the exsitance of an element:
  1. Element is definiely not in set.
  2. Maybe in set (possibily of False positives).


Bloom filter representation is **one demension array initiated with zeros** (length is **_m_**).
To seed this array you need to use hash functions. We can use more that one hash function (number of hash functions is **_k_**). Hashed input will mark ones in this initiated array.


![Bloom filter](/images/Bloom_filter.svg.png)
An example of a Bloom filter, representing the set {x, y, z}. The colored arrows show the positions in the bit array that each set element is mapped to. The element w is not in the set {x, y, z}, because it hashes to one bit-array position containing 0. 

For this figure:
  * m = 18
  * k = 3

### Bloom Filter in Python

```python
import mmh3                             # 3rd party library


class Bloomfilter:

    def __init__(self, size: int, hash_count: int) -> None:
        self.size = size                # this is m
        self.hash_count = hash_count    # this is k
        self.bitarray = [0] * size      # we initiate the bitarray with 0 values

    def add(self, element: str) -> None:
        # to add the element to bitarray we use hash function to find the index
        # of the bitarray that will be set to 1

        for seed in range(self.hash_count):
            index = mmh3.hash(element, seed) % self.size
            self.bitarray[index] = 1

    def lookup(self, element: str) -> bool:
        # for checkin if the element exists in bloomfilter we hash it with same
        # hash function in add method and we check if all bitarray are set to 1
        # if not that means element doens't exist.
        for seed in range(self.hash_count):
            index = mmh3.hash(element, seed) % self.size
            if self.bitarray[index] == 0:
                return False
        return True 

```

### Usage
```python
>>> bloom_filter = Bloomfilter(10, 2)
>>> print(bloom_filter.bitarray)
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> bloom_filter.add('test')
>>> print(bloom_filter.bitarray)
[0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
>>> assert bloom_filter.lookup('test')
>>> assert not bloom_filter.lookup("does not exist")

```

[jekyll]:      http://jekyllrb.com
[jekyll-gh]:   https://github.com/jekyll/jekyll
[jekyll-help]: https://github.com/jekyll/jekyll-help
