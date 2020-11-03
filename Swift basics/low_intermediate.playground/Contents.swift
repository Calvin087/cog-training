import Foundation
// #=============

// Tuples and Sets

var dog : (String, Int) = ("Fido", 8)
// var dog = ("Fido", 8)

print(dog.0) // >> Fido
print(dog.1) // >> 8

// Sets have unique like Python
// Also not locked in order like Python, random allocation

var nums : Set = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
// var nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

var names : Set = ["dave", "Sam", "Tom"]
// Strings too

nums.insert(199)
nums.contains(1)

// #=============

// Dictionaries

var dicts : [String:String] = ["Dave":"Tall","Tom":"Fast","Zaff":"Fake Person"]

dicts["Tom"] // >> Fast

dicts["Joe"] = "Slow"
dicts.removeValue(forKey: "Tom")

// #=============

// Functions
// I have a feeling Typescript is going to be exactly the same.

func addTwonums(num1 : Int, num2 : Int) -> Int {
    return num1 + num2
}

print(addTwonums(num1: 90, num2: 10))


// Function Names - New info!!

var nameList = ["Dave", "James", "Simon"]

func position(of string: String, in array: [String]) -> Int {
//    of is the 1st parameter, converted to name string
//    in is the 2nd parameter, converted to name array
    for i in 0..<array.count {
        if array[i] == string {
            return i
        }
    }
    
    return 0
}

let davepos = position(of: "Dave", in: nameList) // 0
let jamespos = position(of: "James", in: nameList) // 1
let simonpos = position(of: "Simon", in: nameList) // 2
let bobpos = position(of: "Bob", in: nameList) // 0 problem


// #=============
// Optionals
// Look up unwrapping optionals!!
// Can be the defined value or nil

//

var age10 : Int? = 33
var name10 : String? = "Sam"


if let age = Int("40") {
    print(age)
}
// because this could possibly not be a number/int we're safeguarding against a complete app shut down.

func printOptional(text : String?) {
    if let theText = text {
        print(theText)
    } else {
        print("It's nil")
    }
}

printOptional(text: "Hello")


//------------------
Optional

func albumReleased(year: Int) -> String? {
    switch year {
    case 2006: return "Year 1"
    case 2007: return "Year 2"
    case 2008: return "Year 3"
    default: return nil
    }
}

let album = albumReleased(year: 2006)?.uppercased()
// Everything after the  mark will run IF ng before is valid.
print("The album is \(album)")

