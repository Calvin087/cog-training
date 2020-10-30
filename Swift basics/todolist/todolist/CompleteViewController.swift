//
//  CompleteViewController.swift
//  todolist
//
//  Created by Calvin T on 30/10/2020.
//

import UIKit

class CompleteViewController: UIViewController {
    
    @IBOutlet weak var toDoLabel: UILabel!
    var toDo = ToDo()
    var toDoTableVC : ToDoTableViewController? = nil
    
    override func viewDidLoad() {
        super.viewDidLoad()
        if toDo.important {
            toDoLabel.text = "‼️ " + toDo.name 
        } else {
            toDoLabel.text = toDo.name
        }
        
    }
    
    @IBAction func completeTapped(_ sender: Any) {
        if let toDos = toDoTableVC?.toDosList {
            var index = 0
            for x in toDos {
                if x.name == toDo.name {
                    toDoTableVC?.toDosList.remove(at: index)
                    toDoTableVC?.tableView.reloadData()
                    navigationController?.popViewController(animated: true)
                    return
            }
                index += 1
            
        }
    }
}

}
