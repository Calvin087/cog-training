//
//  ViewController.swift
//  tipcalc
//
//  Created by Calvin T on 29/10/2020.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var billTotalTextField: UITextField!
    @IBOutlet weak var tipPercentageTextField: UITextField!
    @IBOutlet weak var tipLabel: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    @IBAction func calculateTapped(_ sender: Any) { // Automatic function brought in via Storyboard nodes
        
        let billTotal = Double(billTotalTextField.text!)!
            // converting this to a "double" number | This variable also returns and optional that needs unwrapping
        
        let tipPercentage = Double(tipPercentageTextField.text!)!
            // converting this to a "double" number | This variable also returns and optional that needs unwrapping
        
        let tipToPay = billTotal * (tipPercentage / 100)
        
        tipLabel.text = String("Tip: $\(tipToPay)")
        
    }
    
}

