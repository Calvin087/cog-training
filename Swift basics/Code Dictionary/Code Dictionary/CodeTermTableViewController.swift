//
//  CodeTermTableViewController.swift
//  Code Dictionary
//
//  Created by Calvin T on 29/10/2020.
//

import UIKit

class CodeTermTableViewController: UITableViewController {
    
    var terms = ["Boolean", "Int", "Double", "String", "Array"]

    override func viewDidLoad() {
        super.viewDidLoad()

        
    }

    
//      How many rows
//  This function takes two params and returns an Int.
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return terms.count
        
    }

//      What goes in each row
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = UITableViewCell()

        cell.textLabel?.text = terms[indexPath.row]

        return cell
    }
    
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        
        let selectedPath = terms[indexPath.row]
        
        performSegue(withIdentifier: "goToDefinition", sender: selectedPath)
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        let codeVC = segue.destination as! CodeViewController
        let selectedTerm = sender as! String
        codeVC.term = selectedTerm
    }
    
}
