//
//  SignupFormModelValidator.swift
//  Photo-appTests
//
//  Created by Calvin T on 06/11/2020.
//

import XCTest
@testable import Photo_app

class SignupFormModelValidatorTests: XCTestCase {
    
    var sut: SignupFormModelValidator!
//    CURRENTLY NOT SET, BUT TYPE IS EXPECTED WHEN IT IS SET ON LINE 18

    override func setUpWithError() throws {
        
        sut = SignupFormModelValidator()
//        HERE WE GET SUT A VALUE THAT IT WAS EXPECTING
        
    }

    override func tearDownWithError() throws {
        
        sut = nil
        
    }

    func testSignupFormModelValidator_WhenValidFirstNameProvided_ShouldReturnTrue(){
//  TESTING A CLASS

//        Arrange
//        let sut = SignupFormModelValidator() this is now static + setup
//        INSTANCE OF CLASS METHOD
        
//        Act
        let isFirstNameValid = sut.isFirstNameValid(firstName: "Dave")
//        RANDOM VARIABLE = CLASS.CLASSMETHOD(ARGS TO TEST)
        
//        Assert
        XCTAssertTrue(isFirstNameValid, "Yo! Failed error should go here!")
//        LINE 29 SHOULD RETURN TRUE
        
    }
    
    func testSignupFormModelValidator_WhenTooShortFirstNameProvided_ShoudReturnFalse() {
//  TESTING A CLASS
        
//        Arrange
//        let sut = SignupFormModelValidator() this is now static + setup
//        INSTANCE OF CLASS METHOD
        
//        Act
        let isFirstNameValid = sut.isFirstNameValid(firstName: "S")
//        RANDOM VARIABLE = CLASS.CLASSMETHOD(ARGS TO TEST)
        
//        Assert
        XCTAssertFalse(isFirstNameValid, "Should be no less than \(SignupConstants.firstNameMinLength) characters")
//        LINE 46 SHOULD RETURN FALSE
    }
    
    func testSignupFormModelValidator_WhenTooLongFirstNameProvided_ShouldReturnFalse(){
        
//        Act
        let isFirstNameValid = sut.isFirstNameValid(firstName: "asdasdasdasdasdasdasdasdasd")
        
//        Assert
        XCTAssertFalse(isFirstNameValid, "Should be no more than \(SignupConstants.firstNameMaxLength) characters")
        
    }
    
    func testSignupFormModelValidator_WhenEqualPasswordProvided_ShouldReturnTrue(){
        
        let doPasswordsMatch = sut.doPasswordsMatch(password: "something", repeatPass: "something")
        
        XCTAssertTrue(doPasswordsMatch, "Should have returned True, but has returned false.")
        
    }
    
    func testSignupFormModelValidator_WhenNoMatchingPasswordProvided_ShouldReturnFalse(){
        
        let doPasswordsMatch = sut.doPasswordsMatch(password: "dave1", repeatPass: "Dave21")
        
        XCTAssertFalse(doPasswordsMatch, "Should have returned False, but is true")
        
    }

}











