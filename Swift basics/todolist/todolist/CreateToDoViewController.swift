//
//  CreateToDoViewController.swift
//  todolist
//
//  Created by Calvin T on 30/10/2020.
//

import UIKit

class CreateToDoViewController: UIViewController {
    
    
    @IBOutlet weak var nameTextField: UITextField!
    @IBOutlet weak var importantSwitch: UISwitch!
    
    var toDoTableVC : ToDoTableViewController? = nil
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Do any additional setup after loading the view.
    }
    
    
    @IBAction func addTapped(_ sender: Any) {
        if let context = (UIApplication.shared.delegate as? AppDelegate)?.persistentContainer.viewContext {
            let newToDo = ToDoItemDB(context: context)
            if let name = nameTextField.text { // If this returned Optional is not NIL, do something
                newToDo.name = name
                newToDo.important = importantSwitch.isOn // returns true or false which is the attribute needed
                (UIApplication.shared.delegate as? AppDelegate)?.saveContext()
                navigationController?.popViewController(animated: true)
            }
        }
        
        
    }
    
    
}
