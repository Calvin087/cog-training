import PlaygroundSupport
import Foundation

// Variables are the var
var age = 30
var name = "Calvin T"

// Constants are let...
let air = "breathable"
let myTime = -10

// Not recommended
// Long-hand way of writing the same thing
// Is this what Typescript looks like?
var age2 : Int = 30
let hisName : String = "Sam"

print(air)

//======================

// Math
// DOUBLES are more accurate than FLOATS
// Can't mix types Int Doubles
// But you can convert and then add / divide

var weight = 185.32423742398748293743829
var myAge = 33

print(Int(weight) + myAge)
print(weight + Double(myAge))

let feet = 5
let inches = 7

var myHeight = feet * 12 + inches // 67
var myWeight = 100

print(myHeight)

//======================

// Booleans and If statements

var amIOld = true
//var amIOld : Bool = true <-- same thing

if myHeight > 70 && myWeight >= 100 {
    print("Go ahead")
} else {
    print("Nah, maybe later")
}

// Pretty much the same as Javascript.

//======================

// Arrays and Array Types

var myArray : [String] = ["one", "two", "four"]
myArray1.append(5) // <--- NOPE!!


var myArray1 : [Any] = ["one", "two", "four"]
myArray1.append(5) // <--- YES!!
//["one", "two", "four", 5]

myArray1.insert("three", at: 2)
// >> ["one", "two", "three", "four", 5]

myArray1.remove(at: 4)
// >> ["one", "two", "three", "four"]

myArray1.count
// >> 4

//======================

// For Loops + Ranges + interpolation

for i in myArray1 {
    print(i)
}

for i in 1...100 {
    print(i)
}

var count = 0
for i in myArray1 {
    print("\(count). \(i)")
    count += 1
}

for i in 0..<myArray1.count {
    print("\(count). \(myArray1[i])")
    count += 1
}

var numbers = [6895,1078,4920,410,5058,8167,2797,4742,6091,774,2666,1297,7560,132,9213,3776,3768,6179,8132,2689,4132,3697,579,5014,3347,8341,5880,3804,6154,7309,5292,136,952,690,619,7392,4672,7461,4247,5637,8485,7137,2632,8063,2493,1491,5166,1020,6499,2987,7137,1382,5985,8581,8602,4450,6977,4329,5525,7921,7433,675,7385,7445,4702,6385,6967,249,8782,8856,7025,2074,433,9994,2548,4909,6360,2620,3573,7910,2514,1287,3547,1421,184,5165,1205,1873,5248,7636,2562,6281,7000,7841,2362,8050,9075,3100,5106,1438,]

var counter = 0
for i in numbers {
    if i > 5000 {
        counter += 1
    }
}

print(counter)

// Pretty much the UGLIEST way to create a list of random numbers.

var str = "["

for _ in 1...10 {
    str += "\(Int.random(in: 0...10_000)), "
}

str += "]"

print(str)
