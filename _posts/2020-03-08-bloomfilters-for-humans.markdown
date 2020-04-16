---
title:  "Bloom filters for Humans (Draft)"
date:   2020-04-10 23:04:23
categories: 
tags: [data_structure]
---

![Bloom filter](/images/bloom_intro.jpg)
My story with Bloom filters started back in 2018 or 2017 .. not quite sure. Our team manager reached out and pointed to this data structure that could be used for anonymizing stored personal data (PII) in our servers. We needed to prepare ourselves for GDPR migration. To fully understand it, I decided to write a Bloom Filter from scratch. If you are planning to google "bloom filter" just hold for second and follow me along.
**_what is a Bloom filter ?_**


A Bloom Filer is a **probablistic** data structure which is used to check the existance of an element in set.
It mainly used for its **space effeciancy**. The price paid for that is **accucrancy** -> that's why it's called probablictic data structure.
In other words, there is the possibility for **false positive** values (BF claims that the element exists in the set but in realty it's not). 

To resume that, there are two cases when checking the exsitance of an element:
  1. Element is definiely **_not_** in set.
  2. **_Maybe_** in set (possibily of False positives).


Bloom filter representation is **one demension array initiated with zeros** (length is **_m_**).
To seed this array we need to use hash functions. We can use more that one hash function (number of hash functions is **_k_**). Hashed input will mark ones in this initiated array.


The bloom filter essentially consists of a bit-vector or bit-array(a list containing only either 0 or 1-bit value) of length **_m_**). Initially all values are set to zero, as shown below.
![Empty Bloom Filter](/images/empty_bf.png)

To add an item to the bloom filter, we feed it to **_k_** different hash functions and set the bits to one at the resulting positions. As you can see, in hash tables we would’ve used a single hash function, and, as a result, had only a single index as output. But in the case of the bloom filter, we would use multiple hash functions, which would give us multiple indexes.
![Seeded Bloom Filter](/images/test_added_to_bf.png)


In the above example:
  * m = 10  -> **lenght of the bitarray**
  * k = 2    -> **number of hash functions**


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
>>> |
```

The classic example is using bloom filters to reduce expensive disk (or network) lookups for non-existent keys.

If the element is not in the bloom filter, then we know for sure we don't need to perform the expensive lookup. On the other hand, if it is in the bloom filter, we perform the lookup, and we can expect it to fail some proportion of the time (the false positive rate).

In my use case the main puropose of Using Bloom Filter is not to reduce data size or to perform faster data lookups but to make sure that our company is confirming to GDPR regulation and not storing PII data in our server. Basically, we replaced our raw IP blacklist with Bloom filters. Since IPs are condidered as Personal data (PII) we are no longer storing raw IPs but a representaiton of them in a bitarray. 🧠

My production implimentaiton is using files to save blacklist. Files are more convinent support to transfer data betweeen servers. There are other solutions like using redis which has its advantage in front of files; like centralized data storage, but it can have other drawbacks like availability and concurrency, and it's has limitiatoin for quick local development. 


## Conclusion

The Bloom Filter is a powerful tool for reducing data to single bits what makes it possible to store large amounts of information in only few megabytes. Furthermore, since the bloom filter is basically one binary array, combined with a hash function, the search is in O(1), if hashing is implemented right. That makes it very useful for new IoT devices with small memory amounts, as well as for tiny PC’s like Rasperry PI and alternatives. Bloom filter can also be used for high-load backends, windows in streaming application, caching engines and many more...

The usage of Bloom Filters has also some limitaion if the filtered data has addtional information.
for example in my use case, some of the ip blacklist has a score attached to it which tell how dangerous the ip using a range from 0 to 100. So, I come with a "new" data structered to not loose this information; I called it Scores Bloomfilter. Maybe I will write about it in another Blog.. Stay tunned :) 

[jekyll]:      http://jekyllrb.com
[jekyll-gh]:   https://github.com/jekyll/jekyll
[jekyll-help]: https://github.com/jekyll/jekyll-help
