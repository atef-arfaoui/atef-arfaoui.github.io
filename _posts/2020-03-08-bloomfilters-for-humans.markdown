---
title:  "Bloom filters for Humans"
date:   2020-03-07 23:04:23
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


[jekyll]:      http://jekyllrb.com
[jekyll-gh]:   https://github.com/jekyll/jekyll
[jekyll-help]: https://github.com/jekyll/jekyll-help
