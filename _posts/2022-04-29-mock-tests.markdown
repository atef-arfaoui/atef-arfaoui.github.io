---
title:  "Mock in Pytest"
date:   2022-04-28 20:04:23
categories: 
tags: [python, pytest, unit-tests]
---
When I first started writing unit tests in my early career, I thought it's boring task and tried to avoid them.
I think unit tests should never be ignored and it's better to start writiing them before it's too late :) Once you get used to them and use the right tools it will be really enjoyable task.

One of the struggles to write unit tests is mocking functions; changing the behavior of external calls, dependencies, database connections, etc.
So, I decided to write a blog series about unit testing and start with mocking functions.



Let's start with a simple example: A script that interacts with AWS S3 - It checks if there are dev buckets (dev buckets start with "dev-")

### Files structure
```bash

├── main.py
├── tests
│   ├── __init__.py
│   └── test_utils.py
└── utils
    └── s3_utils.py
```

_main.py_
```python
from utils.s3_utils import list_s3_buckets

def check_dev_buckets() -> bool:
    """
    Checks if the dev buckets exist 
    """
    buckets = list_s3_buckets()
    for bucket in buckets:
        if bucket.startswith('dev-'):
            return True
    
    return False


if __name__ == '__main__':
    if check_dev_buckets():
        print('Dev buckets exist')
    else:
        print('No dev buckets found')
```

_s3_utils.py_
```python
from boto3 import client


S3_CLIENT = client('s3')


def list_s3_buckets():
    """
    Lists all S3 buckets
    """
    response = S3_CLIENT.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    return buckets
```


_test_utils.py_
```python
import mock
from main import check_dev_buckets


def test_check_dev_buckets():
    with mock.patch('main.list_s3_buckets') as mock_list_s3_buckets:
        mock_list_s3_buckets.return_value = ['dev-bucket-1', 'dev-bucket-2']
        assert check_dev_buckets() 
```
### ⚠️ Note
in mock.patch() you need to pass the function where it's imported (used) not wehre it's defined. it should be `main.list_s3_buckets` and not `utils.s3_utils.list_s3_buckets` 