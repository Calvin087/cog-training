import Foundation

// Classes / Objects

class Dog {
    var name = ""
    var age = 0
    var furColour = ""

    func bark() {
        print("Damn! Who named me \(name), and why am i \(age) years old?")
    }
}

var dog1 = Dog()
dog1.age = 10
dog1.name = "Fido"
dog1.furColour = "Black"

print(dog1.bark())

// #==========================

// Structs
// Creating a Struct as a Variable gives you the ability to change the values after it has been initialised - BUT if you create a let Constant, you're not able to change those values. ie: let cat1 = Cat() ..../// cat1.name = "Dave" <---- Error. You also don't need to set default initial values.

struct Cat {
    var name : String
    var age : Int
    var furColour : String

    func meow() {
        print("What! Who named me \(name), and why am i \(age) years old?")
    }
}

var cat1 = Cat(name: "Carmen", age: 30, furColour: "Yellow")

print(cat1.meow())


// #==========================

// Enums


enum FurColour {
    case black
    case brown
    case white
    case golden
}

struct Hamster {
    var name : String
    var age : Int
    var furColour : FurColour

    func attack() {
        print("Take That!")
    }
    
    func whichColour() {
        switch furColour {
        case .black:
            print("Oo \(furColour) fur, nice")
        case .brown:
            print("Oo \(furColour) fur, nice")
        case .white:
            print("Oo \(furColour) fur, nice")
        case .golden:
            print("Oo \(furColour) fur, nice")
        }
    }
}

var russainHam1 = Hamster(name: "Killer", age: 2, furColour: .golden)

print(russainHam1.whichColour())


// #==========================

// Switches
// Seems similar to redux switches?? Kind of like an if else statement. We can also place these inside functions. Referencing the value/parameter passed in as an Enum and move through the switch cases to do something.

// Cases for switches, Cases for Enums
//    Enums Sets the Case.
//    Switches act on a Case.

var edad = 100

switch edad {

    case 0...12:
        print("Kid")
    case 13...20:
        print("Teen")
    case 21...30:
        print("Happy")

    default:
        print("something else...")
    }
