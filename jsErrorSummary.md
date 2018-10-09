### array error
```JavaScript
// this will fill the copy of new Array(5), and you modify one of them, other will change
const dp = new Array(7);
dp.fill(new Array(5));

// fix
const dp = [];
for (let i=0;i<7;i++){
    dp.push(new Array(5));
}

```
