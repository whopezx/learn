下面第1行程序会有中间数组产生，即`x/a`会产生一个中间数组，`np.log()`会产生一个中间数组，`/b`会产生一个中间数组，`np.sqrt()`会产生一个中间数组，最后这个中间数组赋值给`x`，这些中间数组都会占用内存。使用universal function的out参数可以避免这些中间数组的产生，进而节省内存，可以将第1行程序写为第2行的形式。
```
x = np.sqrt(np.log(x/a)/b)

np.sqrt(np.divide(np.log(np.divide(x, a, out=x), out=x), out=x), out=x)
```

