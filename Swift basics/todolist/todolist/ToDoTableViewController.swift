//
//  ToDoTableViewController.swift
//  todolist
//
//  Created by Calvin T on 30/10/2020.
//

import UIKit

class ToDoTableViewController: UITableViewController {
    
    var toDosList : [ToDo] = []
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let toDo1 = ToDo()
        toDo1.name = "buy bread"
        toDo1.important = true
        
        let toDo2 = ToDo()
        toDo2.name = "walk the dog"
        toDo2.important = false
        
        toDosList = [toDo1, toDo2]
    }
    
    override func viewWillAppear(_ animated: Bool) {
        if let context = (UIApplication.shared.delegate as? AppDelegate)?.persistentContainer.viewContext {
            let newToDo = ToDoItemDB(context: context)
        }
    }
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // #warning Incomplete implementation, return the number of rows
        
        return toDosList.count
        
    }
    
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = UITableViewCell()
        
        let toDo = toDosList[indexPath.row]
        
        
        if toDo.important {
            cell.textLabel?.text = "‼️ " + toDo.name
        } else {
            cell.textLabel?.text = toDo.name
        }
        
        return cell
    }
    
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        let selectedToDo = toDosList[indexPath.row]
        performSegue(withIdentifier: "goToComplete", sender: selectedToDo)
    }
    
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if let createVC = segue.destination as? CreateToDoViewController {
            createVC.toDoTableVC = self
        }
        
        if let completeVC = segue.destination as? CompleteViewController {
            if let toDo = sender as? ToDo {
                completeVC.toDo = toDo
                completeVC.toDoTableVC = self
            }
        }
    }
}
