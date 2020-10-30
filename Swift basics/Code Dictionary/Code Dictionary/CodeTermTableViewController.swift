//
//  CodeTermTableViewController.swift
//  Code Dictionary
//
//  Created by Calvin T on 29/10/2020.
//

// import TERM <- This doesn't need to happen because
// they're all available automatically within the project -- WHAT!!!

import UIKit

// This is a typical class, it just looks different to what i'm used to.
// INHERIT Class name CodeTerm etc, and it's INHERITING from UITableViewController
// OVERRIDE This is us telling swift to ignore the method that's been inherited as we're making a new one.

class CodeTermTableViewController: UITableViewController {
    
    var terms : [Term] = []

        //  ["Boolean", "Int", "Double", "String", "Array"]

    override func viewDidLoad() {
        super.viewDidLoad()
        
//        On Load we're adding these objects to the array above

        let term1 = Term()
        term1.name = "Boolean"
        term1.definition = "A true or false situation"
        term1.isType = true
        terms.append(term1)
        
        let term2 = Term()
        term2.name = "Double"
        term2.definition = "A number with decimals"
        term2.isType = true
        terms.append(term2)
        
        let term3 = Term()
        term3.name = "If Statement"
        term3.definition = "Allows us to go one way or another"
        term3.isType = false
        terms.append(term3)
        
    }

    
//      How many rows
//  This function takes two params and returns an Int.
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return terms.count
        
    }

//      What goes in each row
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = UITableViewCell()

        if terms[indexPath.row].isType {
            cell.textLabel?.text = terms[indexPath.row].name + " - Type"
        } else {
            cell.textLabel?.text = terms[indexPath.row].name
        }
        
        

        return cell
    }
    
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        
        let selectedPath = terms[indexPath.row]
        
        performSegue(withIdentifier: "goToDefinition", sender: selectedPath)
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if let codeVC = segue.destination as? CodeViewController {
            if let selectedTerm = sender as? Term {
                codeVC.term = selectedTerm
            }
        }
    }
    
}
