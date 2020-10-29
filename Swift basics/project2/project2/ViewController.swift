//
//  ViewController.swift
//  project2
//
//  Created by Calvin T on 29/10/2020.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var centerLabel: UILabel!
    var count = 0
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
    }

    @IBAction func buttonTapped(_ sender: Any) {
        
        count += 1
        if count >= 10 {
            view.backgroundColor = .systemGreen
        }
        
        centerLabel.text = String(count)
    }
    
}

