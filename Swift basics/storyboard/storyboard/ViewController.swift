//
//  ViewController.swift
//  storyboard
//
//  Created by Calvin T on 28/10/2020.
//

import UIKit

class ViewController: UIViewController {
    
    
    @IBOutlet weak var myFirstLabel: UILabel! // Variable for Label on main screen
    
    var count = 0
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
    }
    
    
    @IBAction func buttonTapped(_ sender: Any) {
        
        count = count + 1
        
        myFirstLabel.text = String(count)
        
        
        if count >= 10 {
            view.backgroundColor = UIColor.systemTeal
        }
        
        
        
        //        Actions that are performed OnClick of a button that I attached here.
    }
    
    
}

