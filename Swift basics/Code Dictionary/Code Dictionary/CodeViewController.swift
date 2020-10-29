//
//  CodeViewController.swift
//  Code Dictionary
//
//  Created by Calvin T on 29/10/2020.
//

import UIKit

class CodeViewController: UIViewController {

    @IBOutlet weak var definitionLabel: UILabel!
    var term = "I like to code."
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
        
    title = term
        
    }
}
