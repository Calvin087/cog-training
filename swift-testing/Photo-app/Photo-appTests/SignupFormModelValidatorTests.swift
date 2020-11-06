//
//  SignupFormModelValidator.swift
//  Photo-appTests
//
//  Created by Calvin T on 06/11/2020.
//

import XCTest
@testable import Photo_app

class SignupFormModelValidatorTests: XCTestCase {

    override func setUpWithError() throws {
        // Put setup code here. This method is called before the invocation of each test method in the class.
    }

    override func tearDownWithError() throws {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
    }

    func testSignupFormModelValidator_WhenValidFirstNameProvided_ShouldReturnTrue(){
        
//        Arrange
        let sut = SignupFormModelValidator()
        
//        Act
        let isFirstNameValid = sut.isFirstNameValid(firstName: "Bald")
        
//        Assert
        XCTAssertTrue(isFirstNameValid, "Yo! Failed error should go here!")
        
    }

}
