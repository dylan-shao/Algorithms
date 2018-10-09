### grammar error
forget len() in range(1, len(item))

### logic error
did not check the condition of else expression, which is not the not expected

### array error
```python
# this will create same inner array, if you change one, other will change
dp =[[False]*3]*4

# fix
dp = [[False]*(n) for _ in range(m)]

```
