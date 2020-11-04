//
//  ViewController.swift
//  Project1
//
//  Created by Calvin T on 03/11/2020.
//

import UIKit

class ViewController: UITableViewController {

    var pictures = [String]()
    
    override func viewDidLoad() {
        super.viewDidLoad()
       
        title = "StormViewer"
        
        navigationController?.navigationBar.prefersLargeTitles = true
        
        let fm = FileManager.default // built in file system
        let path = Bundle.main.resourcePath! // set resource path of app bundle (my compiled app directory)
        let items = try! fm.contentsOfDirectory(atPath: path) // an array of all the files in the app
        
        for item in items {
            if item.hasPrefix("nssl") {
                // this is an image to load
                // everythin after load is destroyed so we need to persist it outside the DidLoad()
                pictures.append(item)
            }
        }
     

    }
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return pictures.count
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "Picture", for: indexPath)
        cell.textLabel?.text = pictures[indexPath.row]
        return cell
    }
    
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        if let vc = storyboard?.instantiateViewController(identifier: "Detail") as? DetailViewController {
            vc.selectedImage = pictures[indexPath.row]
            navigationController?.pushViewController(vc, animated: true)
    }
}

}
