//
//  SignupWebServiceTests.swift
//  Photo-appTests
//
//  Created by Calvin T on 12/11/2020.
//

import XCTest
@testable import Photo_app

class SignupWebServiceTests: XCTestCase {

    override func setUpWithError() throws {
        // Put setup code here. This method is called before the invocation of each test method in the class.
    }

    override func tearDownWithError() throws {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
    }

    func testSignupWebService_WhenGivenSuccessfullResponse_ReturnsSuccess() {
        
//        Arrange
        let sut = SignupWebService(urlString: "http://appsdeveloperblog.com:8080/signup-mock-service/users")
        
        let signupFormRequestModel = SignupFormRequestModel(firstName: "Cally", lastName: "Davy", email: "cdavy@sliame.com", password: "123456")
        
        let expectation = self.expectation(description: "Sign up web service response expectation.")
        
//        Act
        
        sut.signup(withForm: signupFormRequestModel) { (signupResponseModel, error) in
        
            XCTAssert(signupResponseModel?.status, "ok")
            expectation.fulfill()
        }
        
        self.wait(for: [expectation], timeout: 5)
        
//        Aseert
        
    }

}
