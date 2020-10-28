import Foundation

var longSentence = "something about this project isn't right, there could be a ghost or something in this machine. Maybe they're trying to steal the right keys for the master password"

func wordCounter(text : String) {
    var lowered = text.lowercased()
    
    lowered = lowered.replacingOccurrences(of: "\n", with: " ")
    lowered = lowered.replacingOccurrences(of: ",", with: " ")
    lowered = lowered.replacingOccurrences(of: "?", with: " ")
    lowered = lowered.replacingOccurrences(of: ".", with: " ")

    //    THIS IS THE UGLIEST SOLUTION I'VE SEEN.
    
    let split = lowered.components(separatedBy: " ")
    
    var myDict : [String:Int] = [:]

    for word in split {
        if myDict[word] == nil {
            myDict[word] = 1
        } else {
            myDict[word] = myDict[word]! + 1
        }
    }

    print("There are \(myDict.count) Words")
    
    let sortedWords = myDict.sorted { (word1, word2) -> Bool in
        return word1.value > word2.value
    }
    
    var leftSideCount = 1
    for word in sortedWords {
        print("\(leftSideCount). \(word.key) - \(word.value)")
        leftSideCount += 1
    }
    
}

print(wordCounter(text : longSentence))
