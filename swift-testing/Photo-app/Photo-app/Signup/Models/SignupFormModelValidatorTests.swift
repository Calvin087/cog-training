//
//  SignupFormModelValidatorTests.swift
//  Photo-app
//
//  Created by Calvin T on 06/11/2020.
//

import Foundation

class SignupFormModelValidator{
    
    func isFirstNameValid(firstName: String) -> Bool {
        var returnValue = true
        
        if firstName.count < SignupConstants.firstNameMinLength || firstName.count > SignupConstants.firstNameMaxLength {
            
            returnValue = false
            
        }
        
        return returnValue
    }
    
    func doPasswordsMatch(password: String, repeatPass: String) -> Bool {
        
        return password == repeatPass
        
    }
    
    
}
