//
//  SignupWebService.swift
//  Photo-app
//
//  Created by Calvin T on 12/11/2020.
//

import Foundation

class SignupWebService {
    
    private var urlString: String
    
    init(urlString: String) {
        self.urlString = urlString
    }
    
    func signup(withForm formModel: SignupFormRequestModel, completionHandler: @escaping (SignupResponseModel?, SignupErrors?) -> Void) {
        
    }
    
}
