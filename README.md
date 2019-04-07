```py
def func():
    print("hello world")

```
```js
function printlen():
    console.log('hello world')
```
```go
    Run code
    package main
    import "fmt"
    func main() {
            fmt.Println("hello world")
    }
```
```haskell
calc :: String -> [Float]
calc = foldl f [] . words
  where 
    f (x:y:zs) "+" = (y + x):zs
    f (x:y:zs) "-" = (y - x):zs
    f (x:y:zs) "*" = (y * x):zs
    f (x:y:zs) "/" = (y / x):zs
    f (x:y:zs) "FLIP" =  y:x:zs
    f xs y = read y : xs
```


