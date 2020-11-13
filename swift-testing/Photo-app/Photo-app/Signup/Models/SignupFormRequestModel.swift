//
//  SignupFormRequestModel.swift
//  Photo-app
//
//  Created by Calvin T on 12/11/2020.
//

import Foundation

struct SignupFormRequestModel: Encodable { //JSON ENCODABLE
    let firstName: String
    let lastName: String
    let email: String
    let password: String
}
