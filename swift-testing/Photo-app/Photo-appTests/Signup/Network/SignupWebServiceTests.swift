//
//  SignupWebServiceTests.swift
//  Photo-appTests
//
//  Created by Calvin T on 12/11/2020.
//

import XCTest
@testable import Photo_app

class SignupWebServiceTests: XCTestCase {
    
    var sut:SignupWebService!
    var signFormRequestModel:SignupFormRequestModel!

    override func setUpWithError() throws {
        let config = URLSessionConfiguration.ephemeral
        config.protocolClasses = [MockURLProtocol.self]
        let urlSession = URLSession(configuration: config)
        sut = SignupWebService(urlString: SignupConstants.singupURLString, urlSession: urlSession)
        signFormRequestModel = SignupFormRequestModel(firstName: "Cally", lastName: "Davy", email: "cdavy@sliame.com", password: "123456789")
    }

    override func tearDownWithError() throws {
        sut = nil
        signFormRequestModel = nil
        MockURLProtocol.stubResponseData = nil
        MockURLProtocol.error = nil
    }

    func testSignupWebService_WhenGivenSuccessfullResponse_ReturnsSuccess() {
        
//        Arrange
        
        let jsonString = "{\"status\":\"ok\"}"
        MockURLProtocol.stubResponseData = jsonString.data(using: .utf8)
        
        let expectation = self.expectation(description: "Sign up web service response expectation.")
        
//        Act
        
        sut.signup(withForm: signFormRequestModel) { (signupResponseModel, error) in
        
            XCTAssertEqual(signupResponseModel?.status, "ok")
            expectation.fulfill()
        }
        
        self.wait(for: [expectation], timeout: 15)
        
//        Aseert
        
    }
    
    func testSignupWebservice_WhenReceuvedDufferentJSONResponse_ErrorTookPlace() {
        
        let jsonString = "{\"path\":\"/users\", \"error\":\"Internal Server Error\"}"
        MockURLProtocol.stubResponseData = jsonString.data(using: .utf8)
        
        let expectation = self.expectation(description: "Sign up web service response expectation.")
        
//        Act
        
        sut.signup(withForm: signFormRequestModel) { (signupResponseModel, error) in
        
            XCTAssertNil(signupResponseModel, "The response model for a request containing unknow JSON response, should have been nil")
            XCTAssertEqual(error, SignupError.invalidResponseModel, "The signup() method did not return expected error")
            expectation.fulfill()
        }
        
        self.wait(for: [expectation], timeout: 15)
        
//        Aseert
    }
    
    func testSignupWebservice_WhenEmptyURLStringProvided_ReturnsError(){
        let expectation = self.expectation(description: "An empty request URL string expectation")
        
        sut = SignupWebService(urlString: "")
        
        sut.signup(withForm: signFormRequestModel) { (signupResponseModel, error) in
            XCTAssertEqual(error, SignupError.invalidRequestURLString, "The signup() method did not return an expected error for a invalidRequestURLString error")
            XCTAssertNil(signupResponseModel, "When an invalidRequestURLString taks place, the response model must be nil")
            expectation.fulfill()
        }
        
        self.wait(for: [expectation], timeout: 2)
    }
    
    func testSignupWebService_WhenURLRequestFails_ReturnsErrorMessageDescription(){
        
        let expectation = self.expectation(description: "a failed request expectation")
        let errorDescription = "A localized description of an error"
        
        MockURLProtocol.error = SignupError.failedRequest(description: errorDescription)
        
        sut.signup(withForm: signFormRequestModel) { (signupResponseModel, error) in
            
            XCTAssert(error, SignupError.failedRequest(description:errorDescription), "something else")
//            XCTAssertEqual(error?.localizedDescription, errorDescription)
            expectation.fulfill()
        }
        
        self.wait(for: [expectation], timeout: 2)
    }

}
