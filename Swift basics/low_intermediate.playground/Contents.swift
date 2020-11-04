import Foundation
import UIKit
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
//Optional chaining

func albumReleased(year: Int) -> String? {
    switch year {
    case 2006: return "Year 1"
    case 2007: return "Year 2"
    case 2008: return "Year 3"
    default: return nil
    }
}

let album = albumReleased(year: 2006)?.uppercased() //CHAINGING
// Everything after the  mark will run IF ng before is valid.
print("The album is \(album)")


//------------------
//Optional Coaliation/Coercian
// This seems to be a little bit like ternary operators.
// You DONT HAVE TO UNWRAP anything, as you provide a default of sorts.
// No Crashes


func albumReleased2(year: Int) -> String? {
    switch year {
    case 2006: return "Year 1"
    case 2007: return "Year 2"
    case 2008: return "Year 3"
    default: return nil
    }
}

let album2 = albumReleased2(year: 2010) ?? "Unknown"
// Everything after the  mark will run IF ng before is valid.
print("The album is \(album2)")
// >> The album is Unknown

// #=============
// Enums
// Gives us a list of types to check against. Anything other than those values, Swift will trigger an error.


enum WeatherType {
    case sun
    case cloud
    case rain
    case wind
    case snow
}

func getWeatherStatus(weather: WeatherType) -> String? {
    if weather == WeatherType.sun {
        return nil
    } else {
        return "bleh"
    }
}

getWeatherStatus(weather: WeatherType.cloud)

//------------------

enum WeatherType1 {
    case sun
    case cloud
    case rain
    case wind(speed: Int)
    case snow
}

func getWeatherStatus(weather: WeatherType1) -> String? {
    switch weather {
    case .sun:
        return nil
    case .wind(let speed) where speed < 10:
        return "Meh"
//    grab value inside of speed and check
    case .cloud, .wind:
        return "dislike"
    case .rain, .snow:
        return "hate"
    }
}

getWeatherStatus(weather: .wind(speed: 20))

// #=============
// Struct
// These are similar to objects, but you can also copy a newly made object

struct Person {
    var clothes: String
    var shoes: String
}

let dave = Person(clothes: "Tees", shoes: "Sneaks")
let sam = Person(clothes: "dungarees", shoes: "heels")

print(dave.shoes)
print(sam.clothes)

var clone = dave
clone.shoes = "kicks"

print(clone)
// >> Person(clothes: "Tees", shoes: "kicks")

// #=============
// Classes (Important in Cocoa Touch)
// Similar to structs, but need to have init methods

class Human {
    
    var clothes: String
    var shoes: String
    
    init(clothes: String, shoes: String) {
        self.clothes = clothes
        self.shoes = shoes
    }
    
    func sing() {
        print("la la la")
    }
}

class Clone: Human {
    
    override func sing() { // redefines the method that it has inherited from Human
        print("Kill all humans")
    }
}

class SuperSoldier: Human {
    var powerLevel: Int
    
    init(clothes: String, shoes: String, powerLevel: Int) {
        self.powerLevel = powerLevel
        super.init(clothes: clothes, shoes: shoes) // passing values to parent class to initialise
    }
    
    override func sing() {
        print("Destroy all clones")
    }
}

var vegeta = SuperSoldier(clothes: "Armour", shoes: "Saiyan Boots", powerLevel: 9000)
var trunks = SuperSoldier(clothes: "Jacket", shoes: "Sneaks", powerLevel: 7000)
var gohan = SuperSoldier(clothes: "Dress Shirt", shoes: "Brogues", powerLevel: 17000)

// #=============
// Polymorphism
var fighters: [Human] = [vegeta, trunks, gohan]
// Polymorphism on the Above Class

for fighter in fighters {
    print(fighter.sing())
}

// #=============
// TypeCasting
// as ! or as ?
// NEED MORE INFO FOR THIS


// #=============
// Closures

let vw = UIView()

UIView.animate(withDuration: 0.5) {
    vw.alpha = 0
}
